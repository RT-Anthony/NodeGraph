import os
from PyQt5.QtWidgets import *
from NodeEditorWidget import NodeEditorWidget


class NodeEditorWindow(QMainWindow):
    def __init__(self, config=None):
        super().__init__()
        self._config = config
        self.initUI()
        self.filename = None

    def createAction(self, name, shortcut, tooltip, callback):
        action = QAction(name, self)
        action.setShortcut(shortcut)
        action.setToolTip(tooltip)
        action.triggered.connect(callback)
        return action

    def initUI(self):
        menubar = self.menuBar()

        # menu
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(self.createAction('&New', 'Ctrl+N', "Create new graph", self.onFileNew))
        fileMenu.addSeparator()
        fileMenu.addAction(self.createAction('&Open', 'Ctrl+O', "Open file", self.onFileOpen))
        fileMenu.addAction(self.createAction('&Save', 'Ctrl+S', "Save file", self.onFileSave))
        fileMenu.addAction(self.createAction('Save &As...', 'Ctrl+Shift+S', "Save file as...", self.onFileSaveAs))
        fileMenu.addSeparator()
        fileMenu.addAction(self.createAction('E&xit', 'Ctrl+Q', "Exit application", self.close))

        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(self.createAction('&Undo', 'Ctrl+Z', "Undo last operation", self.onEditUndo))
        editMenu.addAction(self.createAction('&Redo', 'Ctrl+Shift+Z', "Redo last operation", self.onEditRedo))
        editMenu.addSeparator()
        editMenu.addAction(self.createAction('&Delete', 'Del', "Delete selected items", self.onEditDelete))

        # connect node graph
        nodeEditor = NodeEditorWidget(self)
        self.setCentralWidget(nodeEditor)

        self.statusBar().showMessage("")
        self.status_mouse_pos = QLabel("")
        self.statusBar().addPermanentWidget(self.status_mouse_pos)
        nodeEditor.view.scenePosChanged.connect(self.onScenePosChanged)

        if self._config:
            self.setGeometry(200, 200, self._config["default_display"]["width"], self._config["default_display"]["height"])
        else:
            self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("Node Editor")
        self.show()

    def onScenePosChanged(self, x, y):
        self.status_mouse_pos.setText("Scene Pos: [%d, %d]" % (x, y))

    def onFileNew(self):
        self.centralWidget().scene.clear()

    def onFileOpen(self):
        fname, filter = QFileDialog.getOpenFileName(self, 'Open graph from file')
        if fname == '':
            return
        if os.path.isfile(fname):
            self.centralWidget().scene.loadFromFile(fname)

    def onFileSave(self):
        if self.filename is None: return self.onFileSaveAs()
        self.centralWidget().scene.saveToFile(self.filename)
        self.statusBar().showMessage("Successfully saved %s" % self.filename)

    def onFileSaveAs(self):
        fname, filter = QFileDialog.getSaveFileName(self, 'Save graph to file')
        if fname == '':
            return
        self.filename = fname
        self.onFileSave()

    def onEditUndo(self):
        self.centralWidget().scene.history.undo()

    def onEditRedo(self):
        self.centralWidget().scene.history.redo()

    def onEditDelete(self):
        self.centralWidget().scene.grScene.views()[0].deleteSelected()


