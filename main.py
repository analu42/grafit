import customtkinter as ctk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("GRAFIT - Gerador de Gráficos Táteis")
        self.geometry("700x600")

        self.campos = {}
        self.figura_atual = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # =========================
        # SIDEBAR
        # =========================

        self.barra_lateral = ctk.CTkFrame(self, width=250)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")

        # =========================
        # ÁREA PRINCIPAL
        # =========================

        self.area_principal = ctk.CTkFrame(self)

        self.barra_superior = ctk.CTkFrame(
            self.area_principal,
            fg_color="transparent",
            height=50
        )

        self.barra_superior.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.area_principal.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.menu_exportar = ctk.CTkOptionMenu(
            self.barra_superior,
            values=[
                "TXT",
                "SVG",
                "JPEG",
                "PNG",
                "PDF",
                "STL",
                "Braille"
            ],
            command=self.exportar_grafico
        )

        self.menu_exportar.set("Exportar")

        self.menu_exportar.pack(
            side="right"
        )

        self.area_grafico = ctk.CTkFrame(
            self.area_principal
        )

        self.area_grafico.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        self.construir_aba_lateral()

    # ==================================================
    # TEMA
    # ==================================================

    def alternar_modo(self):

        if self.switch_modo.get():

            ctk.set_appearance_mode("Dark")
            self.switch_modo.configure(text="Modo Escuro")

        else:

            ctk.set_appearance_mode("Light")
            self.switch_modo.configure(text="Modo Claro")

    # ==================================================
    # SIDEBAR
    # ==================================================

    def construir_aba_lateral(self):

        titulo = ctk.CTkLabel(
            self.barra_lateral,
            text="GRAFIT™",
            font=ctk.CTkFont(size=25, weight="bold")
        )

        titulo.grid(
            row=0,
            column=0,
            padx=10,
            pady=15
        )

        # Tipo de movimento

        self.tipo_movimento = ctk.CTkOptionMenu(
            self.barra_lateral,
            values=["MRU", "MRUV"],
            command=self.escolher_movimento
        )

        self.tipo_movimento.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        # Tipo de gráfico

        self.tipo_grafico = ctk.CTkOptionMenu(
            self.barra_lateral,
            values=["Posição x Tempo"],
            command=self.escolher_grafico
        )

        self.tipo_grafico.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        # Área de parâmetros

        self.area_parametros = ctk.CTkFrame(
            self.barra_lateral,
            fg_color="transparent"
        )

        self.area_parametros.grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        # Switch tema

        self.switch_modo = ctk.CTkSwitch(
            self.barra_lateral,
            text="Modo Claro",
            command=self.alternar_modo
        )

        self.switch_modo.grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        # Botão gerar

        self.botao_gerar = ctk.CTkButton(
            self.barra_lateral,
            text="Gerar",
            command=self.gerar_grafico
        )

        self.botao_gerar.grid(
            row=5,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.escolher_movimento("MRU")

    # ==================================================
    # MOVIMENTO
    # ==================================================

    def escolher_movimento(self, movimento):

        self.tipo_grafico.configure(
            values=[
                "Posição x Tempo",
                "Velocidade x Tempo",
                "Aceleração x Tempo"
            ]
        )

        grafico_atual = self.tipo_grafico.get()

        if grafico_atual not in [
            "Posição x Tempo",
            "Velocidade x Tempo",
            "Aceleração x Tempo"
        ]:
            grafico_atual = "Posição x Tempo"

        self.tipo_grafico.set(grafico_atual)

        self.escolher_grafico(grafico_atual)

    # ==================================================
    # CRIAÇÃO DOS CAMPOS
    # ==================================================

    def escolher_grafico(self, grafico):

        for widget in self.area_parametros.winfo_children():
            widget.destroy()

        self.campos.clear()

        # -------------------------
        # POSIÇÃO x TEMPO
        # -------------------------

        if grafico == "Posição x Tempo":

            self.campos["posicao"] = ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Posição inicial (m)"
            )
            self.campos["posicao"].grid(
                row=0,
                column=0,
                pady=5,
                sticky="ew"
            )

            self.campos["velocidade"] = ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Velocidade (m/s)"
            )
            self.campos["velocidade"].grid(
                row=1,
                column=0,
                pady=5,
                sticky="ew"
            )

            if self.tipo_movimento.get() == "MRUV":

                self.campos["aceleracao"] = ctk.CTkEntry(
                    self.area_parametros,
                    placeholder_text="Aceleração (m/s²)"
                )
                self.campos["aceleracao"].grid(
                    row=2,
                    column=0,
                    pady=5,
                    sticky="ew"
                )

            self.campos["tempo"] = ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Tempo final (s)"
            )
            self.campos["tempo"].grid(
                row=3,
                column=0,
                pady=5,
                sticky="ew"
            )

        # -------------------------
        # VELOCIDADE x TEMPO
        # -------------------------

        elif grafico == "Velocidade x Tempo":

            self.campos["velocidade"] = ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Velocidade inicial (m/s)"
            )
            self.campos["velocidade"].grid(
                row=0,
                column=0,
                pady=5,
                sticky="ew"
            )

            if self.tipo_movimento.get() == "MRUV":

                self.campos["aceleracao"] = ctk.CTkEntry(
                    self.area_parametros,
                    placeholder_text="Aceleração (m/s²)"
                )
                self.campos["aceleracao"].grid(
                    row=1,
                    column=0,
                    pady=5,
                    sticky="ew"
                )

            self.campos["tempo"] = ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Tempo final (s)"
            )
            self.campos["tempo"].grid(
                row=2,
                column=0,
                pady=5,
                sticky="ew"
            )

        # -------------------------
        # ACELERAÇÃO x TEMPO
        # -------------------------

        elif grafico == "Aceleração x Tempo":

            self.campos["aceleracao"] = ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Aceleração (m/s²)"
            )
            self.campos["aceleracao"].grid(
                row=0,
                column=0,
                pady=5,
                sticky="ew"
            )

            self.campos["tempo"] = ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Tempo final (s)"
            )
            self.campos["tempo"].grid(
                row=1,
                column=0,
                pady=5,
                sticky="ew"
            )
    # ==================================================
    # MOSTRAR OS GRÁFICOS
    # ==================================================

    def mostrar_grafico(self, figura):

        # remove gráfico anterior
        for widget in self.area_grafico.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(
            figura,
            master=self.area_grafico
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    # ==================================================
    # GERAÇÃO DOS GRÁFICOS
    # ==================================================

    def gerar_grafico(self):

        try:

            grafico = self.tipo_grafico.get()
            movimento = self.tipo_movimento.get()

            if grafico == "Posição x Tempo":

                s0 = float(self.campos["posicao"].get())
                v0 = float(self.campos["velocidade"].get())
                tf = float(self.campos["tempo"].get())

                t = np.linspace(0, tf, 100)

                if movimento == "MRU":

                    s = s0 + v0 * t

                else:

                    a = float(self.campos["aceleracao"].get())
                    s = s0 + v0*t + (a*t**2)/2

                fig, ax = plt.subplots(figsize=(8, 5))

                ax.plot(t, s)

                ax.set_title("Posição x Tempo")
                ax.set_xlabel("Tempo (s)")
                ax.set_ylabel("Posição (m)")
                ax.grid(True)

                self.figura_atual = fig

                self.mostrar_grafico(fig)

            elif grafico == "Velocidade x Tempo":

                v0 = float(self.campos["velocidade"].get())
                tf = float(self.campos["tempo"].get())

                t = np.linspace(0, tf, 100)

                if movimento == "MRU":

                    v = np.full_like(t, v0)

                else:

                    a = float(self.campos["aceleracao"].get())
                    v = v0 + a*t

                fig, ax = plt.subplots(figsize=(8, 5))

                ax.plot(t, v)

                ax.set_title("Velocidade x Tempo")
                ax.set_xlabel("Tempo (s)")
                ax.set_ylabel("Velocidade (m/s)")
                ax.grid(True)

                self.figura_atual = fig

                self.mostrar_grafico(fig)

            elif grafico == "Aceleração x Tempo":

                a = float(self.campos["aceleracao"].get())
                tf = float(self.campos["tempo"].get())

                t = np.linspace(0, tf, 100)
                aceleracao = np.full_like(t, a)

                fig, ax = plt.subplots(figsize=(8, 5))

                ax.plot(t, aceleracao)

                ax.set_title("Aceleração x Tempo")
                ax.set_xlabel("Tempo (s)")
                ax.set_ylabel("Aceleração (m/s²)")
                ax.grid(True)

                self.figura_atual = fig

                self.mostrar_grafico(fig)

        except ValueError:

            print("Preencha todos os campos com números válidos.")

    def exportar_grafico(self, formato):

        if self.figura_atual is None:
            print("Nenhum gráfico gerado.")
            self.menu_exportar.set("Exportar")
            return

        extensoes = {
            "PNG": ".png",
            "PDF": ".pdf",
            "SVG": ".svg",
            "JPEG": ".jpeg"
        }

        if formato not in extensoes:
            self.mostrar_aviso(
                "Função indisponível",
                f"A exportação para {formato} ainda não foi implementada."
            )

            self.menu_exportar.set("Exportar")
            return

        arquivo = filedialog.asksaveasfilename(
            defaultextension=extensoes[formato],
            filetypes=[
                (f"Arquivo {formato}", f"*{extensoes[formato]}")
            ]
        )

        if arquivo:
            self.figura_atual.savefig(arquivo)

            print(f"Salvo em: {arquivo}")

        self.menu_exportar.set("Exportar")

    def mostrar_aviso(self, titulo, mensagem):

        janela = ctk.CTkToplevel(self)
        janela.title(titulo)
        janela.geometry("350x150")

        janela.grab_set()  # impede interação com a janela principal

        label = ctk.CTkLabel(
            janela,
            text=mensagem,
            wraplength=300
        )
        label.pack(pady=20)

        botao = ctk.CTkButton(
            janela,
            text="OK",
            command=janela.destroy
        )
        botao.pack(pady=10)
        

app = App()
app.mainloop()