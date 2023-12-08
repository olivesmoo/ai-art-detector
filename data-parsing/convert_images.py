import json
import pandas as pd
import numpy as np
import os

def files_to_df(dir_name):
    
    full_df = pd.DataFrame() # initialize full df compilation of files
    files = os.listdir(dir_name) # get list of files in directory
    print(f"{len(files)} files found in {dir_name}")

    for i in files:
        filename = os.path.join(dir_name, i)
        with open(filename, 'r') as f:
            data = json.loads(json.load(f))['data']
            df = pd.DataFrame(data)
        full_df = pd.concat([full_df, df], ignore_index = True) # join current json file to full df

    return full_df


def df_to_json(query):
    
    print(f"Converting json files in raw_data/{query} to dataframe.")
    df = files_to_df(f'raw_data/{query}')
    print(f"Shape of dataframe: {df.shape}")
        
    # convert dataframe back to json and export it
    export = df.to_json(f"full_data/{query}.json")
    print("Export complete.")
    
    return df
import time
import requests

def pause_report(length, random_delay, file_count, disp = True):
    
    pause_time = length*np.random.normal(1,random_delay)
    if disp: print(f"Downloaded {file_count} images. Pausing scraper for {round(pause_time,2)} seconds.")
    time.sleep(pause_time)

    
def download_files(query, df, file_start, file_end, short_pause = 2, long_pause = 60, random_delay = 0.25):

    file_count = 0 #number of files downloaded
    alrdy_exists = 0 #number of files that already exist and are skipped over
    skipped_urls = {} #urls that can't be connected to - need to retry at a later time
    
    if not os.path.exists(f'images/{query}'):
        print(f'Creating directory: images/{query}')
        os.makedirs(f'images/{query}')
    
    for i in range(file_start, file_end):

        if i >= len(df):
            print(f"Index {i} does not exist in dataframe.")
            print("End of dataframe has probably been reached. Process is terminating.")
            return 0
        
        filename = f"images/{query}/{df['hash_id'][i]}.jpg" # name the image using its hash_id

        if not os.path.exists(filename): # skip over files that have been downloaded
            
            try:
                img_url = df['smaller_square_cover_url'][i]
                print(f'Downloading {img_url} as {filename}')
                
                f = open(filename,'wb')
                f.write(requests.get(img_url).content)
                f.close()

                file_count += 1

                # take a short pause per url scraped
                pause_report(short_pause, random_delay, file_count)
                
            except:
                print("Cannot establish connection with the following row in df:")
                print(f"{i}:{img_url}")
                print("Skipping to next row")
                skipped_urls[i] = img_url #add key value pair to skipped_urls dict
                
                if len(skipped_urls) > 10:
                    print("More than 10 urls have had connection error.")
                    print(skipped_urls)
                    pause_report(300, random_delay, file_count) # pause for 5 minutes if more than 10 urls with connection error
                       
        else: 
            print(f"{filename} already exists. Skipping to next image url in df.")
            alrdy_exists += 1
            
        # take a long pause if 100 images have been downloaded
        if file_count > 0 and file_count%100 == 0:
            pause_report(long_pause, random_delay, file_count)
            
        # take a long pause x 2 if 500 images have been downloaded
        if file_count > 0 and file_count%500 == 0:
            pause_report(long_pause*2, random_delay, file_count)
      
    # Retry skipped urls
    print(f"Skipped the following urls because failed to make a connection:")
    print(skipped_urls)
    
    if len(skipped_urls) > 0:
        print("Retrying skipped urls.")
        
        for index, url in skipped_urls.items():
            try:
                filename = f"images/{query}/{df['hash_id'][index]}.jpg"
                print(f'Downloading {url} as {filename}.')

                f = open(filename,'wb')
                f.write(requests.get(img_url).content)
                f.close()

                file_count += 1

                # take a short pause per url scraped
                pause_report(short_pause, random_delay, file_count)

            except Exception as e:
                print("Still unable to connect to skipped urls. Please manually check for error.")
                print(e.message, e.args)
                return 0
    
    print(f"{file_count} images downloaded.")
    print(f"Skipped {alrdy_exists} images because already exists in database.")
    print("Process finished.")
    return 1
genres = ['landscape']

# convert the raw json files of a specific keyword to a dataframe
df = df_to_json(genres[0])
download_files(genres[0], df, 0, 1000)
