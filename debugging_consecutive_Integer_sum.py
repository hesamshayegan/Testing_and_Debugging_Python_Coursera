# fix the follwing code:
# number = int(input("Enter an integer: "))

# i = 1

# while i < nomber:
#     if number % 2 = 0:
#         total = total + number
#     i = i + 1

# print(total)

# solution:
# number = int(input("Enter an integer: "))

# i = 1
# if number % 2 == 0:
#     total = 0
#     while 2*i <= number:
#         total += (2 * i)
#         i += 1
# else:
#     total = 1
#     while (2 * i + 1) <= number:
#         total += 2 * i + 1
#         i += 1

# print(total)

number = int(input("Enter an integer: "))

i = 1
total = 0 if number % 2 == 0 else 1

while 2 * i <= number:
    total += (2 * i) if number % 2 == 0 else (2 * i + 1)
    i += 1

print(total)