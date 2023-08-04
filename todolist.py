#importing necessary files
import tkinter
from tkinter import *

#creating the gui frame
root = Tk()
root.title("Abilan's To-Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

tasklist = []

def addTask():
    t = task_entry.get()
    task_entry.delete(0, END)
    
    if t:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{t}")
        tasklist.append(t)
        itembox.insert(END, t)

def deleteTask():
    global tasklist
    t = str(itembox.get(ANCHOR))
    if t in tasklist:
        tasklist.remove(t)
        with open("tasklist.txt", "w") as taskfi:
            for t in tasklist:
                taskfi.write(t + "\n")

        itembox.delete(ANCHOR)


def openTaskFile():
    with open("tasklist.txt", "r") as taskfile:
        tasks = taskfile

    for task in tasks:
        if task != "\n":
            tasklist.append(task)
            itembox.insert(END, task)


#gui icon
icon = PhotoImage(file = "/Users/abilanravi/Desktop/todolist/images/task.png")
root.iconphoto(False, icon)

#the top of the gui
Bar = PhotoImage(file = "/Users/abilanravi/Desktop/todolist/images/bar.png")
Label(root, image = Bar).pack()

dock = PhotoImage(file = "/Users/abilanravi/Desktop/todolist/images/dock.png")
Label(root, image = dock, bg = (("#32405b"))).place(x = 30, y = 25)

task = PhotoImage(file = "/Users/abilanravi/Desktop/todolist/images/task.png")
Label(root, image = task, bg = (("#32405b"))).place(x = 320, y = 20)

header = Label(root, text = "ALL TASKS", font = "timesnewroman 20 bold", fg = (("#ffffff")), bg = (("#32405b")))
header.place(x = 135, y = 20)

#main part of gui
frame = Frame(root, width = 400, height = 50, bg = (("#323232")))
frame.place(x=0, y= 180)

taskbox = StringVar()
task_entry = Entry(frame, width = 20, font="timesnewroman 20", bd = 0)
task_entry.place(x=10, y = 7)
task_entry.focus()

button = Button(frame, text = "ADD", font = "timesnewroman 20 bold", width = 7, bg = (("#Faff00")), fg = (("#fff")), bd = 0, command = addTask)
button.place(x = 285, y = 5)

newframe = Frame(root, bd = 3, width = 700, height = 280, bg = (("#32405b")))
newframe.pack(pady = (160, 0))

itembox = Listbox(newframe, font=('arial', 12), width = 40, height = 16, bg = (("#32405b")), fg = (("#FFFFFF")),cursor = "hand2", selectbackground ="#5a95ff")
itembox.pack(side = LEFT, fill = BOTH, padx = 2)
scrollbar = Scrollbar(newframe)
scrollbar.pack(side = RIGHT, fill = BOTH)

itembox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command=itembox.yview)

#delete button
Deletephoto = PhotoImage(file = "/Users/abilanravi/Desktop/todolist/images/trash.png")
Button(root, image = Deletephoto, command = deleteTask, bg = (("#32405b")), bd = 0).pack(side = BOTTOM, pady = 13)


root.mainloop()
