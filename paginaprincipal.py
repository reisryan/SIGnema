from customtkinter import *
from PIL import Image

set_default_color_theme("green")

class SIGnemaApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("SIGnema App")

        # Configurar a barra lateral (Hamburger menu)
        self.sidebar_frame = CTkFrame(self, width=200, height=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")

        self.sidebar_toggle_button = CTkButton(self, text="☰", width=40, height=40, command=self.toggle_sidebar)
        self.sidebar_toggle_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        # Botões da barra lateral
        self.create_sidebar_buttons()

        # Área principal
        self.main_frame = CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.create_main_content()

        # Barra inferior
        self.bottom_bar_frame = CTkFrame(self, height=40, width=800, corner_radius=0)
        self.bottom_bar_frame.place(x=0, y=560)  # Configura a posição e o tamanho da barra inferior

        self.create_bottom_bar()

        # Configurar layout responsivo
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def create_sidebar_buttons(self):
        self.my_orders_button = CTkButton(self.sidebar_frame, text="Ver Meus Pedidos", command=self.show_my_orders)
        self.my_orders_button.place(x=0,y=60)

        self.my_data_button = CTkButton(self.sidebar_frame, text="Meu Perfil", command=self.show_my_data)
        self.my_data_button.place(x=0,y=90)

        self.change_password_button = CTkButton(self.sidebar_frame, text="Alterar Senha", command=self.change_password)
        self.change_password_button.place(x=0,y=120)

    def create_main_content(self):
        self.recommendations_label = CTkLabel(self.main_frame, text="Recomendações de Filmes", font=("Arial", 20))
        self.recommendations_label.pack(pady=20)

        # Adicione aqui mais widgets para mostrar recomendações de filmes

    def create_bottom_bar(self):
        self.home_button = CTkButton(self.bottom_bar_frame, text="Home", command=self.show_home)
        self.home_button.place(relx=0.15, rely=0.5, anchor="center")

        self.movies_button = CTkButton(self.bottom_bar_frame, text="Filmes", command=self.show_movies)
        self.movies_button.place(relx=0.5, rely=0.5, anchor="center")

        self.cinemas_button = CTkButton(self.bottom_bar_frame, text="Cinemas", command=self.show_cinemas)
        self.cinemas_button.place(relx=0.85, rely=0.5, anchor="center")

    def toggle_sidebar(self):
        if self.sidebar_frame.winfo_viewable():
            self.sidebar_frame.grid_remove()
        else:
            self.sidebar_frame.grid()

    def show_home(self):
        self.clear_main_frame()
        self.home_label = CTkLabel(self.main_frame, text="Home", font=("Arial", 20))
        self.home_label.pack(pady=20)
        # Adicione widgets relacionados à página inicial

    def show_movies(self):
        self.clear_main_frame()
        self.movies_label = CTkLabel(self.main_frame, text="Filmes", font=("Arial", 20))
        self.movies_label.pack(pady=20)
        # Adicione widgets relacionados à página de filmes

    def show_cinemas(self):
        self.clear_main_frame()
        self.cinemas_label = CTkLabel(self.main_frame, text="Cinemas", font=("Arial", 20))
        self.cinemas_label.pack(pady=20)
        # Adicione widgets relacionados à página de cinemas

    def show_my_orders(self):
        self.clear_main_frame()
        self.orders_label = CTkLabel(self.main_frame, text="Meus Pedidos", font=("Arial", 20))
        self.orders_label.pack(pady=20)
        # Adicione widgets relacionados aos pedidos

    def show_my_data(self):
        self.clear_main_frame()
        self.data_label = CTkLabel(self.main_frame, text="Meus Dados", font=("Arial", 20))
        self.data_label.pack(pady=20)
        # Adicione widgets relacionados aos dados

    def change_password(self):
        self.clear_main_frame()
        self.password_label = CTkLabel(self.main_frame, text="Alterar Senha", font=("Arial", 20))
        self.password_label.pack(pady=20)
        # Adicione widgets relacionados à alteração de senha

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = SIGnemaApp()
    app.mainloop()
