
from tkinter import *  
from decimal import Decimal  
from tkinter import ttk  
def set_grad_point(n):
    if(n>=90):
        n=10
    elif(n>=80 and n<90):
        n=9
    elif(n>=70 and n<80):
        n=8
    elif(n>=60 and n<70):
        n=7
    elif(n>=50 and n<60):
        n=6
    elif(n>=40 and n<50):
        n=5
    elif(n>=30 and n<40):
        n=4
    else:
        n=0       
    return n
def tgpa1():
    a=int(a1.get())
    ai=set_grad_point(a)
    b=int(b1.get())
    c=int(c1.get())
    ci=set_grad_point(c)
    d=int(d1.get())
    e=int(e1.get())
    ei=set_grad_point(e)
    f=int(f1.get())
    g=int(g1.get())
    gi=set_grad_point(g)
    h=int(h1.get())
    i=int(i1.get())
    ii=set_grad_point(i)
    j=int(j1.get())
    k=int(k1.get())
    ki=set_grad_point(k)
    l=int(l1.get())
    re1=(ai*b)+(ci*d)+(ei*f)+(gi*h)+(ii*j)+(ki*l)
    xs1=(b+d+f+h+j+l)
    pres1=re1/xs1

    pres1=round(pres1,2)
    dire5.set(pres1)
    return pres1
    

#for calculating term 2 Tgpa 
def tgpa2():
    a3=int(a2.get())
    a3i=set_grad_point(a3)
    b3=int(b2.get())
    c3=int(c2.get())
    c3i=set_grad_point(c3)
    d3=int(d2.get())
    e3=int(e2.get())
    e3i=set_grad_point(e3)
    f3=int(f2.get())
    g3=int(g2.get())
    g3i=set_grad_point(g3)
    h3=int(h2.get())
    i3=int(i2.get())
    i3i=set_grad_point(i3)
    j3=int(j2.get())
    k3=int(k2.get())
    k3i=set_grad_point(k3)
    l3=int(l2.get())
    re3=(a3i*b3)+(c3i*d3)+(e3i*f3)+(g3i*h3)+(i3i*j3)+(k3i*l3)
    xs3=(b3+d3+f3+h3+j3+l3)
    pres3=re3/xs3
    pres3=round(pres3,2)
    dire4.set(pres3)
    return pres3

#for calculating combined Cgpa,Remark,Grade
def cgpa():
    a=int(a1.get())
    ai=set_grad_point(a)
    b=int(b1.get())
    c=int(c1.get())
    ci=set_grad_point(c)
    d=int(d1.get())
    e=int(e1.get())
    ei=set_grad_point(e)
    f=int(f1.get())
    g=int(g1.get())
    gi=set_grad_point(g)
    h=int(h1.get())
    i=int(i1.get())
    ii=set_grad_point(i)
    j=int(j1.get())
    k=int(k1.get())
    ki=set_grad_point(k)
    l=int(l1.get())
    a3=int(a2.get())
    a3i=set_grad_point(a3)
    b3=int(b2.get())
    c3=int(c2.get())
    c3i=set_grad_point(c3)
    d3=int(d2.get())
    e3=int(e2.get())
    e3i=set_grad_point(e3)
    f3=int(f2.get())
    g3=int(g2.get())
    g3i=set_grad_point(g3)
    h3=int(h2.get())
    i3=int(i2.get())
    i3i=set_grad_point(i3)
    j3=int(j2.get())
    k3=int(k2.get())
    k3i=set_grad_point(k3)
    l3=int(l2.get())
    re3=(a3i*b3)+(c3i*d3)+(e3i*f3)+(g3i*h3)+(i3i*j3)+(k3i*l3)+(ai*b)+(ci*d)+(ei*f)+(gi*h)+(ii*j)+(ki*l)
    xs3=(b3+d3+f3+h3+j3+l3+b+d+f+h+j+l)
    pres3=re3/xs3
    pres3=round(pres3,2)
    if (pres3>10):
        dire.set('10')
    else:    
        dire.set(pres3)
    remark=pres3
    if(remark<6):
        dire6.set('Need of Improvment  [B]')
    elif(remark>=6 and remark<7):
        dire6.set('Ok but can be Improved  [B+]')
    elif(remark>=7 and remark<8):
        dire6.set('Good Keep Going  [A]')
    elif(remark>=8 and remark<9):
        dire6.set('V.Good Keep Going  [A+]')
    elif(remark>=9 and remark<=10):
        dire6.set('Brilliant  [O]')
    else:
        pass

