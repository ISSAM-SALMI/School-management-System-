from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
root = Tk()
root.iconbitmap(R"C:\Users\issam\Desktop\school_manage\image\icon.ico")
window_height = 768
window_width = 1366
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate,y_cordinate))
root.title("تسجيل الدخول")
root.resizable(0,0)
user  = StringVar()
passw = StringVar()
username  = "aaaa"
passworld = "aaaa"

def login(Event=None) :
    userr = user.get()
    passe = passw.get()
    if (username==userr) and (passe==passworld) :
        messagebox.showinfo("صفحة تسجيل الدخول","تم تسجيل الدخول بنجاح")
        page1.entry1.delete(0,END)
        page1.entry2.delete(0,END)
        root.withdraw()
        global principale
        global page2
        principale   = Toplevel()
        page2 = Page_principale(principale)
    else :
        messagebox.showerror("Error", "اسم المستخدم أو كلمة المرور غير صحيحة")
        page1.entry2.delete(0, END)

class login_page :
    def __init__(self, top=None) :
        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\login.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.373, rely=0.373, width=374, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.373, rely=0.512, width=374, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passw)

        self.button1 = Button(root)
        self.button1.place(relx=0.403, rely=0.673, width=280, height=71)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#77d9da")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#77d9da")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(command=login)
    

class Page_principale :
    def __init__(self, top=None) :
        window_height = 768
        window_width  = 1366
        screen_width  = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate,y_cordinate))
        top.resizable(0, 0)
        top.title("Page principale")
        top.iconbitmap(R"C:\Users\issam\Desktop\school_manage\image\icon.ico")
        self.label1 = Label(principale)
        self.label1.place(x=0,y=0)
        self.img = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\pafeprici.png")
        self.label1.configure(image=self.img)
        
        self.button1 = Button(principale)
        self.button1.place(x=280,y=220, width=143, height=150)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#ffffff")
        self.button1.configure(borderwidth="0")
        self.img2 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\inscription.png")
        self.button1.configure(image=self.img2)
        self.button1.configure(command=self.inscrii)
        
        self.label2 = Label(principale, text=" Inscription " , bg="#ffffff", fg="black",font=("Arial Black",18))
        self.label2.place(x=270,y=355)
        
        self.button2 = Button(principale)
        self.button2.place(x=590,y=220, width=143, height=150)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#ffffff")
        self.button2.configure(borderwidth="0")
        self.img3 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\suiv.png")
        self.button2.configure(image=self.img3)
        self.label3 = Label(principale, text=" Suivi " , bg="#ffffff", fg="black",font=("Arial Black",18))
        self.label3.place(x=610,y=355)
        self.button2.configure(command=self.suivi)
        
        self.button3 = Button(principale)
        self.button3.place(x=900,y=220, width=143, height=150)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#ffffff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#ffffff")
        self.button3.configure(borderwidth="0")
        self.img4 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\recherchee.png")
        self.button3.configure(image=self.img4)
        self.label4 = Label(principale, text=" Recherche " , bg="#ffffff", fg="black",font=("Arial Black",18))
        self.label4.place(x=900,y=355)
        self.button3.configure(command=self.rechercheretudiant)
        
        self.button4 = Button(principale)
        self.button4.place(x=900,y=410, width=143, height=150)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#ffffff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#ffffff")
        self.button4.configure(borderwidth="0")
        self.img5 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\ficheinscrii.png")
        self.button4.configure(image=self.img5)
        self.label5 = Label(principale, text=" Fiche d'Inscription " , bg="#ffffff", fg="black",font=("Arial Black",18))
        self.label5.place(x=850,y=540)
        self.button4.configure(command=self.print)

        self.button5 = Button(principale)
        self.button5.place(x=280,y=410, width=143, height=150)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#ffffff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#ffffff")
        self.button5.configure(borderwidth="0")
        self.img6 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\basedonne.png")
        self.button5.configure(image=self.img6)
        self.button5.configure(command=self.basedonne)
        self.label5 = Label(principale, text=" Database " , bg="#ffffff", fg="black",font=("Arial Black",18))
        self.label5.place(x=280,y=540)


        self.button6 = Button(principale)
        self.button6.place(x=590,y=410, width=143, height=150)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#ffffff")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#ffffff")
        self.button6.configure(borderwidth="0")
        self.img7 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\aboutus.png")
        self.button6.configure(image=self.img7)
        self.button6.configure(command=self.startpdf)
        self.label5 = Label(principale, text=" Qui Nous " , bg="#ffffff", fg="black",font=("Arial Black",18))
        self.label5.place(x=590,y=540)
    
    def startpdf(self) :
        os.startfile(R"C:\Users\issam\Desktop\school_manage\Centre AFAQ.pdf")

    def inscrii(self) :
        global inscription
        global page3
        inscription = Toplevel()
        page3 = Page_inscription(inscription)
        inscription.mainloop()
    def rechercheretudiant(self) :
        global page4
        global search
        search = Toplevel()
        page4  = pourchercher(search)
        search.mainloop()
    def basedonne(self) :
        global page5
        global bsdn
        bsdn  = Toplevel()
        page5 = basedonée(bsdn) 
    def suivi(self)  :
        global page6
        global suivii
        suivii = Toplevel()
        page6  = suivietudiant(suivii)
    def print(self) :
        global page7
        global printt
        printt = Toplevel()
        page7  = Imprimmer(printt)
