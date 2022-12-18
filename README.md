# Cat Class

Read this guideline before completing the task:  
[Guideline](https://github.com/ketstap162/tasks-guideline)

## Task
1) You have to make a class `Cat` that represents a cat.  
2) The class takes arguments `name` and `age` for create an example of class.
3) Also, the class must also have `info` and `voice` methods.
4) The `info` method must return a dictionary with two keys: 
`"cat": {cat's name}` and `"age": {cat's age}`
5) The `voice` method must return a string  
`{cat's name}: Meow!`

Example:
```python
bob = Cat("Bob", 5)

print(bob.name)  # "Bob"
print(bob.age)  # 5
print(bob.info())  # {"cat": "Bob", "age": 5}
print(bob.voice())  # "Bob: Meow!"
```

Run command `pytest` in terminal
before pushing solution