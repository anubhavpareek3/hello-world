import tkinter as tk

window = tk.Tk()
window.title("Addess Entry Form")

frame = tk.Frame(master=window, relief=tk.SUNKEN, bg="#F0F0F0", borderwidth=3)
frame.pack()

label = tk.Label(master=frame, text="First Name:")
entry = tk.Entry(master=frame,width=50)
label.grid(row=0, column=0, sticky="e")
entry.grid(row=0, column=1)

label2 = tk.Label(master=frame, text="Last Name:")
entry2 = tk.Entry(master=frame, width=50)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)

label3 = tk.Label(master=frame, text="Address Line 1:")
entry3 = tk.Entry(master=frame, width=50)
label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)

label4 = tk.Label(master=frame, text="Address Line 2:")
entry4 = tk.Entry(master=frame, width=50)
label4.grid(row=3, column=0)
entry4.grid(row=3, column=1)

label5 = tk.Label(master=frame, text="City:")
entry5 = tk.Entry(master=frame, width=50)
label5.grid(row=4, column=0)
entry5.grid(row=4, column=1)

label6 = tk.Label(master=frame, text="State/Province:")
entry6 = tk.Entry(master=frame, width=50)
label6.grid(row=5, column=0)
entry6.grid(row=5, column=1)

label7 = tk.Label(master=frame, text="Postal Code:")
entry7 = tk.Entry(master=frame, width=50)
label7.grid(row=6, column=0)
entry7.grid(row=6, column=1)

label8 = tk.Label(master=frame, text="Country:")
entry8 = tk.Entry(master=frame, width=50)
label8.grid(row=7, column=0)
entry8.grid(row=7, column=1)

buttonframe = tk.Frame(master=window)
buttonframe.pack(fill=tk.X, ipadx=5, ipady=5)

button = tk.Button(master=buttonframe, text="Submit")
button.pack(side=tk.RIGHT,padx=10, ipadx=10)

button2 = tk.Button(master=buttonframe, text="Clear")
button2.pack(side=tk.RIGHT, ipadx=10)


window.mainloop()