import wx
import src.routes as routes
import src.wx_generated.FrameMain as FrameMain
import src.app.core.Database as Database

class LoginPanel(FrameMain.WxPanelLogin):
    def __init__(self, parent):
        FrameMain.WxPanelLogin.__init__(self, parent)
        self.db = Database.Database()

    def btn_login_onclick(self, event):
        username = self.textCtrl_username.GetValue()
        password = self.textCtrl_password.GetValue()
        queryResult = self.db.set_query("SELECT * FROM `admin` WHERE `username` = '%s'"%(username))\
                             .fetch()
        if (queryResult is not None):
            if (password == queryResult[3]):
                routes.Init.loginPanel.Hide()
                routes.Init.dashboardPanel.Show()
        else:
            wx.MessageBox("Username atau Password tidak sesuai", "Login Gagal")

