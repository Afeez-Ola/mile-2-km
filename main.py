from tkinter import Tk, Label, Entry, Button

def convert_miles_to_km():
    miles = float(mile_input.get())
    kilometers = round(miles * 1.60934, 2)
    result2.config(text=kilometers)

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=60, pady=40)

mile_input = Entry()
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=0)

result1 = Label(text="Is equal to")
result1.grid(column=0, row=1)

result2 = Label(text="")
result2.grid(column=1, row=1, ipadx=10, ipady=10)

text1 = Label(text="km")
text1.grid(column=3, row=1, ipadx=10, ipady=10)

button_km = Button(text="Convert", command=convert_miles_to_km)
button_km.grid(column=1, row=3)

window.mainloop()