class Page_inscription :
    def __init__(self, top=None) :
        window_height = 768
        window_width  = 1366
        screen_width  = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate,y_cordinate))
        top.resizable(0, 0)
        top.title("Page d'Inscription")
        top.iconbitmap(R"C:\Users\issam\Desktop\school_manage\image\icon.ico")
        self.label1 = Label(inscription)
        self.label1.place(x=0,y=0)
        self.img = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\pageinscription.png")
        self.label1.configure(image=self.img)
        self.Id_var = IntVar()
        self.prenom_var = StringVar()
        self.nom_var = StringVar()
        self.date_var = StringVar()
        self.sexe_var = StringVar()
        self.phone_var = StringVar()
        self.adresse_var = StringVar()
        self.type_var = StringVar()


        self.label1 = Label(inscription)
        self.label1.place(x=0,y=0)
        self.img = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\pageinscription.png")
        self.label1.configure(image=self.img)
        self.entry1 = Entry(inscription)
        self.entry1.place(x=140,y=230, width=400, height=28)
        self.entry1.configure(font=("Aileron Heavy",12))
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=self.Id_var)
        
        self.entry2 = Entry(inscription)
        self.entry2.place(x=220,y=330, width=350, height=28)
        self.entry2.configure(font=("Aileron Heavy",12))
        self.entry2.configure(relief="flat")
        self.entry2.configure(textvariable=self.prenom_var)
        
        self.entry3 = Entry(inscription)
        self.entry3.place(x=180,y=427, width=300, height=28)
        self.entry3.configure(font=("Aileron Heavy",12))
        self.entry3.configure(relief="flat")
        self.entry3.configure(textvariable=self.nom_var)
        self.entry4 = DateEntry(inscription,selectmode='day',textvariable=self.date_var)
        self.entry4.place(x=360,y=521, width=200, height=28)
   
   
        self.entry5 = ttk.Combobox(inscription,values=["Homme","Femme"])
        self.entry5.place(x=860,y=230, width=320, height=28)
        self.entry5.configure(font=("Aileron Heavy",12))
        self.entry5.configure(textvariable=self.sexe_var)
        
        self.entry6 = Entry(inscription)
        self.entry6.place(x=930,y=330, width=320, height=28)
        self.entry6.configure(font=("Aileron Heavy",12))
        self.entry6.configure(relief="flat")
        self.entry6.configure(textvariable=self.phone_var)
        
        self.entry7 = Entry(inscription)
        self.entry7.place(x=900,y=428, width=320, height=28)
        self.entry7.configure(font=("Aileron Heavy",12))
        self.entry7.configure(relief="flat")
        self.entry7.configure(textvariable=self.adresse_var)
        
        self.entry8 = ttk.Combobox(inscription,values=["Crèche","Soutiens","Francais","English","Allmangne","Néerlandais","Espagnol","Informatique","Programmation","Comptabilité","Autre"])
        self.entry8.place(x=860,y=520, width=320, height=28)
        self.entry8.configure(font=("Aileron Heavy",12))
        self.entry8.configure(textvariable=self.type_var)
        
        self.button1 = Button(inscription) 
        self.button1.configure(relief="flat", width=7,height=1)
        self.button1.place(x=575,y=610)
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#5ce1e6")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#5ce1e6")
        self.button1.configure(font=("Arial Black",13))
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Ajouter""")
        self.button1.configure(command=self.ajouteretudiant)
        
        
        self.button2 = Button(inscription) 
        self.button2.configure(relief="flat", width=7,height=1)
        self.button2.place(x=710,y=610)
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#5ce1e6")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#5ce1e6")
        self.button2.configure(font=("Arial Black",13))
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Effacer""")
        self.button2.configure(command=self.effacer)
        self.btnimg = Button(inscription)
        self.btnimg.place(x=90,y=40, width=20,height=20)
        self.btnimg.configure(background="white")
        self.btnimg.configure(activebackground="white")
        self.img2 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\arrir.png")
        self.btnimg.configure(image=self.img2)
        self.btnimg.configure(relief='flat')
        self.btnimg.configure(border=0,borderwidth=0)
        self.btnimg.configure(command=self.Logout)


    def Logout(self):
        principale.deiconify()
        inscription.destroy()
    def effacer(self) :
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)
        self.entry5.delete(0,END)
        self.entry6.delete(0,END)
        self.entry7.delete(0,END)
        self.entry8.delete(0,END)
        self.entry1.focus()

    def ajouteretudiant(self) :
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("""insert into Adminzahra values(?,?,?,?,?,?,?,?)""",(
                                                self.Id_var.get(),
                                                self.prenom_var.get(),
                                                self.nom_var.get(),
                                                str(self.date_var.get()),
                                                self.sexe_var.get(),
                                                str(self.phone_var.get()),
                                                self.adresse_var.get(),
                                                self.type_var.get()))
        con.commit()
        con.close()
