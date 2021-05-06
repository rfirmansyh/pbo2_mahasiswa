import src.routes as routes
import src.wx_generated.FrameMain as FrameMain
import src.app.core.Database as Database

class DashboardPanel(FrameMain.WxPanelDashboard):
    def __init__(self, parent):
        FrameMain.WxPanelDashboard.__init__(self, parent)
        self.db = Database.Database()
        self.initData()
        self.show_ontextCtrl_of_row(0)

    # data
    def initData(self):
        column_names = self.db.get_tablecolumn(tableName="mahasiswa")
        datasets = self.db.set_query("SELECT * FROM mahasiswa").fetchall()

        self.table_students.DeleteRows(0, self.table_students.GetNumberRows())
        self.table_students.DeleteCols(0, self.table_students.GetNumberCols())

        self.table_students.AppendCols(len(column_names))
        self.table_students.AppendRows(len(datasets))

        for index in range(len(column_names)):
            self.table_students.SetColLabelValue(index, column_names[index])
        for i in range(len(datasets)):
            for j in range(len(datasets[i])):
                field = "%s"%datasets[i][j]
                self.table_students.SetCellValue(i,j, field)
                print(i,j)

    # event custom
    def show_ontextCtrl_of_row(self, row):
        id = self.table_students.GetCellValue(row, 0)
        nim = self.table_students.GetCellValue(row, 1)
        nama = self.table_students.GetCellValue(row, 2)
        prodi = self.table_students.GetCellValue(row, 3)

        self.textCtrl_id.SetValue(str(id))
        self.textCtrl_nim.SetValue(nim)
        self.textCtrl_nama.SetValue(nama)
        self.textCtrl_prodi.SetValue(prodi)

    # event override
    def btn_dashboard_onclick(self, event):
        routes.Init.dashboardPanel.Hide()
        routes.Init.loginPanel.Show()

    def table_studentsOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        col = event.GetCol()
        self.show_ontextCtrl_of_row(row)

