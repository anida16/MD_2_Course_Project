import tkinter as tk
my_w = tk.Tk()
my_w.geometry("250x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
# create the dictionary
my_dict1={1: 'Fruits', 2: 'Colors', 3: 'Games', 4: 'Vehicles'}

options = tk.StringVar(my_w) # variable 
options.set(my_dict1[1]) # default value

om1 =tk.OptionMenu(my_w, options, *my_dict1.values())
om1.grid(row=2,column=5)

def my_show(*args):  # on select function 
    for i,j in my_dict1.items():
        if j==options.get():
            print(i)            

options.trace('w',my_show)
my_w.mainloop()