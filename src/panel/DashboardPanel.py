import wx
import src.routes as routes
import src.wx_generated.FrameMain as FrameMain
import src.app.core.Database as Database

class DashboardPanel(FrameMain.WxPanelDashboard):
    def __init__(self, parent):
        FrameMain.WxPanelDashboard.__init__(self, parent)
        self.db = Database.Database()
        self.initData()
        self.enable_textCtrl(False)
        self.enable_btn(False)

    # data
    def initData(self):
        column_names = self.db.get_tablecolumn(tableName="mahasiswa")
        datasets = self.db.set_query("SELECT * FROM mahasiswa").fetchall()
        print("init data", datasets)

        self.table_students.DeleteRows(0, self.table_students.GetNumberRows())
        self.table_students.DeleteCols(0, self.table_students.GetNumberCols())

        self.table_students.AppendCols(len(column_names))
        self.table_students.AppendRows(len(datasets))

        # column label
        for index in range(len(column_names)):
            self.table_students.SetColLabelValue(index, column_names[index])
        # colum cell data
        for i in range(len(datasets)):
            for j in range(len(datasets[i])):
                field = "%s"%datasets[i][j]
                self.table_students.SetCellValue(i,j, field)

        self.show_ontextCtrl_of_row(0)

    # event custom
    def enable_textCtrl(self, isEnable):
        if isEnable == True:
            self.textCtrl_nim.Enable()
            self.textCtrl_nama.Enable()
            self.textCtrl_prodi.Enable()
        else:
            self.textCtrl_id.Disable()
            self.textCtrl_nim.Disable()
            self.textCtrl_nama.Disable()
            self.textCtrl_prodi.Disable()
    def enable_btn(self, isEnable):
        if isEnable == True:
            self.btn_simpan.Enable()
        else:
            self.btn_simpan.Disable()

    def clear_textCtrl(self):
        self.textCtrl_id.SetValue("")
        self.textCtrl_nim.SetValue("")
        self.textCtrl_nama.SetValue("")
        self.textCtrl_prodi.SetValue("")

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
    def btn_refresh_onclick( self, event ):
        self.initData()
    def btn_tambah_onclick( self, event ):
        self.clear_textCtrl()
        self.enable_textCtrl(True)
        self.btn_simpan.Enable()
    def btn_simpan_onclick( self, event ):
        nim = self.textCtrl_nim.GetValue()
        nama = self.textCtrl_nama.GetValue()
        prodi = self.textCtrl_prodi.GetValue()

        val = (nim, nama, prodi)
        if (self.db.set_query("INSERT INTO mahasiswa (nim, nama, prodi) VALUES (%s, %s, %s)", val)\
                .execute()\
                .get_rowcount() > 0):
            wx.MessageBox("Data Mahasiswa berhasil Ditambah", "Berhasil")
            self.enable_textCtrl(False)
            self.btn_simpan.Disable()
        else:
            wx.MessageBox("Data Mahasiswa gagal Ditambah", "Gagal")


    def table_studentsOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        col = event.GetCol()
        self.show_ontextCtrl_of_row(row)