def reset():
    a1.set("")
    b1.set("")
    c1.set("")
    d1.set("")
    e1.set("")
    f1.set("")
    g1.set("")
    h1.set("")
    i1.set("")
    j1.set("")
    k1.set("")
    l1.set("")
    a2.set("")
    b2.set("")
    c2.set("")
    d2.set("")
    e2.set("")
    f2.set("")
    g2.set("")
    h2.set("")
    i2.set("")
    j2.set("")
    k2.set("")
    l2.set("")

    dire5.set("")
    dire.set("")
    dire4.set("")
    dire6.set("")
    
root=Tk()
root.geometry("800x650")
root.title('Cgpa Calculator')
root.configure(bg='grey')


a1=StringVar()
b1=StringVar()
c1=StringVar()
d1=StringVar()
e1=StringVar()
f1=StringVar()
g1=StringVar()
h1=StringVar()
i1=StringVar()
j1=StringVar()
k1=StringVar()
l1=StringVar()

a2=StringVar()
b2=StringVar()
c2=StringVar()
d2=StringVar()
e2=StringVar()
f2=StringVar()
g2=StringVar()
h2=StringVar()
i2=StringVar()
j2=StringVar()
k2=StringVar()
l2=StringVar()


#starting of GUI..................

#part 1 of GUI
lab=Label(root,text="",bg="grey") #label
lab.grid(row=1,column=1)
dire=Label(root,text="SEMESTER-1",font="Helvetica 15 bold",bg="white",fg="red") #label
dire.grid(row=1,column=6,pady=5)

