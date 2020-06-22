import tkinter as tk

def converter():
    celsius = 5/9*(float(temperature_entry.get())-32)
    result_label["text"] = f"{round(celsius, 2)}"


window = tk.Tk()
window.title("Temperature converter")
window.rowconfigure(0, minsize=30, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=30, weight=1)

temperature_entry = tk.Entry(master=window, width=10)
temperature_entry.grid(row=0, column=0)

fahrenit_label = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")
fahrenit_label.grid(row=0, column=1)

converter_button = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=converter)
converter_button.grid(row=0, column=2)

result_label = tk.Label(master=window, text="0.0")
result_label.grid(row=0, column=3)

celsius_label = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
celsius_label.grid(row=0, column=4)
window.mainloop()