import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("GRAFIT - Gerador de Gráficos Táteis")
        self.geometry("700x600")

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

        self.janela_abas = ctk.CTkTabview(self)
        self.janela_abas.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.construir_aba_lateral()

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

        # -------------------------
        # Tipo de movimento
        # -------------------------

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

        # -------------------------
        # Tipo de gráfico
        # -------------------------

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

        # -------------------------
        # Área de parâmetros
        # -------------------------

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

        # -------------------------
        # Switch tema
        # -------------------------

        self.switch_modo = ctk.CTkSwitch(
            self.barra_lateral,
            text="Modo Escuro",
            command=self.alternar_modo
        )

        self.switch_modo.grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        # -------------------------
        # Botão gerar
        # -------------------------

        self.botao_gerar = ctk.CTkButton(
            self.barra_lateral,
            text="Gerar"
        )

        self.botao_gerar.grid(
            row=5,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        # Inicialização
        self.escolher_movimento("MRU")

    # ==================================================
    # MOVIMENTO
    # ==================================================

    def escolher_movimento(self, movimento):

        if movimento == "MRU":

            self.tipo_grafico.configure(
                values=[
                    "Posição x Tempo",
                    "Velocidade x Tempo",
                    "Aceleração x Tempo"
                ]
            )

            self.tipo_grafico.set("Posição x Tempo")

        elif movimento == "MRUV":

            self.tipo_grafico.configure(
                values=[
                    "Posição x Tempo",
                    "Velocidade x Tempo",
                    "Aceleração x Tempo"
                ]
            )

            self.tipo_grafico.set("Posição x Tempo")

        self.escolher_grafico(
            self.tipo_grafico.get()
        )

    # ==================================================
    # GRÁFICO
    # ==================================================

    def escolher_grafico(self, grafico):

        # Limpa parâmetros antigos

        for widget in self.area_parametros.winfo_children():
            widget.destroy()

        # -------------------------
        # POSIÇÃO x TEMPO
        # -------------------------

        if grafico == "Posição x Tempo":

            ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Posição inicial (m)"
            ).grid(
                row=0,
                column=0,
                pady=5,
                sticky="ew"
            )

            ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Velocidade (m/s)"
            ).grid(
                row=1,
                column=0,
                pady=5,
                sticky="ew"
            )

            if self.tipo_movimento.get() == "MRUV":

                ctk.CTkEntry(
                    self.area_parametros,
                    placeholder_text="Aceleração (m/s²)"
                ).grid(
                    row=2,
                    column=0,
                    pady=5,
                    sticky="ew"
                )

            ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Tempo final (s)"
            ).grid(
                row=3,
                column=0,
                pady=5,
                sticky="ew"
            )

        # -------------------------
        # VELOCIDADE x TEMPO
        # -------------------------

        elif grafico == "Velocidade x Tempo":

            ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Velocidade inicial (m/s)"
            ).grid(
                row=0,
                column=0,
                pady=5,
                sticky="ew"
            )

            if self.tipo_movimento.get() == "MRUV":

                ctk.CTkEntry(
                    self.area_parametros,
                    placeholder_text="Aceleração (m/s²)"
                ).grid(
                    row=1,
                    column=0,
                    pady=5,
                    sticky="ew"
                )

            ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Tempo final (s)"
            ).grid(
                row=2,
                column=0,
                pady=5,
                sticky="ew"
            )

        # -------------------------
        # ACELERAÇÃO x TEMPO
        # -------------------------

        elif grafico == "Aceleração x Tempo":

            ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Aceleração (m/s²)"
            ).grid(
                row=0,
                column=0,
                pady=5,
                sticky="ew"
            )

            ctk.CTkEntry(
                self.area_parametros,
                placeholder_text="Tempo final (s)"
            ).grid(
                row=1,
                column=0,
                pady=5,
                sticky="ew"
            )


app = App()
app.mainloop()