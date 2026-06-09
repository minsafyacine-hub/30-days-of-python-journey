import numpy as np
print('numpy:', np.__version__)
print(dir(np))

python_list = [1, 2, 3, 4]
print(type(python_list))
two_dimentional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(two_dimentional_list)
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)
numpy_array_float = np.array(python_list, dtype=float)
numpy_two_dimentional_list = np.array(two_dimentional_list)
print(numpy_two_dimentional_list)
print(numpy_array_float)
numpy_bool_array = np.array([0, 0, 1, -1, 0], dtype=bool)
print(numpy_bool_array)
numpy_two_dimentional_array = np.array(two_dimentional_list)
print(type(numpy_two_dimentional_array))
print(numpy_two_dimentional_array)
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print(np_to_list)
print('two dimentional array :', numpy_two_dimentional_list.tolist())
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print(nums.shape)
two_dimentional_shape = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dimentional_shape)
print('two dimentional arrays shape :', two_dimentional_shape.shape)
three_dimentional_shape = np.array([[1, 2, 3, 4], 
                                    [5, 6, 7, 8], 
                                    [9, 10, 11, 12]])
print('three dimentional array shape :', three_dimentional_shape.shape)

int_list = np.array([-3, -2, -1, 0, 1, 2, 3])
float_list = np.array(int_list, dtype=float)
bool_list = np.array(int_list, dtype=bool)

print(int_list)
print(int_list.dtype)
print(float_list)
print(float_list.dtype)
print(bool_list)
print(bool_list.dtype)

print('The size :', int_list.size)
print('The size :', two_dimentional_shape.size)

print('original list :', numpy_array_from_list)
numpy_array_from_list_plus_ten = numpy_array_from_list + 10
print(numpy_array_from_list_plus_ten)
numpy_array_from_list_minus_ten = numpy_array_from_list - 10
print(numpy_array_from_list_minus_ten)
numpy_array_from_list_times_ten = numpy_array_from_list * 10
print(numpy_array_from_list_times_ten)
numpy_array_from_list_dividedby_ten = numpy_array_from_list / 10
print(numpy_array_from_list_dividedby_ten)
numpy_array_from_list_modulus_three = numpy_array_from_list % 3
print(numpy_array_from_list_modulus_three)
numpy_array_from_list_dividedbyby_ten = numpy_array_from_list // 10
print(numpy_array_from_list_dividedbyby_ten)
numpy_array_from_list_expenontiel_ten = numpy_array_from_list ** 10
print(numpy_array_from_list_expenontiel_ten)

numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr)
numpy_float_arr = np.array([1. , 2., 3. , 4.], dtype='int')
print(numpy_float_arr)
numpy_bool_arr = np.array([-3, -2, -1, 0, 1, 2, 3], dtype='bool')
print(numpy_bool_arr)
print(numpy_float_arr.astype('int').astype('str'))

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row :', first_row)
print('Second row :', second_row)
print('Third row :', third_row)
first_column = two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column :', first_column)
print('Second column :', second_column)
print('Third column :', third_column)
print(two_dimension_array)

first_row_and_columns = two_dimension_array[0:2, 0:2]
print(first_row_and_columns)

print(two_dimension_array[::-1, ::-1])

print(np.zeros((3,3), dtype='int', order='C'))
numpy_ones = np.ones((3,3), dtype='int', order='C')
print(numpy_ones)
print(numpy_ones * 2)

first_shape = np.array([(1,2,3), (4,5,6)])
print(first_shape)
print(first_shape.reshape(3,2))
print(first_shape.flatten())

np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append :', np.hstack((np_list_one, np_list_two)))
print('Vertical Append :', np.vstack((np_list_one, np_list_two)))

print(np.random.random())
print(np.random.random(5))
print(np.random.randint(0,11))
print(np.random.randint(0, 11, size=4))
print(np.random.randint(0, 11, size=(3,3)))

normal_array = np.random.normal(79, 15, 80)
print(normal_array)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
plt.hist(normal_array, color='grey', bins=50)

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

even_numbers = np.arange(2, 20, 2)
print(even_numbers)
odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

print(np.linspace(1.0, 5.0, num=10))
print(np.linspace(1.0, 5.0, num=5, endpoint=False))
print(np.logspace(2.0, 4.0, num=5))
print(np.array([1,2,3], dtype=np.complex128))
array = np.array([(1,2,3), (4,5,6)])
print(array)
print('First row :', array[0])
print('Second row :', array[1])

print('min :', two_dimension_array.min())
print('max :', two_dimension_array.max())
print('mean :', two_dimension_array.mean())
print('standart variation :', two_dimension_array.std())
print('Column with minimum :', np.amin(two_dimension_array, axis=0))
print('Column with maximum :', np.amax(two_dimension_array, axis=0))
print('Row with the minimum :', np.amin(two_dimension_array, axis=1))
print('Row with the maximum :', np.amax(two_dimension_array, axis=1))

a = [1,2,3]
print('Tile   ',np.tile(a, 2))
print('Repeat   ',np.repeat(a, 2))

one_random_num = np.random.random()
print(one_random_num)
r = np.random.random(size=[2,3])
print(r)
rann = np.random.randint(0, 10, size=[5,2])
print(rann)
ranchoice = np.random.choice(['a', 'e', 'i', 'o', 'u', 'y'], size=10)
print(ranchoice)

from scipy import stats
np_normal = np.random.normal(5, 0.5, 1000)
print(np_normal)
print('Min :', np.min(np_normal))
print('Max :', np.max(np_normal))
print('Mean :', np.mean(np_normal))
print('Median :', np.median(np_normal))
print('Mode :', stats.mode(np_normal))
print('Standart deviation :', np.std(np_normal))
plt.hist(np_normal, color='grey', bins=21)
plt.show()

f = np.array([1,2,3])
g = np.array([4,5,6])
print('dot :', np.dot(f, g))

h = [[1, 2], [3,4]]
i = [[5,6], [7, 8]]
print(np.matmul(h,i))
print(np.linalg.det(i))
Z = np.zeros((8, 8))
Z[1::2,:1] = 1
Z[:1, 1::2] = 1
print(Z)

plt.figure()
print(np.arange(0, 11, 2))
temp = np.array([1, 2, 3, 4, 5])
pressure = temp  * 2 + 5

plt.plot(temp, pressure)
plt.xlabel('Temperature in C°')
plt.ylabel('Pressure')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6,step=0.5))
plt.show()

plt.figure()
mu = 28
sigma = 15
samples = 100000
random = np.random.normal(mu, sigma, samples)
ax = sns.displot(random)
ax.set(xlabel='x', ylabel='y')
plt.show()