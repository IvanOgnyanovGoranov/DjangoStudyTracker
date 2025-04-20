from datetime import datetime

from tracker.models import StudyProgress


class DateManager:
    def __init__(self):
        self.last_stored_date = self.load_date()


    def load_date(self):
        """Loads the last stored date StudyProgress model."""
        pass

    def save_date(self, date):
        """Save the last stored date to the database."""
        pass
