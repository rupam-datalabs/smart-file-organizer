import os
import shutil
from datetime import datetime
BASE_DIR=os.path.dirname(__file__)
SCRIPT_NAME=os.path.basename(__file__)
FILES=os.listdir(BASE_DIR)
for item in FILES:
    item_path=os.path.join(BASE_DIR,item)
    if item==SCRIPT_NAME:
        print(f"Skipping the script file: {SCRIPT_NAME}")
        continue
    if os.path.isfile(item_path):
        name, ext=os.path.splitext(item)
        if ext.lower() in ['.jpg','.jpeg','.png']:
            category="Images"
        elif ext.lower()=='.pdf':
            category="PDFs"
        elif ext.lower() in ['.csv','.xlsx','.xls']:
            category="Excel"
        else:
            category="Others"
        modified_time=os.path.getmtime(item_path)
        year=str(datetime.fromtimestamp(modified_time).year)
        category_path=os.path.join(BASE_DIR,category,year)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Folder crated : {category}/{year}")
        destination_path=os.path.join(category_path,item)
        if not os.path.exists(destination_path):
            shutil.move(item_path,destination_path)
            print(f"Moved {item} in {category}/{year}")
        else:
            print(f"Skipped (already exists) : {item}")
    else:
        print(f"Skipping the {item} folder...")


