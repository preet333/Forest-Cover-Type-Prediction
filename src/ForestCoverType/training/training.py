import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score
from ForestCoverType import log
from ForestCoverType.utils import save_reports
import joblib

STAGE_NAME = "Training Stage"


class Training:
    def __init__(self, config):
        self.config = config
    
    def model_training(self):
        # load dataset
        dataset_path = self.config['dataset_load']
        log.info(f"dataset loading from {dataset_path} for training ")
        df = pd.read_csv(dataset_path)
        
        #splitting data
        x = df.drop('Loan_Status', axis=1)
        y = df['Loan_Status']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=33)
        log.info(f"Splitting dataset into train and test completed")

        # model Training
        rf = RandomForestClassifier()
        rf.fit(x_train, y_train)
        log.info(f"RandomForestClassifier Model Train Successfully")

        # Scoring Model
        y_pred = rf.predict(x_test)
        f1_test_score = f1_score(y_test, y_pred, average='macro')
        test_accuracy_score = accuracy_score(y_test, y_pred)
        print(test_accuracy_score)
        scores = {
            'test_accuracy': test_accuracy_score,
            'f1_score': f1_test_score
        }

        # saving model and score
        training_root_dir = self.config['root_dir']
        model_file = self.config['local_model_file']
        model_file_path = os.path.join(training_root_dir, model_file)
        
        joblib.dump(rf, model_file_path)
        log.info(f"Trained model save at {model_file_path}")

        score_file = self.config['score_save']
        score_file_path =os.path.join(training_root_dir, score_file)
        log.info(f"predicting test score save at {score_file_path}")

        save_reports(scores, score_file_path)
        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} compleated successfully compleated\n")