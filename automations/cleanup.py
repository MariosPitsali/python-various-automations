import os
from datetime import datetime
from tqdm import tqdm, trange

if __name__ == "__main__":

    downloads_folder = r"C:\Users\User\Downloads"
    downloads_files_list = [item.name for item in os.scandir(downloads_folder)]

    total_mb_saved = 0

    for item in tqdm(set(downloads_files_list), desc="Scanning Downloads Files...", colour='red'):

        if item.endswith(".gif") or item.endswith(".jpeg"):
            item_path = os.path.join(downloads_folder, item)

            if os.path.exists(item_path):

                size_of_file = os.path.getsize(item_path)

                date_created = datetime.fromtimestamp(os.path.getctime(item_path))
                date_created_formatted = date_created.strftime('%Y-%m-%d %H:%M:%S')#formatted for output purposes
                date_modified = datetime.fromtimestamp(os.path.getmtime(item_path))
                date_modified_formatted = date_modified.strftime('%Y-%m-%d %H:%M:%S')#formatted for output purposes
                               
                #delete all files that are older than 3 months

                datetime_now = datetime.today()
                time_difference = datetime_now - date_created

                if time_difference.days> 100:
                    total_mb_saved += round(size_of_file/(1024.0 * 1024.0))
                    os.remove(item_path)
                    #print (f'File {item.name}, with size of {size_of_file/1000} KB and was created at {date_created_formatted}, was deleted')
    
    print (f'Approx. {total_mb_saved} MB saved from hard drive, by deleting files from {os.path.basename(downloads_folder)}.')       
