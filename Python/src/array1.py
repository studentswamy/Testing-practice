arr = []
arr = [0 for i in range(5)] 
print(arr)


#creating Array an initializer 
arr_num = [0] * 2
print(arr_num)


arr_str = ['P'] * 5
print(arr_str)

import array as arr
a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])


import array as arr
numbers = arr.array('i', [10, 11, 12, 12, 13])
(numbers.remove(12))
print(numbers)   # Output: array('i', [10, 11, 12, 13])
print(numbers.pop(2))   # Output: 12
print(numbers)   # Output: array('i', [10, 11, 13])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[3])
print("Last element:", a[-2])