class pourchercher :
    def __init__(self,top=None) :
        window_height = 768
        window_width  = 1366
        screen_width  = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate,y_cordinate))
        top.resizable(0, 0)
        top.title("Recherche")
        top.iconbitmap(R"C:\Users\issam\Desktop\school_manage\image\icon.ico")
        self.label = Label(search)
        self.label.place(x=0,y=0)
        self.img = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\recherche.png")
        self.label.configure(image=self.img)
        self.liste_var = StringVar()
        self.Id_var = IntVar()
        self.prenom_var = StringVar()
        self.nom_var = StringVar()
        self.date_var = StringVar()
        self.sexe_var = StringVar()
        self.phone_var = StringVar()
        self.adresse_var = StringVar()
        self.type_var = StringVar()
        self.char_var = StringVar()
        self.scrollbarx = Scrollbar(search, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(search, orient=VERTICAL)
        self.tree = ttk.Treeview(search,
                    columns=('Id','prénom','Nom','datenaissance','sexe','phone','adresse','type'),
                    xscrollcommand=self.scrollbarx.set,
                    yscrollcommand=self.scrollbary.set)
        self.tree.place(x=458,y=120, width=823, height=540)
        self.scrollbarx.pack(fill=X,side=BOTTOM)
        self.scrollbary.pack(fill=Y,side=LEFT)
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbarx.place(x=459,y=658,width=815)
        self.scrollbary.place(x=1280,y=161,height=491)
        self.tree['show'] = 'headings'
        self.tree.heading('Id',text='Id',anchor=W)
        self.tree.heading('prénom',text='Prénom',anchor=W)
        self.tree.heading('Nom',text='Nom',anchor=W)
        self.tree.heading('datenaissance',text='Date de Naissance',anchor=W)
        self.tree.heading('sexe',text='Sexe',anchor=W)
        self.tree.heading('phone',text='Némuro de Téléphone',anchor=W)
        self.tree.heading('adresse',text='Adresse',anchor=W)
        self.tree.heading('type',text='Type',anchor=W)
        self.tree.column("#0", stretch=NO, minwidth=0)
        self.tree.column("#1", stretch=NO, minwidth=0)
        self.tree.column("#2", stretch=NO, minwidth=0)
        self.tree.column("#3", stretch=NO, minwidth=0)
        self.tree.column("#4", stretch=NO, minwidth=0)
        self.tree.column("#5", stretch=NO, minwidth=0)
        self.tree.column("#6", stretch=NO, minwidth=0)
        self.tree.column("#7", stretch=NO, minwidth=0)

        self.tree.bind("<Double-Button-1>",self.getinformation)
        self.fetch_all()
    def fetch_all(self) :
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("select * from Adminzahra")
        result = cur.fetchall()
        if len(result) != 0 :
            self.tree.delete(*self.tree.get_children())
            for row in result :
                self.tree.insert('',END,value=row)
        con.commit()
        con.close()
        
        self.cmb = ttk.Combobox(search,values=["Id","Prenom","Nom","Date de Naissance"])
        self.cmb.place(x=84,y=156,width=240)
        self.cmb.configure(text="Charcher par Nom")
        self.cmb.configure(background="white")
        self.cmb.configure(font=("Aileron Heavy",12))
        self.cmb.configure(textvariable=self.char_var)
        
        self.entry1 = Entry(search)
        self.entry1.place(x=87,y=202, width=220, height=28)
        self.entry1.configure(font=("Aileron Heavy",12))
        self.entry1.configure(relief="flat")
        
        
        self.button1 = Button(search)
        self.button1.place(x=362,y=183, width=76, height=40)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#5ce1e6")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="white")
        self.button1.configure(background="#5ce1e6")
        self.button1.configure(font=("Arial Black",13))
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_etu)
        
        self.button2 = Button(search)
        self.button2.place(x=155,y=606, width=72, height=45)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#5ce1e6")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="white")
        self.button2.configure(background="#5ce1e6")
        self.button2.configure(font=("Arial Black",13))
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Update""")
        self.button2.configure(command=self.update_étudiant)
        
        self.button3 = Button(search)
        self.button3.place(x=305,y=606, width=72, height=45)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#5ce1e6")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="white")
        self.button3.configure(background="#5ce1e6")
        self.button3.configure(font=("Arial Black",13))
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Effacer""")
        self.button3.configure(command=self.effacettous)
        
        self.entry11 = Entry(search)
        self.entry11.configure(borderwidth=2)
        self.entry11.place(x=200,y=270, width=250, height=28)
        self.entry11.configure(font=("Aileron Heavy",12))
        self.entry11.configure(textvariable=self.Id_var)
        
        self.entry12 = Entry(search)
        self.entry12.configure(borderwidth=2)
        self.entry12.place(x=200,y=310, width=250, height=28)
        self.entry12.configure(font=("Aileron Heavy",12))
        self.entry12.configure(textvariable=self.prenom_var)
        
        self.entry13 = Entry(search)
        self.entry13.configure(borderwidth=2)
        self.entry13.place(x=200,y=350, width=250, height=28)
        self.entry13.configure(font=("Aileron Heavy",12))
        self.entry13.configure(textvariable=self.nom_var)
        
        self.entry14 = DateEntry(search,selectmode='day')
        self.entry14.place(x=200,y=390, width=250, height=28)
        self.entry14.configure(textvariable=self.date_var)

        
        self.entry15 = ttk.Combobox(search,values=["Homme","Femme"])
        self.entry15.place(x=200,y=430, width=250, height=28)
        self.entry15.configure(font=("Aileron Heavy",12))
        self.entry15.configure(textvariable=self.sexe_var)
        
        self.entry16 = Entry(search)
        self.entry16.configure(borderwidth=2)
        self.entry16.place(x=200,y=470, width=250, height=28)
        self.entry16.configure(font=("Aileron Heavy",12))
        self.entry16.configure(textvariable=self.phone_var)
        
        self.entry17 = Entry(search)
        self.entry17.configure(borderwidth=2)
        self.entry17.place(x=200,y=510, width=250, height=28)
        self.entry17.configure(font=("Aileron Heavy",12))
        self.entry17.configure(textvariable=self.adresse_var)
        
        self.entry18 = ttk.Combobox(search,values=["Crèche","Soutiens","Francais","English","Allmangne","Néerlandais","Espagnol","Informatique","Programmation","Comptabilité","Autre"])
        self.entry18.place(x=200,y=550, width=250, height=28)
        self.entry18.configure(font=("Aileron Heavy",12))
        self.entry18.configure(textvariable=self.type_var)
        
        self.label1 = Label(search)
        self.label1.place(x=70,y=270)
        self.label1.configure(text="Id ")
        self.label1.configure(font=("Arial Black",8))
        self.label1.configure(background="#ffffff")
        
        self.label2 = Label(search)
        self.label2.place(x=70,y=310)
        self.label2.configure(text="Prénom")
        self.label2.configure(font=("Arial Black",8))
        self.label2.configure(background="#ffffff")
        
        self.label3 = Label(search)
        self.label3.place(x=70,y=350)
        self.label3.configure(text="Nom")
        self.label3.configure(font=("Arial Black",8))
        self.label3.configure(background="#ffffff")
        
        self.label4 = Label(search)
        self.label4.place(x=70,y=390)
        self.label4.configure(text="Date de Naissance")
        self.label4.configure(font=("Arial Black",8))
        self.label4.configure(background="#ffffff")
        
        self.label5 = Label(search)
        self.label5.place(x=70,y=430)
        self.label5.configure(text="Sexe")
        self.label5.configure(font=("Arial Black",8))
        self.label5.configure(background="#ffffff")
        
        self.label6 = Label(search)
        self.label6.place(x=70,y=470)
        self.label6.configure(text="Téléphone")
        self.label6.configure(font=("Arial Black",8))
        self.label6.configure(background="#ffffff")
        
        self.label7 = Label(search)
        self.label7.place(x=70,y=510)
        self.label7.configure(text="Adresse")
        self.label7.configure(font=("Arial Black",8))
        self.label7.configure(background="#ffffff")
        
        self.label8 = Label(search)
        self.label8.place(x=70,y=550)
        self.label8.configure(text="Type")
        self.label8.configure(font=("Arial Black",8))
        self.label8.configure(background="#ffffff")
        
        self.btnimg = Button(search)
        self.btnimg.place(x=90,y=40, width=20,height=20)
        self.btnimg.configure(background="white")
        self.btnimg.configure(activebackground="white")
        self.img2 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\arrir.png")
        self.btnimg.configure(image=self.img2)
        self.btnimg.configure(relief='flat')
        self.btnimg.configure(border=0,borderwidth=0)
        self.btnimg.configure(command=self.Logout)
    def search_etu(self) :
        searchavec = self.char_var.get()
        if searchavec == "Id" :
            tosearch = self.entry1.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahra where  Id = ?",(tosearch,))
            views = cur.fetchall()
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7],record[8]))
            con.commit()
            con.close()
        elif searchavec == "Prenom" :
            tosearch = self.entry1.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahra where  prenom = ?",(tosearch,))
            views = cur.fetchall()
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7],record[8]))
            con.commit()
            con.close()
        elif searchavec == "Nom" :
            tosearch = self.entry1.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahra where  nom = ?",(tosearch,))
            views = cur.fetchall()
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7],record[8]))
            con.commit()
            con.close()
        elif searchavec == "Date de Naissance" :
            tosearch = self.entry1.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahra where  date = ?",(tosearch,))
            views = cur.fetchall()
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7],record[8]))
            con.commit()
            con.close()
    def getinformation(self,ev) :
        cursor_row = self.tree.focus()
        content = self.tree.item(cursor_row)
        row = content["values"]
        self.Id_var.set(row[0])
        self.prenom_var.set(row[1])
        self.nom_var.set(row[2])
        self.date_var.set(row[3])
        self.sexe_var.set(row[4])
        self.phone_var.set(row[5])
        self.adresse_var.set(row[6])
        self.type_var.set(row[7])
    def update_étudiant(self) :
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute(("""update Adminzahra set prenom = ? , nom = ? , date = ? , sexe = ? , phone = ?, adresse = ?, type = ? where Id = ?"""),(
                                            self.prenom_var.get(),
                                            self.nom_var.get(),
                                            str(self.date_var.get()),
                                            self.sexe_var.get(),
                                            str(self.phone_var.get()),
                                            self.adresse_var.get(),
                                            self.type_var.get(),
                                            self.Id_var.get()))
                         
        con.commit()
        con.close()
        self.fetch_all()
    def effacettous(self) :
        self.entry11.delete(0,END)
        self.entry12.delete(0,END)
        self.entry13.delete(0,END)
        self.entry14.delete(0,END)
        self.entry15.delete(0,END)
        self.entry16.delete(0,END)
        self.entry17.delete(0,END)
        self.entry18.delete(0,END)
        self.entry11.focus()
    def Logout(self):
        sure = messagebox.askyesno("Revenir en arriere", "Êtes-vous sûr de vouloir vous déconnecter?")
        if sure == True :
            principale.deiconify()
            search.destroy()
