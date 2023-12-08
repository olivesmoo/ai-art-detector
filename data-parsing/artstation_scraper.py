'''
Script that scrapes ArtStation using its v2 api for their raw json data
Code obtained from this repository: https://github.com/hueyning/art-station-scraper
'''
import requests
import json
import os
import time
import numpy as np

def pause_report(length, random_delay, file_count, disp = True):
    
    pause_time = length*np.random.normal(1,random_delay)
    if disp: print(f"Downloaded {file_count} files. Pausing scraper for {round(pause_time,2)} seconds.")
    time.sleep(pause_time)

def get_data(query, page_start, page_end, short_pause=3, long_pause=30, random_delay=0.25):

    if page_start < 1:
        print("Starting page number has to be greater than 0.")
        print("Process exiting with error.")
        return 0
    
    if not os.path.exists(f'raw_data/{query}'):
        print(f'Creating directory: raw_data/{query}')
        os.makedirs(f'raw_data/{query}')
        
    saved_files = []
        
    for page_number in range(page_start, page_end):

        url = f"https://www.artstation.com/api/v2/search/projects.json?page={page_number}&per_page=75&query={query}&sorting=relevance&tags_exclude=CreatedWithAI&software_ids_exclude=193982,187754,205467&category_ids_include=5,27&medium_ids_include=1,2&category_ids_exclude=65,66,24,26"
        #https://www.artstation.com/search?sort_by=relevance&query=landscape&tags_exclude=CreatedWithAI&software_ids_exclude=193982,187754,205467&category_ids_include=5,27&medium_ids_include=1,2&category_ids_exclude=65,66,24,26
        filename = f'raw_data/{query}/data_{page_number}.json'
            
        # only scrape url if json file of the url doesn't already exist
        if not os.path.exists(filename):
            client = requests.session()
            r = client.get(url)
            print(f"Scraping {url} {r.status_code}: {r.reason}")
            
            # check if rate-limit was exceeded.
            if r.status_code == 429:
                print("Rate-limit exceeded. Wait for a while and try running scraper again.")
                print("Process exiting with error.")
                return 0
            
            # if "data" in response text is empty, the max page has probably been reached.
            data = json.loads(r.text)
            if len(data['data']) == 0:
                print(f"Data list is empty. Query {query} has no data on page {page_number}.")
                print(f"Max page for this query has probably been reached. Ending scraping process.")
                return 0

            # save file
            print(f'Saving file as {filename}')
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(r.text, f, ensure_ascii=False, indent=4)
                saved_files.append(filename)
                
            # take a short pause per url scraped
            pause_report(short_pause, random_delay, len(saved_files))
        
        else:
            print(f'{filename} already exists. Skipping the current url.')

        # take a long pause if 10 urls have been scraped
        if len(saved_files) > 0 and len(saved_files)%10 == 0:
            pause_report(long_pause, random_delay, len(saved_files))
      
    # process end summary
    print(f"Files saved: {saved_files}")
    print(f"Process finished running.")
    return 1


genres = ['landscape']

# download raw json data
get_data(genres[0], 1, 50, short_pause=10, long_pause=60) 