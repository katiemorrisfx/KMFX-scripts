import fx
from PySide2 import QtWidgets
from PySide2 import QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtWidgets import QLabel
import sys
from fx import *

fx.prefs.add("KMFX.Alpha Overlay Color UI", True)
fx.prefs.add("KMFX_Load.Alpha Overlay Color UI", True)


class KMFXalphaOverlayColor(Action):
    """allows to change the alpha overlay color with UI item and shortcuts"""

    def __init__(self,):
        if fx.prefs["KMFX_Load.Alpha Overlay Color UI"] is True:
            Action.__init__(self, "KMFX|Alpha Overlay Color")
            # if fx.prefs["KMFX.Alpha Overlay Color UI"]:
            if not self.existingAObtn():

                self.AObtn = self.get_widgets()

                AOcolor = self.fxcolor_to_qcolor(fx.prefs["viewer.alphaColor"])
                self.AObtn.setStyleSheet(
                    "background-color: {}".format(AOcolor.name()))

    def available(self):
        pass

    def execute(self, **kwargs):

        if "color" in kwargs.keys():
            fx.prefs["viewer.alphaColor"] = Color(
                kwargs["color"][0], kwargs["color"][1], kwargs["color"][2], fx.prefs["viewer.alphaColor"].a)
            AOcolor = self.fxcolor_to_qcolor(fx.prefs["viewer.alphaColor"])
            self.AObtn.setStyleSheet(
                "background-color: {}".format(AOcolor.name()))
        else:
            self.updateColor()

    def updateColor(self):
        # print(self.AObtn)
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.AObtn.setStyleSheet(
                "background-color: {}".format(color.name()))
            fx.prefs["viewer.alphaColor"] = self.qcolor_to_fxcolor(
                color, fx.prefs["viewer.alphaColor"])

    def fxcolor_to_qcolor(self, color):
        c = QtGui.QColor()
        c.setRgbF(color.r, color.g, color.b, color.a)
        return c

    def qcolor_to_fxcolor(self, qcolor, alpha):
        r = float(qcolor.red()/255.0)
        g = float(qcolor.green()/255.0)
        b = float(qcolor.blue()/255.0)
        return fx.Color(r, g, b, alpha.a)


    def existingAObtn(self):
        """Checks if the AO button already exists to avoid adding 
        multiple instances 
        
        Returns:
            TYPE: Boolean
        """
        widgets = QtWidgets.QApplication.allWidgets()
        plist = []

        AOfound = False
        for w in widgets:
            if AOfound:
                break
            try:
                if isinstance(w.parent().layout(),QtWidgets.QHBoxLayout):
                    if w.parent().layout().count() > 10 and w.parent() not in plist:
                        plist.append(w.parent())
                        for n in range(0, w.parent().layout().count()):
                            try:
                                x = w.parent().layout().itemAt(n).widget().text()
                                if x == "AO":
                                    AOfound = True
                                    break
                            except Exception:
                                pass
            except Exception:
                pass
        return AOfound


    def get_widgets(self):
        widgets = QtWidgets.QApplication.allWidgets()
        plist = []
        gammafound = False
        for w in widgets:
            if gammafound:
                break
            try:

                # to find the correct place (viewer), look for the Gamma label and a QLayout with lots 10+ items
                # found out that the layout that holds the target buttons is QHBoxLayout
                # so by filtering it the "count? WARNING" messages are avoided
                if isinstance(w.parent().layout(),QtWidgets.QHBoxLayout):
                    if w.parent().layout().count() > 10 and w.parent() not in plist:
                        plist.append(w.parent())
                        for n in range(0, w.parent().layout().count()):
                            try:
                                x = w.parent().layout().itemAt(n).widget().text()
                                if x == "Gamma":
                                    btn = QtWidgets.QPushButton("AO")
                                    if fx.prefs["KMFX.Alpha Overlay Color UI"]:
                                        w.parent().layout().addWidget(btn)
                                    btn.clicked.connect(self.updateColor)
                                    gammafound = True
                                    break

                            except Exception:
                                pass

            except Exception:
                pass

        return btn


addAction(KMFXalphaOverlayColor())