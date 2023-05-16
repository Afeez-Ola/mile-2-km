from tkinter import *

window = Tk()

window.title("Mile to KM Converter")

window.minsize(width=500, height=300)
window.config(padx=60, pady=40)

mile_input = Entry()
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=0)

def converter():
    result_km = round((float(mile_input.get()) * 1.60934), 2)
    result2.config(text=result_km)


result1 = Label(text="Is equal to").grid(column=0, row=1)
result2 = Label(text=0)
result2.grid(column=1, row=1, ipadx=10, ipady=10)
text1 = Label(text="km").grid(column=3, row=1, ipadx=10, ipady=10)
button_km = Button(text="Convert", command=converter).grid(column=1, row=3)

window.mainloop()
