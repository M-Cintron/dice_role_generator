# Dice Roller
Simple Python program for generating random numbers based on inputted dice.
* Only tested on Python 3.9

## Things to do:
- [x] Write base tests
- [x] Write base code
- [x] Write proper documentation
- [x] Review code and revise for readability

### Things I'd like to do (but might not get to):
- [x] Make some test to make sure I'm not typing "role" instead of "roll" in every file
- [x] Reformat .history() so that the values associated with "Dice" keys are dictionaries with the keys: 'num_dice', and 'num sides'
- [x] Revise the .roll() method to also function as a static method
- [x] Implement advantage and disadvantage rolling
- [ ] Look into pylint to see if it can do my typo hunting job
- [ ] Write a subclass of dice_roller that adds mobile friendly GUI (Kivy)
  - [ ] 3D dice that can be rolled would be cool but probably out of my scope
- [ ] Figure out how to write tests for GUI
- [ ] Test on Android
- [ ] Update documentation for every thing on this list
- [ ] Review code and revise for readability for everything on this list


## How to use:
1. Copy the file [dice_roller/dice_roller/\_\_init__.py](https://github.com/M-Cintron/dice_roller/blob/main/dice_roller/__init__.py) and paste in desired directory.
2. Import the dice_roller directory.
3. Create an instance of the DiceRoller class.
4. Call roll(), history(), or clear() methods.  
#### OR
1. Copy the file [dice_roller/dice_roller/\_\_init__.py](https://github.com/M-Cintron/dice_roller/blob/main/dice_roller/__init__.py) and paste in desired directory.
2. Import DiceRoller from dice_roller directory
3. Call static_roll() from DiceRoller directly (ie: `DiceRoller.static_roll()`)

### Example:
Let's say you renamed the [dice_roller init file](https://github.com/M-Cintron/dice_roller/blob/main/dice_roller/__init__.py) to "dice_roller.py" and that
your program's directory looks like this:
```
some_project/  
├── dice_roller.py
└── some_program.py
```
If you want to roll 1, 10 sided die in some_program.py and have the record of the roll be called later,
then do:  
```pycon
from dice_roller import DiceRoller


dice_roller_instance = DiceRoller()
print(dice_roller_instance.roll((1, 10)))
```
If you don't care about getting the record of the roll being stored and just want to roll 1, 10 sided die,
then do:
```pycon
from dice_roller import DiceRoller


print(DiceRoller.static_roll((1, 10)))
```

## roll() Method
roll() accepts any number of tuples or lists, with each formatted as 
(``number of dice``, ``number of sides on the dice``).  Note: the number of dice and/or number of sides on the dice cannot 
be zero or less.
But if roll() is ran with no arguments, it will roll 1, 20 sided die by default.  

roll(), by default returns a tuple containing, in this order: the result of the roll, the min possible value,
the max possible value, and the median roll value (roll() also saves what dice you rolled and their roll 
results; this can be accessed with the history() method).
```pycon
output = dice_roller_instance.roll((1, 6))
print(output)
>>> (2, 1, 6, 3.5)

roll_result = output[0]
min_possible_val = output[1]
max_possible_val = output[2]
median_val = output[3]
```

Let's say we want to roll 5, 6 sided dice, and 1, 100 sided die.  This is how we'd do it:  
```pycon
print(dice_roller_instance.roll((5, 6), (1, 100)))
>>> (21, 6, 130, 68.0)
```  
Rolling 1, 20 sided die:  
```pycon
print(dice_roller_instance.roll())
>>> (18, 1, 20, 10.5)
```

roll() also has two keyword arguments: `advantage` and `show_advantage_val`.  By default, advantage is set to
None. If advantage is set to True, then DiceRoller will perform two rolls with the same dice and return the 
higher value as the roll result.  If advantage is set to False, then DiceRoller will perform two rolls with 
the same dice and return the lower value as the roll result.  By default, show_advantage_val is set to False.
If advantage is either True or False and show_advantage_val is set to True, then this method returns a tuple 
formatted as (thrown out val is the number that advantage/disadvantage didn't select):  
`(<roll result>, <min possible roll>, <max possible roll>, <median roll>, <thrown out val>)`  

Rolling 1, 20 sided die with advantage:
```pycon
print(dice_roller_instance.roll(advantage=True, show_advantage_val=True))
>>> (19, 1, 20, 10.5, 7)
```
Rolling 2, 4 sided die with disadvantage:
```pycon
print(dice_roller_instance.roll((2, 4), advantage=False, show_advantage_val=True))
>>> (2, 2, 8, 5.0, 8)
```

On the logic of why roll returns more than just the actual result of the roll (NOT DOCUMENTATION):  
roll() returns the min, max and median possible roll results alongside the actual result of the roll to help
the user identify whether the roll was good or not.  While this might not be difficult to do when rolling, say
1, 20 sided die, because it is apparent that the worst roll would be a 1 and the best would be a 20 and the 
right in the middle is (about) 10. But if we roll 3, 4 sided die plus 2, 6 sided die, it is not immediately
apparent what a good or bad roll would be from that.  The min possible result helps us identify if we got the worst 
result, and the opposite being true for the max possible result. And the median possible result helps us know 
whether the result of our roll was closer to the highest or lowest possible roll result.

## static_roll() Method
static_roll() works the same way as the roll() method, except that it does not require an instance of 
DiceRoller to be called, and it does not save the results.  
```pycon
print(DiceRoller.static_roll())
>>> (13, 1, 20, 10.5)

print(DiceRoller.static_roll((2, 4), (1, 2)))
>>> (4, 3, 10, 6.5)

print(DiceRoller.static_roll((3, 6)))
>>> (8, 3, 18, 10.5)

print(DiceRoller.static_roll((1, 6), advantage=True, show_advantage_val=True))
>>> (3, 1, 6, 3.5, 3)

print(DiceRoller.static_roll((1, 2), (2, 5), advantage=False, show_advantage_val=True))
>>> (4, 3, 12, 7.5, 8)
```

## history() Method
history() takes no arguments and returns a JSON friendly dictionary containing info regarding every roll a given
instance of DiceRoller has made.  The keys in this dictionary are "Roll_X" where x is the number of rolls the 
DiceRoller instance has made before (Ex: "Roll_0" is the key for the first roll made).  The corresponding 
values are another dictionary, with the keys 'Dice' (dice rolled), 'Result' (the result from the roll), 
'Min' (the min possible roll result), 'Max' (the max possible roll result), and 'Median' (median possible roll).
If an instance of DiceRoller has no roll records, then history will just return an empty dictionary.
```pycon
new_instance = DiceRoller()
print(new_instance.history())
>>> {}

print(new_instance.roll((1, 10), (3, 4), (1, 1)))
>>> (7, 5, 23, 14.0)
print(new_instance.roll((1, 4), (2, 6)))
>>> (15, 3, 16, 9.5)

print(new_instance.history())
>>> {'roll_0': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 10}, 
'dice_1': {'number_of_dice': 3, 'number_of_sides': 4}, 
'dice_2': {'number_of_dice': 1, 'number_of_sides': 1}}, 
'result': 7, 'min': 5, 'max': 23, 'median': 14.0}, 
'roll_1': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 4}, 
'dice_1': {'number_of_dice': 2, 'number_of_sides': 6}}, 
'result': 15, 'min': 3, 'max': 16, 'median': 9.5}}
```
Use Python's json package to 'pretty print' the dictionary
```pycon
import json

history_dict = new_instance.history()
print(json.dumps(history_dict, indent=4))
>>>{
    "roll_0": {
        "dice": {
            "dice_0": {
                "number_of_dice": 1,
                "number_of_sides": 10
            },
            "dice_1": {
                "number_of_dice": 3,
                "number_of_sides": 4
            },
            "dice_2": {
                "number_of_dice": 1,
                "number_of_sides": 1
            }
        },
        "result": 7,
        "min": 5,
        "max": 23,
        "median": 14.0
    },
    "roll_1": {
        "dice": {
            "dice_0": {
                "number_of_dice": 1,
                "number_of_sides": 4
            },
            "dice_1": {
                "number_of_dice": 2,
                "number_of_sides": 6
            }
        },
        "result": 15,
        "min": 3,
        "max": 16,
        "median": 9.5
    }
}
```

## clear() Method
clear() takes no arguments and empties the records of rolls from a given instance of DiceRoller.
```pycon
third_instance = DiceRoller()

print(third_instance.history())
>>> {}
print(third_instance.roll())
>>> (4, 1, 20, 10.5)
print(third_instance.history())
>>> {'Roll_0': {'Dice': ((1, 20),), 'Result': 4, 'Min': 1, 'Max': 20, 'Median': 10.5}}

print(third_instance.clear())
>>> History Cleared!
print(third_instance.history())
>>> {}
```

## Development Note
Among the tests for dice_roller there is a directory called typo_hunting, containing a file called test_find_roles.
This purpose of this test is to find what files have a 'role' written in them, and how often it occurs in a given 
file.  This was created because M-Cintron kept on writing 'role's instead of 'roll's throughout this project.
If there is an unexpected number of 'role's in any file, (or if the test is ran on Windows) test_find_roles 
will fail. If a file is supposed to have 'role's written in it, go to test_find_roles, add the file's path to the 
dictionary 'acceptable_roles' as a string, and the associated value being the number of times 'role' appears
in that file.  Make sure that the top two directories of the file path are 'dice_roller/dice_roller'.  

For example, this very README.md file has a lot of purposeful 'role's in it, so here is what the 
acceptable_roles dictionary should look like: 
```pycon
acceptable_roles = {"dice_roller/dice_roller/README.md": 13}
```