class basedonée :
    def __init__(self,top=None) :
        window_height = 768
        window_width  = 1366
        screen_width  = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate,y_cordinate))
        top.resizable(0, 0)
        top.title("Base Donneé")
        top.iconbitmap(R"C:\Users\issam\Desktop\school_manage\image\icon.ico")
        self.label = Label(bsdn)
        self.label.place(x=0,y=0)
        self.img   = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\database.png") 
        self.label.configure(image=self.img)

        self.char_var  = StringVar()
        self.choix_var = StringVar()
        self.label1 = Label(bsdn)
        self.label1.place(x=10,y=15)
        self.label1.configure(text="Supprimer étudiant avec  :")
        self.label1.configure(font=("Arial Black",12))
        self.label1.configure(background="#ffffff")
        
        self.entry = ttk.Combobox(bsdn,values=["Id","Téléphone","Nom"],textvariable=self.choix_var)
        self.entry.place(x=250,y=20)
        
        self.entry1 = Entry(bsdn)
        self.entry1.place(x=250,y=45,width=142)
        self.entry1.configure(textvariable=self.char_var)
        
        self.button1 = Button(bsdn)
        self.button1.place(x=250,y=67)
        self.button1.configure(text="""Supprimer""")
        self.button1.configure(background="white")
        self.button1.configure(fg="white")
        self.button1.configure(relief='flat')
        self.button1.configure(background="black")
        self.button1.configure(font=("Arial Black",8))
        self.button1.configure(command=self.effacer_etudiant)
        self.btnimg = Button(bsdn)
        self.btnimg.place(x=10,y=3, width=20,height=20)
        self.btnimg.configure(background="white")
        self.btnimg.configure(activebackground="white")
        self.img2 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\arrir.png")
        self.btnimg.configure(image=self.img2)
        self.btnimg.configure(relief='flat')
        self.btnimg.configure(border=0,borderwidth=0)
        self.btnimg.configure(command=self.Logout)


        self.scrollbarx = Scrollbar(bsdn, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(bsdn, orient=VERTICAL)
        self.tree = ttk.Treeview(bsdn,
                    columns=('Id','prénom','Nom','datenaissance','sexe','phone','adresse','type'),
                    xscrollcommand=self.scrollbarx.set,
                    yscrollcommand=self.scrollbary.set)
        self.tree.place(x=0,y=100, width=1342, height=618)
        self.scrollbarx.pack(fill=X,side=BOTTOM)
        self.scrollbary.pack(fill=Y,side=LEFT)
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbarx.place(x=0,y=715,width=1344)
        self.scrollbary.place(x=1340,y=100,height=630)
        self.tree['show'] = 'headings'
        self.tree.heading('Id',text='Id',anchor=W)
        self.tree.heading('prénom',text='Prénom',anchor=W)
        self.tree.heading('Nom',text='Nom',anchor=W)
        self.tree.heading('datenaissance',text='Date de Naissance',anchor=W)
        self.tree.heading('sexe',text='Sexe',anchor=W)
        self.tree.heading('phone',text='Némuro de Téléphone',anchor=W)
        self.tree.heading('adresse',text='Adresse',anchor=W)
        self.tree.heading('type',text='Type',anchor=W)
        self.tree.column("#0", stretch=NO, minwidth=0)
        self.tree.column("#1", stretch=NO, minwidth=0)
        self.tree.column("#2", stretch=NO, minwidth=0)
        self.tree.column("#3", stretch=NO, minwidth=0)
        self.tree.column("#4", stretch=NO, minwidth=0)
        self.tree.column("#5", stretch=NO, minwidth=0)
        self.tree.column("#6", stretch=NO, minwidth=0)
        self.tree.column("#7", stretch=NO, minwidth=0)
        self.tree.bind("<ButtonRelease-1>",self.getinformation)
        self.fetch_all()
    def Logout(self):
        principale.deiconify()
        bsdn.destroy()
    def fetch_all(self) :
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("select * from Adminzahra")
        result = cur.fetchall()
        if len(result) != 0 :
            self.tree.delete(*self.tree.get_children())
            for row in result :
                    self.tree.insert('',END,value=row)
        con.commit()
        con.close()
    def getinformation(self,ev) :
        cursor_row = self.tree.focus()
        content = self.tree.item(cursor_row)
        row = content["values"]
        messagebox.showinfo("Information"," Id : {} \n prénom : {} \n nom : {} \n Date de naissance : {} \n Sexe : {} \n Téléphone : {} \n Adresse : {} \n Type : {}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    def effacer_etudiant(self) :
        suprimerpar = self.entry.get()
        try :
            if suprimerpar == 'Id' :
                con = sqlite3.connect("Adminzahra.db")
                cur = con.cursor()
                cur.execute("delete  from Adminzahra where Id = {} ".format(self.char_var.get()))                        
                con.commit()
                con.close()
                self.fetch_all()
            elif suprimerpar == 'Téléphone' :
                con = sqlite3.connect("Adminzahra.db")
                cur = con.cursor()
                cur.execute("delete  from Adminzahra where phone = ? ",(self.char_var.get(),))                      
                con.commit()
                con.close()
                self.fetch_all()
            elif suprimerpar == 'Nom' :
                con = sqlite3.connect("Adminzahra.db")
                cur = con.cursor()
                cur.execute("delete  from Adminzahra where nom = ? ",(self.char_var.get(),))                    
                con.commit()
                con.close()
                self.fetch_all()
        except :
            messagebox.showerror("Erreur","quelque information que vous avez saisi n'existe pas")
class suivietudiant() :
    def __init__(self,top=None) :
        window_height = 768
        window_width  = 1366
        screen_width  = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate,y_cordinate))
        top.title("Suivi")
        top.iconbitmap(R"C:\Users\issam\Desktop\school_manage\image\icon.ico")
        self.id_var = IntVar()
        self.prenom_var = StringVar()
        self.nom_var = StringVar()
        self.type_var = StringVar()
        self.dateinscri_var = StringVar()
        self.prix_var = IntVar()
        self.avance_var = DoubleVar()
        
        self.label = Label(suivii)
        self.label.place(x=0,y=0,width=1366,height=768)
        self.img = PhotoImage(file=R'C:\Users\issam\Desktop\school_manage\image\suivii.png')
        self.label.configure(image=self.img)
        
        self.scrollbarx = Scrollbar(suivii, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(suivii, orient=VERTICAL)
        self.tree = ttk.Treeview(suivii,
                    columns=('Id','prénom','Nom','Type','dateinscription','payment','Avance'),
                    xscrollcommand=self.scrollbarx.set,
                    yscrollcommand=self.scrollbary.set)
        self.tree.place(x=575,y=0, width=775, height=695)
        self.scrollbarx.pack(fill=X,side=BOTTOM)
        self.scrollbary.pack(fill=Y,side=LEFT)
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbarx.place(x=575,y=693,width=775)
        self.scrollbary.place(x=1350,y=0,height=710)
        self.tree['show'] = 'headings'
        self.tree.heading('Id',text='Id',anchor=W)
        self.tree.heading('prénom',text='Prénom',anchor=W)
        self.tree.heading('Nom',text='Nom',anchor=W)
        self.tree.heading('Type',text="Matière",anchor=W)
        self.tree.heading('dateinscription',text="Date d'Inscription",anchor=W)
        self.tree.heading('payment',text='Prix',anchor=W)
        self.tree.heading('Avance',text='Avance',anchor=W)
        self.tree.column("#0", stretch=NO, minwidth=0)
        self.tree.column("#1", stretch=NO, minwidth=0)
        self.tree.column("#2", stretch=NO, minwidth=0)
        self.tree.column("#3", stretch=NO, minwidth=0)
        self.tree.column("#4", stretch=NO, minwidth=0)
        self.tree.column("#5", stretch=NO, minwidth=0)
        self.tree.column("#6", stretch=NO, minwidth=0)
        self.tree.bind("<Double-Button-1>",self.getinformation)
        self.tree.bind("<ButtonRelease-3>",self.getinformation2)
        self.fetch_all()
        
        
        self.menubar = Menu(suivii)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="avec avance",command=self.withavance)
        self.filemenu.add_command(label="Payment complete",command=self.withoutavance)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="Student", menu=self.filemenu)
        
        self.chercher_ = Menu(self.menubar, tearoff=0)
        self.chercher_.add_command(label="Avec Id",command=self.chercheId)
        self.chercher_.add_command(label="Avec Préenom",command=self.chercheprenom)
        self.chercher_.add_command(label="Avec Nom",command=self.cherchenom)
        self.chercher_.add_command(label="Avec Date insciption",command=self.cherchedateinscription)
        self.chercher_.add_command(label="Avec Avance",command=self.chercheavvance)
        self.chercher_.add_separator()
        self.chercher_.add_command(label="Afficher Tous",command=self.fetch_all)       
        self.menubar.add_cascade(label="Recherche",menu=self.chercher_)

        self.supprimer_ = Menu(self.menubar,tearoff=0)
        self.supprimer_.add_command(label="Avec Id",command=self.suprrimerId)
        self.supprimer_.add_command(label="Avec Nom",command=self.supprimernom)
        self.supprimer_.add_command(label="Avec Matière",command=self.suprrimermatiere)
        self.menubar.add_cascade(label="Supprimer",menu=self.supprimer_)

        self.fixdata = Menu(suivii,tearoff=0)
        self.fixdata.add_command(label="Afficher Fixe data",command=self.afficherfixdata)
        self.fixdata.add_command(label="Chercher Avec Id",command=self.chercheIdfix)
        self.fixdata.add_separator()
        self.fixdata.add_command(label="Suprrimer Avec Id",command=self.suprrimerIdfix)
        self.fixdata.add_command(label="Suprrimer Avec Matiere",command=self.suprrimermatierefix)
        self.menubar.add_cascade(label="Fix-data",menu=self.fixdata)



        self.order = Menu(self.menubar,tearoff=0)
        self.order.add_command(label="Avec Id",command=self.orderid)
        self.order.add_command(label="Avec Nom",command=self.ordernom)
        self.order.add_command(label="Avec Prenom",command=self.orderprenom)
        self.order.add_command(label="Avec Prix",command=self.orderpayment)
        self.order.add_command(label="Avec DAte d'inscription",command=self.orderdateinscription)
        self.order.add_command(label="Avec Avance",command=self.orderavance)
        self.order.add_separator()
        self.menubar.add_cascade(label="Order",menu=self.order)
        
        
        self.entry1 = Entry(suivii)
        self.entry1.place(x=70,y=108, width=400, height=28)
        self.entry1.configure(font=("Aileron Heavy",12))
        self.entry1.configure(relief="flat")
        self.entry1.configure(background="#5ce1e6")
        self.entry1.configure(textvariable=self.id_var)
        
        self.entry2 = Entry(suivii)
        self.entry2.place(x=142,y=187, width=300, height=28)
        self.entry2.configure(font=("Aileron Heavy",12))
        self.entry2.configure(relief="flat")
        self.entry2.configure(background="#5ce1e6")
        self.entry2.configure(textvariable=self.prenom_var)
        
        self.entry3 = Entry(suivii)
        self.entry3.place(x=115,y=260, width=300, height=28)
        self.entry3.configure(font=("Aileron Heavy",12))
        self.entry3.configure(relief="flat")
        self.entry3.configure(background="#5ce1e6")
        self.entry3.configure(textvariable=self.nom_var)

        self.entry4 = ttk.Combobox(suivii,values=["Crèche","Soutiens","Francais","English","Allmangne","Néerlandais","Espagnol","Informatique","Programmation","Comptabilité","Autre"])
        self.entry4.place(x=280,y=335, width=220, height=28 )
        self.entry4.configure(textvariable=self.type_var)


        self.entry5 = DateEntry(suivii,selectmode='day')
        self.entry5.place(x=280,y=410, width=220, height=28 )
        self.entry5.configure(textvariable=self.dateinscri_var)
        
        self.entry6 = Entry(suivii)
        self.entry6.place(x=110,y=486, width=350, height=28)
        self.entry6.configure(font=("Aileron Heavy",12))
        self.entry6.configure(relief="flat")
        self.entry6.configure(background="#5ce1e6")
        self.entry6.configure(textvariable=self.prix_var)
        
        self.entry7 = Entry(suivii)
        self.entry7.place(x=145,y=545, width=350, height=28)
        self.entry7.configure(font=("Aileron Heavy",12))
        self.entry7.configure(relief="flat")
        self.entry7.configure(background="#5ce1e6")
        self.entry7.configure(textvariable=self.avance_var)
        
        self.button1 = Button(suivii)
        self.button1.place(x=102,y=622, width=129, height=62)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#5ce1e6")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#5ce1e6")
        self.button1.configure(background="white")
        self.button1.configure(fg="black")
        self.button1.configure(font=("Arial Black",13))
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Ajouter""")
        self.button1.configure(command=self.ajouteretudiant)
        
        self.button2 = Button(suivii)
        self.button2.place(x=283,y=622, width=129, height=62)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#5ce1e6")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#5ce1e6")
        self.button2.configure(background="white")
        self.button2.configure(fg="black")
        self.button2.configure(font=("Arial Black",13))
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Effacer""")
        self.button2.configure(command=self.effacer)
        
        suivii.config(menu=self.menubar)

        self.btnimg = Button(suivii)
        self.btnimg.place(x=10,y=5, width=20,height=20)
        self.btnimg.configure(background="white")
        self.btnimg.configure(activebackground="white")
        self.img2 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\arrir.png")
        self.btnimg.configure(image=self.img2)
        self.btnimg.configure(relief='flat')
        self.btnimg.configure(border=0,borderwidth=0)
        self.btnimg.configure(command=self.Logout)

        
    def Logout(self):
        principale.deiconify()
        suivii.destroy()

    def ajouteretudiant(self) :
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("""insert into Adminzahrasuivi values(?,?,?,?,?,?,?)""",(
                                                self.id_var.get(),
                                                self.prenom_var.get(),
                                                self.nom_var.get(),
                                                self.type_var.get(),
                                                str(self.dateinscri_var.get()),
                                                self.prix_var.get(),
                                                self.avance_var.get()))
        con.commit()
        con.close()
        self.fetch_all()
        conn = sqlite3.connect("Adminzahra.db")
        curr = conn.cursor()
        curr.execute("""insert into Adminzahrasuivi2 values(?,?,?,?,?,?,?)""",(
                                                self.id_var.get(),
                                                self.prenom_var.get(),
                                                self.nom_var.get(),
                                                self.type_var.get(),
                                                str(self.dateinscri_var.get()),
                                                self.prix_var.get(),
                                                self.avance_var.get()))
        conn.commit()
        conn.close()

    def fetch_all(self) :
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("select * from Adminzahrasuivi")
        result = cur.fetchall()
        if len(result) != 0 :
            self.tree.delete(*self.tree.get_children())
            for row in result :
                    self.tree.insert('',END,value=row)
    def effacer(self) :
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)
        self.entry5.delete(0,END)
        self.entry6.delete(0,END)
        self.entry7.delete(0,END)
        self.entry1.focus()
    def withavance(self) :
        for record in self.tree.get_children() :
            self.tree.delete(record)
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("select rowid,* from Adminzahrasuivi where  avance > 0")
        views = cur.fetchall()
        global count
        count = 0
        for record in views :
            self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
        con.commit()
        con.close()
    def withoutavance(self) :
        for record in self.tree.get_children() :
            self.tree.delete(record)
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("select rowid,* from Adminzahrasuivi where  avance = 0")
        views = cur.fetchall()
        global count
        count = 0
        for record in views :
            self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
        con.commit()
        con.close()
    def chercheId(self) :
            tosearch = self.entry1.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi where  Id = ?",(tosearch,))
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def chercheIdfix(self) :
            tosearch = self.entry1.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi2 where  Id = ?",(tosearch,))
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def chercheprenom(self) :
            tosearch = self.entry2.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi where  prenom = ?",(tosearch,))
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def cherchenom(self) :
            tosearch = self.entry3.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi where  nom = ?",(tosearch,))
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def cherchedateinscription(self) :
            tosearch = self.entry5.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi where  dateinscription = ?",(tosearch,))
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def chercheavvance(self) :
            tosearch = self.entry7.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi where  avance = ?",(tosearch,))
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def affichertous(self) :
            tosearch = self.entry6.get()
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select * from Adminzahrasuivi")
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def suprrimerId(self) :
        tosupp = self.entry1.get()
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("delete  from Adminzahrasuivi where Id = ? ",(tosupp,))                      
        con.commit()
        con.close()
        self.fetch_all()
    def suprrimerIdfix(self) :
        tosupp = self.entry1.get()
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("delete  from Adminzahrasuivi2 where Id = ? ",(tosupp,))                      
        con.commit()
        con.close()
        self.afficherfixdata()
    def supprimernom(self) :
        tosupp = self.entry3.get()
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("delete  from Adminzahrasuivi where nom = ? ",(tosupp,))                      
        con.commit()
        con.close()
        self.fetch_all()
    def afficherfixdata(self) :
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("select * from Adminzahrasuivi2")
        result = cur.fetchall()
        if len(result) != 0 :
            self.tree.delete(*self.tree.get_children())
            for row in result :
                    self.tree.insert('',END,value=row)
    def suprrimermatiere(self) :
        tosupp  = self.entry4.get()
        tosuppp = self.entry1.get()
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("delete  from Adminzahrasuivi where Id = ? and matiere = ? ",(tosuppp,tosupp,))                      
        con.commit()
        con.close()
        self.fetch_all()
    def suprrimermatierefix(self) :
        tosupp = self.entry4.get()
        tosuppp = self.entry1.get()
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("delete  from Adminzahrasuivi where Id = ? and matiere = ? ",(tosuppp,tosupp,))                      
        con.commit()
        con.close()
        self.afficherfixdata()
    def getinformation(self,ev) :
        cursor_row = self.tree.focus()
        content = self.tree.item(cursor_row)
        row = content["values"]
        self.id_var.set(row[0])
        self.prenom_var.set(row[1])
        self.nom_var.set(row[2])
        self.type_var.set(row[3])
        self.dateinscri_var.set(row[4])
        self.prix_var.set(row[5])
        self.avance_var.set(row[6])
    def getinformation2(self,ev) :
        cursor_row = self.tree.focus()
        content = self.tree.item(cursor_row)
        row = content["values"]
        a = float(row[5]) - float(row[6])
        messagebox.showinfo("Reste","  {}  {} a {} DH  pour completez le reste du prix en {}".format(row[1],row[2],a,row[5]))
        
    def orderid(self) :
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi order by Id asc")
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def orderidfix(self) :
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi order by Id asc")
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def orderprenom(self) :
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi order by prenom asc")
            views = cur.fetchall()
            global count
            count = 0
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def ordernom(self) :
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi order by nom asc")
            views = cur.fetchall()
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def orderpayment(self) :
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi order by prix asc")
            views = cur.fetchall()
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def orderdateinscription(self) :
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi order by dateinscription")
            views = cur.fetchall()
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
    def orderavance(self) :
            for record in self.tree.get_children() :
                self.tree.delete(record)
            con = sqlite3.connect("Adminzahra.db")
            cur = con.cursor()
            cur.execute("select rowid,* from Adminzahrasuivi order by avance asc")
            views = cur.fetchall()
            for record in views :
                self.tree.insert(parent='',index='end',values=(record[1], record[2], record[3], record[4], record[5],record[6],record[7]))
            con.commit()
            con.close()
