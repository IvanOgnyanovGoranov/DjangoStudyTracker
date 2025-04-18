from datetime import datetime
from tkinter import messagebox, simpledialog
from date_utils import DateManager
from timer_utils import Timer
from subject_manager import SubjectManager

class StudyTrackerApp:
    def __init__(self, window, timer_label, daily_goal_label):
        self.window = window
        self.timer_label = timer_label
        self.daily_goal_label = daily_goal_label
        self.current_subject = ""

        # Initialize instances of managers and timer
        self.subject_manager = SubjectManager()
        self.date_manager = DateManager()
        self.timer = Timer(self.window, self.timer_label)

        # Check if it's a new day and reset data if necessary
        self.check_day()

    def check_day(self):
        """Checks if the current date is different from the last stored date and resets the subject data if needed."""
        today = datetime.now().date()
        if today != self.date_manager.last_stored_date:
            self.subject_manager.update_subjects_info()
            self.date_manager.save_date(today)

    def manage_subjects(self):
        """Handles adding and deleting subjects."""
        action = simpledialog.askstring("Choose Action", "Type 'Add' to add a new subject or 'Delete' to delete a subject:")
        if not action:
            return

        action = action.lower()
        if action == 'add':
            self.add_new_subject()
        elif action == 'delete':
            self.delete_existing_subject()
        else:
            messagebox.showerror("Error", f"Invalid action '{action}'.")

    def add_new_subject(self):
        """Adds a new subject."""
        subject = simpledialog.askstring("New Subject", "Enter the name of the new subject:")
        if subject:
            subject = subject.upper()
            try:
                minutes = simpledialog.askinteger("Enter Goal Time", "Enter the daily goal time in minutes:")
                self.subject_manager.add_subject(subject, minutes)
                messagebox.showinfo("Success", f"Subject '{subject}' added with a {minutes}-minute daily goal.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Subject name cannot be empty.")

    def delete_existing_subject(self):
        """Deletes an existing subject."""
        subject = simpledialog.askstring("Choose Subject", "Enter the name of the subject you want to delete:")
        if subject:
            subject = subject.upper()
            try:
                self.subject_manager.delete_subject(subject)
                messagebox.showinfo("Success", f"Subject '{subject}' deleted.")
                self.daily_goal_label.config(text="Pick your subject of study")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Subject name cannot be empty.")

    def pick_subject(self):
        """Picks the currently studied subject."""
        subject = simpledialog.askstring("Choose Subject", "Enter the name of the subject you want to study:")
        if not subject:
            return
        subject = subject.upper()

        if subject in self.subject_manager.subjects:
            self.current_subject = subject
            self.daily_goal_label.config(text=f"Daily goal achieved for {subject} is {self.calculate_percentages(subject)}%")
        else:
            messagebox.showerror("Error", "Subject not found.")

    def add_study_time(self):
        """Adds the time spent studying to the selected subject."""
        if self.timer.timer_running:
            self.timer.stop_timer()

        time_studied_in_min = (self.timer.elapsed_time - 1) // 60
        if time_studied_in_min < 1:
            messagebox.showerror("Error", "Study time must be at least 1 minute.")
            return

        if not self.current_subject:
            messagebox.showwarning("Warning", "You need to pick a subject of study!")
            return

        add_time = messagebox.askyesno("Add Study Time", f"Do you want to add {time_studied_in_min} minutes to {self.current_subject}?")

        if add_time:
            self.subject_manager.add_time(self.current_subject, time_studied_in_min)
            messagebox.showinfo("Success", f"Added {time_studied_in_min} minute(s) to {self.current_subject}.")
            self.daily_goal_label.config(
                text=f"Daily goal achieved for {self.current_subject} is {self.calculate_percentages(self.current_subject)}%")
            self.timer.reset_timer(True)

    def calculate_percentages(self, subject):
        """Calculates the daily goal reached in percentages."""
        percentage = int((self.subject_manager.subjects[subject]['Studied Today'] / self.subject_manager.subjects[subject]['Daily Goal']) * 100)

        if percentage > 100:
            percentage = 100

        return percentage

    def show_stats(self):
        subjects = [s for s in self.subject_manager.subjects.keys()]
        subject = simpledialog.askstring("Statistics", f"Here are all your subjects: {', '.join(subjects)}."
                                                       f" Pick a subject you want to see the statistics for. ")
        if not subject:
            return

        subject = subject.upper()

        if subject not in subjects:
            messagebox.showerror("Error", "Subject non existent.")

        info = [f"{k}: {v}" for k, v in self.subject_manager.subjects[subject].items()]

        total_minutes_completed = self.subject_manager.subjects[subject]['Total Minutes Completed']
        total_days_studied = self.subject_manager.subjects[subject]['Total Days Studied']

        if total_days_studied > 0:
            avg_time_studied = total_minutes_completed / total_days_studied
        else:
            avg_time_studied = total_minutes_completed

        hours = avg_time_studied // 60
        minutes = avg_time_studied % 60

        info.append(f"On Average you have studied {int(hours)}h and {int(minutes)}m per day!")

        messagebox.showinfo("Statistics", "\n".join(info))