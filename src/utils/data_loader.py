
import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        try:
            data = pd.read_csv(self.file_path)
            print(f"Data loaded successfully from {self.file_path}.")
            return data
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
            return None
        except pd.errors.ParserError:
            print(f"Error: Could not parse the file {self.file_path}.")
            return None

    def summarize(self, data):
        if data is not None:
            print("Data Summary:")
            print(data.describe())
        else:
            print("No data to summarize.")
    