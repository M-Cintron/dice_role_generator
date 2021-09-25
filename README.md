# Dice Roller
Simple Python program for generating random numbers based on inputted dice.
* Only tested on Python 3.9

## Things to do:
- [x] Write base tests
- [x] Write base code
- [ ] Write proper documentation
- [x] Review code and revise for readability

### Things I'd like to do (but might not get to):
- [ ] Revise the .roll() method to also function as a static method
- [ ] Write a subclass of dice_roller that adds mobile friendly GUI (Kivy)
  - [ ] 3D dice that can be rolled would be cool but probably out of my scope
- [ ] Figure out how to write tests for GUI
- [ ] Test on Android
- [ ] Update documentation
- [ ] Review code and revise for readability


## How to use:
1. Copy the file [dice_roller/dice_roller/\_\_init__.py](https://github.com/M-Cintron/dice_roller/blob/main/dice_roller/__init__.py) and paste in desired directory.
2. Import the dice_roller directory.
3. Create an instance of the DiceRoller class.
4. Call .roll(), .history(), or .clear() methods.

### Example:
Let's say you renamed the dice_roller init file to "dice_roller.py" and that
your program's directory looks like this:
```
some_project/  
├── dice_roller.py
└── some_program.py
```
If you want to roll 1, 10 sided dice in some_program.py, then do:  
```
dice_roller import DiceRoller


dice_roller_instance = DiceRoller()
print(dice_roller_instance.roll((1, 10)
```

## .role() Method
.role() accepts any number of tuples or lists, with each formatted as 
(``number of dice``, ``number of sides on the dice``).  Note: the number of dice and/or number of sides on the dice cannot 
be zero or less.
But if .role() is ran with no arguments, it will roll 1, 20 sided die by default.  

.role() returns a tuple containing the result of the role, the min possible value, the max 
possible value, and the median role value (.role() also saves what dice you rolled and their role results; this can be 
accessed with the .history() method).  
```
output = dice_roller_instance.roll((1, 6))
print(output)
>>> (2, 1, 6, 3.5)

role_result = output[0]
min_possible_val = output[1]
max_possible_val = output[2]
median_val = output[3]
```

Let's say we want to roll 5, 6 sided dice, and 1, 100 sided die.  This is how we'd do it:  
``print(dice_roller_instance.roll((5, 6), (1, 100)))``  
Rolling 1, 20 sided die:  
``print(dice_roller_instance.roll())``