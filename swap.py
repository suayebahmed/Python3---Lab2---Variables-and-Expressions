
# Taking two inputs from the user
x = int(input('Enter value for x: '))
y = int(input('Enter value for y: '))
print("")
print(f'Before swap: x = {x}, y = {y}')

# Swapping
new_x = x
x = y
y = new_x
print(f'After swap: x = {x}, y = {y}')
