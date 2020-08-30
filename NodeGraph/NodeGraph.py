import sys
import yaml

from PyQt5.QtWidgets import *

from NodeEditorWindow import NodeEditorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("config.yaml") as file:
        data = yaml.full_load(file)
        print(data)

    window = NodeEditorWindow(data)

    sys.exit(app.exec_())