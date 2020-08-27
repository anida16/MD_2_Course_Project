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

def range_index(table, val):
    for (k1, k2) in table:
        if k1 <= val < k2:
            return table[(k1, k2)]

#from ttk import * 

root_1 = Tk()
root_1.title("Input required Data for Designing")


# Add a grid for Input
mainframe1 = Frame(root_1)
mainframe1.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe1.columnconfigure(0, weight = 1)
mainframe1.rowconfigure(0, weight = 1)
mainframe1.pack(pady = 60, padx = 50) #controls fixed gap inbetween main content and edges, pady for y padx for x


# Create a Tkinter variable
tkvar1 = StringVar(root_1) #this is where value selected by user is stored #Material Designation
tkvar2 = StringVar(root_1) #this is where value selected by user is stored #Condition
tkvar3 = StringVar(root_1)
tkvar4 = StringVar(root_1)
tkvar5 = StringVar(root_1) 

# Dictionary with options

#carbon steel material(Mild Steel) for shaft, key & bolt
mat_des = ['C 14','C 15','C 15 Mn 75','C 20','C 30','C 35','C 35 Mv 75', 'C 40','C 45','C 50','C 55 Mn 75','C 55 Cr 75']
mat_cond = ['Annealed','Tempered','Hardened & tempered']

#Cast Iron Material for Flange
mat_flang = ['GCI 15','GCI 20','GCI 25','MCI B', 'MCI A']

#tkvar1.set('C 40') # set the default option

popupMenu_mat_des = OptionMenu(mainframe1, tkvar1, *mat_des)
popupMenu_mat_cond = OptionMenu(mainframe1, tkvar2, *mat_cond)
popupMenu_mat_des2 = OptionMenu(mainframe1, tkvar4, *mat_des)
popupMenu_mat_cond2 = OptionMenu(mainframe1, tkvar5, *mat_cond)
popupMenu_mat_flang = OptionMenu(mainframe1, tkvar3, *mat_flang)

Label(mainframe1, text="Enter Power (in W)").grid(row = 1, column = 1)
entry1 = tk.Entry (mainframe1) #power
entry1.grid(row=1, column=2)

Label(mainframe1, text="Enter Speed (in RPM)").grid(row = 2, column = 1)
entry2 = tk.Entry (mainframe1) #speed
entry2.grid(row=2, column=2)

Label(mainframe1, text="Enter FoS for Shaft").grid(row = 3, column = 1)
entry3 = tk.Entry (mainframe1) #FoS for Shaft
entry3.grid(row=3, column=2)

Label(mainframe1, text="Enter FoS for Flange").grid(row = 4, column = 1)
entry4 = tk.Entry (mainframe1) #FoS for Flange
entry4.grid(row=4, column=2)

Label(mainframe1, text="Enter FoS for Key & Bolt").grid(row = 5, column = 1)
entry5 = tk.Entry (mainframe1) #FoS for Key & Bolt
entry5.grid(row=5, column=2)

Label(mainframe1, text="Enter Service Factor").grid(row = 6, column = 1)
entry6 = tk.Entry (mainframe1) #Service Factor
entry6.grid(row=6, column=2)

Label(mainframe1, text="Choose Material Designation for Shaft").grid(row = 7, column = 1) #controls position of name of popup grid
popupMenu_mat_des.grid(row = 7, column =2) #controls position of popup grid

Label(mainframe1, text="Choose Material Condition for Shaft").grid(row = 8, column = 1) #controls position of name of popup grid
popupMenu_mat_cond.grid(row = 8, column =2) #controls position of popup grid

Label(mainframe1, text="Choose Material Designation for Key & Bolt").grid(row = 9, column = 1) #controls position of name of popup grid
popupMenu_mat_des2.grid(row = 9, column =2) #controls position of popup grid

Label(mainframe1, text="Choose Material Condition for Key & Bolt").grid(row = 10, column = 1) #controls position of name of popup grid
popupMenu_mat_cond2.grid(row = 10, column =2) #controls position of popup grid

Label(mainframe1, text="Choose Material Designation for Flange").grid(row = 11, column = 1) #controls position of name of popup grid
popupMenu_mat_flang.grid(row = 11, column =2) #controls position of popup grid

b1 = tk.Button(mainframe1,  text='Submit', command=lambda: my_show() )  
b1.grid(row=12,column=1) 

