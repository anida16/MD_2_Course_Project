import tkinter as tk  # import tkinter as tk
from tkinter import *  # from tkinter import *
import numpy as np
import math

class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range): # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item) # or super(RangeDict, self) for Python 2


#from ttk import * 

root = Tk()
root.title("Input required Data for Designing")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 60, padx = 50) #controls fixed gap inbetween main content and edges, pady for y padx for x

# Create a Tkinter variable
tkvar1 = StringVar(root) #this is where value selected by user is stored #Material Designation
tkvar2 = StringVar(root) #this is where value selected by user is stored #Condition
tkvar3 = StringVar(root)
tkvar4 = StringVar(root)
tkvar5 = StringVar(root) 

# Dictionary with options

#carbon steel material(Mild Steel) for shaft, key & bolt
mat_des = ['C 14','C 15','C 15 Mn 75','C 20','C 30','C 35','C 35 Mv 75', 'C 40','C 45','C 50','C 55 Mn 75','C 55 Cr 75']
mat_cond = ['Annealed','Tempered','Hardened & tempered']

#Cast Iron Material for Flange
mat_flang = ['GCI 15','GCI 20','GCI 25','MCI B', 'MCI A']

#tkvar1.set('C 40') # set the default option

popupMenu_mat_des = OptionMenu(mainframe, tkvar1, *mat_des)
popupMenu_mat_cond = OptionMenu(mainframe, tkvar2, *mat_cond)
popupMenu_mat_des2 = OptionMenu(mainframe, tkvar4, *mat_des)
popupMenu_mat_cond2 = OptionMenu(mainframe, tkvar5, *mat_cond)
popupMenu_mat_flang = OptionMenu(mainframe, tkvar3, *mat_flang)

Label(mainframe, text="Enter Power").grid(row = 1, column = 1)
entry1 = tk.Entry (mainframe) #power
entry1.grid(row=1, column=2)

Label(mainframe, text="Enter Speed").grid(row = 2, column = 1)
entry2 = tk.Entry (mainframe) #speed
entry2.grid(row=2, column=2)

Label(mainframe, text="Enter FoS for Shaft").grid(row = 3, column = 1)
entry3 = tk.Entry (mainframe) #FoS for Shaft
entry3.grid(row=3, column=2)

Label(mainframe, text="Enter FoS for Flange").grid(row = 4, column = 1)
entry4 = tk.Entry (mainframe) #FoS for Flange
entry4.grid(row=4, column=2)

Label(mainframe, text="Enter FoS for Key & Bolt").grid(row = 5, column = 1)
entry5 = tk.Entry (mainframe) #FoS for Key & Bolt
entry5.grid(row=5, column=2)

Label(mainframe, text="Enter Service Factor").grid(row = 6, column = 1)
entry6 = tk.Entry (mainframe) #Service Factor
entry6.grid(row=6, column=2)

Label(mainframe, text="Choose Material Designation for Shaft").grid(row = 7, column = 1) #controls position of name of popup grid
popupMenu_mat_des.grid(row = 7, column =2) #controls position of popup grid

Label(mainframe, text="Choose Material Condition for Shaft").grid(row = 8, column = 1) #controls position of name of popup grid
popupMenu_mat_cond.grid(row = 8, column =2) #controls position of popup grid

Label(mainframe, text="Choose Material Designation for Key & Bolt").grid(row = 9, column = 1) #controls position of name of popup grid
popupMenu_mat_des2.grid(row = 9, column =2) #controls position of popup grid

Label(mainframe, text="Choose Material Condition for Key & Bolt").grid(row = 10, column = 1) #controls position of name of popup grid
popupMenu_mat_cond2.grid(row = 10, column =2) #controls position of popup grid

Label(mainframe, text="Choose Material Designation for Flange").grid(row = 11, column = 1) #controls position of name of popup grid
popupMenu_mat_flang.grid(row = 11, column =2) #controls position of popup grid

b1 = tk.Button(mainframe,  text='Submit', command=lambda: my_show() )  
b1.grid(row=12,column=1) 

str_out=tk.StringVar(root)
str_out.set("Output")


#l2 = tk.Label(my_w,  textvariable=str_out, width=10 )  
#l2.grid(row=2,column=4) 


