from ForestCoverType.data_ingestion import DataIngestionConfigurationManager, DataIngestion
from ForestCoverType import log 

def start_training_pipeline():
    config = DataIngestionConfigurationManager()
    data_ingestion_config = config.data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.save_data()


if __name__ == "__main__":
    try:
        log.info(f">>>>>>>>>>>>>>>>> Training Pipeline started")
        start_training_pipeline()
        log.info(f">>>>>>>>>>>>>>>>>> Training Pipeline compleated successfully\n\n X========================X\n\n")
    except Exception as e:
        log.exception(e)
        raise e