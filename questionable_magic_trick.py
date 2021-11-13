
# Taking input from the user
print('You stand in the presence of the Magnificent Magic Mademoiselle Millicent.\nPrepare to be amazed!')
num = int(input('Enter an integer: '))

print("")  # empty line

# starting magic, doing math and showing results
print('OK, watch this...')
new_num = num * 2
print("We'll multiply by 2 and get", new_num)
new_num += 12
print("Then we'll add 12 and get", new_num)
new_num = new_num // 2
print("Then we'll divide by 2 and get", new_num)
new_num -= num
print(f"Then we'll subtract the original number and get... {new_num}.   Amazing!!!")
