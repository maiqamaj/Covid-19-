import pandas as pd
from tkinter import *
from pandastable import Table
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns
def exit() :
    x=messagebox.askyesno(title="Exit", message="Do you want to exit ")
    if (x):
         root.destroy()
def de():
    peace.pack_forget()
    lbl.pack_forget()
    lb.pack_forget()
    pe.pack_forget()
    frame2.pack(side=RIGHT)
    peac.pack(side=LEFT)

def bi():
    peace.pack()
    lb.pack()
    lbl.pack()
    pe.pack()
    frame2.pack_forget()
    frame3.pack_forget() #@
    all()


def display():
    all()
    frame3.pack(side=LEFT)
    table = Table(frame3, dataframe=df,showtoolbar=False,showstatusbar=False,width=730,height=415)
    table.show()
def d():
    all()
    x=clicked.get()
    x = df.loc[df.countriesAndTerritories == x]
    frame3.pack(side=LEFT)
    table = Table(frame3, dataframe=x, showtoolbar=False, showstatusbar=False,width=730,height=415)
    table.show()

def f():
    all()
    z = cl.get()
    x = df.loc[df.countriesAndTerritories == z]
    a = x.groupby('month').cases.sum()
    a = pd.DataFrame(a)
    frame3.pack(side=LEFT)
    table1 = Table(frame3, dataframe=a, showtoolbar=False, showstatusbar=False,width=730,height=415)
    table1.show()

def f1():
    all()
    z = cll.get()
    x = df.loc[df.countriesAndTerritories == z]
    a = x.groupby('month').deaths.sum()
    a = pd.DataFrame(a)
    frame3.pack(side=LEFT)
    table1 = Table(frame3, dataframe=a, showtoolbar=False, showstatusbar=False,width=730,height=415)
    table1.show()
def f2():
    all()
    x = df.groupby(['month']).cases.agg([max,sum])
    a = pd.DataFrame(x)
    frame3.pack(side=LEFT)
    table1 = Table(frame3, dataframe=a , showtoolbar=False, showstatusbar=False,width=730,height=415)
    table1.show()
def f3():
    all()
    x = df.groupby(['month']).deaths.agg([max, sum])
    a = pd.DataFrame(x)
    frame3.pack(side=LEFT)
    table1 = Table(frame3, dataframe=a , showtoolbar=False, showstatusbar=False,width=730,height=415)
    table1.show()
def all():
    ClAAAfrica.pack_forget()
    ClAafrica.pack_forget()
    ChLabel.pack_forget()
    peac.pack_forget()
    Cl.pack_forget()
    ClA.pack_forget()
    ClAA.pack_forget()
    Cll.pack_forget()
def ll():
    peac.pack_forget()
    frame3.pack_forget()
def f44():
    ll()
    Cll.pack_forget()
    ClAAAfrica.pack_forget()
    ClAafrica.pack_forget()
    ClA.pack_forget()
    Cl.pack_forget()
    ClAA.pack_forget()
    ChLabel.pack(side=LEFT)
def f55():
    ll()
    Cll.pack_forget()
    ClAAAfrica.pack_forget()
    ClAafrica.pack_forget()
    ClA.pack_forget()
    ChLabel.pack_forget()
    ClAA.pack_forget()
    Cl.pack(side=LEFT)
def asia():
    ll()
    Cll.pack_forget()
    ClAAAfrica.pack_forget()
    ClAafrica.pack_forget()
    Cl.pack_forget()
    ChLabel.pack_forget()
    ClAA.pack_forget()
    ClA.pack(side=LEFT)
def Asia():
    ll()
    Cll.pack_forget()
    ClAAAfrica.pack_forget()
    ClAafrica.pack_forget()
    Cl.pack_forget()
    ChLabel.pack_forget()
    ClA.pack_forget()
    ClAA.pack(side=LEFT)
def africa():
    ll()
    Cll.pack_forget()
    ClAAAfrica.pack_forget()
    Cl.pack_forget()
    ChLabel.pack_forget()
    ClA.pack_forget()
    ClAA.pack_forget()
    ClAafrica.pack(side=LEFT)
