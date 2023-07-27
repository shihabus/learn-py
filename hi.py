# pretty print
from pprint import pprint

greetings =["Hello","Hi","Hola"]

for greeting in greetings:
    print(f"{greeting} World!")
    # pprint(greetings)


def print_info(name,state,country,gender):
    print(f"{name} is a {gender} from {state} in {country}")

# named arguments
print_info(gender="male",country="India",name="Shihab",state="Kerala")
