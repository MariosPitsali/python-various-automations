#%%
import sys, os
from collections import namedtuple
from datetime import datetime

root_folder = r"C:\Users\User\Downloads"
# %%
for item in os.scandir(root_folder):
    if item.name.endswith(".rar") or item.name.endswith(".zip"):
        item_path = os.path.join(root_folder, item.name)

        print (f'{item.name} is at location {item_path}.')

        if os.path.exists(item_path):
            size_of_file = os.path.getsize(item_path)
            date_created = datetime.fromtimestamp(os.path.getctime(item_path))
            date_created_formatted = date_created.strftime('%Y-%m-%d %H:%M:%S')
            print (f'File {item.name} has size of {size_of_file/1000} KB and was created at {date_created_formatted}')
            print (datetime.today())
            

# %%
