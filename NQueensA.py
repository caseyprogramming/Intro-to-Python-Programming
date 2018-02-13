# NQueensA.py
# Write a brief Python program to randomly generate a solution to the N-Queens problem
import random
# ask the user for an N value

N = int(input("Please give me a value for N: "))

nq = list(range(N))

# generate a candidate NQ solution

def NQ_solution( NQ ):
        NQ = [random.randint(0,N-1) for x in range(N)]
        return NQ


# define a function to count number of conflicts()
def count_conflicts( NQ ):
	conflicts = 0
	for i in range( len(NQ) - 1):
		for j in range(i+1, len(NQ) ):
			if abs(i-j) == abs(NQ[i] - NQ[j]):
				conflicts += 1
			if (NQ[i] == NQ[j]):
				conflicts += 1
	return conflicts

count = 0
while count_conflicts(nq) != 0:
        nq = NQ_solution(nq)
        count += 1
        
# print NQ

print(nq)

# print number of iterations

print(count)
