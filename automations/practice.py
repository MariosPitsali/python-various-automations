
import os
from datetime import datetime
from tqdm import tqdm, trange

if __name__ == "__main__":

    downloads_folder = r"C:\Users\User\Downloads"

    downloads_files_list = [item.name for item in os.scandir(downloads_folder)]

    for item in tqdm(downloads_files_list, desc="Scanning Downloads Files...", colour='red', unit=" files scanned"):

        if item.endswith(".rar") or item.endswith(".zip"):
            item_path = os.path.join(downloads_folder, item)

            print (f'{item} is at location {item_path}.')

            if os.path.exists(item_path):
                size_of_file = os.path.getsize(item_path)
                date_created = datetime.fromtimestamp(os.path.getctime(item_path))
                date_created_formatted = date_created.strftime('%Y-%m-%d %H:%M:%S')
                date_modified = datetime.fromtimestamp(os.path.getmtime(item_path))
                date_modified_formatted = date_modified.strftime('%Y-%m-%d %H:%M:%S')
                print (date_created_formatted, date_modified_formatted)
                #print (f'File {item.name} has size of {size_of_file/1000} KB and was created at {date_created_formatted}')
                
                #delete all files that have been extracted and are older than six months
                datetime_now = datetime.today()

                print (f'File {item} was created {(datetime_now - date_created)} ago.')
                print (type((datetime_now - date_created)))
            
