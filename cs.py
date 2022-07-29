from tkinter import *
root=Tk()
root.geometry('490x300')
root.geometry('+650+50')
root.title('测试')
picture=PhotoImage(file="E:\壁纸\dc4488063dcd5fab2430d5c22aa482f9.gif")
button3=Button(root,text='图片',image=picture,command='left')
button3.grid(row=2,column=8)
root.mainloop()