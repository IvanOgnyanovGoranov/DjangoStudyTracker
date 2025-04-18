from tkinter import messagebox

# To replace the message box
class Timer:
    def __init__(self, window, timer_label):
        self.window = window
        self.timer_label = timer_label
        self.timer_running = False
        self.elapsed_time = 0
        self.session_time = 60 * 60

    def start_timer(self):
        """Starts the timer if it's on zero, stopped or under 60 minutes."""
        if not self.timer_running and self.elapsed_time <= self.session_time:
            self.timer_running = True
            self.count_up()
        elif self.elapsed_time > self.session_time:
            messagebox.showinfo("Session Time", "You have reached the time limit! You have to either reset the timer or add the time to your goal.")

    def count_up(self):
        if self.timer_running:
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.elapsed_time += 1
            if self.elapsed_time <= self.session_time:
                self.window.after(1000, self.count_up)  # Continue every second
            else:
                self.timer_running = False
                # You can prompt the user here if needed

    def reset_timer(self, reset=False):
        """Resets the timer on zero."""
        self.stop_timer()

        if not reset:
            reset = messagebox.askyesno("Reset Timer", "Are you sure you want to reset the timer? If you reset it you cannot add it to your goals!")

        if reset:
            self.elapsed_time = 0
            self.timer_label.config(text="00:00")

    def stop_timer(self):
        """Stops the timer."""
        self.timer_running = False