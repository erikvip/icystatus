"""Gather currently playing track from an Icecast/Shoutcast server

Supports multiple pls files and will return a list with now playing track
"""

import icymeta
import pprint

def run():
    """Main run from commmand line

        Gather URLs to be read
    """
    #meta = icymeta.fetchMeta('http://173.239.76.146:80');
    #pprint.pprint(meta)
    #print meta['StreamTitle']

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
    ]

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

        status = "{0} :: {1}".format(StreamUrl, meta['StreamTitle'])
        
        response.append( status )
    return response

if __name__ == "__main__":
    run()