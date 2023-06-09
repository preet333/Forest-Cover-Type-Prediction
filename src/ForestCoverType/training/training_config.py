import os
from pathlib import Path
from ForestCoverType import log, read_yaml_file, create_directories, CONFIG_FILE_PATH, PARAMS_FILE_PATH

STAGE_NAME = "Training Stage"

class TrainingConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH):
        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} started")
        self.config = read_yaml_file(config_file_path)
        self.dataset_load = os.path.join(self.config['data_preprocessing']['root_dir'], self.config['data_preprocessing']['local_file'])
        create_directories([self.config['artifacts_root']])

    def training_config(self):
        config = self.config['training']
        config_root_dir = Path(config['root_dir'])
        create_directories([config_root_dir])

        training_config = {'root_dir': Path(config['root_dir']), 'dataset_load': Path(self.dataset_load),
                           'local_model_file': Path(config['local_model_file']), 'score_save': Path(config['score_save'])}
        
        return training_config