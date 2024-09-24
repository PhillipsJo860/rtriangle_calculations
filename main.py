# Joshua Phillips
# 9/23/2024
# Calculating a right triangle using python

# I
print('Please make sure that the triangle is a right triangle or else this code wont work.')
base = input('Please enter the base here: ')
height = input('Please enter the height here: ')

# P
rtriangle = float(base) * float(height) / float(2)

# O
print(f'The base of {base} times the height of {height} is going to create a right triangle with an area of {rtriangle}.')