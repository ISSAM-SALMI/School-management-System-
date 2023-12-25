import os
from tkinter import *
from tkinter import messagebox
#""""""""""""""""""""""""""""""""""""
main = Tk()
main.iconbitmap(R"C:\Users\issam\Desktop\school_manage\image\icon.ico")
window_height = 768
window_width = 1366
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate,y_cordinate))
main.resizable(False,False)
main.title("الوفاق")

def emp() :
    main.withdraw()
    os.system("python C:/Users/issam/Desktop/school_manage/pageprinc.py")

def Exit() :
    sure = messagebox.askyesno("oups","هل أنت متأكد أنك تريد الخروج",parent=main)
    if sure == True :
        main.destroy()
main.protocol("WM_DELETE_WINDOW", Exit)


label1 = Label(main)
label1.place(relx=0,rely=0,width=1366,height=768)
img = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\main.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.620, rely=0.500, width=143, height=150)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#eade56")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#eade56")
button1.configure(borderwidth="0")
img2 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\admin3.png")
button1.configure(image=img2)
button1.configure(command=emp)
label2 = Label(main, text=" ADMIN " , bg="#eade56", fg="black",font=("Arial Black",18))
label2.place(x=862,y=515)

button2 = Button(main)
button2.place(relx=0.740, rely=0.500, width=143, height=150)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#eade56")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#eade56")
button2.configure(borderwidth="0")
img3 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\quit.png")
button2.configure(image=img3)
button2.configure(command=main.quit)

label3 = Label(main, text=" Quit " , bg="#eade56", fg="black",font=("Arial Black",18))
label3.place(x=1045,y=515)

main.mainloop()