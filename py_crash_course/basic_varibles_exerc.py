universe_age = 14_200_000_000

x, y, z = 1, 5, 8

print(universe_age)

# for(3):
print(x, y, z)

# List

motorcycles = ['honda', 'ducati', 'tvs', 'harley', 'yamaha']

# print(f"A {motorcycles[-2].title()} is expensive for me")

too_expensive = motorcycles[1]

motorcycles.remove((too_expensive))

print((too_expensive))

for motorcycle in motorcycles:
    print(f"I cant wait to see the next trick, {motorcycle.title()}.\n")

numbers = list(range(1, 8))

print(min(numbers))
print(sum(numbers))

sum_numbers = [sums + sums for sums in range(1, 5)]

print(sum_numbers)
# Odd
for i in range(1, 8, 2):
    print(i)
