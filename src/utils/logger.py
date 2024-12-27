
import datetime

class Logger:
    @staticmethod
    def log(message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] {message}")

    @staticmethod
    def error(message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp} ERROR]: {message}")
    