def africadeaths():
    ll()
    Cll.pack_forget()
    ClAafrica.pack_forget()
    Cl.pack_forget()
    ChLabel.pack_forget()
    ClA.pack_forget()
    ClAA.pack_forget()
    ClAAAfrica.pack(side=LEFT)

def cases():
    ll()
    ClAafrica.pack_forget()
    Cl.pack_forget()
    ChLabel.pack_forget()
    ClA.pack_forget()
    ClAA.pack_forget()
    Cll.pack(side=LEFT)


root = Tk()
root.minsize(1000, 600)
root.title("COVID-19")
root.resizable(0,0)
df = pd.read_csv('covid-19.csv')
#################################
phot = PhotoImage(file='CA.PNG')
peac = Label(master=root, image=phot, width=800,height=450)
###################################################################
frame1 = Frame(root, highlightbackground="black", highlightthickness=3, width=980, height=40)
frame1.place(relx=0.01, rely=0.01)
frame2 = Frame(root, highlightbackground="black", highlightthickness=3, width=105, height=500)
frame3 = Frame(root, highlightbackground="black", highlightthickness=3)

#################################
display = Button(root,text='Display Data',font=('Arial'), bg='#812109',bd=3,fg='white',command=display)
display.place(relx=0.012, rely=0.015)
dis = Button(root,text='Display Data City',font=('Arial'),bg='#812109',fg='white', bd=3,command=d)
dis.place(relx=0.2, rely=0.015)
xz=df['countriesAndTerritories'].unique()
clicked=StringVar()
clicked.set('Jordan')
d1=OptionMenu(root,clicked,*xz)
d1.place(relx=0.12, rely=0.015)
###########################################)
cl=StringVar()
cl.set('Jordan')
d2=OptionMenu(root,cl,*xz)
d2.place(relx=0.34, rely=0.015)
dis = Button(root,text='Number of Cases ',font=('Arial'),bg='#812109',fg='white', bd=3,command=f)
dis.place(relx=0.42, rely=0.015)
##############################################
cll=StringVar()
cll.set('Jordan')
d2=OptionMenu(root,cll,*xz)
d2.place(relx=0.565, rely=0.015)
dis = Button(root,text='Number of Deaths ',font=('Arial'),bg='#812109',fg='white', bd=3,command=f1)
dis.place(relx=0.645, rely=0.015)
####################################
dis = Button(root,text='Cases',font=('Arial'),width=9,bg='#812109',fg='white', bd=3,command=f2)
dis.place(relx=0.796, rely=0.015)
####################################
dis = Button(root,text='Deaths',font=('Arial'),bg='#812109',width=9,fg='white', bd=3,command=f3)
dis.place(relx=0.894, rely=0.015)
####################################
tExit=Button(root,text="Exit",font=('Arial'),bg='#812109',fg='white',width=10 ,bd=5,command=lambda: exit())
tExit.place(relx = 0.0,rely = 1.0,anchor ='sw')
GO = Button(root, text="Next",font=('Arial'),bg='#812109',fg='white', bd=5,width=10, command=lambda: de())
GO.place(relx = 0.895,rely = 1.0,anchor ='sw')
G = Button(root, text="Back",font=('Arial'),bg='#812109',fg='white', bd=5,width=10, command=lambda: bi())
G.place(relx = 0.78,rely = 1.0,anchor ='sw')
####################################
photo = PhotoImage(file='Capture.PNG')
peace = Label(master=root,image=photo, width=1000, height=300)
peace.pack()
lb =Label(root, text='COVID-19', foreground="#000000",font=('Arial',17), height=1, width=10)
lb.pack()
lbl =Label(root, text='The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing pandemic of coronavirus disease 2019 (COVID-19)\n caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2),It was first identified in December 2019 in Wuhan, China.\n  The World Health Organization declared the outbreak a Public Health Emergency of International Concern in January 2020 and a pandemic \n in March 2020, As of 24 December 2020, more than 78.7 million cases of the disease have been confirmed, with more than 1.73 million \n deaths attributed to COVID-19.', foreground="#000000",font=('Arial',10), height=6, width=100)
lbl.pack()
pho= PhotoImage(file='C.PNG')
pe = Label(master=root,image=pho, width=350, height=100)
pe.pack()
#222222222222222222222222222222222222
Z=df.loc[:,['continentExp','cases']]
x=Z.groupby('continentExp').cases.sum()
sns.barplot(x=x.index,y= x.values)
C11 = PhotoImage(file="ALLcases.PNG")
Cll = Label(root, image=C11)
Cll.img = C11
d11 = Button(frame2,text='ALL Cases Chart',font=('Arial'),bg='#707070',width=17,height=2,fg='white', bd=3,command=cases)
d11.pack()
#######################################
Z=df.loc[df['countriesAndTerritories'].isin(['Armenia', 'Austria','Spain','Turkey','Italy','United_Kingdom','France','Greece','Iceland','Monaco'])]
x=Z.groupby('countriesAndTerritories').cases.sum()
sns.barplot(x=x.index,y= x.values)
C2 = PhotoImage(file="Europe.PNG")
Cl = Label(root, image=C2)
Cl.img = C2
d22 = Button(frame2,text='Europe Cases Chart',font=('Arial'),bg='#812109',width=17,height=3,fg='white', bd=3,command=f55)
d22.pack()
#################################
E=Z.groupby('countriesAndTerritories').deaths.sum()
sns.barplot(x=E.index,y= E.values)
sns.relplot(data=df, x='month', y='cases')
C1 = PhotoImage(file="Er.PNG")
ChLabel = Label(root, image=C1)
ChLabel.img = C1
d11 = Button(frame2,text='Europe Deaths Chart',font=('Arial'),bg='#812109',width=17,height=3,fg='white', bd=3,command=f44)
d11.pack()

