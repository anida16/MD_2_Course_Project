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


Diameter_of_Shaft = 55 #comes from test of shearing of shaft

width_check = RangeDict({
    range(6,8): 2, 
    range(9,10): 3,
    range(11,12): 4, 
    range(13,17): 5,
    range(18,22): 6, 
    range(23,30): 8,
    range(31,38): 10, 
    range(39,44): 12,
    range(45,50): 14, 
    range(51,58): 16,
    range(59,65): 18, 
    range(66,75): 20,
    range(76,85): 22, 
    range(86,95): 25,
    range(96,110): 28, 
    range(111,130): 32,
    range(131,150): 36, 
    range(151,170): 40,
    range(171,200): 45, 
    range(201,230): 50,
    range(231,260): 56, 
    range(261,290): 63,
    range(291,330): 70, 
    range(331,380): 80,
    range(381,440): 90, 
    range(441,500): 100
    })
width_key = width_check[Diameter_of_Shaft]

height_check = RangeDict({
    range(6,8): 2, 
    range(9,10): 3,
    range(11,12): 4, 
    range(13,17): 5,
    range(18,22): 6, 
    range(23,30): 7,
    range(31,38): 8, 
    range(39,44): 8,
    range(45,50): 9, 
    range(51,58): 10,
    range(59,65): 11, 
    range(66,75): 12,
    range(76,85): 14, 
    range(86,95): 14,
    range(96,110): 16, 
    range(111,130): 18,
    range(131,150): 20, 
    range(151,170): 22,
    range(171,200): 25, 
    range(201,230): 28,
    range(231,260): 32, 
    range(261,290): 32,
    range(291,330): 36, 
    range(331,380): 40,
    range(381,440): 45, 
    range(441,500): 50
    })
height_key = height_check[Diameter_of_Shaft]

print("Width of Key is",width_key) # prints width
print("Height of Key is",height_key) # prints height
