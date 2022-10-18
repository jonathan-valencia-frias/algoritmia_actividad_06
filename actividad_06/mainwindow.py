from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from lista_particulas import Lista_Particulas
from _particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.lista_particulas = Lista_Particulas()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_inicio.clicked.connect(self.click_agregar_inicio)
        self.ui.btn_enviar_final.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_datos.clicked.connect(self.mostrar_datos)
        
    @Slot()
    def mostrar_datos(self):
        self.ui.Canvas_mostar.insertPlainText(str(self.lista_particulas))
    @Slot()
    def click_agregar_inicio(self):
        id=int(self.ui.input_id.text())
        origen_x=int(self.ui.input_origenx.text())
        origen_y=int(self.ui.input_origeny.text())
        destino_x=int(self.ui.input_destinox.text())
        destino_y=int(self.ui.input_destinoy.text())
        velocidad=int(self.ui.input_velocidad.text())
        red=int(self.ui.input_red.text())
        green=int(self.ui.input_green.text())
        blue=int(self.ui.input_blue.text())
        
        particula=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista_particulas.insertar_inicio(particula)
        
    @Slot()
    def click_agregar_final(self):
        id=int(self.ui.input_id.text())
        origen_x=int(self.ui.input_origenx.text())
        origen_y=int(self.ui.input_origeny.text())
        destino_x=int(self.ui.input_destinox.text())
        destino_y=int(self.ui.input_destinoy.text())
        velocidad=int(self.ui.input_velocidad.text())
        red=int(self.ui.input_red.text())
        green=int(self.ui.input_green.text())
        blue=int(self.ui.input_blue.text())
        
        particula=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista_particulas.insertar_final(particula)
        