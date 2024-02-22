
import random

n = int(input())
letters = input().split()
k = int(input())

a_count = letters.count("a")

print(a_count)
total_combinations = len(letters) ** k

print(total_combinations)
all_different_combinations = total_combinations - a_count ** k

print(all_different_combinations)
favorable_cases = total_combinations - all_different_combinations

print(favorable_cases)
probability = favorable_cases / total_combinations

print(f"{probability:.7f}")

#print(probability)
#probability = round(probability, 6)

#print(probability)
