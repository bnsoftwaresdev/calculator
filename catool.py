#!usr/bin/env python
#-*- coding: utf-8 -*-
#from __future__ import with_statement  # <-- Python 2.5 ONLY
import Tix
from Tkinter import*
import random
import time
import webbrowser
import ttk
from PIL import ImageTk, Image
import xml

class SplashScreen(object):
    def __init__(self, tkRoot, imageFilename, minSplashTime=0):
        self._root = tkRoot
#        self._image = Tix.PhotoImage(file = "try2.png")
        self._image = ImageTk.PhotoImage(Image.open(path))
        self._splash = None
        self._minSplashTime = time.time() + minSplashTime

    def __enter__(self):
        # Remove the app window from the display
        self._root.withdraw()

        # Calculate the geometry to center the splash image
        scrnWt = self._root.winfo_screenwidth()
        scrnHt = self._root.winfo_screenheight()

        imgWt = self._image.width()
        imgHt = self._image.height()

        imgXPos = (scrnWt / 2) - (imgWt / 2)
        imgYPos = (scrnHt / 2) - (imgHt / 2)

        # Create the splash screen
        self._splash = Tix.Toplevel()
        self._splash.overrideredirect(1)
        self._splash.geometry('+%d+%d' % (imgXPos, imgYPos))
        Tix.Label(self._splash, image=self._image, cursor='watch').pack()

        # Force Tk to draw the splash screen outside of mainloop()
        self._splash.update()

    def __exit__(self, exc_type, exc_value, traceback):
        # Make sure the minimum splash time has elapsed
        timeNow = time.time()
        if timeNow < self._minSplashTime:
            time.sleep(self._minSplashTime - timeNow)

        # Destroy the splash window
        self._splash.destroy()

        # Display the application window
        self._root.deiconify()


# --------------------------------------------
# Now putting up splash screens is simple



# Create the tkRoot window
root = Tk()
path = "try2.png"
img = ImageTk.PhotoImage(Image.open(path))
with SplashScreen(root, img, 5.0):
#    initializeMyApplication()
#    buildTheGUI(tkRoot)

    root.geometry("482x330-620+210")
#    root.overrideredirect(True)
    root.title("Black Node Softwares Calculator")
    root.config(background = "#E4E4E4")
    root.iconbitmap(default = 'desktop.ico')

    toolbar = Frame(root)
    toolbar.configure(relief = "groove")

    #path1 = "opens.png"
    img = Image.open("save.png")
    eimg = ImageTk.PhotoImage(img)
    b=Button(toolbar, justify = LEFT,relief = "flat", activebackground = "#CCCC99", image = eimg)
    #photo= img
    b.config(image=eimg, width = "25", height="25")
    b.pack(side=LEFT, padx = 2, pady = 2)
    b.image=img

    s = ttk.Style()
    s.theme_names()
('aqua', 'step', 'clam', 'alt', 'default', 'classic', 'gtk+ style', 'motif', 'plastique', 'CDE', 'windows')
s.theme_use('clam')

style = ttk.Style()
style.configure('TLabelFrame',
    background='red',
    foreground='white',
    font=('Helvetica', 13, 'bold'))


style = ttk.Style()
style.configure('Minis.TButton',
    background='red',
    foreground='white',
    highlightthickness='50',
    font=('arial', 10, 'bold'))
style.map('Minis.TButton',
foreground=[('disabled', 'yellow'),
            ('pressed', 'white'),
            ('active', 'white')],
background=[('disabled', 'red'),
            ('pressed', '!focus', 'white'),
            ('active', '#993300')],
highlightcolor=[('focus', 'grey'),
                ('!focus', 'grey')],
relief=[('pressed', 'flat'),
        ('!pressed', 'flat')])
overrelief = [('pressed', 'flat'),
              ('!pressed', 'flat')]
#===================================
style = ttk.Style()
style.configure('Mini.TButton',
    background='#0066CC',
    foreground='white',
    highlightthickness='50',
    font=('DejaVu Sans Mono', 10, 'bold'))
style.map('Mini.TButton',
foreground=[('disabled', 'yellow'),
            ('pressed', 'white'),
            ('active', 'white')],
background=[('disabled', 'blue'),
            ('pressed', '!focus', 'blue'),
            ('active', 'blue')],
highlightcolor=[('focus', 'blue'),
                ('!focus', 'blue')],
relief=[('pressed', 'flat'),
        ('!pressed', 'flat')])
overrelief = [('pressed', 'flat'),
              ('!pressed', 'flat')]
#===================================


photo1 = StringVar()
b1=Button(toolbar, justify = LEFT, relief = "flat", activebackground = "#CCCC99")
photo1= PhotoImage("saveas.png")
b1.config(image=photo1, width = "25", height="25")
b1.pack(side=LEFT)
b1.image=photo1

b2=Button(toolbar, justify = LEFT, relief = "flat", activebackground = "#CCCC99")
photo= PhotoImage("undos.png")
b2.config(image=photo, width = "25", height="25")
b2.pack(side=LEFT)
b2.image=photo

