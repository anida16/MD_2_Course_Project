def range_index(table, val):
    for (k1, k2) in table:
        if k1 < val <= k2:
            return table[(k1, k2)]

Bolt_check = ({
        (1,2.208): 'M2.5',
        (2.208,2.675): 'M3', 
        (2.675,3.545): 'M4',
        (3.545,4.48): 'M5',
        (4.48,5.35): 'M6',
        (5.35,7.188): 'M8',
        (7.188,9.026): 'M10', 
        (9.026,10.863): 'M12',
        (10.863,14.701): 'M16',
        })

print(range_index(Bolt_check, 2.208))