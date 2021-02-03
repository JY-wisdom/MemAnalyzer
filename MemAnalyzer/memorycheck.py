import matplotlib.pyplot as plt
from tkinter import messagebox
import numpy as np
import re
import win32api
import win32con


# 构建单个存储器检查类
class Drawfigure(object):
    # 通过传入参数进行三种存储器分别处理
    def __init__(self, inttype, filepath, intid, intsize):
        self.filepath = filepath
        self.figureid = intid
        self.figuresize = intsize

        if inttype == 0:
            self.memorytype = 0
        elif inttype == 1:
            self.memorytype = 1
        else:
            self.memorytype = 2
            self.figuresize = self.figuresize * 1024
        self.figuresize = self.figuresize * 1024
        self.x_start, self.start_y = 0,0
        self.signstr = '(0,0)'

    def __main__(self):
        # 获取屏幕最大分辨率
        self.screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        self.screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

        # 定义坐标范围
        self.array1x = np.arange(0, self.figuresize, 1, dtype=int)
        self.array1y = np.arange(0, self.figuresize, 1, dtype=int)
        # 初始化
        self.array1y[0:-1] = 0
        self.array1y[-1] = 0
        # 初始化画布大小为屏幕最大尺寸的5/6
        self.fig = plt.figure(dpi=100, figsize=(self.screen_x / 120, self.screen_y / 120))
        # 只画一个图
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        # 标签
        self.text0 = plt.text(self.array1x[-1], self.array1y[-1],
                              '(' + str(self.array1x[-1]) + ',' + str(self.array1y[-1]) + ')', fontsize=10)

        # 事件关联
        self.fig.canvas.mpl_connect('button_press_event', self.signqstart)
        self.fig.canvas.mpl_connect('button_release_event', self.signqend)
        self.fig.canvas.mpl_connect('motion_notify_event', self.motion)
        self.fig.canvas.mpl_connect('scroll_event', self.scroll)
        self.fig.canvas.mpl_connect('key_press_event', self.movemouse)

        self.procdata()

    # 定义处理函数
    def procdata(self):
        self.eeprom1 = {}
        self.eeprom2 = {}
        self.array1y[0:-1] = 0
        self.array1y[-1] = 0
        index = self.filepath.rfind('.txt', 0, len(self.filepath))
        if index == -1:
            messagebox.showerror('错误', '文件格式错误')
            return
        file = open(self.filepath, 'r')
        filelines = file.readlines()  # 获取text文件的行数

        idx = self.figureid

        maxXlim = 0
        index = 0
        fromvalue = 0
        linenum = 0
        while linenum < len(filelines):
            try:
                line = filelines[linenum]
                linenum = linenum + 1
                line = re.match('[0-9]{1,8}', line)
                value = int(line.group(0))
                if index == 0:
                    if value == idx:
                        index = 1
                    else:
                        linenum = linenum + 2
                        index = 0
                    continue
                if index == 1:
                    index = 2
                    fromvalue = value
                    continue
                if index == 2:
                    index = 0
                    tovalue = fromvalue + value
                    if maxXlim < tovalue:
                        maxXlim = tovalue
                    for i in range(fromvalue, tovalue):
                        self.array1y[i] = self.array1y[i] + 1
                    continue
                else:
                    continue
            except TypeError:
                print(linenum)

        self.ax1.plot(self.array1x, self.array1y, color='blue')
        self.ax1.set_xlim(0, maxXlim + 10)
        plt.show()
        plt.ion()

    # 滚轮缩放
    def scroll(self, event):
        x_start, x_end = event.inaxes.get_xlim()
        x_now = event.xdata
        xstart_new = 0
        xend_new = 0

        if event.button == 'up':
            xstart_new = (x_start + x_now) / 2
            xend_new = (x_end + x_now) / 2
        elif event.button == 'down':
            xstart_new = 2 * x_start - x_now
            xend_new = 2 * x_end - x_now
        if xstart_new < 0:
            xstart_new = 0
        if xend_new > self.figuresize:
            xend_new = self.figuresize
        event.inaxes.set(xlim=(xstart_new, xend_new))
        self.fig.canvas.draw_idle()

    # 实时更新图片的显示内容
    def motion(self, event):
        try:
            temp = self.array1y[int(np.round(event.xdata))]
            self.text0.set_position((event.xdata, event.ydata))
            self.text0.set_text('(' + str(int(np.round(event.xdata))) + ',' + str(temp) + ')')
            self.fig.canvas.draw_idle()
        except TypeError:
            pass

    # 标注开始
    def signqstart(self, event):
        if event.key == 'shift':
            self.x_start, self.start_y = self.text0.get_position()
            self.start_y = self.array1y[int(self.x_start)]
            self.signstr = '(' + str(int(self.x_start)) + ',' + str(self.start_y) + ')'

    # 标注结束
    def signqend(self, event):
        if event.key == 'shift':
            x, y = self.text0.get_position()
            self.ax1.annotate(self.signstr,
                              xy=(self.x_start, self.start_y), xytext=(x, y), xycoords='data',
                              arrowprops=dict(width=1, headwidth=3, facecolor='black', shrink=0.05)
                              )

    # 左右键移动标注点位置
    def movemouse(self, event):
        x, y = self.text0.get_position()
        if event.key == 'right':
            x = x + 1
        elif event.key == 'left':
            x = x - 1
        temp = self.array1y[int(x)]
        self.text0.set_position((x, y))
        self.text0.set_text('(' + str(int(x)) + ',' + str(temp) + ')')

        self.fig.canvas.draw_idle()
