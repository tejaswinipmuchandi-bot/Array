
scores = list(map(int, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)

maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum of Scores:", total)
print("Average of Scores:", average)
print("Maximum Score:", maximum)
print("Minimum Score:", minimum)