#Boa:Frame:Frame1

import wx

import urllib2
import time
import re
import traceback
import xlwt
import search
import threading


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1GAUGE1, wxID_FRAME1GAUGE2, 
 wxID_FRAME1NOTEBOOK1, wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, 
 wxID_FRAME1PANEL3, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
 wxID_FRAME1TEXTCTRL3, 
] = [wx.NewId() for _init_ctrls in range(17)]


class InputSearchTread(threading.Thread):
    def __init__(self, input_file_name, output_file_name, frame, max_page, random_time):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.frame = frame
        self.max_page = max_page
        self.random_time = random_time
        return super(InputSearchTread, self).__init__()
        
    def run(self):
        if search.input_search(self.input_file_name, self.output_file_name, self.frame, self.max_page, self.random_time):
            wx.MessageBox("OK")
        else:
            wx.MessageBox("Error")
            


class Frame1(wx.Frame):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=True,
              text=u'\u5bfc\u5165\u67e5\u8be2')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text=u'\u7c98\u8d34\u67e5\u8be2')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text=u'\u53c2\u6570\u8bbe\u7f6e')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(507, 273), size=wx.Size(673, 426),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Ali Rank Spider')
        self.SetClientSize(wx.Size(657, 388))

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(657, 388), style=0)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(649, 362),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(649, 362),
              style=wx.TAB_TRAVERSAL)

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(649, 362),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'\u9009\u62e9\u5bfc\u5165\u6587\u4ef6', name='button1',
              parent=self.panel1, pos=wx.Point(80, 96), size=wx.Size(128, 31),
              style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=u'-',
              name='staticText1', parent=self.panel1, pos=wx.Point(64, 168),
              size=wx.Size(528, 13), style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label=u'\u5f00\u59cb\u8fd0\u884c', name='button2',
              parent=self.panel1, pos=wx.Point(80, 232), size=wx.Size(128, 32),
              style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel2, pos=wx.Point(24, 16), size=wx.Size(600, 208),
              style=wx.TE_MULTILINE, value=u'')

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3,
              label=u'\u5f00\u59cb\u8fd0\u884c', name='button3',
              parent=self.panel2, pos=wx.Point(112, 256), size=wx.Size(136, 32),
              style=0)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'\u6e05\u7a7a',
              name='button4', parent=self.panel2, pos=wx.Point(344, 256),
              size=wx.Size(136, 32), style=0)

        self.gauge2 = wx.Gauge(id=wxID_FRAME1GAUGE2, name='gauge2',
              parent=self.panel2, pos=wx.Point(32, 312), range=100,
              size=wx.Size(592, 28), style=wx.GA_HORIZONTAL)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'\u67e5\u8be2\u9875\u6570:', name='staticText3',
              parent=self.panel3, pos=wx.Point(192, 120), size=wx.Size(52, 13),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'\u968f\u673a\u6682\u505c\u65f6\u95f4:',
              name='staticText4', parent=self.panel3, pos=wx.Point(168, 176),
              size=wx.Size(76, 13), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel3, pos=wx.Point(258, 114), size=wx.Size(100, 21),
              style=0, value=u'10')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel3, pos=wx.Point(259, 173), size=wx.Size(100, 21),
              style=0, value=u'1-3')

        self.gauge1 = wx.Gauge(id=wxID_FRAME1GAUGE1, name='gauge1',
              parent=self.panel1, pos=wx.Point(64, 304), range=100,
              size=wx.Size(528, 28), style=wx.GA_HORIZONTAL)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        input_file_name = wx.FileSelector("Open", wildcard="*.txt")
        if input_file_name:
            self.staticText1.SetLabel(input_file_name)
        event.Skip()

    def OnButton2Button(self, event):
        input_file_name = self.staticText1.GetLabel()
        if input_file_name and input_file_name != "-":
            output_file_name = wx.FileSelector("Save", default_extension=".xls", wildcard="*.xls", flags=wx.SAVE)
            if output_file_name:
                max_page = int(self.textCtrl2.GetValue())
                random_time = self.textCtrl3.GetValue()
                t = InputSearchTread(input_file_name, output_file_name, self, max_page, random_time)
                t.start()
        event.Skip()
