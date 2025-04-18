import csv
from datetime import datetime

class DateManager:
    def __init__(self):
        self.date_file = "last_stored_date.csv"
        self.last_stored_date = self.load_date()

    def load_date(self):
        """Load the last stored date from the date file."""
        try:
            with open(self.date_file, mode='r') as file:
                reader = csv.reader(file)
                last_date = next(reader)[0]
                return datetime.strptime(last_date, "%Y-%m-%d").date()
        except (FileNotFoundError, StopIteration):
            # If the file doesn't exist or is empty, default to some past date
            return datetime(2020, 1, 1).date()

    def save_date(self, date):
        """Save the last stored date to the date file."""
        with open(self.date_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date.strftime("%Y-%m-%d")])
