import json
import pyktok as pyk
import sys

def collect_metadata(inputFile, outputFile):
    """Call pyktok with a list of URLs to collect post metadata.
    """

    try:
        with open(inputFile) as fin:
            data = json.load(fin)
    except FileNotFoundError:
        print(f"File '{inputFile}' couldn't be found.")
        return 
    
    try:
        urls = []
        [urls.append(url) for search_term in data for url in data[search_term]['urls']]
        #urls = [entry[search_term]['urls'] for entry in data for search_term in entry]
    except:
        print("There is something wrong with the data format.")
        return
    
    pyk.specify_browser('chrome')
    pyk.save_tiktok_multi_urls(urls,  # list of URLs to visit
                               False, # don't save videos   
                		       outputFile, # csv file
                		       5) # max time sleep
    
if __name__ == "__main__":
    _, fin, fout = sys.argv
    collect_metadata(fin, fout)