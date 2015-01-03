"""Gather currently playing track from an Icecast/Shoutcast server

Supports multiple pls files and will return a list with now playing track
"""

import icymeta
import pprint

def run():
    """Main run from commmand line

        Gather URLs to be read
    """


    urls = [
        'http://xstream1.somafm.com:8062',
        'http://xstream1.somafm.com:2800',
        'http://xstream1.somafm.com:8900',
        'http://uwstream2.somafm.com:80',
        'http://uwstream2.somafm.com:8400',
        'http://uwstream1.somafm.com:80',
        'http://xstream1.somafm.com:8800',
        'http://xstream1.somafm.com:2020',
        'http://xstream1.somafm.com:2200',
        'http://uwstream3.somafm.com:8000',
        'http://xstream1.somafm.com:2504',
        'http://xstream1.somafm.com:8884',
        'http://uwstream2.somafm.com:7770',
        'http://205.164.62.15:6900',
        'http://108.61.73.115:8052',
        'http://listen.radionomy.com/AdultAlternative'

    ]
    '''
    urls = [
       'http://205.164.62.15:6900',
       'http://108.61.73.115:8052',
       'http://listen.radionomy.com/AdultAlternative'
    ]
    '''

    stats = fetchStatus(urls)
    pprint.pprint(stats)

def fetchStatus(urls = []):
    response = []
    for url in urls:
        meta = icymeta.fetchMeta(url)
        
        if meta['StreamUrl'] == None or meta['StreamUrl'] == '': 
            StreamUrl = url
        else: 
            StreamUrl = meta['StreamUrl']

        # Use IcyName for the name if it exists
        name = StreamUrl
        
        if 'icy-name' in meta['headers']:
            name = meta['headers']['icy-name']
            if ':' in name:
                name = name.split(':', 1)[0]
        

        #status = "{0} :: {1}".format(StreamUrl, meta['StreamTitle'])
        
        status = { 
            'StreamUrl': StreamUrl,  
            'CurrentTrack': meta['StreamTitle'], 
            'Name' : name
        }
        
        response.append( status )
    return response

if __name__ == "__main__":
    run()