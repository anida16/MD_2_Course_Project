import tkinter as tk  # import tkinter as tk
from tkinter import *  # from tkinter import *

#from ttk import * 

#############################################################################################

#Diameter_of_Shaft = 55 #comes from test of shearing of shaft
#carbon steel material(Mild Steel) for shaft, key & bolt

#Material_for_Shaft = dict({
#    'C07': 340,
#    'C30': 400,
#    'C30': 400
#})

#def my_dict(argument):
#my_dict = dict([(1,'apple'), (2,'ball')])

#Emperical relations

#library for selecting key dimensions (width & breath)


#############################################################################################

root = Tk()
root.title("Material Selection")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100) #controls fixed gap inbetween main content and edges, pady for y padx for x

# Create a Tkinter variable
tkvar1 = StringVar(root) #this is where value selected by user is stored #Material Designation
tkvar2 = StringVar(root) #this is where value selected by user is stored #Condition
#tkvar3 = StringVar(root) #this is where value selected by user is stored #Tensile or Yield

# Dictionary with options

mat_des = ['C 14','C 15','C 15 Mn 75','C 20','C 30','C 35','C 35 Mv 75', 'C 40','C 45','C 50','C 55 Mn 75','C 55 Cr 75']
mat_cond = ['Annealed','Tempered','Hardened & tempered']
#mat_stre = ['Tensile Strength','Yield Strength']

#tkvar1.set('C 40') # set the default option

popupMenu_mat_des = OptionMenu(mainframe, tkvar1, *mat_des)
popupMenu_mat_cond = OptionMenu(mainframe, tkvar2, *mat_cond)
#popupMenu_mat_stre = OptionMenu(mainframe, tkvar3, *mat_stre)

Label(mainframe, text="Choose Material Designation").grid(row = 1, column = 1) #controls position of name of popup grid
popupMenu_mat_des.grid(row = 1, column =2) #controls position of popup grid

Label(mainframe, text="Choose Material Condition").grid(row = 2, column = 1) #controls position of name of popup grid
popupMenu_mat_cond.grid(row = 2, column =2) #controls position of popup grid

#Label(mainframe, text="Choose Strength (Yield Recommended)").grid(row = 3, column = 1) #controls position of name of popup grid
#popupMenu_mat_stre.grid(row = 3, column =2) #controls position of popup grid

# on change dropdown value
def change_dropdown1(*args):
    #print( tkvar1.get() )
    return ( tkvar1.get() )

    #if tkvar1.get() == 'C 14' and tkvar2.get() == 'Annealed':
    #    Yield = 190
    #return Yield
   
def change_dropdown2(*args):
    #print( tkvar2.get() )
    return ( tkvar2.get() )
    #print( tkvar3.get() )

    #if tkvar1.get() == 'C 14' and tkvar2.get() == 'Tempered':
    #    Yield = 380
    #return Yield


# link function to change dropdown
tkvar1.trace('w', change_dropdown1)
tkvar2.trace('w', change_dropdown2)
#tkvar3.trace('w', change_dropdown)

print(change_dropdown1())
print(change_dropdown2())

root.mainloop()

#print("dict of Shaft is",my_dict[Diameter_of_Shaft]) # prints height
#print my_dict.get(argument, "Invalid month")
