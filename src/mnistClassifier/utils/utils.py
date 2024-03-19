import os
import sys

import numpy as np 
import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import joblib
import requests
import time
import zipfile
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml


from mnistClassifier.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            joblib.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return joblib.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def download_file(url:str, output_path:str):
    # Send a GET request to download the file
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    start_time = time.time()
    bytes_written = 0

    # Write the contents of the response to the output file
    with open(output_path, 'wb') as f:
        for data in response.iter_content(block_size):
            f.write(data)
            bytes_written += len(data)
            if time.time() - start_time >= 1:
                print_progress(bytes_written, total_size)
                start_time = time.time()

    print_progress(total_size, total_size)  # Print 100% progress at the end
    print("\nDownload complete!")

def print_progress(current, total):
    progress = min(100, int(100 * current / total))
    print(f'\r[{"#" * (progress // 2):50s}] {progress}% ', end='', flush=True)

def extract_zip(zip_file_path:str, extract_dir:str):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
        
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e,sys)