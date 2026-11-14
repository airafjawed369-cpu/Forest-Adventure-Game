import random
import tkinter as tk

health=100
score=0

root=tk.Tk()
root.title("Forest Game")
root.geometry("480x360")
root.resizable(False, False)

def cave():
    global health, score
    dam=random.randint(10,40)
    health-=dam
    if health>0:
        score+=20
        message.config(
            text=f"CAVE: Cave spider attacks!!"\n
                 f"Damage: {dam}"\n
                 f"You've found a key in the cave! (+20 Score)"
        )
    else:
        dead()

def dead():
    message.config(text="Game Over"\n
                   f"You fought and died a legend"\n
                   f"Score:{score}  Health:{health}")


button_frame
cave_button=tk.Button()
#hello