import tkinter
def W():
    print('Hello,getting out of here')


root=tkinter.Tk()
Wind1=tkinter.Tk()
Wind1.title("King")
Widgt1=tkinter.Label(root,text='hello virendar').pack()
tkinter.Button(root,text='hello world',command=root.quit).pack()
tkinter.Button(root,text='press me',command=root.quit).pack()
#tkinter.Menu(root,'Hello Aman').pack()

root.mainloop()
