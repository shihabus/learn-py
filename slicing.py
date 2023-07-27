my_str = "Hello World!"

sliced_str = ""

sliced_str = my_str[3:8]
print(f"chars between 3 and 5: {sliced_str}")

sliced_str = my_str[3:]
print(f"chars from 3 to end: {sliced_str}")

sliced_str = my_str[:4]
print(f"chars till 4: {sliced_str}")

sliced_str = my_str[-7:-3]
print(f"chars between 3 and 5 from end: {sliced_str}")
