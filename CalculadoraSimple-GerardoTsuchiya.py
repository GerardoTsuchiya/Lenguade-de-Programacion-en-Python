import tkinter as tk
from tkinter import *
from tkinter import messagebox

def suma():
    try:
        n1 = val1.get()
        n2 = val2.get()

        if n1 == "" and n2 == "":
            lbl_res_t["text"] = "ERROR"
            messagebox.showerror("ERROR", "AGREGUE VALORES")
        else:
            r = int(n1) + int(n2)
            lbl_res_t["text"] = r
    except:
        messagebox.showerror("ERROR", "VALORES INVALIDOS")


def resta():
    try:
        n1 = val1.get()
        n2 = val2.get()

        if n1 == "" and n2 == "":
            lbl_res_t["text"] = "ERROR"
            messagebox.showerror("ERROR", "AGREGUE VALORES")
        else:
            r = int(n1) - int(n2)
            lbl_res_t["text"] = r
    except:
        messagebox.showerror("ERROR", "VALORES INVALIDOS")


def multi():
    try:
        n1 = val1.get()
        n2 = val2.get()

        if n1 == "" and n2 == "":
            lbl_res_t["text"] = "ERROR"
            messagebox.showerror("ERROR", "AGREGUE VALORES")
        else:
            r = int(n1) * int(n2)
            lbl_res_t["text"] = r
    except:
        messagebox.showerror("ERROR", "VALORES INVALIDOS")


def divi():
    try:
        n1 = val1.get()
        n2 = val2.get()

        if n1 == "" and n2 == "":
            lbl_res_t["text"] = "ERROR"
            messagebox.showerror("ERROR", "AGREGUE VALORES")
        elif int(n2) == 0:
            lbl_res_t["text"] = "ERROR"
            messagebox.showerror("ERROR", "ERROR MATEMATICO")
        else:
            r = int(n1) / int(n2)
            lbl_res_t["text"] = r
    except:
        messagebox.showerror("ERROR", "VALORES INVALIDOS")


## Ventana 
root = Tk()
root.geometry("450x400")
root.title("Calculdora simple")
root.configure(background= "black")
root.resizable(0,0)

## LabelFrame Numeros

lbl_num = LabelFrame(root, text = "Numeros", width=440, height=100, font=("Arimo", 10), bg= "black", fg= "white")
lbl_num.place(x=5, y=25)

## Label numero 1

lbl_n1 = Label(lbl_num, text="Numero 1", fg= "white", bg= "black", font=("Arimo", 10))
lbl_n1.place(x= 46, y= 5)

## Label numero 2

lbl_n2 = Label(lbl_num, text="Numero 2", fg= "white", bg= "black", font=("Arimo", 10))
lbl_n2.place(x= 187, y= 5)

## Label resultado

lbl_res = Label(lbl_num, text= "Resultado", fg= "white", bg= "black", font=("Arimo", 10))
lbl_res.place(x=328, y=5)

## Entry numero 1

val1 = Entry(root, fg="black", font=("Arimo", 10), width= 10, justify="right")
val1.place(x=46, y= 84)
val1.insert(0, "0")

## Entry numero 2

val2 = Entry(root, fg="black", font=("Arimo", 10), width= 10, justify="right")
val2.place(x=187, y=84)
val2.insert(0, "0")

## Label Resultado_Total

lbl_res_t = Label(root, fg="black", bg="white", font=("Arimo", 10), width= 9)
lbl_res_t.place(x=328, y=84)
lbl_res_t["text"] = "0"

## LabelFrame Operadores

lbl_opp = LabelFrame(root, text= "Operadores", width= 440, height= 235, font=("Arimo", 10), bg= "black", fg= "white")
lbl_opp.place(x= 5, y= 150)

## Botones

btn_suma = Button(root, text= "+", width= 10, height= 12, background= "gray", command= suma)
btn_suma.place(x= 16, y= 177)

btn_resta = Button(root, text= "-", width= 10, height= 12, background= "gray", command= resta)
btn_resta.place(x= 128, y= 177)

btn_multi = Button(root, text= "*", width= 10, height= 12, background= "gray", command= multi)
btn_multi.place(x= 242, y= 177)

btn_divi = Button(root, text= "/", width= 10, height= 12, background= "gray", command= divi)
btn_divi.place(x= 348, y= 177)


root.mainloop()