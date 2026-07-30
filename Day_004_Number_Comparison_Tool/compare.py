first = float(input("first number:").strip())
second = float(input("second number:").strip())

if first > second:
    print(f"{first} is greater than {second}")
elif second > first:
    print(f"{second} is greater than {first}")
else:
    print(f"Both {first} and {second} are equal")

diff = abs(first - second)
print(f"Difference is: {diff}")
