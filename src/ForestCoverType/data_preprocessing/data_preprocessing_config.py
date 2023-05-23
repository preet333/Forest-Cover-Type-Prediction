import os
from pathlib import Path
from ForestCoverType import read_yaml_file, create_directories, CONFIG_FILE_PATH, PARAMS_FILE_PATH
from ForestCoverType import log

STAGE_NAME = "Data Preprocessing Stage"

class DataPreprocessingConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} started")
        self.config = read_yaml_file(config_file_path)
        self.dataset_load = os.path.join(self.config['data_ingestion']['root_dir'], self.config['data_ingestion']['train_file'])
        create_directories([self.config['artifacts_root']])

    def data_preprocessing_config(self):
        config = self.config['data_preprocessing']
        config_root_dir = Path(config['root_dir'])
        create_directories([config_root_dir])

        data_preprocessint_config = {'root_dir': Path(config['root_dir']), 'dataset_load': Path(self.dataset_load),
                                      'localfile': Path(config['localfile'])}

        return data_preprocessint_config

