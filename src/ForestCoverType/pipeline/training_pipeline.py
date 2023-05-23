from ForestCoverType.data_ingestion import DataIngestionConfigurationManager, DataIngestion
from ForestCoverType.data_preprocessing import DataPreprocessingConfigurationManager, DataPreprocessing
from ForestCoverType.training import TrainingConfigurationManager, Training
from ForestCoverType import log 

def start_training_pipeline():
    # Data Ingestion Stage
    data_ingestion_configuration = DataIngestionConfigurationManager()
    data_ingestion_config = data_ingestion_configuration.data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.save_data()

    # Data Preprocessing Stage
    data_preprocessing_configuration = DataPreprocessingConfigurationManager()
    data_preprocessing_config = data_preprocessing_configuration.data_preprocessing_config()
    data_preprocessing = DataPreprocessing(config=data_preprocessing_config)
    data_preprocessing.preprocessing_data()

    # Training Stage
    training_configuration = TrainingConfigurationManager()
    training_config = training_configuration.training_config()
    training = Training(config=training_config)
    training.model_training()

if __name__ == "__main__":
    try:
        log.info(f">>>>>>>>>>>>>>>>> Training Pipeline started")
        start_training_pipeline()
        log.info(f">>>>>>>>>>>>>>>>>> Training Pipeline compleated successfully\n\n X========================X\n\n")
    except Exception as e:
        log.exception(e)
        log.info(f">>>>>>>>>>>>>>>>>> Training Pipeline Failed\n\n X========================X\n\n")
        raise e