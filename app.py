
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
import time

# Desabilitar o SSL (não recomendado mas necessário)
ssl._create_default_https_context = ssl._create_unverified_context

class DownloaderApp(QMainWindow, Ui_MainWindow):

    # Iniciar APP
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_options()

        # Iniciando botões:
        self.btnPath.clicked.connect(self.choose_folder)
        self.btnDownload.clicked.connect(self.download)

    # Adicionar as opções no select-box
    def set_options(self):
        self.option.addItems(["Audio mp3", "Video mp4"])

    # Escolher pasta output
    def choose_folder(self):
        folder_path_target = QFileDialog.getExistingDirectory(self, "Selecione uma pasta", "/")
        # Atualizar o texto do QLineEdit com o caminho da pasta selecionada
        self.location.setText(folder_path_target)

    def show_message_log(self, msg, type=None):
        # Criar uma instância de QMessageBox
        message_box = QMessageBox()
        # Definir o ícone para indicar uma mensagem de sucesso (ícone de informação)
        if type == "error":
            message_box.setIcon(QMessageBox.Critical)
        else:
            message_box.setIcon(QMessageBox.Information)
        # Definir o texto da mensagem
        message_box.setText(msg)
        # Exibir o pop-up de mensagem
        message_box.exec()
        return       

    # Funcão download
    def download(self):
        link = self.link.text()
        folder = self.location.text()
        option = self.option.currentText()


        # Erro link inválido
        if not link:
            self.show_message_log("Insira um link válido!")
            return


        # Erro pasta output não selecionada
        if not os.path.exists(folder):
            self.show_message_log("Selecione uma pasta de download válida!")
            return


        # Iniciar download
        try:
            yt = YouTube(link)

            # UX - Mensagens avisando o cliente
            self.result.setText("Download iniciado, aguarde...")
            self.btnDownload.setText("Carregando...")
            self.btnDownload.setEnabled(False)
            time.sleep(2)
            self.show_message_log("Download iniciado, aguarde...")

            if option == "Audio mp3":
                stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
                filename = stream.download(folder)
                # Renomear o arquivo para ter a extensão .mp3
                os.rename(filename, filename[:-4] + ".mp3")
            else:
                stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
                filename = stream.download(folder)
            
            # UX - Mensagens avisando o cliente
            self.show_message_log(f"Download completo: {filename}")
            self.result.setText(f"Download finalizado com sucesso")
            self.btnDownload.setText("Baixar")
            self.btnDownload.setEnabled(True)
        except Exception as e:
            # UX - Mensagens avisando o cliente
            self.result.setText(f"Erro ao fazer o download")
            self.btnDownload.setText("Baixar")
            self.btnDownload.setEnabled(True)
            self.show_message_log(f"Erro ao fazer o download: {str(e)}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DownloaderApp()
    window.show()
    app.exec()
