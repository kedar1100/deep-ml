import numpy as np

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	# Your code here
	res = 0 
	if(len(vec1) != len(vec2)):
		return -(res)
	for i in range(len(vec1)):
		curr = (vec1[i] * vec2[i])
		res = res + curr
		
	return res