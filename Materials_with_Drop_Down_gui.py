import tkinter as tk  # import tkinter as tk
from tkinter import *  # from tkinter import *

#from ttk import * 

#############################################################################################

#Diameter_of_Shaft = 55 #comes from test of shearing of shaft


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
mainframe.pack(pady = 60, padx = 100) #controls fixed gap inbetween main content and edges, pady for y padx for x

# Create a Tkinter variable
tkvar1 = StringVar(root) #this is where value selected by user is stored #Material Designation
tkvar2 = StringVar(root) #this is where value selected by user is stored #Condition
tkvar3 = StringVar(root) #this is where value selected by user is stored #Tensile or Yield

# Dictionary with options

#carbon steel material(Mild Steel) for shaft, key & bolt
mat_des = ['C 14','C 15','C 15 Mn 75','C 20','C 30','C 35','C 35 Mv 75', 'C 40','C 45','C 50','C 55 Mn 75','C 55 Cr 75']
mat_cond = ['Annealed','Tempered','Hardened & tempered']

#Cast Iron Material for Flange
mat_flang = ['GCI 15','GCI 20','GCI 25','MCI B', 'MCI A']

#tkvar1.set('C 40') # set the default option

popupMenu_mat_des = OptionMenu(mainframe, tkvar1, *mat_des)
popupMenu_mat_cond = OptionMenu(mainframe, tkvar2, *mat_cond)
popupMenu_mat_flang = OptionMenu(mainframe, tkvar3, *mat_flang)

Label(mainframe, text="Choose Material Designation for Shaft/Bolt/Keys").grid(row = 1, column = 1) #controls position of name of popup grid
popupMenu_mat_des.grid(row = 1, column =2) #controls position of popup grid

Label(mainframe, text="Choose Material Condition for Shaft/Bolt/Keys").grid(row = 2, column = 1) #controls position of name of popup grid
popupMenu_mat_cond.grid(row = 2, column =2) #controls position of popup grid

Label(mainframe, text="Choose Material Designation for Flange").grid(row = 3, column = 1) #controls position of name of popup grid
popupMenu_mat_flang.grid(row = 3, column =2) #controls position of popup grid


b1 = tk.Button(mainframe,  text='Submit', command=lambda: my_show() )  
b1.grid(row=4,column=1) 


str_out=tk.StringVar(root)
str_out.set("Output")


#l2 = tk.Label(my_w,  textvariable=str_out, width=10 )  
#l2.grid(row=2,column=4) 


def my_show():
    #str_out.set(options1.get())
    print(tkvar1.get())
    print(tkvar2.get())

    ##########################################################################

    #C14 Section
    if tkvar1.get() == 'C 14' and tkvar2.get() == 'Annealed':
        Yield_Shaft = 190

    if tkvar1.get() == 'C 14' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 380

    if tkvar1.get() == 'C 14' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = "Not Available"

    #C15 Section
    if tkvar1.get() == 'C 15' and tkvar2.get() == 'Annealed':
        Yield_Shaft = 190

    if tkvar1.get() == 'C 15' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 280

    if tkvar1.get() == 'C 15' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = "Not Available"

    #C15 Mn 75 Section
    if tkvar1.get() == 'C 15 Mn 75' and tkvar2.get() == 'Annealed':
        Yield_Shaft = 190

    if tkvar1.get() == 'C 15 Mn 75' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 380

    if tkvar1.get() == 'C 15 Mn 75' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = "Not Available"

    #C20 Section
    if tkvar1.get() == 'C 20' and tkvar2.get() == 'Annealed':
        Yield_Shaft = 220

    if tkvar1.get() == 'C 20' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 420

    if tkvar1.get() == 'C 20' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = "Not Available"

    #C30 Section
    if tkvar1.get() == 'C 30' and tkvar2.get() == 'Annealed':
        Yield_Shaft = "Not Available"

    if tkvar1.get() == 'C 30' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 400

    if tkvar1.get() == 'C 30' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = "Not Available"

    #C35 Section
    if tkvar1.get() == 'C 35' and tkvar2.get() == 'Annealed':
        Yield_Shaft = 280

    if tkvar1.get() == 'C 35' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 500

    if tkvar1.get() == 'C 35' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = "Not Available"

    #C 35 Mv 75 Section
    if tkvar1.get() == 'C 35 Mv 75' and tkvar2.get() == 'Annealed':
        Yield_Shaft = 280

    if tkvar1.get() == 'C 35 Mv 75' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 500

    if tkvar1.get() == 'C 35 Mv 75' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = 400

    #C40 Section
    if tkvar1.get() == 'C 40' and tkvar2.get() == 'Annealed':
        Yield_Shaft = "Not Available"

    if tkvar1.get() == 'C 40' and tkvar2.get() == 'Tempered':
        Yield_Shaft = "Not Available"

    if tkvar1.get() == 'C 40' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = 380

    #C45 Section
    if tkvar1.get() == 'C 45' and tkvar2.get() == 'Annealed':
        Yield_Shaft = 340

    if tkvar1.get() == 'C 45' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 600

    if tkvar1.get() == 'C 45' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = 380

    #C50 Section
    if tkvar1.get() == 'C 50' and tkvar2.get() == 'Annealed':
        Yield_Shaft = 340

    if tkvar1.get() == 'C 50' and tkvar2.get() == 'Tempered':
        Yield_Shaft = 600

    if tkvar1.get() == 'C 50' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = 460

    #C55 Mn75 Section
    if tkvar1.get() == 'C 55 Mn 75' and tkvar2.get() == 'Annealed':
        Yield_Shaft = "Not Available"

    if tkvar1.get() == 'C 55 Mn 75' and tkvar2.get() == 'Tempered':
        Yield_Shaft = "Not Available"

    if tkvar1.get() == 'C 55 Mn 75' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = 460

    #C55 Cr75 Section
    if tkvar1.get() == 'C 55 Mn 75' and tkvar2.get() == 'Annealed':
        Yield_Shaft = "Not Available"

    if tkvar1.get() == 'C 55 Mn 75' and tkvar2.get() == 'Tempered':
        Yield_Shaft = "Not Available"

    if tkvar1.get() == 'C 55 Mn 75' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = 660

    print(" Yield Strength of Shaft/Bolts/Keys is ",Yield_Shaft)
    
    if tkvar3.get() == 'GCI 15':
        Yield_Flange = 150

    if tkvar3.get() == 'GCI 20':
        Yield_Flange = 200

    if tkvar3.get() == 'GCI 25':
        Yield_Flange = 250

    if tkvar3.get() == 'MCI B':
        Yield_Flange = 320

    if tkvar3.get() == 'MCI A':
        Yield_Flange = 400    

    print(" Yield Strength of Flange is ",Yield_Flange)
    ##########################################################################


root.mainloop()

#print("dict of Shaft is",my_dict[Diameter_of_Shaft]) # prints height
#print my_dict.get(argument, "Invalid month")
