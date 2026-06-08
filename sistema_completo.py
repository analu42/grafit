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
        titulo = ctk.CTkLabel(self.barra_lateral, text="GRAFIT™", font=ctk.CTkFont(size=25, weight="bold")) # Grafit
        titulo.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nw")

        tipo = ctk.CTkOptionMenu(self.barra_lateral, values=["MRU", "MRUV"]) # Escolher tipo de gráfico
        tipo.grid(row=1, column=0, padx=(10, 20), pady=(30, 10))

'''     if tipo == "MRU":
            mru = ctk.CTkEntry(self.barra_lateral, text="Velocidade")
            mru.grid(row=1, column=1, padx=(10, 20), pady=(30, 10))
        elif tipo == "MRUV":
            mruv = ctk.CTkEntry(self.barra_lateral, text="Tempo")
            mruv.grid(row=1, column=2, padx=(10, 20), pady=(30, 10))'''


        modo = ctk.CTkSwitch(self.barra_lateral, text="Modo Escuro") # Alternar entre modo claro ou escuro
        modo.grid(row=2, column=0, padx=(10, 10), sticky="w")

        botao = ctk.CTkButton(self.barra_lateral, text="Gerar") # Botão para gerar o gráfico
        botao.grid(row=2, column=99, padx=(10, 10),  sticky="e")

    def construir_aba_perfil(self):
        pass

    def construir_aba_preferencias(self):
        pass

    def construir_aba_sistema(self):
        pass


janela = App()#
janela.mainloop()