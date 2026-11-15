# Project Summary: Text-Based Adventure Game (PS 31)

## Problem Definition

Build a text-based adventure game in Python 3 where the player explores a forest, a cave and a river by choosing menu options. The player faces random monster attacks, collects score, and the game ends when the player quits or Health reaches 0.

## Approach

The game keeps two values, `health` (starts at 100) and `score` (starts at 0). Each place is a separate function:

- **forest()** shows the menu (1 Cave, 2 River, 3 Quit) and validates the input.
- **cave()** reduces health by a random amount from 10 to 40. If the player survives, a key adds 20 to the score.
- **river()** adds 50 to the score for finding treasure.
- **get_damage()** returns the monster damage, either random or a fixed value for testing.

A `while` loop in `main()` keeps the game running until the player quits or health reaches 0. Invalid input prints an error and returns to the menu without any health loss.

## Concepts Applied

| Concept | Where it is used |
|---|---|
| Conditions | Menu choices, survival check, health floor at 0 |
| Loops | Main game loop that runs while health is above 0 |
| Functions | One function per place, plus a damage function |
| Random | `random.randint(10, 40)` for monster damage |

## Testing Summary

All four test cases from the problem statement were run and matched the expected output: normal input, boundary case (health reaching exactly 0), invalid input (`7` and `abc`), and a mixed scenario ending in Quit with score 70 and health 70.

## Challenges and Learning

- Validating input as a string prevents crashes when the player types text instead of a number.
- Using a fixed-damage setting makes random behavior testable and repeatable.
- Clamping health at 0 avoids negative health values.

## Possible Improvements

- Add more places and items, such as a healing potion.
- Save and show a high score.
- Add a graphical interface (for example with Tkinter).

## Conclusion

The project meets all the bare minimum requirements: functions for each place, conditions for choices, a game loop, the random module for damage, input validation and a final score display.
