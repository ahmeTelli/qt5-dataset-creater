
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import cv2
import numpy as np
from PyQt5.QtGui import QPixmap
import time
import imutils
from PyQt5.QtWidgets import QFileDialog

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1544, 785)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1024, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Pictures/Screenshot from 2023-03-08 15-51-25.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1280, 620, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.resetButon = QtWidgets.QPushButton(self.centralwidget)
        self.resetButon.setGeometry(QtCore.QRect(1150, 620, 89, 25))
        self.resetButon.setObjectName("resetButon")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1150, 30, 351, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.filterTab = QtWidgets.QWidget()
        self.filterTab.setObjectName("filterTab")
        self.gaussLabel = QtWidgets.QLabel(self.filterTab)
        self.gaussLabel.setGeometry(QtCore.QRect(20, 46, 67, 21))
        self.gaussLabel.setObjectName("gaussLabel")
        self.gaussSlider = QtWidgets.QSlider(self.filterTab)
        self.gaussSlider.setGeometry(QtCore.QRect(120, 50, 160, 16))
        self.gaussSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gaussSlider.setObjectName("gaussSlider")
        self.tabWidget.addTab(self.filterTab, "")
        self.imageTab = QtWidgets.QWidget()
        self.imageTab.setObjectName("imageTab")
        self.labelThreshold = QtWidgets.QLabel(self.imageTab)
        self.labelThreshold.setGeometry(QtCore.QRect(20, 240, 67, 17))
        self.labelThreshold.setObjectName("labelThreshold")
        self.brightness_label = QtWidgets.QLabel(self.imageTab)
        self.brightness_label.setGeometry(QtCore.QRect(20, 10, 67, 17))
        self.brightness_label.setObjectName("brightness_label")
        self.pozlama_slider = QtWidgets.QSlider(self.imageTab)
        self.pozlama_slider.setGeometry(QtCore.QRect(100, 70, 160, 16))
        self.pozlama_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pozlama_slider.setObjectName("pozlama_slider")
        self.threshSlider = QtWidgets.QSlider(self.imageTab)
        self.threshSlider.setGeometry(QtCore.QRect(100, 240, 160, 16))
        self.threshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.threshSlider.setObjectName("threshSlider")
        self.label_5 = QtWidgets.QLabel(self.imageTab)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 67, 17))
        self.label_5.setObjectName("label_5")
        self.brightness_slider = QtWidgets.QSlider(self.imageTab)
        self.brightness_slider.setGeometry(QtCore.QRect(100, 10, 160, 16))
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightness_slider")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.imageTab)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(100, 180, 160, 16))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.contast_label = QtWidgets.QLabel(self.imageTab)
        self.contast_label.setGeometry(QtCore.QRect(20, 130, 67, 17))
        self.contast_label.setObjectName("contast_label")
        self.labelPozlama = QtWidgets.QLabel(self.imageTab)
        self.labelPozlama.setGeometry(QtCore.QRect(20, 70, 67, 17))
        self.labelPozlama.setObjectName("labelPozlama")
        self.contrast_slider = QtWidgets.QSlider(self.imageTab)
        self.contrast_slider.setGeometry(QtCore.QRect(100, 130, 160, 16))
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setObjectName("contrast_slider")
        self.tabWidget.addTab(self.imageTab, "")
        self.tabZoom = QtWidgets.QWidget()
        self.tabZoom.setObjectName("tabZoom")
        self.zoomInButton = QtWidgets.QPushButton(self.tabZoom)
        self.zoomInButton.setGeometry(QtCore.QRect(50, 340, 89, 25))
        self.zoomInButton.setObjectName("zoomInButton")
        self.zoomOutButton = QtWidgets.QPushButton(self.tabZoom)
        self.zoomOutButton.setGeometry(QtCore.QRect(200, 340, 89, 25))
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.tabZoom)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(80, 220, 221, 20))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalSlider = QtWidgets.QSlider(self.tabZoom)
        self.verticalSlider.setGeometry(QtCore.QRect(50, 29, 20, 201))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.tabWidget.addTab(self.tabZoom, "")
        self.dosyaSecButon = QtWidgets.QPushButton(self.centralwidget)
        self.dosyaSecButon.setGeometry(QtCore.QRect(1410, 620, 89, 25))
        self.dosyaSecButon.setObjectName("dosyaSecButon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1544, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.brightness_slider.valueChanged['int'].connect(self.brigthnessValue)
        self.pozlama_slider.valueChanged['int'].connect(self.exposureValue)
        self.contrast_slider.valueChanged['int'].connect(self.contrastValue)
        self.threshSlider.valueChanged['int'].connect(self.thresholdValue)
        
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()
        
        self.pushButton.clicked.connect(self.take_image)
        self.zoomInButton.clicked.connect(self.zoomRatioValue)
        self.zoomOutButton.clicked.connect(self.zoomRatioValue)
        self.resetButon.clicked.connect(self.resetDefault)
        self.dosyaSecButon.clicked.connect(self.openFileExplorer)
        
        
        self.folder = ""
        print(self.folder)
        
        self.tmp = None # Will hold the temporary image for display
        self.brightness_value_now = 20 # Updated brightness value
        self.exposureVal = 2
        self.contrastVal = 2
        self.blur_value_now = 0 # Updated blur value
        self.zoomRatioVal = 1
        self.zoomRightArea = 0
        self.thresholdVal = 0
        self.default = False
        self.disply_width = 1080
        self.display_height = 720

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Fotoğraf"))
        self.resetButon.setText(_translate("MainWindow", "Reset"))
        self.gaussLabel.setText(_translate("MainWindow", "gauss :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filterTab), _translate("MainWindow", "Filters"))
        self.labelThreshold.setText(_translate("MainWindow", "threshold"))
        self.brightness_label.setText(_translate("MainWindow", "parlaklık:"))
        self.label_5.setText(_translate("MainWindow", "kontrast"))
        self.contast_label.setText(_translate("MainWindow", "kontrast"))
        self.labelPozlama.setText(_translate("MainWindow", "pozlama:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageTab), _translate("MainWindow", "İmage"))
        self.zoomInButton.setText(_translate("MainWindow", "Zoom İn"))
        self.zoomOutButton.setText(_translate("MainWindow", "Zoom Out"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabZoom), _translate("MainWindow", "Zoom"))
        self.dosyaSecButon.setText(_translate("MainWindow", "Dosya Sec"))
        
    
    def openFileExplorer(self):
        # file_dialog = QFileDialog()
        folder_path = QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QFileDialog.ShowDirsOnly)

        if folder_path:
            self.folder = folder_path
            print("Seçilen Klasör:", self.folder)
    
    def update_image(self, cv_img):
        if not self.default:
            qt_img0 = self.changeBrightness(cv_img,self.brightness_value_now,self.contrastVal)
            cv_img = self.changeExposureValue(qt_img0,self.exposureVal)
            #cv_img = self.changeZoomRatioValue(qt_img1,self.zoomRatioVal)
            #cv_img = self.changeThresholdValue(cv_img,self.thresholdVal)
            #self.gaussYuksekGeciren(cv_img)
        qt_img = self.convert_cv_qt(cv_img)
        
        self.label.setPixmap(qt_img)
    
    def convert_cv_qt(self,cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h ,w , ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
    def take_image(self):
        self.filename = self.folder+'/Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png' # Will hold the image address location
        image = self.convert_qt_cv(self.label.pixmap())
        cv2.imwrite(self.filename, image)
        print(f"{self.filename} saved!")
        
    
    def convert_qt_cv(self, qt_img):
    # Convert the QPixmap to a QImage
        image = qt_img.toImage()
        # Convert the QImage to a compatible format
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        data = buffer.data()
        arr = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        n_img = np.array(img)
        return n_img


    def brigthnessValue(self,value):
        self.brightness_value_now = value
        self.default = False
        
        
    def changeBrightness(self,img,value,contrast):
        out = cv2.addWeighted(img, contrast, img, 0, value)
        return out 
    
    def contrastValue(self,contrast):
        self.contrastVal = contrast
        self.default = False
        
    def exposureValue(self,expValue):
        self.exposureVal = expValue
        
    def changeExposureValue(self,img,value):
        gamma_table=[np.power(x/255.0,value)*255.0 for x in range(256)]
        gamma_table=np.round(np.array(gamma_table)).astype(np.uint8)
        return cv2.LUT(img,gamma_table)
    
    def zoomRatioValue(self):
        self.zoomRatioVal += 10.2

    def changeZoomRatioValue(self,img,ratioValue):
        print(ratioValue)
        img = cv2.resize(img, (int(img.shape[1] * ratioValue), int(img.shape[0] * ratioValue)))
        print(img.shape[0])
        return img
    
    def resetDefault(self):
        self.default = True
    
    def thresholdValue(self, value):
        self.thresholdVal = value
    
    def changeThresholdValue(self,img, value):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        ret, thres1 =  cv2.threshold(img, value, 255, cv2.THRESH_BINARY)
        
        return thres1 
    
    
    def histogram(self, image):
        print("a")
      
    ###########-> Çok yavaş  
    # def fourierTransform(self,image):

    #     h, w, _ = image.shape
    #     f_size = min(h, w) // 1000
    #     transformed_channels = []
    #     for i in range(3):
            
    #         channel_fft = np.fft.fftshift(np.fft.fft2(image[:, :, i]))
    #         mask = np.zeros_like(channel_fft)
    #         mask[h//2-f_size:h//2+f_size, w//2-f_size:w//2+f_size] = 1
    #         channel_fft *= (1-mask)
    #         transformed_channels.append(np.fft.ifft2(np.fft.ifftshift(channel_fft)).real)
    #     final_image = np.dstack([np.clip(transformed_channels[0], 0, 255).astype('uint8'),
    #                             np.clip(transformed_channels[1], 0, 255).astype('uint8'),
    #                             np.clip(transformed_channels[2], 0, 255).astype('uint8')])
    #     return final_image
    
    
    def gaussYuksekGeciren(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)
        
        d = 30
        sigma = 5
        n = 1
        rows, cols = gray.shape
        crow, ccol = int(rows/2), int(cols/2)
        mask = np.zeros((rows, cols), np.uint8)
        for i in range(rows):
            for j in range(cols):
                d_ij = np.sqrt((i-crow)**2 + (j-ccol)**2)
                mask[i,j] = 1 - np.exp(-((d_ij**n) / (d**(2*n))) * (sigma**2))

        # Filtrelemeyi uygulayın
        fshift_filtered = fshift * mask

        # Sonuç için ters Fourier Dönüşümü uygulayın
        f_ishift = np.fft.ifftshift(fshift_filtered)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)

        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())