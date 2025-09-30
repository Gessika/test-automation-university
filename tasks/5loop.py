#for loop
'''
fruits = ['apple', 'banana', 'mango']

for fruit in fruits:
    print(f"fruit: {fruit}")

for number in range (1,4):
    print(f"number is: {number}")
'''
#while loop
temp_f = 40

while temp_f > 32:
    print(f"the temp is {temp_f}")
    temp_f -= 1
    if temp_f == 35:
        break
#continue
for number in range (1,4):
    if number == 2:
        print("\nwe skipping number 2")
        continue
    print(f"\nprint a number {number}")

#pass
for number in range (1,4):
    if number == 2:
        pass
    else:
        print(f"print a number {number}")
