#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1GAUGE1, 
 wxID_FRAME1NOTEBOOK1, wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, 
 wxID_FRAME1PANEL3, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Frame1(wx.Frame):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text=u'\u5bfc\u5165\u67e5\u8be2')
        parent.AddPage(imageId=-1, page=self.panel2, select=True,
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
              parent=self.panel1, pos=wx.Point(64, 48), size=wx.Size(128, 31),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=u'-',
              name='staticText1', parent=self.panel1, pos=wx.Point(64, 120),
              size=wx.Size(520, 13), style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label=u'\u5f00\u59cb\u8fd0\u884c', name='button2',
              parent=self.panel1, pos=wx.Point(72, 192), size=wx.Size(128, 32),
              style=0)

        self.gauge1 = wx.Gauge(id=wxID_FRAME1GAUGE1, name='gauge1',
              parent=self.panel1, pos=wx.Point(64, 272), range=100,
              size=wx.Size(536, 28), style=wx.GA_HORIZONTAL)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label=u'-',
              name='staticText2', parent=self.panel1, pos=wx.Point(72, 328),
              size=wx.Size(4, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel2, pos=wx.Point(96, 32), size=wx.Size(472, 152),
              style=wx.TE_MULTILINE, value='textCtrl1')

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
