def fibonacci(n):
	"""Calculate the Fibonacci sequence up to n terms."""
	sequence = []
	a, b = 0, 1
	for _ in range(n):
		sequence.append(a)
		a, b = b, a + b
	return sequence