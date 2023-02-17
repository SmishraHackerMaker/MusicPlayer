# Open the text file
with open('data.txt', 'r') as file:

    # Initialize an empty dictionary to store the pairs
    pairs = {}

    # Initialize variables to store the current question and answer
    current_question = ''
    current_answer = ''

    # Loop through each line in the file
    for line in file:
        # Strip whitespace from the line
        line = line.strip()

        # Check if the line starts with 'Question :'
        if line.startswith('Question :'):
            # If so, update the current question and clear the current answer
            current_question = line.replace('Question : ', '')
            current_answer = ''
        # Check if the line starts with 'Answer :'
        elif line.startswith('Answer   :'):
            # If so, update the current answer and store the pair in the dictionary
            current_answer = line.replace('Answer   : ', '')
            pairs[current_question] = current_answer

    # Print the resulting dictionary
   # print(pairs)
 
Everything = []




x = 0
while x != 50:
	for key, value in pairs:
		print(f"Q: {key}")
		print(f"A: {value}")
	x += 1
#	
#	Everything.append([key, [value]])
