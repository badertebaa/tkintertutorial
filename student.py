from tkinter import *
from tkinter import*
from connexion import connexion;
from tkinter import messagebox;
from tkinter import ttk

mywin=Tk()
mywin.geometry("1000x1000")
mywin.configure(bg="gray")
idlab=Label(mywin,fg="red" ,background="gray",font=('Calibri',13),text="id student")
idlab.place(x=10,y=10);
labelenom=Label(mywin,fg="red" ,background="gray",font=('Calibri',13),text="nom")
labelenom.place(x=280,y=10)
labelprenom=Label(mywin,fg="red" ,background="gray",font=('Calibri',13),text="prenom")
labelprenom.place(x=560,y=10)

def GetValue(event):
    studentid.delete(0, END)
    nomstudent.delete(0, END)
    prenomstudent.delete(0, END)
   
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    studentid.insert(0,select['idstudent'])
    nomstudent.insert(0,select['nom'])
    prenomstudent.insert(0,select['prenom'])
    




#enrty
idstudent=StringVar()
nom=StringVar()
prenom=StringVar()
studentid=Entry(fg="red",font=(8),textvariable=idstudent)
studentid.place(x=10,y=60)
nomstudent=Entry(fg="red",font=(8),textvariable=nom)
nomstudent.place(x=280,y=60)
prenomstudent=Entry(fg="red",font=(8),textvariable=prenom)
prenomstudent.place(x=540,y=60)
#functions
def removeall():
      x=listBox.get_children()
      if(x!='()'):
            for child in x:
              listBox.delete(child);


def add():
 if(idstudent.get()==""or prenom.get()==""or nom.get()==""):
    messagebox.showerror("champs vide")
 else:
    try:
      connect=connexion()
      conn = connect.connectionWithmysql()
      cursor = conn.cursor()
      sqlquery="insert into student(idstudent,nom,prenom )VALUES (%s,%s,%s)"
      val=(idstudent.get(),nom.get(),prenom.get(),);
      cursor.execute(sqlquery,val)
      conn.commit()
      conn.close()
      messagebox.showinfo("student insert correctly")
      idstudent.set("")
      nom.set("")
      prenom.set("")



    except:
        messagebox.showerror("utilisateur deja exist or champs vide")


def show():
    removeall()
    try:
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlQuery="SELECT*FROM student"
         cursor.execute(sqlQuery);
         myresulte=cursor.fetchall()
         conn.commit()
         conn.close()
         for book in myresulte:
            listBox.insert("",END,values=book)
    except:
        messagebox.showerror("error")

def delete():
     try:
       
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlquery="DELETE FROM student WHERE idstudent = %s"
         val=(idstudent.get(),)
         cursor.execute(sqlquery,val)
         conn.commit()
         conn.close
         messagebox.showinfo("user deleted succesfully")
         idstudent.set("")
         nom.set("")
         prenom.set("")
         
     except:
          messagebox.showerror("user is not in database")

def update():
     
     try:
        
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlquery="Update student set nom=%s,prenom=%s where idstudent=%s"
         values=(nom.get(),prenom.get(),idstudent.get())
         cursor.execute(sqlquery,values)
         conn.commit()
         conn.close()
         
         messagebox.showinfo("update is correctly done")
         idstudent.set("");
         nom.set("");
         prenom.set("")
     except:
          messagebox.showerror("error to change something")



#button
updatebutoon= Button(mywin,bg="green",text="update",width=20,height=3,command=update)
updatebutoon.place(x=130,y=200)
addbutton=Button(mywin,bg="green",text="add",width=20,height=3,command=add)
addbutton.place(x=330,y=200)
deletebutton=Button(mywin,bg="green",text="delete",width=20,height=3,command=delete)
deletebutton.place(x=530,y=200)
searchbtn=Button(mywin,bg="green",text="show all book",width=20,height=3,command=show)
searchbtn.place(x=730,y=200)














cols = ('idstudent', 'nom', 'prenom')
listBox = ttk.Treeview(mywin, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=400)
 
listBox.bind('<Double-Button-1>',GetValue)











mywin.mainloop()