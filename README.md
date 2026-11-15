# Text-Based Adventure Game (PS 31)

A console-based adventure game written in Python 3. The player explores a forest, a cave and a river by choosing options from a menu, faces random monster attacks, collects score, and ends the game by quitting or losing all health.

**Name:** <your name>
**Roll No.:** <your roll number>
**Course / Semester:** <course>, Semester 1

## Features

- Three places, each handled by its own function: Forest (menu), Cave, River
- Random monster damage (10 to 40) using the `random` module
- Health and score tracking (start: Health 100, Score 0)
- Input validation: invalid choices show an error and no health is lost
- Game ends when the player quits or Health reaches 0, and the final score is shown

## Game Rules

| Choice | Place | Effect |
|---|---|---|
| 1 | Cave | Monster attacks (random damage 10 to 40). If the player survives, a key gives +20 score |
| 2 | River | Treasure gives +50 score |
| 3 | Quit | Ends the game and shows the final score |

The game also ends when Health reaches 0.

## Concepts Used

- Conditions (`if` / `elif` / `else`)
- Loops (`while`)
- Functions
- Random module (`random.randint`)

## How to Run

1. Install Python 3.
2. Download `adventure_game.py`.
3. Run it from the console:

```bash
python adventure_game.py
```

## Testing

Two settings at the top of the file make testing easier:

```python
START_HEALTH = 100
FIXED_DAMAGE = None   # set to 30 for testing; None = random 10-40
```

| Test Case | Settings | Input | Expected Output |
|---|---|---|---|
| 1. Normal | defaults | `2` | You found a treasure! Score: 50 \| Health: 100 |
| 2. Boundary | `START_HEALTH = 30`, `FIXED_DAMAGE = 30` | `1` | Monster attacks! Damage: 30. Health: 0, then Game Over! Final score: 0 |
| 3. Invalid | defaults | `7`, `abc` | Invalid choice. Enter 1, 2 or 3. (no health lost) |
| 4. Mixed | `FIXED_DAMAGE = 30` | `1`, `2`, `3` | Health 70, key found (Score 20), treasure (Score 70), then You left the adventure. Final score: 70 \| Health: 70 |

## Project Structure

```
.
├── adventure_game.py   # Game source code
├── README.md           # This file
└── PROJECT_SUMMARY.md  # Short project report
```

## Notes

<!-- If your course requires it, add a line here about any tools or resources you used, e.g. "I used an AI assistant to help me understand the approach." -->
