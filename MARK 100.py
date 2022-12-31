def nameRank(names, marks, updates, n):
	
	# Array of students
	x = [[0 for j in range(3)] for i in range(n)]
	for i in range(n):
		
		# Store the name of the student
		x[i][0] = names[i]
		
		# Update the marks of the student
		x[i][1]= int(marks[i] )+ int(updates[i])
		
		# Store the current rank of the student
		x[i][2] = i + 1
		
	highest = x[0]
	for j in range(1, n):
		if (x[j][1] >= highest[1]):
			highest = x[j]
	print(highest)
			
	# Print the name and jump in rank
	print("Name: ", highest[0], ", Jump: ",(highest[0] ))

# Driver code

# Names of the students
names= input("enter students name:").split(",")
# Marks of the students
marks = input("enter marks").split(",")

# Updates that are to be done
updates = input("enter new marks").split(",")

# Number of students
n = len(marks)

nameRank(names, marks, updates, n)