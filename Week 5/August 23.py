a, b = map(int, input().split())

years_taken = 0
while a <= b:
    a *= 3
    b *= 2
    years_taken += 1

print(years_taken)