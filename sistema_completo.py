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

        # acho que é equivalente às divs do html

        # criar divisão da tela
        # weight = 1 -> expande junto com a tela
        # weight = 0 -> não se expande junto com a tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # parte lateral
        self.barra_lateral = ctk.CTkFrame(self, width=200)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")

        # parte principal
        self.janela_abas = ctk.CTkTabview(self, width=400)
        self.janela_abas.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # preencher as partes/abas

        # preencher aba lateral
        self.construir_aba_lateral()

        # preencher aba perfil
        self.construir_aba_perfil()

        # preencher aba preferências
        self.construir_aba_preferencias()

        # preencher aba sistema
        self.construir_aba_sistema()

    def construir_aba_lateral(self):
        pass

    def construir_aba_perfil(self):
        pass

    def construir_aba_preferencias(self):
        pass

    def construir_aba_sistema(self):
        pass


janela = App()
janela.mainloop()