dire=Label(root,text="Marks  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=2,column=6)
dire=Label(root,text="Credit  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=2,column=8)


dire=Label(root,text="Subject 1 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=4,column=1)

entry1=Entry(root,textvariable=a1,justify='center') #Entry field
entry1.grid(row=4,column=6)

entry2=Entry(root,textvariable=b1,justify='center') #Entry field
entry2.grid(row=4,column=8)

dire=Label(root,text="Subject 2 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=5,column=1)

entry3=Entry(root,textvariable=c1,justify='center') #Entry field
entry3.grid(row=5,column=6)

entry4=Entry(root,textvariable=d1,justify='center') #Entry field
entry4.grid(row=5,column=8)

dire=Label(root,text="Subject 3 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=6,column=1)

entry5=Entry(root,textvariable=e1,justify='center') #Entry field
entry5.grid(row=6,column=6)

entry6=Entry(root,textvariable=f1,justify='center') #Entry field
entry6.grid(row=6,column=8)

dire=Label(root,text="Subject 4 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=7,column=1)

entry7=Entry(root,textvariable=g1,justify='center') #Entry field
entry7.grid(row=7,column=6)

entry8=Entry(root,textvariable=h1,justify='center') #Entry field
entry8.grid(row=7,column=8)

dire=Label(root,text="Subject 5 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=8,column=1)

entry9=Entry(root,textvariable=i1,justify='center') #Entry field
entry9.grid(row=8,column=6)

entry10=Entry(root,textvariable=j1,justify='center') #Entry field
entry10.grid(row=8,column=8)

dire=Label(root,text="Subject 6 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=9,column=1)

entry11=Entry(root,textvariable=k1,justify='center') #Entry field
entry11.grid(row=9,column=6)

entry12=Entry(root,textvariable=l1,justify='center') #Entry field
entry12.grid(row=9,column=8)

button1=ttk.Button(root,text="Find Tgpa",command=tgpa1) #Button for action
button1.grid(row=6,column=14)

dire5=StringVar()

dire1=Label(root,text="Tgpa1:",bg="grey",font="Times 11 bold") #label
dire1.grid(row=8,column=12)
dire1=Label(root,textvariable=dire5,bg="grey") #label
dire1.grid(row=8,column=14)


lab=Label(root,text="       ",bg="grey") #label
lab.grid(row=10,column=1)
dire=Label(root,text="SEMESTER-2",font="Helvetica 15 bold",bg="white",fg="red") #label
dire.grid(row=10,column=6,pady=5)

dire=Label(root,text="Marks  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=11,column=6)
dire=Label(root,text="Credit  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=11,column=8)

dire=Label(root,text="Subject 1 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=12,column=1)

entry1=Entry(root,textvariable=a2,justify='center') #Entry field
entry1.grid(row=12,column=6)
 
entry2=Entry(root,textvariable=b2,justify='center') #Entry field
entry2.grid(row=12,column=8)

dire=Label(root,text="Subject 2 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=13,column=1)

entry3=Entry(root,textvariable=c2,justify='center') #Entry field
entry3.grid(row=13,column=6)

entry4=Entry(root,textvariable=d2,justify='center') #Entry field
entry4.grid(row=13,column=8)

dire=Label(root,text="Subject 3 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=14,column=1)

entry5=Entry(root,textvariable=e2,justify='center') #Entry field
entry5.grid(row=14,column=6)

entry6=Entry(root,textvariable=f2,justify='center') #Entry field
entry6.grid(row=14,column=8)

dire=Label(root,text="Subject 4 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=15,column=1)

entry7=Entry(root,textvariable=g2,justify='center') #Entry field
entry7.grid(row=15,column=6)

entry8=Entry(root,textvariable=h2,justify='center') #Entry field
entry8.grid(row=15,column=8)

dire=Label(root,text="Subject 5 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=16,column=1)

entry9=Entry(root,textvariable=i2,justify='center') #Entry field
entry9.grid(row=16,column=6)

entry10=Entry(root,textvariable=j2,justify='center') #Entry field
entry10.grid(row=16,column=8)

dire=Label(root,text="Subject 6 :  ",bg="grey",font="Times 11 bold") #label
dire.grid(row=17,column=1)

entry11=Entry(root,textvariable=k2,justify='center') #Entry field
entry11.grid(row=17,column=6)

entry12=Entry(root,textvariable=l2,justify='center') #Entry field
entry12.grid(row=17,column=8)

button1=ttk.Button(root,text="Find Tgpa",command=tgpa2) #Button for action
button1.grid(row=14,column=14)

dire4=StringVar()

dire1=Label(root,text="Tgpa2:",bg="grey",font="Times 11 bold") #label
dire1.grid(row=16,column=12)
dire1=Label(root,textvariable=dire4,bg="grey") #label
dire1.grid(row=16,column=14)

lab=Label(root,text="       ",bg="grey") #label
lab.grid(row=18,column=6)



lab=Label(root,text="       ",bg="grey") #label
lab.grid(row=22,column=6)

button1=ttk.Button(root,text="Find cgpa",width=10,command=cgpa) #Button for action
button1.grid(row=23,column=4)

dire=StringVar()

dire1=Label(root,text="Cgpa : ",bg="grey",font="Times 11 bold") #label
dire1.grid(row=23,column=6)
dire1=Label(root,textvariable=dire,bg="grey") #label
dire1.grid(row=23,column=8)

dire6=StringVar()

dire1=Label(root,text="Remark : ",font="Times 11 bold") #label
dire1.grid(row=25,column=4)
dire1=Label(root,textvariable=dire6,bg="grey") #label
dire1.grid(row=25,column=6)

lab=Label(root,text="       ",bg="grey") #label
lab.grid(row=26,column=6)

button_reset=ttk.Button(root,text="Reset All The Data",width=20,command=reset) #Button for action
button_reset.grid(row=27,column=6)

lab=Label(root,text="       ",bg="grey") #label
lab.grid(row=28,column=6)


root.mainloop()