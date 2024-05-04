counts = [0] * 10

numbers = map(int, input("Enter sequence of numbers (end with zero):").split())

for num in numbers:
    if num == 0:
        break
    counts[num] += 1

for i in range(1, 10):
    print(f"Quantity {i}: {counts[i]}")