str_out=tk.StringVar(root_1)
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
    Crush_Bolt = (1.5 * Yield_Bolt)/float(FoS_Bolt)
    print(Shear_Bolt)
    print(Shear_Flange)
    print(Shear_Shaft)

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

    counter = 0
    while True:
        if counter != 0:
            Diameter_of_Shaft = 1.05 * Diameter_of_Shaft

        # check for shear in key
        shearStress = (Max_Torque * 2) / (width_key * length_key * Diameter_of_Shaft)
        print("Shearing of key is ",shearStress)
        if shearStress > (Shear_Bolt):
            print("Fail 1")
            counter += 1
            continue
        else:  # crushing test for key
            crushStress = (4 * Max_Torque) / (height_key * length_key * Diameter_of_Shaft)
            print("Compress stress needed to Compress Key is ",crushStress)
            if crushStress > (Crush_Bolt):
                print("Fail 2")
                counter += 1
                continue
            else:
                # dimensions for hub
                hubOD = 2 * Diameter_of_Shaft  # since, shaft dia= inner dia of hub
                # shear stress test for hub #PSG 7.135
                shearStress_hub = (16 * Max_Torque * hubOD) / (np.pi * (pow(hubOD, 4) - pow(Diameter_of_Shaft, 4)))
                print("Torsional Shear of Hub is ",shearStress_hub)
                if shearStress_hub > Shear_Flange:
                    print("Fail 3")
                    counter += 1
                    continue
                else:
                    # dimension of flange
                    flangeThick = 0.5 * Diameter_of_Shaft
                    # shear stress for flange
                    shearStress_flang = (2 * Max_Torque) / (np.pi * pow(hubOD, 2) * flangeThick)
                    print("Shear stress needed to shear flange is ", shearStress_flang)
                    if shearStress_flang > Shear_Flange:
                        print("Fail 4")
                        counter += 1
                        continue
                    else:
                        # dimensions of the bolt
                        pitchDia = 3 * Diameter_of_Shaft
                        if Diameter_of_Shaft < 40:
                            n = 3
                        if Diameter_of_Shaft >= 40 and Diameter_of_Shaft < 100:
                            n = 4
                        if Diameter_of_Shaft >= 100 and Diameter_of_Shaft < 180:
                            n = 6
                            
                        d1 = math.sqrt((8 * Max_Torque) / (np.pi * Shear_Bolt * n * pitchDia))
                        #print(d1)
                        #print(n)
                        #print(pitchDia)
                        #print(Max_Torque)
                        #print(Shear_Bolt)

                        #PSG 5.42
                        Bolt_check = ({
                        (1,2.208): 2.5,
                        (2.208,2.675): 3, 
                        (2.675,3.545): 4,
                        (3.545,4.48): 5,
                        (4.48,5.35): 6,
                        (5.35,7.188): 8,
                        (7.188,9.026): 10, 
                        (9.026,10.863): 12,
                        (10.863,14.701): 16,
                        (14.701, 18.376): 20,
                        (18.376,22.051): 24, 
                        (22.051,27.727): 30,
                        (27.727,30.727): 33,
                        (30.727, 33.402): 36
                        })

                        Diameter_of_bolt = range_index(Bolt_check, d1)
                        print("We are Selecting bolt - M",Diameter_of_bolt)   

                        Designation_of_Bolt = "M" + str(Diameter_of_bolt)

                        #compressive failure of bolts
                        compress_fail = ((2 * Max_Torque)/(pitchDia * n * Diameter_of_bolt * flangeThick))    
                        
                        print("Compress stress needed to Compress Bolt is ", compress_fail)
                        if compress_fail > Crush_Bolt:
                            print("Fail 5")
                            counter += 1
                            continue       
                        else:
                            print("Sucessfully completed all Tests")
                            # Add a grid for Output

                            root_2 = Tk()
                            root_2.title("Result")

                            mainframe2 = Frame(root_2)
                            mainframe2.grid(column=0,row=0, sticky=(N,W,E,S) )
                            mainframe2.columnconfigure(0, weight = 1)
                            mainframe2.rowconfigure(0, weight = 1)
                            mainframe2.pack(pady = 60, padx = 50) #controls fixed gap inbetween main content and edges, pady for y padx for x

                            Label(mainframe2, text="Diameter of Shaft is").grid(row = 1, column = 1)
                            Label(mainframe2, text=Diameter_of_Shaft).grid(row = 1, column = 2)

                            Label(mainframe2, text="Width of Key is ").grid(row = 2, column = 1)
                            Label(mainframe2, text=width_key).grid(row = 2, column = 2)
                            Label(mainframe2, text="Height of Key is ").grid(row = 3, column = 1)
                            Label(mainframe2, text=height_key).grid(row = 3, column = 2)
                            Label(mainframe2, text="Length of Key is ").grid(row = 4, column = 1)
                            Label(mainframe2, text=length_key).grid(row = 4, column = 2)
                            Label(mainframe2, text="  ").grid(row = 5, column = 1)

                            Label(mainframe2, text="Diameter of Hub  ").grid(row = 6, column = 1)
                            Label(mainframe2, text=2 * Diameter_of_Shaft).grid(row = 6, column = 2)
                            Label(mainframe2, text="Thickness of Hub  ").grid(row = 7, column = 1)
                            Label(mainframe2, text=1.5 * Diameter_of_Shaft).grid(row = 7, column = 2)
                            Label(mainframe2, text="  ").grid(row = 8, column = 1)

                            Label(mainframe2, text="PCB of Flange for Bolt Holes ").grid(row = 9, column = 1)
                            Label(mainframe2, text=3 * Diameter_of_Shaft).grid(row = 9, column = 2)
                            Label(mainframe2, text="Diameter of Bolts ").grid(row = 10, column = 1)
                            Label(mainframe2, text=Designation_of_Bolt).grid(row = 10, column = 2)
                            Label(mainframe2, text="Number of Bolts ").grid(row = 11, column = 1)
                            Label(mainframe2, text=n).grid(row = 11, column = 2)
                            Label(mainframe2, text="  ").grid(row = 12, column = 1)

                            Label(mainframe2, text="Diameter of Flange ").grid(row = 13, column = 1)
                            Label(mainframe2, text=4 * Diameter_of_Shaft).grid(row = 13, column = 2)
                            Label(mainframe2, text="Thickness of Flange ").grid(row = 14, column = 1)
                            Label(mainframe2, text=0.5 * Diameter_of_Shaft).grid(row = 14, column = 2)
                            Label(mainframe2, text="  ").grid(row = 15, column = 1)
                        
                            root_3 = Tk()
                            root_3.title("Result of Testing")

                            mainframe3 = Frame(root_3)
                            mainframe3.grid(column=0,row=0, sticky=(N,W,E,S) )
                            mainframe3.columnconfigure(0, weight = 1)
                            mainframe3.rowconfigure(0, weight = 1)
                            mainframe3.pack(pady = 60, padx = 50) #controls fixed gap inbetween main content and edges, pady for y padx for x

                            Label(mainframe3, text="Compress stress needed to Compress Key is    ").grid(row = 1, column = 1)
                            Label(mainframe3, text=crushStress    ).grid(row = 1, column = 2)
                            Label(mainframe3, text="   which is less than    ").grid(row = 1, column = 3)
                            Label(mainframe3, text=Crush_Bolt).grid(row = 1, column = 4)

                            Label(mainframe3, text="Shearing of key is      ").grid(row = 2, column = 1)
                            Label(mainframe3, text=shearStress    ).grid(row = 2, column = 2)
                            Label(mainframe3, text="   which is less than    ").grid(row = 2, column = 3)
                            Label(mainframe3, text=Shear_Bolt).grid(row = 2, column = 4)

                            Label(mainframe3, text="Torsional Shear of Hub is     ").grid(row = 3, column = 1)
                            Label(mainframe3, text=shearStress_hub    ).grid(row = 3, column = 2)
                            Label(mainframe3, text="   which is less than    ").grid(row = 3, column = 3)
                            Label(mainframe3, text=Shear_Flange).grid(row = 3, column = 4) 

                            Label(mainframe3, text="Shear stress needed to shear flange is     ").grid(row = 4, column = 1)
                            Label(mainframe3, text=shearStress_flang    ).grid(row = 4, column = 2)
                            Label(mainframe3, text="   which is less than    ").grid(row = 4, column = 3)
                            Label(mainframe3, text=Shear_Flange).grid(row = 4, column = 4)

                            Label(mainframe3, text="Compress stress needed to Compress Bolt is      ").grid(row = 5, column = 1)
                            Label(mainframe3, text=compress_fail    ).grid(row = 5, column = 2)
                            Label(mainframe3, text="   which is less than    ").grid(row = 5, column = 3)
                            Label(mainframe3, text=Crush_Bolt).grid(row = 5, column = 4)

                            Label(mainframe3, text="Sucessfully completed all Tests").grid(row = 6, column = 2)



                            root_2.mainloop()

                        


        break

root_1.mainloop()
