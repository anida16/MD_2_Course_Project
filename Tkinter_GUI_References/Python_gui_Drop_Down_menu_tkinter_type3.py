import tkinter as tk

my_w = tk.Tk()
my_w.geometry("500x400")  # Size of the window 
my_w.title("Material Data")  # Adding a title

options1 = tk.StringVar(my_w)
options2 = tk.StringVar(my_w)
#options.set("One") # default value

l1 = tk.Label(my_w,  text='Choose Material Designation', width=10 )  
l1.grid(row=2,column=4) 

om1 =tk.OptionMenu(my_w, options1, 'C 14','C 15','C 15 Mn 75','C 20','C 30','C 35','C 35 Mv 75', 'C 40','C 45','C 50','C 55 Mn 75','C 55 Cr 75')
om1.grid(row=2,column=5) 

om2 =tk.OptionMenu(my_w, options2, 'Annealed','Tempered','Hardened & tempered')
om2.grid(row=3,column=5) 

b1 = tk.Button(my_w,  text='Submit', command=lambda: my_show() )  
b1.grid(row=4,column=5) 

str_out=tk.StringVar(my_w)
str_out.set("Output")

#l2 = tk.Label(my_w,  textvariable=str_out, width=10 )  
#l2.grid(row=2,column=4) 


def my_show():
    #str_out.set(options1.get())
    print(options1.get())
    print(options2.get())

my_w.mainloop()