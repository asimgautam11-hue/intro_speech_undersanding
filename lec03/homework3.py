
def words2characters(words):
	characters = []
	for item in words:
		for char in str(item):
			characters.append(char)
	return characters

test_input = ['hello', 1.234, True]
result = words2characters(test_input)
print("Input list:", test_input)
print("Output list:", result)
