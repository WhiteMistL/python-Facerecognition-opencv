from tkinter import *
from tkinter.filedialog import askopenfilename
import base64
import choiceEXE
import tkinter


tk=Tk()
tk.title("Face Recognition Check-in ")

#标签控件，显示文本和位图，展示在第一行
Label(tk,text="First").grid(row=0,sticky=E)#靠右
Label(tk,text="正脸照").grid(row=1,sticky=E)#第二行，靠左
#
def selectPath():
    path_ = askopenfilename()
    path.set(path_)



#输入控件
TEXT=Entry(tk)
TEXT.grid(row=0,column=1)
path = StringVar()
file=Entry(textvariable = path)
file.grid(row = 1, column = 1)
button1=Button(text = "路径选择", command = selectPath)
button1.grid(row=1,column=2, sticky=W+E)
#插图/插话
photo=PhotoImage(file="guiphoto\\gui.jpg")
label=Label(image=photo)
label.image=photo
label.grid(row=0,column=3,rowspan=2,columnspan=2,sticky=W+E+N+S,padx=5, pady=5)
labe2=Label(text="by 林海锋")
labe2.grid(row=3,column=0,columnspan=2)


#触发函数上传资料
def submit():

    str = path.get()
    addr2 = str.replace('/',r'\\')
    print(addr2)
    f = open(addr2, 'rb')
    f_str = base64.b64encode(f.read())
    f.close()
    str = f_str
    file_str = open('Material bank\\%s.jpg'%TEXT.get(), 'wb')
    file_str.write(base64.b64decode(str))
    file_str.close()

#转跳按键
#当素材库中存在非正脸照时（即五点定位无法识别的人脸），会报数据越界，切记切记！
button2=Button(tk,text="上传资料", command = submit)
button2.grid(row=3,column=2,sticky=W)
button3=Button(tk,text="打开摄像头", command = choiceEXE.action)
button3.grid(row=3,column=4,sticky=W)

#主事件循环
mainloop()

