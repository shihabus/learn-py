colors=["red","green","yellow","blue"]

for color in colors:
    print(f"Color is {color}")

# this will be the last value
print("Color outside the loop is ",color)

my_list=list(range(9,14))
print(f"my_list is {my_list}")

for num in range(5,10):
    print(f"Current num is {num}")

# list(enumerate(colors)) -> tuples
# [(0,'red'),(1,'green'),(2,'yellow'),...]

# to extract index and values
for index, value in enumerate(colors):
    print(f"we have {value} at {index}")


person_info={
    'name':'Shihab',
    'origin':'India',
    'job':'Dev',
    'company':'Salesforce'
}

for key in person_info:
    print(f'the key is {key}')

for key,value in person_info.items():
    print('-------------------')
    print(f"key: {key}")
    print('-----')
    print(f'value: {value}')
    print('------------------')