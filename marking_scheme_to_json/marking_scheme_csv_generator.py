'''
This tool quickly generates a JSON representation of the marking scheme required for use by software

Example of an input file:
q11
a 2
b 2
...
q12
a 11211
b 22
c 22
d 1
...

where the marks for individual questions are put on the RHS of each question letter.
Roman numerals are automatically added.
'''

import sys
import json

input_file = sys.argv[1]
output_file = open(sys.argv[2], "w")

zero = 1 # Set this to 0 for all marks to be set to 0 (for zeroing student marks)

main = {}
temp = {}
question = ""

def roman(i):
    if i == 1:
        return 'i'
    elif i == 2:
        return 'ii'
    elif i == 3:
        return 'iii'
    elif i == 4:
        return 'iv'
    elif i == 5:
        return 'v'
    elif i == 6:
        return 'vi'
    elif i == 7:
        return 'vii'
    elif i == 8:
        return 'viii'
       

with open(input_file, "r") as f:
    for line in f:
        if line[0] == 'q':
            question = line.strip()
            main[question] = {}
        else:
            letter, marks = line.split()
            if len(marks) == 1:
                index = question[1:] + letter
                main[question][index] = zero * int(marks)
            else:
                for x in range(len(marks)):
                    index = question[1:] + letter + roman(x+1)
                    main[question][index] = zero * int(marks[x])
            
output_file.write(json.dumps(main))

