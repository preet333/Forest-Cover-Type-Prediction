import os
from pathlib import Path
from ForestCoverType import read_yaml_file, create_directories
from ForestCoverType import CONFIG_FILE_PATH
from ForestCoverType import log

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} started")
        self.config = read_yaml_file(config_file_path)
        create_directories([self.config['artifacts_root']])

    def data_ingestion_config(self):
        config = self.config['data_ingestion']
        config_root_dir = Path(config['root_dir'])
        create_directories([config_root_dir])

        data_ingestion_config = {'root_dir': Path(config['root_dir']), 'train_file': Path(config['train_file']),
                                 'test_file': Path(config['test_file'])}

        return data_ingestion_config

