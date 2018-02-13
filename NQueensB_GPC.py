# NQueensB.py
# Write a brief Python program to randomly generate a solution to the N-Queens problem
import random

# ask the user for an N value

N = int(input("Please give me a value for N: "))

# generate a candidate NQ solution [random.randint(0,n-1) for x in range(n)]

nq = list( range(N))

# define a function to count number of conflicts()

def count_conflicts( NQ ):
	conflicts = 0
	for i in range( len(NQ) - 1):
		for j in range(i+1, len(NQ) ):
			if abs(i-j) == abs(NQ[i] - NQ[j]):
				conflicts += 1
	return conflicts

shuffles = 0
while count_conflicts(nq) != 0:
     random.shuffle(nq)
     shuffles += 1
     
# print NQ

print(nq)

# print number of iterations

print("Shuffles: " + str(shuffles))
