# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.frameMain_on_size )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def frameMain_on_size( self, event ):
		event.Skip()


###########################################################################
## Class WxPanelLogin
###########################################################################

class WxPanelLogin ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Aplikasi Perpus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER, 5 )


		bSizer2.Add( ( 0, 20), 0, 0, 5 )

		self.textCtrl_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		bSizer2.Add( self.textCtrl_username, 0, wx.ALIGN_CENTER, 0 )


		bSizer2.Add( ( 0, 2), 0, 0, 5 )

		self.textCtrl_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), wx.TE_PASSWORD )
		bSizer2.Add( self.textCtrl_password, 0, wx.ALIGN_CENTER|wx.TOP, 5 )


		bSizer2.Add( ( 0, 15), 0, 0, 5 )

		self.btn_login = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_login, 0, wx.ALIGN_CENTER, 0 )


		bSizer2.Add( ( 0, 30), 0, 0, 5 )


		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.btn_login.Bind( wx.EVT_BUTTON, self.btn_login_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_login_onclick( self, event ):
		event.Skip()


###########################################################################
## Class WxPanelDashboard
###########################################################################

class WxPanelDashboard ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMaxSize( wx.Size( 600,400 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer14.Add( self.m_staticText18, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer3.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.table_students = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.table_students.CreateGrid( 25, 4 )
		self.table_students.EnableEditing( False )
		self.table_students.EnableGridLines( True )
		self.table_students.EnableDragGridSize( False )
		self.table_students.SetMargins( 0, 0 )

		# Columns
		self.table_students.SetColSize( 0, 60 )
		self.table_students.EnableDragColMove( False )
		self.table_students.EnableDragColSize( True )
		self.table_students.SetColLabelSize( 30 )
		self.table_students.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.table_students.EnableDragRowSize( True )
		self.table_students.SetRowLabelSize( 50 )
		self.table_students.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.table_students.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.table_students.SetMaxSize( wx.Size( -1,272 ) )

		bSizer13.Add( self.table_students, 0, wx.ALL, 5 )

		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_refresh = wx.Button( self, wx.ID_ANY, u"refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.btn_refresh, 0, wx.ALL, 5 )


		bSizer101.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambah = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.btn_tambah, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer101, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer13, 0, 0, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.m_panel2.SetMaxSize( wx.Size( -1,30 ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Operasi Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer11.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer11 )
		self.m_panel2.Layout()
		bSizer11.Fit( self.m_panel2 )
		bSizer10.Add( self.m_panel2, 1, wx.EXPAND, 0 )


		bSizer10.Add( ( 0, 10), 0, 0, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer10.Add( self.m_staticText6, 0, wx.LEFT, 5 )

		self.textCtrl_id = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.textCtrl_id.SetMinSize( wx.Size( -1,26 ) )

		bSizer10.Add( self.textCtrl_id, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText61 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nim", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		bSizer10.Add( self.m_staticText61, 0, wx.LEFT, 5 )

		self.textCtrl_nim = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.textCtrl_nim.SetMinSize( wx.Size( -1,26 ) )

		bSizer10.Add( self.textCtrl_nim, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText611 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611.Wrap( -1 )

		bSizer10.Add( self.m_staticText611, 0, wx.ALL, 5 )

		self.textCtrl_nama = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.textCtrl_nama.SetMinSize( wx.Size( -1,26 ) )

		bSizer10.Add( self.textCtrl_nama, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6111 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Prodi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6111.Wrap( -1 )

		bSizer10.Add( self.m_staticText6111, 0, wx.ALL, 5 )

		self.textCtrl_prodi = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.textCtrl_prodi.SetMinSize( wx.Size( -1,26 ) )

		bSizer10.Add( self.textCtrl_prodi, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( ( 0, 10), 0, 0, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_simpan = wx.Button( self.m_panel1, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.btn_simpan, 0, 0, 5 )


		bSizer10.Add( bSizer12, 0, wx.ALIGN_RIGHT|wx.RIGHT, 5 )


		self.m_panel1.SetSizer( bSizer10 )
		self.m_panel1.Layout()
		bSizer10.Fit( self.m_panel1 )
		bSizer9.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.btn_dashboard_onclick )
		self.table_students.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.table_studentsOnGridCmdSelectCell )
		self.table_students.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.table_studentsOnGridSelectCell )
		self.btn_refresh.Bind( wx.EVT_BUTTON, self.btn_refresh_onclick )
		self.btn_tambah.Bind( wx.EVT_BUTTON, self.btn_tambah_onclick )
		self.btn_simpan.Bind( wx.EVT_BUTTON, self.btn_simpan_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_dashboard_onclick( self, event ):
		event.Skip()

	def table_studentsOnGridCmdSelectCell( self, event ):
		event.Skip()

	def table_studentsOnGridSelectCell( self, event ):
		event.Skip()

	def btn_refresh_onclick( self, event ):
		event.Skip()

	def btn_tambah_onclick( self, event ):
		event.Skip()

	def btn_simpan_onclick( self, event ):
		event.Skip()


