from tkinter import *
root=Tk()
root.geometry("350x500")
root.resizable(0,0)
root.title("My Calculator")
num=''
def display(number):
    global num
    num=num+str(number)
    label1['text']=num
def clear_everything():
    global num
    num=''
    label1['text']=num
def compute():
    global num
    num = num.replace('^',"**")
    result=str(eval(num))
    label1['text']=result
var=StringVar()
frame1=Frame(root)
frame1.pack(expand=True,fill=BOTH)
frame2=Frame(root)
frame2.pack(expand=True,fill=BOTH)
frame3=Frame(root)
frame3.pack(expand=True,fill=BOTH)
frame4=Frame(root)
frame4.pack(expand=True,fill=BOTH)
frame5=Frame(root)
frame5.pack(expand=True,fill=BOTH)
label1=Label(frame1,textvariable='',font=('Arial',20),background='#5A5A5A',foreground='white',anchor=SE)
label1.pack(expand=True,fill=BOTH)
button_dot=Button(frame1,text='^',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display('^'))
button_dot.pack(expand=True,fill=BOTH,side=LEFT)
button_power=Button(frame1,text='/',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display('/'))
button_power.pack(expand=True,fill=BOTH,side=LEFT)
button_modulo=Button(frame1,text='%',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display('%'))
button_modulo.pack(expand=True,fill=BOTH,side=LEFT)

button1=Button(frame2,text='1',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(1))
button1.pack(expand=True,fill=BOTH,side=LEFT)
button2=Button(frame2,text='2',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(2))
button2.pack(expand=True,fill=BOTH,side=LEFT)
button3=Button(frame2,text='3',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(3))
button3.pack(expand=True,fill=BOTH,side=LEFT)
button_addition=Button(frame2,text='+',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display('+')).pack(expand=True,fill=BOTH,side=LEFT)
button4=Button(frame3,text='4',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(4))
button4.pack(expand=True,fill=BOTH,side=LEFT)
button5=Button(frame3,text='5',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(5))
button5.pack(expand=True,fill=BOTH,side=LEFT)
button6=Button(frame3,text='6',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(6))
button6.pack(expand=True,fill=BOTH,side=LEFT)
button_subtraction=Button(frame3,text='-',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display('-'))
button_subtraction.pack(expand=True,fill=BOTH,side=LEFT)

button7=Button(frame4,text='7',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(7))
button7.pack(expand=True,fill=BOTH,side=LEFT)
button8=Button(frame4,text='8',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(8))
button8.pack(expand=True,fill=BOTH,side=LEFT)
button9=Button(frame4,text='9',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(9))
button9.pack(expand=True,fill=BOTH,side=LEFT)
button_multiplication=Button(frame4,text='*',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display('*'))
button_multiplication.pack(expand=True,fill=BOTH,side=LEFT)

button_clear=Button(frame5,text='C',font=('Arial',20),border=0,background='black',foreground='white',command=clear_everything)
button_clear.pack(expand=True,fill=BOTH,side=LEFT)
button0=Button(frame5,text='0',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display(0))
button0.pack(expand=True,fill=BOTH,side=LEFT)
button_div=Button(frame5,text='.',font=('Arial',20),border=0,background='black',foreground='white',command=lambda:display('.'))
button_div.pack(expand=True,fill=BOTH,side=LEFT)
button_equal=Button(frame5,text='=',font=('Arial',20),border=0,background='black',foreground='white',command=compute)
button_equal.pack(expand=True,fill=BOTH,side=LEFT)


root.mainloop()
