import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
				QPushButton, QLabel, QLineEdit, QTabBar,
				QFrame, QStackedLayout, QTabWidget)

from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *

class AddressBar(QLineEdit):
	def __init__(self):
		super().__init__()

	def mousePressEvent(self, e):
		self.selectAll()

class App(QFrame):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Web Browser")

		self.CreateApp()
		self.setBaseSize(1366,768)

	def CreateApp(self):
		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0,0,0,0)

		self.tabbar = QTabBar(movable=True, tabsClosable=True)
		self.tabbar.tabCloseRequested.connect(self.CloseTab)

		self.tabbar.addTab("Tab 1")
		self.tabbar.addTab("Tab 2")

		self.tabbar.setCurrentIndex(0)

		# Create Addressbar
		self.Toolbar = QWidget()
		self.ToolbarLayout = QHBoxLayout()
		self.addressbar = AddressBar()#Done till here
		
		self.Toolbar.setLayout(self.ToolbarLayout)
		self.ToolbarLayout.addWidget(self.addressbar)
		
		# New tab button
		self.AddTabButton = QPushButton("+")
		self.AddTabButton.clicked.connect(self.AddTab)
		
		self.ToolbarLayout.addWidget(self.AddTabButton)
		
		# Set main View
		self.container = QWidget()
		self.container.layout = QStackedLayout()
		self.container.setLayout(self.container.layout)

		self.layout.addWidget(self.tabbar)
		self.layout.addWidget(self.Toolbar)
		self.layout.addWidget(self.container)

		self.setLayout(self.layout)

		self.show()

	def AddTab():
		pass

	def CloseTab(self, i):
		self.tabbar.removeTab(i)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = App()

	sys.exit(app.exec_())
