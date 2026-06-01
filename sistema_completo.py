#Agora com POO e mais bonitinho
import customtkinter as ctk

ctk.set_appearance_mode("System") #define o modo (System, Light ou Dark)
ctk.set_default_color_theme("blue") #blue, green, dark-blue

class App(ctk.CTk): #"cópia" do root = ctk.CTk
    def __init__(self):
        super().__init__()
        #o python vai executar tudo da classe init e então os seus comandos personalizados
        self.title("GRAFIT - Gerador de Graficos Táteis")
        self.geometry("600x600")
        self.construir_tela()

    def construir_tela(self):
        pass

janela = App()
janela.mainloop()