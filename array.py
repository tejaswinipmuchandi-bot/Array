
scores = list(map(int, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum of Scores:", total)
print("Average of Scores:", average)