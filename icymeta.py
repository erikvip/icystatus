"""Retreive metadata from a Shoutcast server

Connect to a shoutcast stream and extract metadata broadcast. 

Some details on the protocol here:
http://www.smackfu.com/stuff/programming/shoutcast.html

The process is like this:
 # Make an HTTP GET request to url, with Icy-MetaData:1 HTTP header
 # Parse the ICY Response and extract the metadata-interval (metaint)
 # Read metaint bytes ahead of stream - this is mp3 Icy-MetaData
 # Retreive 1 byte, which is the lengh of the meta packet, binary encoded, /16
 # Read metaLength * 16 bytes ahead, and extract metadata
 """

import urllib2
import struct 
import pprint

__all__ = ["fetchMeta"]


def fetchMeta(stream_url):
    icy = IcyMeta()
    return icy.fetchMeta(stream_url)

class IcyMeta:
    def fetchMeta(self, stream_url):
        request = urllib2.Request(stream_url)        
        request.add_header('Icy-MetaData', 1)
        
        # Spoof the user agent...some streams will not report properly without a known user-agent
        # Example: 181.fm http://108.61.73.115:8052  ... don't ask me why...
        request.add_header('User-Agent', 'VLC/2.2.0-pre2 LibVLC/2.2.0-pre2')
        
        response = urllib2.urlopen(request)
        
        # HTTP Status
        statusCode = response.getcode()

        if statusCode != 200:
            raise Exception('Exepcted a 200 response code but got: %s ' % statusCode )

        # Parse headers
        # If no headers were parsed by urllib2, then attempt to parse manually. Some servers return ICY instead of HTTP
        if  len(response.info().headers) == 0:
            # This is an ICY 200 response
            status = response.readline()
            rawHeaders = response
        else:
            # This is an HTTP 200 response
            rawHeaders = response.info().headers

        headers = {}
        for line in rawHeaders:
            if line == "\r\n": break
            key, value = line.rstrip().split(':', 1)
            headers[key] = value

        if headers['icy-metaint'].isdigit() == False:
            raise Exception('metaint value was not a number. Header object: %s ' % pprint.pformat(headers) )

        # blockSize is metainterval
        blockSize = int(headers['icy-metaint'])

        # Skip to next meta broadcast
        response.read(blockSize)

        # Length of the metadata
        metaLen = ord(struct.unpack('c', response.read(1))[0] )

        #if metaLen < 1:
        #    raise Exception("Could not determine meta length. %s" % metaLen)

        # Lengh is metaLen * 16
        metaLen = int(metaLen) * 16

        # Now read the variable length metadata packet, size of metaLen
        metaPacket = response.read(metaLen)

        # Meta is now a semicolon delimited string of key=value pairs with quoting ''
        meta = {'headers': headers, 'StreamTitle': '', 'StreamUrl': stream_url}
        for item in metaPacket.split(';'):
            if '=' in item:
                key, value = item.rstrip().split('=', 1)
                meta[key] = value[1:-1]

        return meta