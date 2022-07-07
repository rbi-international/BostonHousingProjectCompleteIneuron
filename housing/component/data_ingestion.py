from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
from housing.exception import HousingException
from housing.entity.artifact_entity import DataIngestionArtifact
import sys, os
from housing.logger import logging

class DataIngestion:
    
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
           logging.info(f"{'='*20}Data Ingestion log started.{'-'*20}")
           self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys) from e
        
        
    def download_housing_data(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
        
    def extract_tgz_file(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
        
    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
        
    
    def initiate_data_ingestion(self) -> DataIngestionConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e