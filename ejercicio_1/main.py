from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
button = QtWidgets.QPushButton("Hello World!")
window.setCentralWidget(button)
window.show()
sys.exit(app.exec_())
