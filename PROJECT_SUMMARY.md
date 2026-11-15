# Project Summary: Text-Based Adventure Game (PS 31)

## Problem Definition

Create a text-based adventure game in Python 3 in which the player explores a forest, a cave and a river by choosing menu options, faces random monster attacks, collects score, and ends the game by quitting or losing all health.

## Approach

The program tracks two global variables, `health` (starts at 100) and `score` (starts at 0).

**Console version**
- `main()` prints the forest menu (1 Cave, 2 River, 3 Quit) and calls the matching function. After each action it calls `main()` again, so the game continues.
- `cave()` subtracts random damage (10 to 40) from health. If health is still above 0, the player finds a key and gets +20 score. Otherwise `dead()` is called.
- `river()` adds +50 score for finding treasure.
- `dead()` sets health to 0 and prints the Game Over message with the final health and score.
- Choosing Quit prints a thank-you message with the final health and score.

**Graphical version**
- Built with Tkinter using the same game logic. Buttons replace the typed menu, and Health and Score labels update after every action.
- When health reaches 0, the Cave and River buttons are disabled and a Game Over message is shown.
- Quit closes the window.

## Concepts Applied

| Concept | Where it is used |
|---|---|
| Conditions | Menu choices, survival check after a monster attack |
| Loops | Menu repeats until quit or death (CLI); event loop `mainloop()` (GUI) |
| Functions | Separate functions for the menu, cave, river and game over |
| Random | `random.randint(10, 40)` for monster damage |
| GUI basics | Labels, buttons, frames and button commands (Tkinter) |

## Testing Summary

The four test cases from the problem statement (normal input, boundary case, invalid input and a mixed scenario) were checked by fixing the damage to 30 and setting the starting health where required.

## Challenges and Learning

- Sharing `health` and `score` between functions using `global`.
- Making a random event testable by temporarily fixing the value.
- Moving the same logic from a console program to a Tkinter interface.

## Possible Improvements

- Handle non-numeric input in the CLI version.
- Show the final score in the GUI when the player quits.
- Add more places, items and a high score.

## Conclusion

Both versions implement the required game flow: place functions, menu choices, random damage, score and health tracking, and a game-ending condition.
