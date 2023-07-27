names = ["Shihab", "Shana", "Shifa", "Althaf"]

name_len = []
for name in names:
    name_len.append(len(name))

print(f"Before: {name_len}")

# list comprehension
name_len = [len(name) for name in names]
print(f"After: {name_len}")

filtered_names = [name for name in names if len(name) % 2]
print(f"Name with even length {filtered_names}")

# generator expression

# loop over numbers divisible by 3 between 0 and 30
gen_exp = (x for x in range(0, 30) if x % 3 == 0)
for num in gen_exp:
    print(f"{num} is divisible by three")
