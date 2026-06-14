# This module defines a class that reads data from CSV files and returns them as DataFrames.

import pandas as pd

class DatasetLoader:

    def load_csv(self, path):
        return pd.read_csv(path)