#######################################
Z=df.loc[df['countriesAndTerritories'].isin(['Jordan','Iraq','Lebanon','Palestine','China','Syria','Japan','Qatar','Iran','Saudi_Arabia'])]
x=Z.groupby('countriesAndTerritories').cases.sum()
sns.barplot(x=x.index,y= x.values)
C3= PhotoImage(file='Asia.PNG')
ClA = Label(root, image=C3)
ClA.img = C3
As = Button(frame2,text='Asia Cases Chart',font=('Arial'),bg='#812109',width=17,height=3,fg='white', bd=3,command=asia)
As.pack()
####################################
AS=Z.groupby('countriesAndTerritories').deaths.sum()
sns.barplot(x=AS.index,y= AS.values)
C4= PhotoImage(file="As.PNG")
ClAA= Label(root, image=C4)
ClAA.img = C4
Ass = Button(frame2,text='Asia Deaths Chart',font=('Arial'),bg='#812109',width=17,height=3,fg='white', bd=3,command=Asia)
Ass.pack()
#####################################
Z=df.loc[df['countriesAndTerritories'].isin(['Egypt', 'Liberia','Tunisia','Libya','South_Africa','Comoros','Sudan','Eritrea','Chad','Namibia'])]
x=Z.groupby('countriesAndTerritories').cases.sum()
sns.barplot(x=x.index,y= x.values)
C5= PhotoImage(file='Africa.PNG')
ClAafrica = Label(root, image=C5)
ClAafrica.img = C3
Asafrica = Button(frame2,text='Africa Cases Chart',font=('Arial'),bg='#812109',width=17,height=3,fg='white', bd=3,command=africa)
Asafrica.pack()
#######################################
AS=Z.groupby('countriesAndTerritories').deaths.sum()
sns.barplot(x=AS.index,y= AS.values)
C6= PhotoImage(file="Africadeaths.PNG")
ClAAAfrica= Label(root, image=C4)
ClAAAfrica.img = C6
Assafrica = Button(frame2,text='Africa Deaths Chart',font=('Arial'),bg='#812109',width=17,height=3,fg='white', bd=3,command=africadeaths)
Assafrica.pack()
####################################


root.mainloop()
