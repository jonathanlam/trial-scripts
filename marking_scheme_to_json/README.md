This tool quickly generates a JSON representation of the marking scheme required for use by software
Example of an input file:
```
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
```

where the marks for individual questions are put on the RHS of each question letter.
Roman numerals are automatically added.

Usage:
```
python marking_scheme_csv_generator.py input.txt output.json
```