def my_show():
    #str_out.set(options1.get())
    #print(tkvar1.get())
    #print(tkvar2.get())

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
        Yield_Shaft = "Not Available"

    if tkvar1.get() == 'C 30' and tkvar2.get() == 'Hardened & tempered':
        Yield_Shaft = 400

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

    #print(" Yield Strength of Shaft is ",Yield_Shaft)
    
    #########################################################################################

    #C14 Section
    if tkvar4.get() == 'C 14' and tkvar5.get() == 'Annealed':
        Yield_Bolt = 190

    if tkvar4.get() == 'C 14' and tkvar5.get() == 'Tempered':
        Yield_Bolt = 380

    if tkvar4.get() == 'C 14' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = "Not Available"

    #C15 Section
    if tkvar4.get() == 'C 15' and tkvar5.get() == 'Annealed':
        Yield_Bolt = 190

    if tkvar4.get() == 'C 15' and tkvar5.get() == 'Tempered':
        Yield_Bolt = 280

    if tkvar4.get() == 'C 15' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = "Not Available"

    #C15 Mn 75 Section
    if tkvar4.get() == 'C 15 Mn 75' and tkvar5.get() == 'Annealed':
        Yield_Bolt = 190

    if tkvar4.get() == 'C 15 Mn 75' and tkvar5.get() == 'Tempered':
        Yield_Bolt = 380

    if tkvar4.get() == 'C 15 Mn 75' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = "Not Available"

    #C20 Section
    if tkvar4.get() == 'C 20' and tkvar5.get() == 'Annealed':
        Yield_Bolt = 220

    if tkvar4.get() == 'C 20' and tkvar5.get() == 'Tempered':
        Yield_Bolt = 420

    if tkvar4.get() == 'C 20' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = "Not Available"

    #C30 Section
    if tkvar4.get() == 'C 30' and tkvar5.get() == 'Annealed':
        Yield_Bolt = "Not Available"

    if tkvar4.get() == 'C 30' and tkvar5.get() == 'Tempered':
        Yield_Bolt = "Not Available"

    if tkvar4.get() == 'C 30' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = 400

    #C35 Section
    if tkvar4.get() == 'C 35' and tkvar5.get() == 'Annealed':
        Yield_Bolt = 280

    if tkvar4.get() == 'C 35' and tkvar5.get() == 'Tempered':
        Yield_Bolt = 500

    if tkvar4.get() == 'C 35' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = "Not Available"

    #C 35 Mv 75 Section
    if tkvar4.get() == 'C 35 Mv 75' and tkvar5.get() == 'Annealed':
        Yield_Bolt = 280

    if tkvar4.get() == 'C 35 Mv 75' and tkvar5.get() == 'Tempered':
        Yield_Bolt = 500

    if tkvar4.get() == 'C 35 Mv 75' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = 400

    #C40 Section
    if tkvar4.get() == 'C 40' and tkvar5.get() == 'Annealed':
        Yield_Bolt = "Not Available"

    if tkvar4.get() == 'C 40' and tkvar5.get() == 'Tempered':
        Yield_Bolt = "Not Available"

    if tkvar4.get() == 'C 40' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = 380

    #C45 Section
    if tkvar4.get() == 'C 45' and tkvar5.get() == 'Annealed':
        Yield_Bolt = 340

    if tkvar4.get() == 'C 45' and tkvar5.get() == 'Tempered':
        Yield_Bolt = 600

    if tkvar4.get() == 'C 45' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = 380

    #C50 Section
    if tkvar4.get() == 'C 50' and tkvar5.get() == 'Annealed':
        Yield_Bolt = 340

    if tkvar4.get() == 'C 50' and tkvar5.get() == 'Tempered':
        Yield_Bolt = 600

    if tkvar4.get() == 'C 50' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = 460

    #C55 Mn75 Section
    if tkvar4.get() == 'C 55 Mn 75' and tkvar5.get() == 'Annealed':
        Yield_Bolt = "Not Available"

    if tkvar4.get() == 'C 55 Mn 75' and tkvar5.get() == 'Tempered':
        Yield_Bolt = "Not Available"

    if tkvar4.get() == 'C 55 Mn 75' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = 460

    #C55 Cr75 Section
    if tkvar4.get() == 'C 55 Mn 75' and tkvar5.get() == 'Annealed':
        Yield_Bolt = "Not Available"

    if tkvar4.get() == 'C 55 Mn 75' and tkvar5.get() == 'Tempered':
        Yield_Bolt = "Not Available"

    if tkvar4.get() == 'C 55 Mn 75' and tkvar5.get() == 'Hardened & tempered':
        Yield_Bolt = 660

    #print(" Yield Strength of Bolts/Keys is ",Yield_Bolt)

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

    #print(" Yield Strength of Flange is ",Yield_Flange)
    ##########################################################################

    Power = entry1.get()
    #print(Power)

    Speed = entry2.get()
    #print(Speed)

    FoS_Shaft = entry3.get()
    #print(FoS_Shaft)

    FoS_Flange = entry4.get()
    #print(FoS_Flange)

    FoS_Bolt = entry5.get()
    #print(FoS_Bolt)

    Service_factor = entry6.get()
    #print(Service_factor)

    ##########################################################################

    #Calculations start here
    #Permissible stresses

    Shear_Shaft = (0.5*Yield_Shaft)/float(FoS_Shaft)
    Shear_Flange = (0.5*Yield_Flange)/float(FoS_Flange)
    Shear_Bolt = (0.5*Yield_Bolt)/float(FoS_Bolt)
    #print(Shear_Bolt)
    #print(Shear_Flange)
    #print(Shear_Shaft)

    #Torque Calculations
    Torque = (60 * float(Power) * 1000)/(2 * np.pi * float(Speed))
    Max_Torque = float(Service_factor) * Torque
    print("Max Torque is ",Max_Torque)

    #Diameter Calculations
    Float_Diameter_of_Shaft = ((16 * Max_Torque)/(Shear_Shaft * np.pi))**(1/3)
    Diameter_of_Shaft = math.ceil(Float_Diameter_of_Shaft/ 2.) * 2
    print(Float_Diameter_of_Shaft)
    print("Diameter of shaft is ",Diameter_of_Shaft)

    #Key Selection

    width_check = RangeDict({
        range(6,9): 2, 
        range(9,11): 3,
        range(11,13): 4, 
        range(13,18): 5,
        range(18,23): 6, 
        range(23,31): 8,
        range(31,39): 10, 
        range(39,45): 12,
        range(45,51): 14, 
        range(51,59): 16,
        range(59,66): 18, 
        range(66,76): 20,
        range(76,86): 22, 
        range(86,96): 25,
        range(96,111): 28, 
        range(111,131): 32,
        range(131,151): 36, 
        range(151,171): 40,
        range(171,201): 45, 
        range(201,231): 50,
        range(231,261): 56, 
        range(261,291): 63,
        range(291,331): 70, 
        range(331,381): 80,
        range(381,441): 90, 
        range(441,501): 100
        })
    width_key = width_check[Diameter_of_Shaft]

    height_check = RangeDict({
        range(6,9): 2, 
        range(9,11): 3,
        range(11,13): 4, 
        range(13,18): 5,
        range(18,23): 6, 
        range(23,31): 7,
        range(31,39): 8, 
        range(39,45): 8,
        range(45,51): 9, 
        range(51,59): 10,
        range(59,66): 11, 
        range(66,76): 12,
        range(76,86): 14, 
        range(86,96): 14,
        range(96,111): 16, 
        range(111,131): 18,
        range(131,151): 20, 
        range(151,171): 22,
        range(171,201): 25, 
        range(201,231): 28,
        range(231,261): 32, 
        range(261,291): 32,
        range(291,331): 36, 
        range(331,381): 40,
        range(381,441): 45, 
        range(441,501): 50
        })
    height_key = height_check[Diameter_of_Shaft]

    Float_length_key = 1.5 * Diameter_of_Shaft
    length_key = math.ceil(Float_length_key/ 2.) * 2


    print("Width of Key is",width_key) # prints width
    print("Height of Key is",height_key) # prints height
    print("Length of Key is",length_key) # prints length


    



root.mainloop()

#print("dict of Shaft is",my_dict[Diameter_of_Shaft]) # prints height
#print my_dict.get(argument, "Invalid month")
