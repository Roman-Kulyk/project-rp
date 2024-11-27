# number = 10
# if number > 5:
#     raise Exception(f"The number should not exceed 5.({number=})")
# print(number)

number = 10
assert (number < 5), f"The number should not exceed 5.({number=})"
print(number)