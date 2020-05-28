Switches Problem
------

Explanation:
---
Andrew do trip for switch the lamp, first trip switch will press all switch, second trip will press switch with number multiply by two, and third trip will press switch with number multiply by three. and repeated, so 4 trip will same like first trip, etc.

So we need indentify the trip, if result of module is 1, so that will use first trip pattern, if 2, so use second trip pattern, and if 0, so use third trip pattern. 

And then, to press the switch, I use first number of switch, and then add with multiply number. and to change condition lamp from on to off and vice versa, I using nand operation with True bolean value, cause True NAND True will result False, and False NAND True will result True.

Requirement:
> Python 3.x

How to Run?
---
```
python3 main.py
```