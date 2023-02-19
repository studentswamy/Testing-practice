word="anaconda"
for letter in word:
    print (letter)
nums = (1, 2, 3, 4)

sum_nums = 0
for num in nums:
    sum_nums = sum_nums + num
print(f'Sum of numbers is {sum_nums}')
for x in range(3):
    print("Printing:", x)
    
for i in range (1,11):
    # nested loop
    # to iterate from 1 to 10
    for j in range (1,11):
        #print multiplication
        print(i*j, end='')
    print()