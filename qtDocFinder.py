import sublime
import sublime_plugin
import webbrowser

class qtdocfinderCommand(sublime_plugin.TextCommand):
    def run(self, edit, index):
        sel = self.view.sel()
        if len(sel):
            text = self.view.substr(sel[0])
            text = text.strip()
            print ("caca culo")
            
            if index == 0:
                webbrowser.open("http://doc.qt.io/qt-5/{}.html".format(text))
            if index == 1:
                webbrowser.open("http://doc.qt.io/qt-4.8/{}.html".format(text))
            if index == 2:
                webbrowser.open("http://pyside.github.io/docs/pyside/search.html?q={}".format(text))
            if index == 3:
                webbrowser.open("http://pyqt.sourceforge.net/Docs/PyQt5/search.html?q={}".format(text.lower()))
            if index == 4: 
                webbrowser.open("http://pyqt.sourceforge.net/Docs/PyQt4/{}.html".format(text.lower()))
                