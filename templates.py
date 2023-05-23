import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

package_name = 'ForestCoverType'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/data_ingestion/__init__.py",
    f"src/{package_name}/data_preprocessing/__init__.py",
    f"src/{package_name}/training/__init__.py",
    f"src/{package_name}/evaluation/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/utils.py",
    f"src/{package_name}/logging.py",
    "configs/config.yaml",
    "params.yaml",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "init_setup.sh"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating {filedir} for {filename}")
    
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file {filename}")
    else:
        logging.info(f"file {filename} successfully created")