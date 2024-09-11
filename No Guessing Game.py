import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        self.root.geometry("400x300")  # Fixed window size
        self.root.configure(bg="#f0f4f7")  # Light background color

        # Generate a random number between 1 and 100
        self.number_to_guess = random.randint(1, 100)
        self.attempts_left = 10

        # Title Frame
        self.title_frame = tk.Frame(self.root, bg="#007bff", pady=10)
        self.title_frame.pack(fill="x")

        self.label_title = tk.Label(self.title_frame, text="Guess the Number", font=("Helvetica", 16, "bold"), bg="#007bff", fg="white")
        self.label_title.pack()

        # Main Game Frame
        self.game_frame = tk.Frame(self.root, bg="#f0f4f7", pady=20)
        self.game_frame.pack()

        # Message Label
        self.label_message = tk.Label(self.game_frame, text="Guess a number between 1 and 100", font=("Arial", 12), bg="#f0f4f7")
        self.label_message.grid(row=0, column=0, columnspan=2, pady=10)

        # Guess Entry
        self.entry_guess = tk.Entry(self.game_frame, font=("Arial", 14), width=10, justify='center')
        self.entry_guess.grid(row=1, column=0, padx=10, pady=10)

        # Submit Button
        self.button_submit = tk.Button(self.game_frame, text="Submit Guess", font=("Arial", 12), bg="#28a745", fg="white", command=self.check_guess)
        self.button_submit.grid(row=1, column=1, padx=10, pady=10)

        # Attempts Label
        self.label_attempts = tk.Label(self.game_frame, text=f"Attempts left: {self.attempts_left}", font=("Arial", 12), bg="#f0f4f7")
        self.label_attempts.grid(row=2, column=0, columnspan=2, pady=10)

        # Feedback Label
        self.label_feedback = tk.Label(self.game_frame, text="", font=("Arial", 12, "italic"), bg="#f0f4f7", fg="#ff0000")
        self.label_feedback.grid(row=3, column=0, columnspan=2, pady=10)

        # Reset Button (Initially hidden)
        self.button_reset = tk.Button(self.game_frame, text="Play Again", font=("Arial", 12), bg="#007bff", fg="white", command=self.reset_game)
        self.button_reset.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_reset.grid_remove()

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
        except ValueError:
            self.label_feedback.config(text="Please enter a valid number!", fg="#ff0000")
            return

        if guess < self.number_to_guess:
            self.label_feedback.config(text="Too low!", fg="#ff0000")
        elif guess > self.number_to_guess:
            self.label_feedback.config(text="Too high!", fg="#ff0000")
        else:
            self.label_feedback.config(text=f"Correct! The number was {self.number_to_guess}.", fg="#28a745")
            self.end_game()
            return

        self.attempts_left -= 1
        self.label_attempts.config(text=f"Attempts left: {self.attempts_left}")

        if self.attempts_left == 0:
            self.label_feedback.config(text=f"Game over! The number was {self.number_to_guess}.", fg="#ff0000")
            self.end_game()

    def end_game(self):
        self.button_submit.config(state=tk.DISABLED)
        self.button_reset.grid()

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts_left = 10
        self.entry_guess.delete(0, tk.END)
        self.label_feedback.config(text="")
        self.label_attempts.config(text=f"Attempts left: {self.attempts_left}")
        self.button_submit.config(state=tk.NORMAL)
        self.button_reset.grid_remove()

# Create the main window
root = tk.Tk()
game = GuessNumberGame(root)

# Start the Tkinter event loop
root.mainloop()
