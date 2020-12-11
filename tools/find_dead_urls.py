import glob
import os, re
from urlextract import URLExtract
from multiprocessing.dummy import Pool as ThreadPool
import requests

WHITE_LIST = ('localhost:9005')

PATH = '..' + os.sep + 'content'
EXTENSION = '.md'
VALID_LIST = (200,)

def main():

    # find external urls in all source markdown files
    url_list = find_urls(PATH)

#    for x in url_list: # debugging
#        print(x)
#    exit(0)

    pool = ThreadPool(8)
    #url_list = url_list[0:10] # debugging
    # check status of all urls
    results = pool.map(check_url, url_list)

    for x in results:
        if x.get('status') not in VALID_LIST and x.get('status') is not None and x.get('url') not in WHITE_LIST:
            print('WARNING:',x.get('status'), x.get('url'))

def find_urls(p):

    markdown_files = glob.glob(p + os.sep + '**/*'+EXTENSION, recursive=True)
    #print(markdown_files)

    url_list = []
    extractor = URLExtract()

    for f in markdown_files:
        with open(f, 'r') as fp:
            md = fp.read()
            # remove leading and trailng () characteres
            # this only finds urls that are in markdown []()
            # TO-DO: add second url parser that finds non-linked markdown
            #urls = [x[1:-1] for x in re.findall(r'\(https?://[^\s]+\)', md)]

            urls = extractor.find_urls(md)

            # extend main list
            url_list += urls
    
    # make list unique urls
    url_list = list(set(url_list))

    return url_list

def check_url(url):

    status = None

    if url not in WHITE_LIST:
        try:
            r = requests.get(url, timeout = 10.0, headers={'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',})
            status = r.status_code
        except requests.ConnectionError:
            pass
        except requests.exceptions.ReadTimeout:
            print('TIMEOUT:', url)
        except requests.exceptions.MissingSchema:
            print('INVALID:',url)

        return {'url' : url, 'status' : status}
    else:
        return {'url' : url, 'status' : None}

if __name__ == "__main__":
    main()