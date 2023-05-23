import os
import pandas as pd
from ForestCoverType import log
from sklearn.preprocessing import StandardScaler

STAGE_NAME = "Data Preprocessing Stage"

class DataPreprocessing:
    def __init__(self, config):
        self.config = config

    def preprocessing_data(self):
        # loading dataset
        dataset_path = self.config['dataset_load']
        log.info(f"dataset loading from {dataset_path} for preprocess ")
        df = pd.read_csv(dataset_path)

        scaler = StandardScaler()
        df_scaled = pd.DataFrame(scaler.fit_transform(df.drop('Cover_Type', axis=1)), columns=df.columns[:-1])
        df_scaled['Cover_Type'] = df['Cover_Type']
        log.info("Scaling data with StandardScaler Done")
        
        # saving dataset
        data_preprocess_root_dir = self.config['root_dir']
        local_file = self.config['localfile']

        local_file_path = os.path.join(data_preprocess_root_dir, local_file)

        df_scaled.to_csv(local_file_path, index=False)
        
        log.info(f"data saved successfully at {local_file_path}")

        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} compleated successfully compleated\n")