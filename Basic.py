import numpy as np

# Creating Arrays
integer_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Integer Array: ", integer_array)

zeros_matrix = np.zeros((3, 3))
print("Matrix of Zeros: ", zeros_matrix)

ones_matrix = np.ones((3, 3))
print("Matrix of Ones: ", ones_matrix)

even_numbers = np.arange(0, 10, 2)
print("Even Numbers Array: ", even_numbers)

random_matrix = np.random.randint(0, 10, size=(3, 3))
print("Random Integer Matrix: ", random_matrix)

evenly_spaced_array = np.linspace(0, 10, num=6)
print("Evenly Spaced Array: ", evenly_spaced_array)

two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Integer Array: ", two_dimensional_array)

three_dimensional_array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("3D Integer Array: ", three_dimensional_array)

# Array Attributes
print("Shape of Integer Array: ", integer_array.shape)
print("Dimensions of Integer Array: ", integer_array.ndim)
print("Size of Integer Array: ", integer_array.size)
print("Data Type of Integer Array: ", integer_array.dtype)

# Array Indexing
print("First element of Integer Array: ", integer_array[0])
print("Last element of Integer Array: ", integer_array[-1])

# Array Slicing
print("First three elements of Integer Array: ", integer_array[:3])
print("Last three elements of Integer Array: ", integer_array[-3:])
print("Middle elements of Integer Array: ", integer_array[3:6])

# Array Operations
sqrt_array = np.sqrt(integer_array)
print("Square Root of Integer Array: ", sqrt_array)

exp_array = np.exp(sqrt_array)
print("Exponential of Square Root: ", exp_array)

sin_array = np.sin(exp_array)
print("Sine of Exponential: ", sin_array)

cos_array = np.cos(sin_array)
print("Cosine of Sine: ", cos_array)

tan_array = np.tan(cos_array)
print("Tangent of Cosine: ", tan_array)

log_array = np.log(tan_array)
print("Logarithm of Tangent: ", log_array)

# Array Math
addition_array = np.add(integer_array, integer_array)
print("Addition of Integer Array: ", addition_array)

subtraction_array = np.subtract(integer_array, integer_array)
print("Subtraction of Integer Array: ", subtraction_array)

multiplication_array = np.multiply(integer_array, integer_array)
print("Multiplication of Integer Array: ", multiplication_array)

division_array = np.divide(integer_array, integer_array)
print("Division of Integer Array: ", division_array)

exponentiation_array = np.power(integer_array, integer_array)
print("Exponentiation of Integer Array: ", exponentiation_array)

total_sum = np.sum(integer_array)
print("Sum of Integer Array: ", total_sum)

minimum_value = np.min(integer_array)
print("Minimum Value in Integer Array: ", minimum_value)

maximum_value = np.max(integer_array)
print("Maximum Value in Integer Array: ", maximum_value)

mean_value = np.mean(integer_array)
print("Mean of Integer Array: ", mean_value)

median_value = np.median(integer_array)
print("Median of Integer Array: ", median_value)
