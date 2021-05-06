import src.panel.LoginPanel as LoginPanel
import src.panel.DashboardPanel as DashboardPanel

class Init:
    loginPanel = LoginPanel.LoginPanel
    dashboardPanel = DashboardPanel.DashboardPanel

    @staticmethod
    def base(parent):
        Init.loginPanel = LoginPanel.LoginPanel(parent)
        Init.dashboardPanel = DashboardPanel.DashboardPanel(parent)
        Init.initPanel()

    @staticmethod
    def initPanel():
        Init.loginPanel.Hide()
        Init.dashboardPanel.Hide()


