# [Notes](https://practical.learnpython.dev/)

- `venv` helps you install modules and packages w/o polluting the global
- if **name** == 'main':
  this is the entry point when the code is run
- variable names are snake_cased
- `None` signifies null
- REPL methods
  - help(): helps with documentation, like help(int)
  - type(): returns type of variable
  - dir(): show the available methods on argument, like dir(str)
- Math operations
  - / float division
  - // integer division
  - \*\* raised to the power
- Strings
  - """ for multi-line strings
  - \n new line
  - \t tab space
- List
  - ` []`` or  `list()`
  - insert, append, reverse, sort, pop (it can take index)
  - in operator
- Tuple
  - immutable and maintains order
  - (1,2,3,4,"Shihab")
  - empty Tuple with single entry is created as (1,)
- Set
  - collection of unique immutable items
  - but the set itself is mutable
  - things that can be hashed are immutable
  - so sets can't have a dict or list in it
  - {"Shihab","Shana",1}
  - empty set is created as set()
  - .add(x) to insert
  - .discard(x) to remove
  - there is no guaranty that things will appear in the same order as inserted
- from pprint import pprint
- ```
  def print_info(name,state,country,gender):
      print(f"{name} is a {gender} from {state} in {country}")

  # named arguments
  print_info(gender="male",country="India",name="Shihab",state="Kerala")
  ```

-

```
names=[]
if names:
  print("Names are available)
else:
  print("Names is empty)
```

pip freeze > requirement.txt
pip install -r requirement.txt
