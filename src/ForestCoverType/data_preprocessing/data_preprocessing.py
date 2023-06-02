import os
import pandas as pd
from ForestCoverType import log
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from pathlib import Path
import joblib

STAGE_NAME = "Data Preprocessing Stage"

class DataPreprocessing:
    def __init__(self, config):
        self.config = config

    def handle_missing_value(self):
        data_path = self.config['dataset_load']
        log.info(f"dataset loading from {data_path} for preprocess ")
        self.df = pd.read_csv(data_path)
        
        # first drop Loan_ID column
        self.df = self.df.drop('Loan_ID', axis=1)

        # handling categorical missing value
        df_categorical = self.df.select_dtypes('O')
        self.df[df_categorical.columns] = self.df[df_categorical.columns].fillna(self.df[df_categorical.columns].mode().iloc[0])

        # handling numerical missing value
        self.df = self.df.fillna(self.df.median(numeric_only=True))
        log.info(f"Handling Missing Value done for Categorical and Numerical")

    def cat_to_numeric(self):
        # first convert out dependent variable to numeric
        self.df['Loan_Status'] = self.df['Loan_Status'].replace(['Y', 'N'], [1, 0])

        # now convert our independent features to numeric with OneHotEncoding
        self.df = pd.get_dummies(self.df)
        log.info("Categorical Variable successfully converted into Numerical")

    def handle_imbalanced_data(self):
        # using oversampling SMOTE
        sm = SMOTE()
        self.df_3 = self.df.drop('Loan_Status', axis=1)
        # self.df_over_sample, df_loan_new = sm.fit_resample(self.df.drop('Loan_Status', axis=1), self.df.Loan_Status)
        self.df_over_sample, df_loan_new = sm.fit_resample(self.df_3, self.df.Loan_Status)
        self.df_over_sample['Loan_Status'] = df_loan_new
        log.info("Handling imbalanced data with oversampling SMOTE done")
        
    def scaling_data(self):
        scaler = StandardScaler()
        self.df_scaled = pd.DataFrame(scaler.fit_transform(self.df_over_sample.drop("Loan_Status", axis=1)), columns=self.df_over_sample.columns[:-1])
        self.df_scaled['Loan_Status'] = self.df_over_sample['Loan_Status']
        
        log.info("Scaling data with StandardScaler Done")
        
        # saving Standard Scaler model
        data_preprocee_dir = self.config['root_dir']
        scaler_model_file = self.config['scaling_model_file']
        scaler_model_file_path = os.path.join(data_preprocee_dir, scaler_model_file)
        joblib.dump(scaler, scaler_model_file_path)
        log.info(f"StandardScaler model save at {scaler_model_file_path}")

         
    def save_preprocess_data(self):
        data_preprocess_root_dir =  Path(self.config['root_dir'])
        local_file_dir = Path(self.config['local_file'])

        raw_local_file_path = os.path.join(data_preprocess_root_dir, local_file_dir)

        self.df_scaled.to_csv(raw_local_file_path, index=False)
        
        log.info(f"data saved successfully at {raw_local_file_path}")

        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} compleated successfully compleated\n")