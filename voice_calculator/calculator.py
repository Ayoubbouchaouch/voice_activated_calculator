import tkinter as tk
import pyttsx3 as ts
import pyaudio
import math
#import speech_recognition as sr

def inserer(s):
    par1, par2 = 0, 0
    aff1.insert(tk.END, s)
    if s.isnumeric():
        aff2.delete(0, tk.END)
        rslt = aff1.get()
        for i in rslt:
            if i == '(':
                par1 += 1
            elif i == ')':
                par2 += 1
        if par2 < par1:
            rslt += (par1 - par2) * ')'
        aff2.insert(0, result(rslt))
def aalamt_lijab():
    return
def eff_tt():
    global memo
    memo = aff2.get()
    aff1.delete(0, tk.END)
    aff2.delete(0, tk.END)

def eff_1():
    var = aff1.get()
    var = var[:-1]
    aff1.delete(0, tk.END)
    aff1.insert(0, var)
    aff2.delete(0, tk.END)
    if var != '':
        if var[-1] in op:
            aff2.insert(0, result(var[:-1]))
        else:
            aff2.insert(0, result(var))

def memoire():
    aff2.delete(0, tk.END)
    aff2.insert(0, memo)

def dire():
    audio = ts.init()
    if r_var.get() == 'v':
        audio.say('utilisez votre voix')
    else:
        audio.say('utilisez les boutons')
    audio.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    aff1.delete(0, tk.END)
    aff1.insert(0, r.recognize_google(audio))
    aff2.delete(0, tk.END)
    aff2.insert(0, result(aff1.get()))

def retour():
    fonction['text'] = 'func'
    fonction['command'] = function
    for i in range(len(L1)):
        if i < 6:
            L2[i][0]['bg'] = 'gray'
            L2[i][0]['text'] = L2[i][2]
            L2[i][0]['command'] = lambda x=i: inserer(L2[x][1])
        L1[i][0]['bg'] = 'gray'
        L1[i][0]['text'] = L1[i][1]
        L1[i][0]['command'] = lambda x=i: inserer(L1[x][1])

def function():
    fonction['text'] = 'op'
    fonction['command'] = retour
    for i in range(len(L1)):
        if i < 6:
            L2[i][0]['bg'] = 'blue'
            L2[i][0]['text'] = L22[i][1]
            L2[i][0]['command'] = lambda x=i: inserer(L22[x][0])
        L1[i][0]['bg'] = 'blue'
        L1[i][0]['text'] = L11[i] + 'x)'
        L1[i][0]['command'] = lambda x=i: inserer(L11[x])

def functions(s, n):
    if s == 'exp':
        return math.exp(n)
    elif s == 'ln':
        return math.log(n, math.exp(1))
    elif s == 'log':
        return math.log10(n)
    elif s == 'cos':
        return math.cos(n)
    elif s == 'sin':
        return math.sin(n)
    elif s == 'tan':
        return math.tan(n)
    elif s == 'cotan':
        return 1 / math.tan(n)
    elif s == 'sinc':
        return math.sin(n) / n
    else:
        return math.fabs(n)

def result(res):
    global pare, K
    liste, pare, K, fun, num = [], [], [], [], ''
    for i in range(len(res)):
        if res[i] == '(':
            pare.append(True)
            K.append([])
            if not(num.isnumeric()):
                fun.append(num)
                num = ''
        elif res[i] == ')':
            K[-1].append(num)
            num = (resultat(K[-1]))
            if fun != []:
                num = functions(fun[-1], float(num))
                fun.remove(fun[-1])
            K.remove(K[-1])
            pare.remove(pare[-1])
        elif res[i] in op:
            if num == '':
                num = 0
            if pare != []:
                K[-1] += [num, res[i]]
            else:
                liste += [num, res[i]]
            num = ''
        else:
            num += res[i]
    if num != '':
        liste.append(num)
    return resultat(liste)

def resultat(L):
    l = []
    for i in range(len(L)):
        if L[i] == '*':
            l.remove(L[i - 1])
            L[i + 1] = float(L[i - 1]) * float(L[i + 1])
        elif L[i] == '/':
            l.remove(L[i - 1])
            L[i + 1] = float(L[i - 1]) / float(L[i + 1])
        else:
            l.append(L[i])
    for i in range(len(l)):
        if l[i] == '+':
            l[i + 1] = float(l[i - 1]) + float(l[i + 1])
        elif l[i] == '-':
            l[i + 1] = float(l[i - 1]) - float(l[i + 1])
    r = str(l[-1])
    if r[-2:] == '.0':
        r = r[:-2]
    return r

