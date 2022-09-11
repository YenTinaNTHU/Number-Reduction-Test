from re import X
import tkinter as tk
import tkmacosx

def show():
    ans=radioVar.get()
    print(ans)


window = tk.Tk()
window.title('GUI')
window.geometry('380x400')
window.resizable(False, False)

label = tk.Label(text='1 2 3 4 5')
label.pack()

radioVar = tk.IntVar()
radio1 = tk.Radiobutton(text='1',variable=radioVar, value=1) 
radio2 = tk.Radiobutton(text='4',variable=radioVar, value=4) 
radio3 = tk.Radiobutton(text='9',variable=radioVar, value=9)
radio1.pack()
radio2.pack()
radio3.pack()

btn = tk.Button(text="submit",command=show)
btn.pack()
window.mainloop()

print(radioVar.get())