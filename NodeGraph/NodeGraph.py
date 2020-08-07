import sys

from PyQt5.QtWidgets import *

from NodeEditorWindow import NodeEditorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = NodeEditorWindow()

    sys.exit(app.exec_())