# Text-Based Adventure Game (PS 31)

A Python 3 adventure game where the player explores a forest, a cave and a river, faces random monster attacks, collects score, and ends the game by quitting or losing all health. The project has two versions: a console (CLI) version and a graphical (Tkinter) version.

**Name:** <your name>
**Roll No.:** <your roll number>
**Course / Semester:** <course>, Semester 1

## Versions

| File | Description |
|---|---|
| `<cli_file>.py` | Console version. Menu-driven, uses `input()` and `print()` |
| `<gui_file>.py` | Graphical version built with Tkinter, with buttons and live Health/Score labels |

## Features

- Starts in the forest with Health 100 and Score 0
- Cave: a cave spider attacks for random damage (10 to 40). If the player survives, a key gives +20 score
- River: a treasure gives +50 score
- Game over when Health reaches 0, with a closing message
- Player can quit at any time (CLI: option 3, GUI: Quit button)
- Each place has its own function: `cave()`, `river()`, plus `main()` for the menu and `dead()` in the CLI version

## Concepts Used

- Conditions (`if` / `elif` / `else`)
- Loops (the CLI menu repeats by calling `main()` again; the GUI runs on Tkinter's `mainloop()`)
- Functions
- Random module (`random.randint(10, 40)`)
- Global variables for `health` and `score`
- Tkinter widgets (GUI version): `Label`, `Button`, `Frame`

## How to Run

Install Python 3, then run from the console:

```bash
python <cli_file>.py     # console version
python <gui_file>.py     # graphical version (Tkinter comes with Python)
```

## Game Rules

| Choice | Place | Effect |
|---|---|---|
| 1 | Cave | Random damage 10 to 40. If Health is still above 0, +20 score (key) |
| 2 | River | +50 score (treasure) |
| 3 | Quit | Shows final health and score (CLI) |

## Testing

To test the fixed-damage cases from the problem statement, temporarily change the damage line in `cave()` to a fixed value:

```python
dam = 30   # instead of random.randint(10, 40)
```

For the boundary case, also set `health = 30` at the top of the file.

| Test Case | Input | Expected Result |
|---|---|---|
| 1. Normal | River | Treasure found, Score 50, Health 100 |
| 2. Boundary | Health 30, damage 30, Cave | Health 0, Game Over, Final score 0 |
| 3. Invalid | `7` | Invalid choice message, no health lost |
| 4. Mixed | damage 30, Cave, River, Quit | Health 70, Score 70 at the end |

## Known Limitations

<!-- Delete this section once you have fixed these. -->
- CLI: typing text such as `abc` instead of a number is not handled yet.
- GUI: only valid choices are possible because input is by buttons.

## Screenshots

Add screenshots of the CLI and GUI versions in a `screenshots/` folder.
