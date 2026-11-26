input = input("Enter The No List : ")
numbers = list(map(int, input.split()))
if not numbers:
    print("The list is empty.")
else:
    max_val = numbers [0]
    min_val = numbers [0]
for num in numbers [1:]:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print (f"Maximum value: {max_val}")
print (f"Minimum value: {min_val}")