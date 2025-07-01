import tkinter
from PIL import ImageTk, Image
import numpy as np
import cv2 as cv


class Frames:
    def __init__(self, mainObj, MainWin, wWidth, wHeight, function=None, Object=None, xAxis=10, yAxis=10):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.MainWindow = MainWin
        self.MainObj = mainObj
        self.MainWindow.title("Brain Tumor Detection")
        self.callingObj = Object
        self.method = function

        self.winFrame = tkinter.Frame(self.MainWindow, width=wWidth, height=wHeight)
        self.winFrame['borderwidth'] = 5
        self.winFrame['relief'] = 'ridge'
        self.winFrame.place(x=xAxis, y=yAxis)

        self.btnClose = tkinter.Button(self.winFrame, text="Close", width=8,
                                      command=lambda: self.quitProgram(self.MainWindow))
        self.btnClose.place(x=1020, y=600)
        self.btnView = tkinter.Button(self.winFrame, text="View", width=8, command=self.nextWindow)
        self.btnView.place(x=900, y=600)
        self.image = None

    def setCallObject(self, obj):
        self.callingObj = obj

    def setMethod(self, function):
        self.method = function

    def quitProgram(self, window):
        self.MainWindow.destroy()

    def getFrames(self):
        return self.winFrame

    def unhide(self):
        self.winFrame.place(x=self.xAxis, y=self.yAxis)

    def hide(self):
        self.winFrame.place_forget()

    def nextWindow(self):
        listWF = list(self.MainObj.listOfWinFrame)

        if not callable(self.method):
            print("Error: self.method is not callable")
            return

        try:
            self.method()  # Call the method if it's callable
        except Exception as e:
            print(f"Error while calling method: {e}")
            return

        if self.callingObj == self.MainObj.DT:
            img = self.MainObj.DT.getImage()
        else:
            print("Error: No specified object for getImage() function")
            return

        jpgImg = Image.fromarray(img)
        current = listWF.index(self)

        for frame in listWF:
            frame.hide()

        if current == len(listWF) - 1:
            listWF[current].unhide()
            listWF[current].readImage(jpgImg)
            listWF[current].displayImage()
            self.btnView['state'] = 'disable'
        else:
            listWF[current + 1].unhide()
            listWF[current + 1].readImage(jpgImg)
            listWF[current + 1].displayImage()

        print(f"Step {current} Extraction complete!")

    def removeComponent(self):
        self.btnClose.destroy()
        self.btnView.destroy()

    def readImage(self, img):
        self.image = img
        self.Img = np.array(img)
        self.curImg = np.array(img)
        gray = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)
        self.ret, self.thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)




    def displayImage(self):
        imgTk = self.image.resize((250, 250), Image.LANCZOS)
        imgTk = ImageTk.PhotoImage(image=imgTk)
        self.image = imgTk
        self.labelImg = tkinter.Label(self.winFrame, image=self.image)
        self.labelImg.place(x=700, y=150)