def my_res():
    res = aff1.get()
    aff1.delete(0, tk.END)
    aff2.delete(0, tk.END)
    aff1.insert(0, result(res))
    aff2.insert(0, result(res))
#mn hna lta7t rana 7atin l position des butoons mohim organisation
win = tk.Tk()
win.title('calculatrice')
win.geometry('350x500')
win.resizable(False, False)

aff1 = tk.Entry(win, width=30, borderwidth=10, font=1)
aff1.grid(row=1, column=0, columnspan=6, ipady=6)
aff2 = tk.Entry(win, width=14, borderwidth=10, font=1, fg='green')
aff2.grid(row=2, column=0, columnspan=3, ipady=6)

chiffre = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
op = ['+', '-', '*', '/', '//', '%', '!']
par = ['(', '0', ')']
L1 = [['plus', '+'], ['moins', '-'], ['mul', '*'], ['div', '/'], ['pi', 'π'], ['e', 'e'], ['ent', '//'], ['mod', '%']]
L11 = ['sin(', 'cos(', 'tan(', 'sinc(', 'ln(', 'log(', 'exp(', 'cotan(']
L2 = [['rac', '√(', '√(x)'], ['car', '^2', 'x^2'], ['abs', 'abs(', 'abs(x)'], ['inv', '', '1/x'], ['dix', '10^', '10^x'], ['fact', '!', 'n!']]
L22 = [['^', 'x^y'], ['√', 'x√y'], ['b', 'c'], ['e', 'f'], ['h', 'i'], ['k', 'l']]
for i in range(9):
    chiffre[i] = tk.Button(win, text=str(i + 1), width=5, height=1, padx=3, pady=5, font=1, command=lambda x=i: inserer(str(x + 1)))
    chiffre[i].grid(row=i // 3 + 5, column=i % 3)
for i in range(len(par)):
    tk.Button(win, text=par[i], width=5, height=1, padx=3, pady=5, font=1, command=lambda x=i: inserer(par[x])).grid(row=8, column=i % 3)
for i in range(len(L1)):
    if i < 6:
        L2[i][0] = tk.Button(win, text=L2[i][2], width=5, height=1, padx=3, pady=5, font=1, bg='gray', command=lambda x=i: inserer(L2[x][1]))
        L2[i][0].grid(row=3 + i // 3, column=i % 3)
    L1[i][0] = tk.Button(win, text=L1[i][1], width=5, height=1, padx=3, pady=5, font=1, bg='gray', command=lambda x=i: inserer(L1[x][1]))
    L1[i][0].grid(row=6 + i % 4, column=3 + i // 4)
egal = tk.Button(win, width=10, text='=', fg='white', height=1, padx=12, pady=6, font=1, bg='green', command=my_res)
egal.grid(row=9, column=0, columnspan=2)
point = tk.Button(win, width=5, text='.', height=1, padx=3, pady=6, font=1, bg='gray', command=lambda: inserer('.')).grid(row=9, column=2)
tk.Button(win, text='clr', width=5, height=1, padx=3, pady=5, font=1, bg='red', fg='white', command=eff_tt).grid(row=5, column=3)
tk.Button(win, text='del', width=5, height=1, padx=3, pady=5, font=1, bg='brown', fg='white', command=eff_1).grid(row=5, column=4)
tk.Button(win, text='mem', width=5, height=1, padx=3, pady=5, font=1, bg='green', fg='white', command=memoire).grid(row=4, column=3)
tk.Button(win, text='', width=5, height=1, padx=3, pady=5, font=1).grid(row=3, column=3)
tk.Button(win, text='', width=5, height=1, padx=3, pady=5, font=1).grid(row=3, column=4)

fonction = tk.Button(win, text='func', width=5, height=1, padx=3, pady=5, font=1, bg='yellow', command=function)
fonction.grid(row=4, column=4)
modes = ['scientifique', 'graphique', 'programmeur', 'calcul']
v_mode = tk.StringVar()
mode = tk.OptionMenu(win, v_mode, *modes)
mode.grid(row=0, column=0, columnspan=2, pady=5)
v_mode.set(modes[0])
mode.config(width=8, height=1, pady=5, bg='pink', fg='blue', font=1)
r_var = tk.StringVar()
write = tk.Radiobutton(win, text='écriture', variable=r_var, value='e', font=1, command=dire)
voice = tk.Radiobutton(win, text='voix', variable=r_var, value='v', font=1, command=dire)
write.grid(row=0, column=2, columnspan=2)
voice.grid(row=0, column=4)
r_var.set('e')


win.mainloop()