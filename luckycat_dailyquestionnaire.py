import tkinter as tk
from datetime import datetime, time
import csv
import os

class PatientQuestionnaire:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Questionnaire")

        # Set the window size to match the screen resolution
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.current_question = 0
        self.user_responses = {}  # Dictionary to store user responses

        self.all_questions = [
            "HI MR. LI! Did you have a good day?",
            "Were you able to get some physical activity?",
            "Have you brushed your teeth & showered?",
            "Have you taken your medicine?",
            "Have you reached out to family/friends today?",
            "How is your physical pain (1 = No Pain, 5 = Painful)?",
            "What is your emotional level (1 = Happy, 5 = Sad)?"
        ]

        self.all_options = [
            ["Yes", "No"],
            ["Yes", "No"],
            ["Yes", "No"],
            ["Yes", "No"],
            ["Yes", "No"],
            [str(i) for i in range(1, 11)],
            [str(i) for i in range(1, 11)]
        ]

        # Update the options for the last two questions to "1-5" options
        self.all_options[-2] = [str(i) for i in range(1, 6)]  # 1-5 options for physical pain
        self.all_options[-1] = [str(i) for i in range(1, 6)]  # 1-5 options for emotional level

        # Adjust the font size for the question label
        question_label_font = ("Helvetica", 24)

        self.label_question = tk.Label(self.root, text="", font=question_label_font)
        self.label_question.pack(pady=20)

        # Create a variable to store the selected option
        self.option_var = tk.StringVar()

        # Make the buttons bigger
        button_width = 20
        button_height = 3

        self.button_back = tk.Button(self.root, text="Back", state=tk.DISABLED, command=self.show_previous_question,
                                     width=button_width, height=button_height, font=("Helvetica", 16))
        self.button_back.pack(side=tk.LEFT, padx=30, pady=20)

        self.button_next = tk.Button(self.root, text="Next", command=self.show_next_question,
                                     width=button_width, height=button_height, font=("Helvetica", 16))
        self.button_next.pack(side=tk.RIGHT, padx=30, pady=20)

        self.show_question()

    def show_question(self):
        question = self.all_questions[self.current_question]
        options = self.all_options[self.current_question]

        self.label_question.config(text=question)

        # Clear previous options
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()

        # Create radio buttons for each option with added vertical padding
        for option in options:
            tk.Radiobutton(self.root, text=option, variable=self.option_var, value=option, font=("Helvetica", 20), padx=20, pady=10).pack()

        self.option_var.set(self.user_responses.get(question, options[0]))

        if self.current_question == 0:
            self.button_back.config(state=tk.DISABLED)
        else:
            self.button_back.config(state=tk.NORMAL)

        if self.current_question == len(self.all_questions) - 1:
            self.button_next.config(text="Submit", command=self.submit_responses)
        else:
            self.button_next.config(text="Next", command=self.show_next_question)

    def show_next_question(self):
        question = self.all_questions[self.current_question]
        answer = self.option_var.get()

        self.user_responses[question] = answer  # Store the user's response

        if self.current_question < len(self.all_questions) - 1:
            self.current_question += 1
            self.show_question()
        else:
            # If it's the last question, directly call the submit_responses function
            self.submit_responses()

    def show_previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()

    def submit_responses(self):
        # Ensure the final answer is updated before printing responses
        final_question = self.all_questions[-1]
        self.user_responses[final_question] = self.option_var.get()

        responses = {
            "Submission Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **self.user_responses
        }

        # Print all responses
        for question, answer in responses.items():
            print(f"{question}: {answer}")

        # Save responses to CSV file
        self.save_to_csv(responses)

        # TODO: Save responses to a file or perform other actions

        self.root.destroy()

    def save_to_csv(self, responses):
        file_path = "patient_responses.csv"

        # Check if the file already exists
        is_new_file = not os.path.exists(file_path)

        with open(file_path, mode="a", newline="") as file:
            writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Write header if it's a new file
            if is_new_file:
                writer.writerow(responses.keys())

            # Write responses
            writer.writerow(responses.values())

def main():
    # Check if the current time is within the desired time range
    current_time = datetime.now().time()
    start_time = time(0, 0)  # Adjust the start time as needed
    end_time = time(23, 59)   # Adjust the end time as needed

    if start_time <= current_time <= end_time:
        root = tk.Tk()
        app = PatientQuestionnaire(root)
        root.mainloop()
    else:
        print("Not within the specified time range.")

if __name__ == "__main__":
    main()