from tkinter import *

window = Tk()
window.config(width=300, height=200)
window.title("Miles to KM converter")

miles_label = Label(text="Miles")
miles_label.place(x=200, y=52)

km_label = Label(text="Km")
km_label.place(x=200, y=100)

is_equal = Label(text="is equal to")
is_equal.place(x=65, y=100)

miles_input = Entry(width=5, )
miles_input.place(x=140, y=50)

result_label = Label()
result_label.place(x=150, y=100)


def button_clicked():
    click = float(miles_input.get())
    result = int(click * 1.60934)
    result_label.config(text=result)


calculate_button = Button(text="calculate", command=button_clicked)
calculate_button.place(x=115, y=150)



window.mainloop()
