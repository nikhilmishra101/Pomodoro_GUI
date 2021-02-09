from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break",fg=PINK)

    elif reps%8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=1)



# Label
timer = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW,highlightthickness=0)
timer.grid(column=2,row=0)

checkmark = Label(text="✔",fg=GREEN,bg=YELLOW,highlightthickness=0)
checkmark.grid(column=2,row=4)

#button
start = Button(text="Start",command=start_timer,highlightthickness=0)
start.grid(column=1,row=3)
reset = Button(text="Reset",highlightthickness=0)
reset.grid(column=3,row=3)







window.mainloop()