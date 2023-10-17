import tkinter as tk
from PIL import Image, ImageTk


def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    result = num1 * num2

    result_label.config(text=f"Result: {result}")


#App Menu

root = tk.Tk()
root.title("Budget App")

bottom_frame = tk.Frame(root,bg="lightgreen")
bottom_frame.pack(side="bottom", fill="both", expand=True)

gif_image = Image.open("malpa.gif")
gif_photo = ImageTk.PhotoImage(gif_image,)

gif_label = tk.Label(bottom_frame, image=gif_photo, bg="lightgreen")
gif_label.pack()

root.configure(bg="lightgreen")

root.geometry("600x500")

label = tk.Label(root, text="Budget App", font=("Helvetica, 16"), bg="lightgreen")
label.pack()

label = tk.Label(root, text="How many days are you working?", bg="lightgreen")
label.pack()

entry1 = tk.Entry(root)
entry1.pack()

label = tk.Label(root, text="How much money you make per day?", bg="lightgreen")
label.pack()

entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="Calculate Salary", command=calculate, bg="green")
calculate_button.pack()

result_label = tk.Label(root, text="",bg="lightgreen")
result_label.pack()


root.mainloop()

