import ttkbootstrap as ttk


class MainWindow(ttk.Window):
    def __init__(self) -> None:
        super().__init__(
            title="Meu projeto",
            themename="cosmo",
        )
        self.resizable(width=False, height=False)
        self.buid()

    def buid(self):
        # Crie uma label
        label = ttk.Label(self, text="Olá, mundo!")
        label.pack(padx=10, pady=10)

        # Crie um botão
        button = ttk.Button(self, text="Clique aqui")
        button.pack(padx=10, pady=10)

        # Adicione um evento ao botão
        button.config(command=self.botao_clicado)

    def botao_clicado(self):
        print("Botão clicado!")
