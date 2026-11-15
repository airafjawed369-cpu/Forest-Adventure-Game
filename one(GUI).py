import random
import tkinter as tk

health=100
score=0

root=tk.Tk()
root.title("Forest Game")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#17251B")

header_frame=tk.Frame(root, bg="#17251B")
header_frame.pack(pady=20)


title=tk.Label(
    header_frame,
    text="Forest Adventure",
    font=("Georgia", 26, "bold"),
    fg="#D4E6C3",
    bg="#17251B"
)
title.pack()


status_frame=tk.Frame(root, bg="#263B2C")
status_frame.pack(pady=15)

game_frame=tk.Frame(root, bg="#17251B")
game_frame.pack(pady=20)


health_label=tk.Label(
    status_frame,
    text=f"Health: {health}",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#263B2C"
)
health_label.grid(row=0, column=0,padx=40, pady=15)


score_label=tk.Label(
    status_frame,
    text=f"Score: {score}",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#263B2C"
)
score_label.grid(row=0, column=1, padx= 40,pady=15)


def cave():
    global health, score
    dam=random.randint(10,40)
    health-=dam
    if health>0:
        score+=20

        intro.config(text="Cave spider attacks!!! \n" \
        "You have found a key (+20 Score)")
    else:
        health=0
        game_over()
    health_label.config(text=f"Health: {health}")
    score_label.config(text=f"Score: {score}")

def river():
    global score
    score+=60
    intro.config(text="RIVER: You found a treasure in the river bed!\n (+60 Score)")
    score_label.config(text=f"Score: {score}")
def quit():
    root.destroy()

def game_over():
    intro.config(
        text="GAME OVER! \n" \
        "You fought bravely and died a legend."
    )
    cave_btn.config(state="disabled")
    river_btn.config(state="disabled")



intro=tk.Label(
    game_frame,
    text="You are in a mysterious forest.....",
    font=("Arial", 14),
    fg="white",
    bg="#17251B",
    wraplength=450
)
intro.pack(pady=10)

instruction=tk.Label(
    root,
    bg="lightgreen",
    text="Choose your path",
    font=("Arial", 14, "bold")
)
instruction.pack(pady=10)


button_style={
    "font": ("Arial", 12, "bold"),
    "width": 20,
    "bg": "#52734D",
    "fg": "white",
    "activebackground": "#73966C",
    "activeforeground": "white",
    "relief": "flat",
    "cursor": "hand2"
}

cave_btn=tk.Button(
    root,
    text="Enter Cave",
    command=cave,
    **button_style
)
cave_btn.pack(pady=8)


river_btn=tk.Button(
    root,
    text="Enter River",
    command= river,
    **button_style
)
river_btn.pack(pady=8)

quit_btn=tk.Button(
    root,
    text="QUIT GAME",
    command=quit,
    **button_style
)
quit_btn.pack(pady=8)




root.mainloop()