#===================================
path = "dek1.png"
img = ImageTk.PhotoImage(Image.open(path))
def update_clock():
    t = time.strftime('%H:%M:%S', time.localtime())
    if t!='':
        lbl.config(text=t, font = 'times 15')
    root.after(100, update_clock)

def help():
    que = Toplevel()
    que.title("Help")
#    photo = PhotoImage(file="dek1.png")
    que.geometry("490x170-110+250")
    que.resizable(0, 0)
    que.attributes("-toolwindow", 1)
#    que.minsize("520", "150")
#    que.maxsize("520", "150")
#    que.config(background = "#666666")
#    que.overrideredirect(True)\

#    photo = PhotoImage(file="dek1.png")
    lbl = Label(que, text = """
This is a simple calculator with basic functionalities.
For any bugs or improvements please do well to write to us.
Email: thedon156@gmail.com
Github: github.com/lincollins

Thank you.""", font = ('arial',12, 'bold'))
    lbl.grid(row = 0, column = 0)

    abn2 = ttk.Button(que, text="Close ", style="Minis.TButton", width=70, command=que.destroy)
    abn2.grid(row=1, column=0, padx=1, pady=1)

def abt():
#    time.sleep(5)
    kn = Toplevel()
    kn.title("About")
#    photo = PhotoImage(file="dek1.png")
    kn.geometry("542x350-60+210")
#    kn.minsize("542", "345")
#    kn.maxsize("542", "345")
#    kn.config(background = "#666666")
    kn.overrideredirect(True)

    def des(event):
        kn.destroy()
#    photo = PhotoImage(file="dek1.png")
    path = "deks.png"
    img = ImageTk.PhotoImage(Image.open(path))
    abn = Label(kn, image = img)
    abn.image = img
    abn.grid(row = 0, column = 0, ipadx = 1, ipady = 1, sticky = 'n')
    abn.bind("<Button-1>", des)

    def click_link(event):
        webbrowser.open_new(r"https://dvslonline.wordpress.com")

    abn1 = ttk.Button(kn, text = " Website: https://dvslonline.wordpress.com", style = "Mini.TButton", width = 70, cursor = "hand2")
    abn1.grid(row=1, column=0, padx = 1, pady = 1, ipadx = 35)
    abn1.bind("<Button-1>", click_link)


    def file1(event):
        webbrowser.open(r"data.yaml")

#    abn2 = Label(kn, text = " Website: https://dvslonline.wordpress.com", fg = "blue", cursor = "hand2")
#    abn2.grid(row = 2, column = 0)
#    abn2.bind("<Button-1>", click_link)

#    abn3 = Label(kn, text = "Open file", cursor = "hand2")
#    abn3.grid(row = 3, column = 0)
#    abn3.bind("<Button-1>", file1)


bt = Button(root, text = "?", cursor = "hand2", command = help, font = ('arial',12, 'bold'), bd = 1, bg = "#0066CC", fg = "white", activeforeground = "white", activebackground = "#0066CC", overrelief = "flat", relief = "flat",)
bt.grid(row = 0, column = 0, sticky = 'w', padx = 1, pady = 1, ipadx = 10, ipady = 1)

bt3 = Button(root, text = "...", command = abt, font = ('arial',12, 'bold'), bd = 1, bg = "#0066CC", fg = "white", activeforeground = "white", activebackground = "#0066CC", overrelief = "flat", relief = "flat",)
bt3.grid(row = 0, column = 0, sticky = 'w', padx = 30, pady = 1, ipadx = 20, ipady = 1)

#grip = ttk.Label(root, bitmap = "gray25")
#grip.grid(row = 0, column = 0)




def StartMove(event):
    x = event.x
    y = event.y


def StopMove(event):
    x = None
    y = None

l = ttk.Label(root, text = "Basic Calculator", font = ('arial', 12, ''), background = "#E4E4E4")
l.grid(row = 0, column = 1,)
#l.bind("<ButtonPress-1>", StartMove)
#l.bind("<ButtonRelease-1>", StopMove)
#l.bind("<B1-Motion>", OnMotion)

text = "Hello"
text = StringVar()
#c = Canvas(root, width = 100, height = 30, background = "#E4E4E4")
#id = c.create_text(focus = 'normal', text = text)
#c.grid(row = 0, columnspan = 3)




lbl = ttk.Label(root, text = "", background = "#E4E4E4")
lbl.grid(row = 0, columnspan = 3, sticky = 'e', padx = 1)
update_clock()

seph = ttk.Separator(root, orient='horizontal', )
# sep.pack(side = BOTTOM)e
seph.grid(row=1, column=0, sticky='n,w,e,s', columnspan=4, ipadx=1, ipady=1, padx=1, pady=1)
#=============================This is for our calculator===============================
Cal_cu = StringVar()

calus = ttk.LabelFrame(root,  text = "", height = 208, width = 10,  labelanchor = "n", relief = "sunken", takefocus = 1)
calus.grid(sticky='n,w,e,s', row = 2, columnspan = 4, column = 0, padx = 5, pady = 10)


