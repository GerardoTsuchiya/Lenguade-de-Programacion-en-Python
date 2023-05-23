from tkinter import *
from tkinter import ttk
import math

def ingresar(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        if entry2.get() == '0':
            entry2.set(tecla)
        else:    
            entry2.set(entry2.get() + tecla)

    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entry1.set(entry2.get() + ' * ')
        elif tecla == '/':
            entry1.set(entry2.get() + ' / ')
        elif tecla == '+':
            entry1.set(entry2.get() + ' + ')
        elif tecla == '-':
            entry1.set(entry2.get() + ' - ')
        entry2.set('')    

    if tecla == '=':
        entry1.set(entry1.get() + entry2.get())
        total = eval(entry1.get())
        entry2.set(total)

def raiz():
    entry1.set('')
    result = math.sqrt(float(entry2.get()))
    entry2.set(result)

def borrar():
    ini = 0
    fin = len(entry2.get())

    entry2.set(entry2.get()[ini:fin-1])

def borrar_t():
    entry1.set('')
    entry2.set('')


root = Tk()
root.title("Calculadora")
root.geometry("300x500")
root.eval('tk::PlaceWindow . center')
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
root.minsize(250, 450)

##Estilo 
style = ttk.Style()
style.theme_use("clam")
style.configure("mainframe.TFrame", background = "#000000")

style_lbl1 = ttk.Style()
style_lbl1.configure("lbl_entry1.TLabel", font = ('Arimo', '15', 'bold'), anchor = "e", foreground = "#893B3B", background = "#DCC9C9")

style_lbl2 = ttk.Style()
style_lbl2.configure("lbl_entry2.TLabel", font = ('Arimo', '35', 'bold'), anchor = "e", foreground = "#893B3B", background = "#DCC9C9")

style_btn = ttk.Style()
style_btn.configure("btn.TButton", font = "arimo 22", width = 5, background = "#FFFFFF", relief = GROOVE)

style_btn_num = ttk.Style()
style_btn_num.configure("btn_num.TButton", font = "arimo 22", width = 5, background = "#FFFFFF", relief = GROOVE)

style_btn_borrartodo = ttk.Style()
style_btn_borrartodo.configure("btn_borrar.TButton", font = "arimo 22", width = 5, background = "#FFFFFF", relief = GROOVE)
style_btn_borrartodo.map("btn_borrar.TButton", foreground =[('active', '#E83C3C')])



##Widgets
mainframe = ttk.Frame(root, style = "mainframe.TFrame")
mainframe.grid(column = 0, row = 0, sticky = (W, E, N, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.columnconfigure(1, weight = 1)
mainframe.columnconfigure(2, weight = 1)
mainframe.columnconfigure(3, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.rowconfigure(1, weight = 1)
mainframe.rowconfigure(2, weight = 1)
mainframe.rowconfigure(3, weight = 1)
mainframe.rowconfigure(4, weight = 1)
mainframe.rowconfigure(5, weight = 1)
mainframe.rowconfigure(6, weight = 1)
mainframe.rowconfigure(7, weight = 1)

entry1 = StringVar()
lbl_entry1 = ttk.Label(mainframe, textvariable = entry1, style = "lbl_entry1.TLabel")
lbl_entry1.grid(column = 0, row = 0, columnspan = 4, sticky= (W, E, N, S))

entry2 = StringVar()
lbl_entry2 = ttk.Label(mainframe, textvariable = entry2, style = "lbl_entry2.TLabel")
lbl_entry2.grid(column = 0, row = 1, columnspan = 4, sticky = (W, E, N, S))


##Botones
btn0 = ttk.Button(mainframe, text = "0", style = "btn_num.TButton", command = lambda: ingresar('0'))
btn1 = ttk.Button(mainframe, text = "1", style = "btn_num.TButton", command = lambda: ingresar('1'))
btn2 = ttk.Button(mainframe, text = "2", style = "btn_num.TButton", command = lambda: ingresar('2'))
btn3 = ttk.Button(mainframe, text = "3", style = "btn_num.TButton", command = lambda: ingresar('3'))
btn4 = ttk.Button(mainframe, text = "4", style = "btn_num.TButton", command = lambda: ingresar('4'))
btn5 = ttk.Button(mainframe, text = "5", style = "btn_num.TButton", command = lambda: ingresar('5'))
btn6 = ttk.Button(mainframe, text = "6", style = "btn_num.TButton", command = lambda: ingresar('6'))
btn7 = ttk.Button(mainframe, text = "7", style = "btn_num.TButton", command = lambda: ingresar('7'))
btn8 = ttk.Button(mainframe, text = "8", style = "btn_num.TButton", command = lambda: ingresar('8'))
btn9 = ttk.Button(mainframe, text = "9", style = "btn_num.TButton", command = lambda: ingresar('9'))

btn_punto = ttk.Button(mainframe, text = ".", style = "btn.TButton", command = lambda: ingresar('.'))
btn_borrar = ttk.Button(mainframe, text = chr(9003), style = "btn_borrar.TButton", command = lambda: borrar())
btn_borrar_todo = ttk.Button(mainframe, text = "C", style = "btn_borrar.TButton", command = lambda: borrar_t())
btn_parentesis1 = ttk.Button(mainframe, text = "(", style = "btn.TButton", command = lambda: ingresar('('))
btn_parentesis2 = ttk.Button(mainframe, text = ")", style = "btn.TButton", command = lambda: ingresar(')'))

btn_suma = ttk.Button(mainframe, text = "+", style = "btn.TButton", command = lambda: ingresar('+'))
btn_resta = ttk.Button(mainframe, text = "-", style = "btn.TButton", command = lambda: ingresar('-'))
btn_multi = ttk.Button(mainframe, text = "x", style = "btn.TButton", command = lambda: ingresar('*'))
btn_divi = ttk.Button(mainframe, text = chr(247), style = "btn.TButton", command = lambda: ingresar('/'))
btn_sqrt = ttk.Button(mainframe, text = "√", style = "btn.TButton", command = lambda: raiz())
btn_igual = ttk.Button(mainframe, text = "=", style = "btn.TButton", command = lambda: ingresar('='))

##print botones
    ##Columna 0
btn_parentesis1.grid(column = 0, row = 2, sticky = (W, E, N, S))
btn7.grid(column = 0, row = 3, sticky = (W, E, N, S))
btn4.grid(column = 0, row = 4, sticky = (W, E, N, S))
btn1.grid(column = 0, row = 5, sticky = (W, E, N, S))
btn0.grid(column = 0, row = 6, columnspan = 2, sticky = (W, E, N, S))
btn_igual.grid(column = 0, row = 7, columnspan = 3, sticky = (W, E, N, S))

    ##Columna 1
btn_parentesis2.grid(column = 1, row = 2, sticky = (W, E, N, S))
btn8.grid(column = 1, row = 3, sticky = (W, E, N, S))
btn5.grid(column = 1, row = 4, sticky = (W, E, N, S))
btn2.grid(column = 1, row = 5, sticky = (W, E, N, S))

    ##Columna 2
btn_borrar_todo.grid(column = 2, row = 2, sticky = (W, E, N, S))
btn9.grid(column = 2, row = 3, sticky = (W, E, N, S))
btn6.grid(column = 2, row = 4, sticky = (W, E, N, S))
btn3.grid(column = 2, row = 5, sticky = (W, E, N, S))
btn_punto.grid(column = 2, row = 6, sticky = (W, E, N, S))

    ##Columna 3
btn_borrar.grid(column = 3, row = 2, sticky = (W, E, N, S))
btn_divi.grid(column = 3, row = 3, sticky = (W, E, N, S))
btn_multi.grid(column = 3, row = 4, sticky = (W, E, N, S))
btn_suma.grid(column = 3, row = 5, sticky = (W, E, N, S))
btn_resta.grid(column = 3, row = 6, sticky = (W, E, N, S))
btn_sqrt.grid(column = 3, row = 7, sticky = (W, E, N, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady = 10)

root.bind('<KeyPress-q>', exit)

root.mainloop()