class Imprimmer :
    def __init__(self,top=None) :
        top.title("Fiche d'Inscription")
        window_height = 768
        window_width  = 1366
        screen_width  = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate,y_cordinate))
        top.resizable(0, 0)
        top.title("Base Donneé")
        top.iconbitmap(R"C:\Users\issam\Desktop\school_manage\image\icon.ico")

        self.label = Label(printt)
        self.label.place(x=0,y=0)
        self.img   = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\database.png") 
        self.label.configure(image=self.img)
        self.btnimg = Button(printt)
        self.btnimg.place(x=10,y=5, width=20,height=20)
        self.btnimg.configure(background="white")
        self.btnimg.configure(activebackground="white")
        self.img2 = PhotoImage(file=R"C:\Users\issam\Desktop\school_manage\image\arrir.png")
        self.btnimg.configure(image=self.img2)
        self.btnimg.configure(relief='flat')
        self.btnimg.configure(border=0,borderwidth=0)
        self.btnimg.configure(command=self.Logout)

        

        self.scrollbarx = Scrollbar(printt, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(printt, orient=VERTICAL)
        self.tree = ttk.Treeview(printt,
                    columns=('Id','prénom','Nom','Dateinscription','payment','avance','matiere'),
                    xscrollcommand=self.scrollbarx.set,
                    yscrollcommand=self.scrollbary.set)
        self.tree.place(x=0,y=100, width=1342, height=618)
        self.scrollbarx.pack(fill=X,side=BOTTOM)
        self.scrollbary.pack(fill=Y,side=LEFT)
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbarx.place(x=0,y=715,width=1344)
        self.scrollbary.place(x=1340,y=100,height=630)
        self.tree['show'] = 'headings'
        self.tree.heading('Id',text='Id',anchor=W)
        self.tree.heading('prénom',text='Prénom',anchor=W)
        self.tree.heading('Nom',text='Nom',anchor=W)
        self.tree.heading('Dateinscription',text="Date d'Inscription",anchor=W)
        self.tree.heading('payment',text='prix',anchor=W)
        self.tree.heading('avance',text='avance',anchor=W)
        self.tree.heading('matiere',text='Matière',anchor=W)
        self.tree.column("#0", stretch=NO, minwidth=0)
        self.tree.column("#1", stretch=NO, minwidth=0)
        self.tree.column("#2", stretch=NO, minwidth=0)
        self.tree.column("#3", stretch=NO, minwidth=0)
        self.tree.column("#4", stretch=NO, minwidth=0)
        self.tree.column("#5", stretch=NO, minwidth=0)
        self.tree.column("#6", stretch=NO, minwidth=0)
        self.tree.bind("<ButtonRelease-1>",self.getinformation)
        self.fetch_all()
    def Logout(self):
        principale.deiconify()
        printt.destroy()
    def fetch_all(self) :
        con = sqlite3.connect("Adminzahra.db")
        cur = con.cursor()
        cur.execute("select c.Id , c.prenom , c.nom , a.dateinscription , a.prix , a.avance , a.matiere from Adminzahra c inner join Adminzahrasuivi a on c.type = a.matiere and c.Id = a.Id")
        result = cur.fetchall()
        if len(result) != 0 :
            self.tree.delete(*self.tree.get_children())
            for row in result :
                    self.tree.insert('',END,value=row)
        con.commit()
        con.close()
    def getinformation(self,ev) :
        cursor_row = self.tree.focus()
        content = self.tree.item(cursor_row)
        row = content["values"]
        self.packet = io.BytesIO()
# create a new PDF with Reportlab
        self.can = canvas.Canvas(self.packet, pagesize=letter)
        self.can.drawString(80, 600, "Id                            :    {}".format(row[0]))
        self.can.drawString(80, 560, "prénom                   :    {}".format(row[1]))
        self.can.drawString(80, 520, "Nom                        :    {}".format(row[2]))
        self.can.drawString(80, 480, "Date d'inscription    :    {}".format(row[3]))
        self.can.drawString(80, 440, "Prix                          :    {}".format(row[4]))
        self.can.drawString(80, 400, "Avance                    :    {}".format(row[5]))
        self.can.drawString(80, 360, "Matière                     :    {}".format(row[6]))
        self.can.save()
        
        #move to the beginning of the StringIO buffer
        self.packet.seek(0)
        self.new_pdf = PdfFileReader(self.packet)
        # read your existing PDF
        self.existing_pdf = PdfFileReader(open(R"C:\Users\issam\Desktop\school_manage\bb.pdf", "rb"))
        self.output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        self.page = self.existing_pdf.getPage(0)
        self.page.mergePage(self.new_pdf.getPage(0))
        self.output.addPage(self.page)
        # finally, write "output" to a real file
        destionation = "{}-{}".format(row[1],row[2])
        self.outputStream = open("{}.pdf".format(destionation), "wb")
        self.output.write(self.outputStream)
        self.outputStream.close()
        os.startfile(R'C:\Users\issam\Desktop\school_manage\{}.pdf'.format(destionation))
        printt.destroy()
                
        
page1 = login_page(root)
root.bind("<Return>", login)
root.mainloop()
        