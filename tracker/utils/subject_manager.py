import csv

class SubjectManager:
    def __init__(self):
        self.subjects = {}
        self.file_path = "study_progress.csv"
        self.load_subjects()

    def add_subject(self, subject_name, goal_time):
        """Add a new subject with daily goal time, zero study time for the day,
           zero total minutes completed, zero total days studied ."""
        if subject_name not in self.subjects:
            self.subjects[subject_name] = {
                                            'Daily Goal': goal_time,
                                            'Studied Today': 0,
                                            'Total Minutes Completed': 0,
                                            'Total Days Studied': 0,
                                           }
            self.save_subjects()
        else:
            raise ValueError(f"Subject '{subject_name}' already exists.")

    def delete_subject(self, subject_name):
        """Delete a subject even if time is more than zero"""
        if subject_name in self.subjects:
            del self.subjects[subject_name]
            self.save_subjects()
        else:
            raise ValueError(f"Subject '{subject_name}' does not exist.")

    def add_time(self, subject_name, time_in_minutes):
        """Add minutes to the specified subject."""
        if subject_name in self.subjects:
            self.subjects[subject_name]['Total Minutes Completed'] += time_in_minutes
            self.subjects[subject_name]['Studied Today'] += time_in_minutes
            self.save_subjects()  # Save after adding study time
        else:
            raise ValueError(f"Subject '{subject_name}' does not exist.")

    def save_subjects(self):
        """Save all subjects and their times to a CSV file."""
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            for subject, data in self.subjects.items():
                writer.writerow([subject, data['Daily Goal'], data['Studied Today'],
                                 data['Total Minutes Completed'], data['Total Days Studied']])

    def load_subjects(self):
        """Load all subjects and their time from a CSV file."""
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.reader(file)

                for row in reader:
                    subject_name, goal_time, studied_today, total_min_completed, total_days = row
                    self.subjects[subject_name] = {
                        'Daily Goal': int(goal_time),
                        'Studied Today': int(studied_today),
                        'Total Minutes Completed': int(total_min_completed),
                        'Total Days Studied': int(total_days)
                    }
        except FileNotFoundError:
            pass

    def update_subjects_info(self):
        """Resets the time studied for the day to zero and adds a day to the total days."""
        for subject in self.subjects:
            self.subjects[subject]['Studied Today'] = 0
            self.subjects[subject]['Total Days Studied'] += 1
        self.save_subjects()