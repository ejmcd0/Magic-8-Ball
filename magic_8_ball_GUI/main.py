from tkinter import *
import random

ASK_BG= "#396CF3"
BACKGROUND= "#D7E2FF"
window = Tk()
window.title("Magic 8 Ball")
window.config(padx=20, pady=60, bg=BACKGROUND)

canvas = Canvas(width=600, height=600, bg=BACKGROUND, highlightthickness=0)
ball = PhotoImage(file="ball-back.png")
canvas.create_image(300, 250, image=ball)
start_text=canvas.create_text(300, 250, text="Ask me anything", fill="white", font=("Helvetica", 20, "normal"))
canvas.grid(column=1, row=1)

def ask_me():
    #canvas.create_text(300, 250, text="Ask me anything", fill="white", font=("Helvetica", 24, "normal"))
    canvas.itemconfig(start_text, text="Ask me anything")

def start_over():
    erase_text()
    q_box.insert(END, chars="Type your question here...")
    

def clear_text_on_click(event):
    q_box.delete("1.0", END)

def erase_text():
    q_box.delete("1.0", END)
    ask_me()

q_box = Text(width=45, height=3, wrap=WORD, highlightbackground=BACKGROUND)
q_box.insert(END, chars="Type your question here...")
q_box.bind("<Button-1>", clear_text_on_click)
did_ask = q_box.get("1.0", END) #get current text value at line 1, character 0 to the end
q_box.grid(column=1, row=2)

with open("8ball_answers.txt") as answers:
    content = answers.readlines()

def thinking():
    answer = random.choice(content)
    canvas.itemconfig(start_text, text=answer)
    # canvas.create_text(300, 250, text="Thinking...", fill="white", font=("Helvetica", 24, "normal"))


ask_button = Button(text="Ask", command=thinking, highlightbackground=BACKGROUND)
ask_button.place(x=125,y=660)
#ask_button.grid(column=1, row=3)

clear_button = Button(text="Clear", command=erase_text, highlightbackground=BACKGROUND)
clear_button.place(x=200, y=660)
#clear_button.grid(column=2, row=3)


play_again = Button(text="Play Again", command=start_over, highlightbackground=BACKGROUND)
play_again.place(x=275, y=660)
#play_again.grid(column=3, row=3)


def close_window():
    window.destroy()

exit_game = Button(text="Quit", command=close_window, highlightbackground=BACKGROUND)
exit_game.place(x=390, y=660)
#exit_game.grid(column=4, row=3)



window.mainloop()