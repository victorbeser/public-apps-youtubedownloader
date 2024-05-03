
###################################################################################
#                                                                                 #   
#   Desenvolvido por:                                                             #   
#                                                                                 #   
#           V          V  III CCCCCC   TTTTTTTTT OOOOOO RRRRRR                    #
#           V          V   I  C           T     O    O  R    R                    #   
#            V        V    I  C           T     O    O  R    R                    #  
#            V        V    I  C           T     O    O  RRRRR                     #   
#             V      V     I  C           T     O    O  R   R                     #   
#             V      V     I  C           T     O    O  R    R                    #   
#              V    V      I  C           T     O    O  R     R                   #   
#               V  V      III CCCCCC      T    OOOOOOO  R      R                  #   
#                                                                                 #   
#                            BBBBB    EEEEE   SSSS   EEEEE  RRRRR                 #   
#                            B    B   E       S      E      R    R                #   
#                            BBBBB    EEEE     SSS   EEEE   RRRRR                 #   
#                            B    B   E           S  E      R  R                  #   
#                            BBBBB    EEEEE   SSSS   EEEEE  R   R                 #   
#                                                                                 #   
#                                                TikTok: @victorbeser             #   
#                                                Instagram: @jvbeesan             #   
#                                                                                 #
#  -----------------------------------------------------------------------------  #
#                                                                                 #
#   Contribuição:                                                                 #   
#                                                                                 #   
#               FFFFF   AAAAA  BBBB    III   OOOO                                 #
#               F      A     A B    B   I   O    O                                # 
#               FFFF   AAAAAAA BBBB     I   O    O                                # 
#               F      A     A B    B   I   O    O                                # 
#               F      A     A BBBB    III   OOOO                                 # 
#                                                                                 #
#               CCCCCC    AAAAA  RRRRR   V     V   AAAAA  L      H    H   OOOOO   #
#               C        A     A R    R   V   V   A     A L      H    H  O     O  #
#               C        AAAAAAA RRRRR     V V    AAAAAAA L      HHHHHH  O     O  #
#               C        A     A R   R      V     A     A L      H    H  O     O  #
#                CCCCCC  A     A R    R     V     A     A LLLLL  H    H   OOOOO   #
#                                                                                 #
#                                                                                 #   
#                                         TikTok: @ofabioacarvalho                #   
#                                         Instagram: @ofabioacarvalho             #   
#                                                                                 #   
###################################################################################


# INSTALE OS MÓDULOS ABAIXO (Leia o README.md)

from PySide6.QtCore import Qt
from pytube import YouTube
import os
import sys
import ssl
from inter.design import *
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit, QPushButton, QMessageBox, QWidget

# Desabilitar o SSL (não recomendado mas necessário)
ssl._create_default_https_context = ssl._create_unverified_context


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()
