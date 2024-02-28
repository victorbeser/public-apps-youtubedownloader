
##########################################################################
#                                                                        #   
#   Desenvolvido por:                                                    #   
#                                                                        #   
#           V          V  III CCCCCC   TTTTTTTTT OOOOOO RRRRRR           #
#           V          V   I  C           T     O    O  R    R           #   
#            V        V    I  C           T     O    O  R    R           #  
#            V        V    I  C           T     O    O  RRRRR            #   
#             V      V     I  C           T     O    O  R   R            #   
#             V      V     I  C           T     O    O  R    R           #   
#              V    V      I  C           T     O    O  R     R          #   
#               V  V      III CCCCCC      T    OOOOOOO  R      R         #   
#                                                                        #   
#                            BBBBB    EEEEE   SSSS   EEEEE  RRRRR        #   
#                            B    B   E       S      E      R    R       #   
#                            BBBBB    EEEE     SSS   EEEE   RRRRR        #   
#                            B    B   E           S  E      R  R         #   
#                            BBBBB    EEEEE   SSSS   EEEEE  R   R        #   
#                                                                        #   
#                                                TikTok: @victorbeser    #   
#                                                Instagram: @jvbeesan    #   
#                                                                        #   
##########################################################################


# IMPORTE OS MÓDULOS ABAIXO
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
import os
import ssl


# Desabilitar o SSL (não recomendado mas necessário)
ssl._create_default_https_context = ssl._create_unverified_context

class DownloaderApp:

    # Iniciar APP
    def __init__(self, root):
        self.root = root
        self.root.title("Youtube Downloader - TikTok @victorbeser")
        self.root.geometry("400x200")

        self.link_label = tk.Label(root, text="Link:")
        self.link_label.pack()
        self.link_entry = tk.Entry(root, width=50)
        self.link_entry.pack()

        self.option_label = tk.Label(root, text="Selecione a Opção:")
        self.option_label.pack()
        self.option_var = tk.StringVar()
        self.option_menu = ttk.OptionMenu(root, self.option_var, "Audio mp3", "Audio mp3", "Video mp4")
        self.option_menu.pack()

        self.folder_frame = tk.Frame(root)
        self.folder_frame.pack()
        self.folder_path = tk.StringVar()
        self.folder_path.set("Pasta de Download")
        self.folder_label = tk.Label(self.folder_frame, textvariable=self.folder_path)
        self.folder_label.pack(side=tk.LEFT)
        self.folder_button = tk.Button(self.folder_frame, text="Escolher", command=self.choose_folder)
        self.folder_button.pack(side=tk.RIGHT)

        self.download_button = tk.Button(root, text="Baixar", command=self.download)
        self.download_button.pack()

    # Escolher pasta output
    def choose_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
        

    # Funcão download
    def download(self):
        link = self.link_entry.get()
        option = self.option_var.get()
        folder = self.folder_path.get()


        # Erro link inválido
        if not link:
            self.show_message("Insira um link válido!")
            return


        # Erro pasta output não selecionada
        if not os.path.exists(folder):
            self.show_message("Selecione uma pasta de download válida!")
            return


        # Iniciar download
        try:
            yt = YouTube(link)
            if option == "Audio mp3":
                stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
                filename = stream.download(folder)
                # Renomear o arquivo para ter a extensão .mp3
                os.rename(filename, filename[:-4] + ".mp3")
            else:
                stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
                filename = stream.download(folder)
            
            self.show_message(f"Download completo: {filename}")
        except Exception as e:
            self.show_message(f"Erro ao fazer o download: {str(e)}")

    def show_message(self, message):
        messagebox.showinfo("Mensagem", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = DownloaderApp(root)
    root.mainloop()
