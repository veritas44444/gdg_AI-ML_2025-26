import numpy as np

num_list = [12, 34, 56, 67, 78 ]

num_array = np.array(num_list) #convert list to numarray

Sum = np.sum(num_array) #find sum
Average = np.mean(num_array) #find means
Max_num = np.max(num_array) #find maximum value

print(f'The sum of the 5 numbers is: {Sum}')
print(f'The average of the 5 numbers is: {Average}')
print(f'The maximum value of the 5 numbers is: {Max_num}')


