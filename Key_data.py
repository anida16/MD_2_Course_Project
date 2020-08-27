class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range): # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item) # or super(RangeDict, self) for Python 2

#dont touch above
import math


Float_Diameter_of_Shaft = 58.1
Diameter_of_Shaft = math.ceil(Float_Diameter_of_Shaft/ 2.) * 2
print(Diameter_of_Shaft)

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

print("Width of Key is",width_key) # prints width
print("Height of Key is",height_key) # prints height
