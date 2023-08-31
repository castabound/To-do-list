from asyncio import tasks
import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("To do list")

def task_adding():
    todo = task_add.get()
    if todo != "":
         todo_box.insert(tkinter.END, todo)
         task_add.delete(0, tkinter.END)
         
    else:
         tkinter.messagebox.showwarning(title="Warning", message="Please enter a task")
         
def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
        
    except:
        tkinter.messagebox.showwarning(title="Warning", message="Please select a task to delete it")
        
def task_loading():
    try:
        todo_list = pickle.load(open("tasks.dat","rb"))    
        list_frame.delete(0, tkinter, tkinter.END)
        for todo in tasks:
            list_frame.insert(tkinter.END, todo)
    except:
        tkinter.messagebox.showwarning(title="Warning", message="Cannot find a task")
        
list_frame = tkinter.Frame()
list_frame.pack()

todo_box = tkinter.Listbox(list_frame, height=25, width=45)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)

task_add = tkinter.Entry(window, width=60)
task_add.pack()

add_task_button = tkinter.Button(window, text= "CLICK TO ADD TASK", font=("serif", 15, "bold"), width=40, command=task_adding)
add_task_button.pack()

remove_task_button = tkinter.Button(window, text= "CLICK TO REMOVE TASK", font=("serif", 15, "bold"), width=40, command=task_removing)
remove_task_button.pack()


window.mainloop()
