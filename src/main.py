import wx
import src.routes as routes
import src.wx_generated.FrameMain as FrameMain

class Main(FrameMain.FrameMain):
    def __init__(self, parent):
        FrameMain.FrameMain.__init__(self, parent)
        routes.Init.base(self)
        routes.Init.loginPanel.Show()

    def frameMain_on_size(self, event):
        routes.Init.loginPanel.SetSize(self.GetSize())
        routes.Init.dashboardPanel.SetSize(self.GetSize())

app = wx.App()
frame = Main(parent=None)
frame.Show()
app.MainLoop()
