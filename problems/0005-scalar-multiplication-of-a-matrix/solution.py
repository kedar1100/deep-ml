def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	res =[]
	for i in range(len(matrix)):
		tempres = []
		for j in range(len(matrix[i])):
			tempres.append( matrix[i][j] * scalar)
		res.append(tempres)


	return res
	pass