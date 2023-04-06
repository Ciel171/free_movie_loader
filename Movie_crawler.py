#!/usr/bin/env python
# coding: utf-8

# In[125]:


from urllib import parse 
import tkinter.messagebox as msgbox
import tkinter as tk
import webbrowser 
import re
import qrcode
from qrcode.image.pure import PyPNGImage

class APP:
    def __init__(self, width=500,height=300):
        self.w = width
        self.h = height
        self.title = '免费看电影追剧！'
        self.root = tk.Tk(className = self.title)
        #定义button控件上的文字
        self.url = tk.StringVar()
        
        #定义选择哪个播放源
        self.v = tk.IntVar()
        
        #默认为1
        self.v.set(1)
        
        #Frame 空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        
        #Menu菜单
        menu = tk.Menu(self.root)
        self.root.config(menu = menu)
        moviemenu = tk.Menu(menu, tearoff = 0)
        menu.add_cascade(label = '友情链接', menu = moviemenu)
        
        #各大视频网站
        moviemenu.add_command(label = '腾讯视频', command = lambda: webbrowser.open('http://v.qq.com/'))
        moviemenu.add_command(label = '搜狐视频', command = lambda: webbrowser.open('http://tv.sohu.com/'))
        moviemenu.add_command(label = '芒果TV', command = lambda: webbrowser.open('http://www.mgtv.com/'))
        moviemenu.add_command(label = '爱奇艺', command = lambda: webbrowser.open('http://www.iqiyi.com/'))
        moviemenu.add_command(label = '优酷', command = lambda: webbrowser.open('http://www.youku.com/'))
        moviemenu.add_command(label = '乐视', command = lambda: webbrowser.open('http://www.le.com/'))
        moviemenu.add_command(label = '土豆', command = lambda: webbrowser.open('http://www.tudou.com/'))
        moviemenu.add_command(label = 'A站', command = lambda: webbrowser.open('http://www.acfun.tv/'))
        moviemenu.add_command(label = 'B站', command = lambda: webbrowser.open('http://www.bilibili.com/'))
        
        #控件内容设置
        group = tk.Label(frame_1, text = '请选择一个视频破解方式：', padx = 10, pady = 10)
        tb1 = tk.Radiobutton(frame_1, text = '通道1',variable = self.v, value = 1, width= 10, height = 3)
        label1 = tk.Label(frame_2,text = '请输入视频链接：')
        entry = tk.Entry(frame_2, textvariable = self.url, highlightcolor = 'Fuchsia', highlightthickness = 1, width = 35)
        label2 = tk.Label(frame_2,text = '')
        play = tk.Button(frame_2, text= '播放', font = ('楷体', 12), fg = 'Purple', width = 2, height =1, command = self.video_play)
        label3 = tk.Label(frame_2, text = '')
        label_explain = tk.Label(frame_3, fg = 'red', font = ('楷体', 18), text = '\n 注意： \n 此工具仅用于交流学习\n 请勿用于任何商业用途！')
        label_warning = tk.Label(frame_3, fg = 'black', font = ('楷体', 16), text = '\n\n')
        QR_Code = tk.Button(frame_3, text = "手机观看", font = ('楷体',12), fg = 'Purple', width = 10, height = 2, command = self.QR_Code)
        
        #控件布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        group.grid(row = 0, column = 0)
        tb1.grid(row = 0, column = 1)
        label1.grid(row = 0, column = 0)
        entry.grid(row = 0, column = 1)
        label2.grid(row = 0, column = 2)
        play.grid(row = 0, column = 3, ipadx = 10, ipady = 10)
        label3.grid(row = 0, column = 4)
        label_explain.grid(row = 1, column = 0)
        label_warning.grid(row = 2, column = 0)
        QR_Code.grid(row = 0, column = 0)

        
    #函数说明：视频播放
    def video_play(self):
        #视频解析网站地址
        #port_1 = 'https://jx.618g.com/?url='
        port_1 = 'http://okjx.cc/?url='
        
        #正则表达判定是否为合法链接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            if self.v.get() == 1:
                #浏览器打开
                webbrowser.open(port_1 + self.url.get())
        #else：
            #msgbox.showerror(title = '错误', message = '视频链接地址无效，请重新输入！')
            
            
                
    #函数说明：tkinter窗口居中
    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws/2)-(self.w/2))
        y = int((hs/2)-(self.h/2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h,x,y))
        
        
    #函数说明:生成二维码,手机观看


    def QR_Code(self):
        port_1 = 'http://okjx.cc/?url='
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            #ip = self.url.get()
            #ip = parse.quote_plus(ip)
            url = port_1 + self.url.get()
            
            #制作二维码
            img = qrcode.make(url, image_factory=PyPNGImage)

            with open('qr.png', 'wb') as qr:
                img.save(qr)
            
            
            top = tk.Toplevel(self.root)
            img = tk.PhotoImage(file='qr.png')
            text_label = tk.Label(top, fg = 'red', font = ('楷体',15), text = "手机浏览器扫描二维码，在线观看视频！")
            img_label = tk.Label(top, image = img)
            text_label.pack()
            img_label.pack()
            top.mainloop()

        #else:
            #msgbox.showerror(title='错误',message='视频链接地址无效，请重新输入！')
            
    #函数说明：等待用户事件
    def loop(self):
        #禁止修改窗口大小
        self.root.resizable(False, False)
        #窗口居中
        self.center()
        self.root.mainloop()
        
if __name__ == '__main__':
    app = APP() #实例化APP对象
    app.loop() #loop等待用户事件

    
        
        
        
        
        
        


# In[ ]:




