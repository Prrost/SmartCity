import tkinter as tk
from tkinter import messagebox

def create_ui(predict_function):
    def on_predict():
        try:
            input_length = float(entry_length.get())
            predicted_time = predict_function(input_length)
            result_label.config(text=f"Predicted run time for {input_length} km: {predicted_time:.2f} seconds")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for length.")

    # Создаем интерфейс
    root = tk.Tk()
    root.title("Run Time Prediction")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label_length = tk.Label(frame, text="Enter length (km):")
    label_length.grid(row=0, column=0, padx=5, pady=5)

    entry_length = tk.Entry(frame)
    entry_length.grid(row=0, column=1, padx=5, pady=5)

    predict_button = tk.Button(frame, text="Predict", command=on_predict)
    predict_button.grid(row=1, column=0, columnspan=2, pady=10)

    result_label = tk.Label(frame, text="")
    result_label.grid(row=2, column=0, columnspan=2, pady=5)

    root.mainloop()