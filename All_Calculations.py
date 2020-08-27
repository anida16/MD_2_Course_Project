import numpy as nm
import math as maths

def range_index(table, val):
    for (k1, k2) in table:
        if k1 <= val < k2:
            return table[(k1, k2)]

Diameter_of_shaft = 60
keyWidth = 18
keyThick = 11
keyLen = 90
Max_Torque = 2984155.17

#No. of Bolts calculations

Shear_Bolt = 80
Shear_Flange = 16.67
Shear_Shaft = 76

Stress_Bolt = 2 * Shear_Bolt
Stress_Flange = 2 *Shear_Flange
Shear_Shaft = 2 * Shear_Shaft

Crush_Bolt = 3 * Shear_Bolt

flag = 0
counter = 0

while True:
    if counter != 0:
        Diameter_of_shaft = 1.05 * Diameter_of_shaft

    # check for shear in key
    shearStress = (Max_Torque * 2) / (keyWidth * keyLen * Diameter_of_shaft)
    print("Shearing of key is ",shearStress)
    if shearStress > (Shear_Bolt):
        print("Fail 1")
        counter += 1
        continue
    else:  # crushing test for key
        crushStress = (4 * Max_Torque) / (keyThick * keyLen * Diameter_of_shaft)
        print("Stress for crushing of key is ",crushStress)
        if crushStress > (Crush_Bolt):
            print("Fail 2")
            counter += 1
            continue
        else:
            # dimensions for hub
            hubOD = 2 * Diameter_of_shaft  # since, shaft dia= inner dia of hub
            # shear stress test for hub #PSG 7.135
            shearStress_hub = (16 * Max_Torque * hubOD) / (nm.pi * (pow(hubOD, 4) - pow(Diameter_of_shaft, 4)))
            print("Torsional Shear of Hub is ",shearStress_hub)
            if shearStress_hub > Shear_Flange:
                print("Fail 3")
                counter += 1
                continue
            else:
                # dimension of flange
                flangeThick = 0.5 * Diameter_of_shaft
                # shear stress for flange
                shearStress_flang = (2 * Max_Torque) / (nm.pi * pow(hubOD, 2) * flangeThick)
                print("Shear stress needed to shear flange is ", shearStress_flang)
                if shearStress_flang > Shear_Flange:
                    print("Fail 4")
                    counter += 1
                    continue
                else:
                    # dimensions of the bolt
                    pitchDia = 3 * Diameter_of_shaft
                    if Diameter_of_shaft < 40:
                        n = 3
                    if Diameter_of_shaft >= 40 and Diameter_of_shaft < 100:
                        n = 4
                    if Diameter_of_shaft >= 100 and Diameter_of_shaft < 180:
                        n = 6
                        
                    d1 = maths.sqrt((8 * Max_Torque) / (nm.pi * Shear_Bolt * n * pitchDia))
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

                    #compressive failure of bolts
                    compress_fail = ((2 * Max_Torque)/(pitchDia * n * Diameter_of_bolt * flangeThick))    
                    
                    print("Compress stress needed to Compress Bolt is ", compress_fail)
                    if compress_fail > Crush_Bolt:
                        print("Fail 5")
                        counter += 1
                        continue       
                    else:
                        print("Sucessfully completed all Tests")
    break

