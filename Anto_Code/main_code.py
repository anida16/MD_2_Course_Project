import math as maths
from tkinter import *

window = Tk()


class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):  # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)  # or super(RangeDict, self) for Python 2


# inputs for the design
# power
window.title("Design of Flange Coupling")
powerLabel = Label(window, text="Power")
powerLabel.grid(row=2, column=5)
powerEntry = StringVar()
powerEntry = Entry(window)
power = float(powerEntry.get())
# speed
speedLabel = Label(window, text="Speed")
speedLabel.grid(row=3, column=5)
speedEntry = StringVar()
speedEntry = Entry(window)
rpm = float(speedEntry.get())
# Factor of safety for shaft
FoS_Shaft_label = Label(window, text="FoS for shaft")
FoS_Shaft_label.grid(row=4, column=5)
FoS_Shaft_entry = StringVar()
FoS_Shaft_entry = Entry(window)
fos1 = float(FoS_Shaft_entry.get())
# Factor of safety for flange
FoS_Flange_label = Label(window, text="FoS for flange")
FoS_Flange_label.grid(row=5, column=5)
FoS_Flange_entry = StringVar()
FoS_Flange_entry = Entry(window)
fos2 = float(FoS_Flange_entry.get())
# Factor of safety for key and bolts
FoS_Key_label = Label(window, text="FoS for key & bolts")
FoS_Key_label.grid(row=6, column=5)
FoS_Key_entry = StringVar()
FoS_Key_entry = Entry(window)
fos3 = float(FoS_Key_entry.get())
# Service Factor
serviceFactor_Label = Label(window, text="Service Factor")
serviceFactor_Label.grid(row=7, column=5)
serviceFactor_Entry = StringVar()
serviceFactor_Entry = Entry(window)
serviceFactor = int(serviceFactor_Entry.get())
# Protective type or Non-protective type
pType_label = Label(window, text="Protective type")
pType_label.grid(row=8, column=5)
pType_entry = StringVar()
pType_entry = Entry(window)
pType = pType_entry.get()


def click():
    return


Submit = Button(window, padx='50', text="Submit", bg="blue", fg="white", command=click)
Submit.grid(row=10)
pi = 3.141
flag = 0
# material selection for the flange coupling
maxStress = 150
# design of shaft
max_torque = ((power * 60) / (2 * pi * rpm)) * serviceFactor * 1000  # torque generated
Diameter_of_shaft = pow((16 * max_torque) / (pi * maxStress), 1 / 3)  # shaft diameter
counter = 0  # counter variable
# key width and diameter
width_check = RangeDict({
    range(6, 8): 2,
    range(9, 10): 3,
    range(11, 12): 4,
    range(13, 17): 5,
    range(18, 22): 6,
    range(23, 30): 8,
    range(31, 38): 10,
    range(39, 44): 12,
    range(45, 50): 14,
    range(51, 58): 16,
    range(59, 65): 18,
    range(66, 75): 20,
    range(76, 85): 22,
    range(86, 95): 25,
    range(96, 110): 28,
    range(111, 130): 32,
    range(131, 150): 36,
    range(151, 170): 40,
    range(171, 200): 45,
    range(201, 230): 50,
    range(231, 260): 56,
    range(261, 290): 63,
    range(291, 330): 70,
    range(331, 380): 80,
    range(381, 440): 90,
    range(441, 500): 100
})
height_check = RangeDict({
    range(6, 8): 2,
    range(9, 10): 3,
    range(11, 12): 4,
    range(13, 17): 5,
    range(18, 22): 6,
    range(23, 30): 7,
    range(31, 38): 8,
    range(39, 44): 8,
    range(45, 50): 9,
    range(51, 58): 10,
    range(59, 65): 11,
    range(66, 75): 12,
    range(76, 85): 14,
    range(86, 95): 14,
    range(96, 110): 16,
    range(111, 130): 18,
    range(131, 150): 20,
    range(151, 170): 22,
    range(171, 200): 25,
    range(201, 230): 28,
    range(231, 260): 32,
    range(261, 290): 32,
    range(291, 330): 36,
    range(331, 380): 40,
    range(381, 440): 45,
    range(441, 500): 50
})

while flag == 0:
    if counter != 0:
        Diameter_of_shaft = 1.5 * Diameter_of_shaft
    # dimensions of the key
    keyWidth = width_check[Diameter_of_shaft]
    keyThick = height_check[Diameter_of_shaft]
    keyLen = 1.5 * Diameter_of_shaft
    # check for shear in key
    shearStress = (max_torque * 2) / (keyWidth * keyLen * Diameter_of_shaft)
    if shearStress > (0.5 * maxStress):
        counter += 1
        continue
    else:  # crushing test for key
        crushStress = (4 * max_torque) / (keyThick * keyLen * Diameter_of_shaft)
        if crushStress > maxStress:
            counter += 1
            continue
        else:
            # dimensions for hub
            hubOD = 2 * Diameter_of_shaft  # since, shaft dia= inner dia of hub
            keyLen = 1.5 * Diameter_of_shaft
            # shear stress test for hub
            shearStress = (16 * max_torque * hubOD) / (pi * (pow(hubOD, 4) - pow(Diameter_of_shaft, 4)))
            if shearStress > maxStress:
                counter += 1
                continue
            else:
                # dimension of flange
                flangeThick = 0.5 * Diameter_of_shaft
                # shear stress for flange
                shearStress = (2 * max_torque) / (pi * pow(hubOD, 2) * flangeThick)
                if shearStress > maxStress:
                    counter += 1
                    continue
                else:
                    # dimensions of the bolt
                    pitchDia = 3 * Diameter_of_shaft
                    d1 = maths.sqrt((2 * max_torque) / (pi * maxStress * 3 * Diameter_of_shaft))
    flag = 1

print(" ")
