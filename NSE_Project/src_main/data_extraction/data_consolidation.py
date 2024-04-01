import pandas as pd

# static classes can't have objects
class DataConsolidation:
    @staticmethod
    def consolidate(dataframes_list):
        return pd.concat(dataframes_list)
        