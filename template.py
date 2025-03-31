import os
from pathlib import Path 
import logging

logging.basicConfig(level = logging.INFO, format= '[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)   # path is used so that tha filepath format is supportable to every os
    filedr, filename = os.path.split(filepath)

    if filedr != "":
        os.makedirs(filedr, exist_ok= True)
        logging.info(f"Creating directory; {filedr} for the file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")