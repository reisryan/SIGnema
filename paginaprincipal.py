from customtkinter import *
from PIL import Image
import sys
import os

set_default_color_theme("green")

class SIGnemaApp(CTk):
    def __init__(self, user, usertype):
        super().__init__()
        
        self.user = user
        self.usertype = usertype
        
        self.geometry("1000x600")
        self.title("SIGnema App")
        self.base_directory = os.path.dirname(os.path.abspath(__file__))
        self.usuarios_file = os.path.join(self.base_directory, "data", "usuarios.txt")

        # Barra lateral
        self.sidebar_frame = CTkFrame(self, width=150, height=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")

        self.sidebar_toggle_button = CTkButton(self, text="☰", width=40, height=40, command=self.toggle_sidebar)
        self.sidebar_toggle_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        # Botões da barra lateral
        self.create_sidebar_buttons()

        # Área principal
        self.main_frame = CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # Barra inferior
        self.bottom_bar_frame = CTkFrame(self, height=40, width=800, corner_radius=0)
        self.bottom_bar_frame.place(x=0, y=560)  # Posição e o tamanho da barra inferior

        self.create_bottom_bar()

        # Layout responsivo
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.show_movies()

    def create_sidebar_buttons(self):
        self.my_orders_button = CTkButton(self.sidebar_frame, text="Ver Meus Pedidos", command=self.show_my_orders)
        self.my_orders_button.place(x=0, y=60)

        self.my_data_button = CTkButton(self.sidebar_frame, text="Meu Perfil", command=self.show_my_data)
        self.my_data_button.place(x=0, y=90)

        self.change_password_button = CTkButton(self.sidebar_frame, text="Alterar Senha", command=self.change_password)
        self.change_password_button.place(x=0, y=120)
        
        if self.usertype == "Gerente":
            self.admin_users_button = CTkButton(self.sidebar_frame, text="Gerenciar Funcionários", command=self.admin_properties)
            self.admin_users_button.place(x=0, y=150)

    def create_bottom_bar(self):
        self.movies_button = CTkButton(self.bottom_bar_frame, text="Filmes", command=self.show_movies)
        self.movies_button.place(relx=0.5, rely=0.5, anchor="center")

        self.rooms_button = CTkButton(self.bottom_bar_frame, text="Salas", command=self.show_rooms)
        self.rooms_button.place(relx=0.85, rely=0.5, anchor="center")

    def toggle_sidebar(self):
        if self.sidebar_frame.winfo_viewable():
            self.sidebar_frame.grid_remove()
        else:
            self.sidebar_frame.grid()

    def show_movies(self):
        self.clear_main_frame()
        self.movies_label = CTkLabel(self.main_frame, text="Filmes", font=("Arial", 20))
        self.movies_label.pack(pady=20)
        self.create_movie_posters()

    def show_rooms(self):
        self.clear_main_frame()
        self.rooms_label = CTkLabel(self.main_frame, text="Salas", font=("Arial", 20))
        self.rooms_label.pack(pady=20)
        pat_button = CTkButton(self.main_frame, text="PAT AT 085", command=self.show_movies)
        pat_button.pack(pady=20)

    def create_movie_posters(self):
        movies = [
            ("Deadpool e Wolverine", "images/filme1.png"),
            ("Meu Malvado Favorito 4", "images/filme2.png"),
            ("Divertida Mente 2", "images/filme3.png"),
            ("Twisters", "images/filme4.png"),
            ("O Exorcismo", "images/filme5.png"),
            ("Letícia", "images/filme6.png"),
        ]
        poster_frame = CTkScrollableFrame(self.main_frame, width=800, height=400, orientation='horizontal')
        poster_frame.pack()

        for i, (name, image_file) in enumerate(movies):
            frame = CTkFrame(poster_frame)
            frame.pack(side="left", padx=10, pady=10)

            image_path = os.path.join(self.base_directory, image_file)
            img = Image.open(image_path)
            photo = CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 265))

            button = CTkButton(frame, image=photo, text='', command=lambda name=name: self.open_movie_page(name))
            button.image = photo
            button.pack()

            label = CTkLabel(frame, text=name)
            label.pack()

    def open_movie_page(self, movie_name):
        self.clear_main_frame()
        movie_label = CTkLabel(self.main_frame, text=f"Página do {movie_name}", font=("Arial", 20))
        movie_label.grid(row=0, column=0, pady=20)
        seat_matrix = self.load_seat_matrix(movie_name)

        self.create_seat_interface(movie_name, seat_matrix)
    
    def create_seat_interface(self, movie_name, seat_matrix):
        seat_frame = CTkScrollableFrame(self.main_frame, width=700, height=400, orientation='horizontal')
        seat_frame.grid(row=0, column=0, pady=20)

        self.seat_buttons = []
        for row in range(5):
            row_buttons = []
            for col in range(10):
                button = CTkButton(seat_frame, text=f"{row * 10 + col + 1}",
                                command=lambda r=row, c=col: self.toggle_seat(r, c, movie_name),
                                width=60, height=60, font=("Arial", 16))
                button.grid(row=row, column=col, padx=5, pady=5)
                if seat_matrix[row][col] == 0:
                    button.configure(fg_color="green")
                elif seat_matrix[row][col] == 1:
                    button.configure(fg_color="gray")
                    button.configure(state="disabled")
                elif seat_matrix[row][col] == 2:
                    button.configure(fg_color="blue")
                row_buttons.append(button)
            self.seat_buttons.append(row_buttons)

        save_button = CTkButton(self.main_frame, text="Salvar e Voltar", command=lambda: self.save_and_return(movie_name))
        save_button.grid(row=2, column=0, pady=10)

    def toggle_seat(self, row, col, movie_name):
        current_color = self.seat_buttons[row][col].cget("fg_color")
        new_color = "blue" if current_color == "green" else "green"
        self.seat_buttons[row][col].configure(fg_color=new_color)

        # Atualiza a matriz de assentos e salva no arquivo
        seat_matrix = self.load_seat_matrix(movie_name)
        seat_matrix[row][col] = 2 if new_color == "blue" else 0
        self.save_seat_matrix(movie_name, seat_matrix)

    def save_and_return(self, movie_name):
        seat_matrix = [[1 if button.cget("fg_color") == "blue" else (1 if button.cget("fg_color") == "gray" else 0) for button in row_buttons] for row_buttons in self.seat_buttons]
        self.save_seat_matrix(movie_name, seat_matrix)
        self.show_movies()

    def clear_seats(self, movie_name):
        # Redefine a matriz de assentos para todos os zeros
        seat_matrix = [[0 for _ in range(10)] for _ in range(5)]
        self.save_seat_matrix(movie_name, seat_matrix)
        self.open_movie_page(movie_name)  # Dá Reload na interface

    def save_seat_matrix(self, movie_name, seat_matrix):
        file_path = os.path.join(self.base_directory, f"{movie_name}_seats.txt")
        with open(file_path, "w") as file:
            for row in seat_matrix:
                file.write("".join(map(str, row)) + "\n")

    def load_seat_matrix(self, movie_name):
        file_path = os.path.join(self.base_directory, f"{movie_name}_seats.txt")
        if not os.path.exists(file_path):
            return [[0 for _ in range(10)] for _ in range(5)]
        with open(file_path, "r") as file:
            return [list(map(int, line.strip())) for line in file]

    def show_my_orders(self):
        self.clear_main_frame()
        self.orders_label = CTkLabel(self.main_frame, text="Meus Pedidos", font=("Arial", 20))
        self.orders_label.pack(pady=20)

    def show_my_data(self):
        self.clear_main_frame()
        self.data_label = CTkLabel(self.main_frame, text="Meus Dados", font=("Arial", 20))
        self.data_label.pack(pady=20)

    def change_password(self):
        self.clear_main_frame()
        self.password_label = CTkLabel(self.main_frame, text="Alterar Senha", font=("Arial", 20))
        self.password_label.pack(pady=20)
        
    def admin_properties(self):
        self.clear_main_frame()
        self.users_list = CTkLabel(self.main_frame, text="Gerenciar Funcionarios", font=("Arial", 20))
        self.users_list.pack(pady=20)
        self.users_frame = CTkFrame(self.main_frame)
        self.users_frame.pack(pady=10)
        users = self.read_users_from_file(self.usuarios_file)
        for user_id, user, passw, usertype in users:
            if usertype == 'Funcionario':
                user_info = f"ID: {user_id}, Usuário: {user}, Tipo: {usertype}"
                user_label = CTkLabel(self.users_frame, text=user_info, font=("Arial", 12))
                user_label.pack(pady=5)

    def read_users_from_file(self, file_path):
        users = []
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    user_data = line.strip().split(",")
                    if len(user_data) == 4:  # Espera-se que cada linha tenha 4 partes
                        users.append(user_data)
        except FileNotFoundError:
            print(f"Arquivo {file_path} não encontrado.")
        return users

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python paginaprincipal.py <user> <usertype>")
        sys.exit(1)

    user = sys.argv[1]
    usertype = sys.argv[2]

    app = SIGnemaApp(user, usertype)
    app.mainloop()