text_Input = StringVar()
mal_Input = StringVar()
operator = ""

current_operator = None
history = ("")

def btnClick(numbers):
    global  operator

    operator = operator + str(numbers)
    text_Input.set(operator)

#    if operator == operator + str(numbers):
#        text_Input.set(operator)

#    else:
#        print "Invalid Expression."

def btncan():
    global operator
    operator = ""
    text_Input.set("0")
    mal_Input.set("")

def btnclear():
    global operator
    operator = ""
    text_Input.set("0")
    mal_Input.set("")

def btneql():
    try:
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""

    except:
        mal_Input.set("Malformed Expression")


def btnper(x):
    global operator
    operator = str(x/100)
    text_Input.set(operator)


def btnmuls(x):
    ans = 0
    if x >= 0:
        while ans * ans <= x:
            if ans * ans ==x:
                return ans
            ans = ans + 1
        return None
    else:
        return None



#style.configure("SW.TButton", indicatoron=[('pressed', '#ececec'), ('selected', '#4a6984')], background="#CCCC99", activeforeground = "green", font = ('arial', 13, 'bold'))

txtDisplay = ttk.Entry(calus, textvariable = text_Input, font = ('arial', 20 , 'bold'), width = 30, justify = 'right')
txtDisplay.grid(row = 0, column = 0, columnspan = 5, rowspan = 1, padx= 5, pady = 5)

txtmal = ttk.Entry(calus, textvariable = mal_Input, font = ('arial', 20 , ''), width = 30, justify = 'right')
txtmal.grid(row = 1, column = 0, columnspan = 5, rowspan = 1, padx= 1, pady = 1)


btn7 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "7", command = lambda: btnClick(7))
btn7.grid(row = 2, column = 0, pady = 5, padx = 5, ipadx = 10)



btn8 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "8", command = lambda: btnClick(8))
btn8.grid(row = 2, column = 1, pady = 5, padx = 5, ipadx = 10)

btn9 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "9", command = lambda: btnClick(9))
btn9.grid(row = 2, column = 2, pady = 5, padx = 5, ipadx = 10)


btnclear = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "← ", command = btncan)
btnclear.grid(row = 2, column = 4, pady = 5, padx = 5, ipadx = 10)

#===========================================================================================
btndiv = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "/", command = lambda: btnClick("/"))
btndiv.grid(row = 2, column = 3, pady = 5, padx = 5, ipadx = 10)

btn4 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "4", command = lambda: btnClick(4))
btn4.grid(row = 3, column = 0, pady = 5, padx = 5, ipadx = 10)

btn5 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "5", command = lambda: btnClick(5))
btn5.grid(row = 3, column = 1, pady = 5, padx = 5, ipadx = 10)

btn6 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "6", command = lambda: btnClick(6))
btn6.grid(row = 3, column = 2, pady = 5, padx = 5, ipadx = 10)

btnadd = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "+", command = lambda: btnClick("+"))
btnadd.grid(row = 3, column = 3, pady = 5, padx = 5, ipadx = 10)

btnmul = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "*", command = lambda: btnClick("*"))
btnmul.grid(row = 3, column = 4, pady = 5, padx = 5, ipadx = 10)

#==================================================================================================
btn1 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "1", command = lambda: btnClick(1))
btn1.grid(row = 4, column = 0, pady = 5, padx = 5, ipadx = 10)

btn2 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "2", command = lambda: btnClick(2))
btn2.grid(row = 4, column = 1, pady = 5, padx = 5, ipadx = 10)

btn3 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "3", command = lambda: btnClick(3))
btn3.grid(row = 4, column = 2, pady = 5, padx = 5, ipadx = 10)

btnmin = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "--", command = lambda: btnClick("-"))
btnmin.grid(row = 4, column = 3, pady = 5, padx = 5, ipadx = 10)

btnmuls = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "^2", command = lambda: btnClick("^2"))
btnmuls.grid(row = 4, column = 4, pady = 5, padx = 5, ipadx = 10)

#=================================================================================================
btn0 = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "0", command = lambda: btnClick(0))
btn0.grid(row = 5, column = 0, pady = 5, padx = 5, ipadx = 10)

btnpoi = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = ".", command = lambda: btnClick("."))
btnpoi.grid(row = 5, column = 1, pady = 5, padx = 5, ipadx = 10)

btncan = ttk.Button(calus, width = 7, style = "Wilds.TButton", text = "C", command = btncan)
btncan.grid(row = 5, column = 2, pady = 5, padx = 5, ipadx = 10)


btneql = Button(calus, padx = 15, font = ('arial', 12, 'bold'), width = 14, height = 1, bd = 1, bg = "#0066CC", fg = "white", activeforeground = "white", activebackground = "#0066CC", overrelief = "sunken", relief = "flat",
               text = "=", command = btneql).grid(row = 5, columnspan = 4, column = 3)



root.mainloop()