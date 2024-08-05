from customtkinter import *
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import sys
import os

set_default_color_theme("green")

class SIGnemaApp(CTk):
    def __init__(self, user, usertype):
        super().__init__()
        
        self.user = user
        self.usertype = usertype
        self.orders = []
        
        self.geometry("1000x600")
        self.title("SIGnema App")
        self.base_directory = os.path.dirname(os.path.abspath(__file__))
        self.usuarios_file = os.path.join(self.base_directory, "data", "usuarios.txt")

        # barra lateral
        self.sidebar_frame = CTkFrame(self, width=150, height=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")

        self.sidebar_toggle_button = CTkButton(self, text="☰", width=40, height=40, command=self.toggle_sidebar)
        self.sidebar_toggle_button.grid(row=0, column=0, sticky="nw", padx=10, pady=8)

        # botões da barra lateral
        self.create_sidebar_buttons()

        # area principal
        self.main_frame = CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # barra inferior
        self.bottom_bar_frame = CTkFrame(self, height=40, width=800, corner_radius=0)
        self.bottom_bar_frame.place(x=0, y=560)

        self.create_bottom_bar()

        # layout responsivo
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.show_rooms()

    def create_sidebar_buttons(self):
        self.my_orders_button = CTkButton(self.sidebar_frame, text="Ver Meus Pedidos", command=self.show_my_orders)
        self.my_orders_button.place(x=0, y=60)

        self.my_data_button = CTkButton(self.sidebar_frame, text="Meu Perfil", command=self.show_my_data)
        self.my_data_button.place(x=0, y=90)

        self.change_password_button = CTkButton(self.sidebar_frame, text="Alterar Senha", command=self.change_password)
        self.change_password_button.place(x=0, y=120)
        
        self.add_saldo_button = CTkButton(self.sidebar_frame, text="Adicionar Saldo", command=self.add_saldo)
        self.add_saldo_button.place(x=0, y=150)
        
        if self.usertype == "Funcionario" or self.usertype == "Gerente":
            self.funcionario_button = CTkButton(self.sidebar_frame, text="Adicionar Filme", command=self.funcionario_properties)
            self.funcionario_button.place(x=0, y=180)
        if self.usertype == "Gerente":
            self.admin_users_button = CTkButton(self.sidebar_frame, text="Gerenciar Funcionários", command=self.admin_properties)
            self.admin_users_button.place(x=0, y=210)

    def add_saldo(self):
        self.clear_main_frame()
        self.add_saldo_label = CTkLabel(self.main_frame, text="Adicionar Saldo", font=("Arial", 20))
        self.add_saldo_label.pack(pady=20)
        self.addsaldol = CTkLabel(self.main_frame, text="Quanto de saldo adicionar:").pack(pady=10)
        self.addsaldoentry = CTkEntry(self.main_frame)
        self.addsaldoentry.pack(pady=10)
        self.addsaldob = CTkButton(self.main_frame, width=4, height=8, text="Adicionar", command=self.addsaldo).pack(pady=10)

    def addsaldo(self):
        plussaldo = float(self.addsaldoentry.get())  # Convertendo a entrada para float
        updated_lines = []
        user_found = False

        # Lendo as linhas do arquivo
        with open(self.usuarios_file, 'r') as file:
            lines = file.readlines()

        # Atualizando as linhas
        with open(self.usuarios_file, 'w') as file:
            for line in lines:
                user_id, username, pw, utype, saldo = line.strip().split(',')
                if self.user == username:
                    saldo = float(saldo) + plussaldo  # Somando o saldo
                    user_found = True
                updated_line = f"{user_id},{username},{pw},{utype},{saldo:.2f}\n"  # Corrigindo a vírgula
                file.write(updated_line)

        if user_found:
            print("Saldo atualizado com sucesso.")
        else:
            print("Usuário não encontrado.")

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
        self.clear_main_frame()

        self.movies_label = CTkLabel(self.main_frame, text="Filmes", font=("Arial", 20))
        self.movies_label.pack(pady=20)
        
        movies = [
            ("Deadpool e Wolverine", "images/filme1.png", "08h00"),
            ("Meu Malvado Favorito 4", "images/filme2.png", "11h00"),
            ("Divertida Mente 2", "images/filme3.png", "14h00"),
            ("Twisters", "images/filme4.png", "17h00"),
            ("O Exorcismo", "images/filme5.png", "20h00"),
            ("Letícia", "images/filme6.png", "23h00"),
        ]
        poster_frame = CTkScrollableFrame(self.main_frame, width=800, height=400, orientation='horizontal')
        poster_frame.pack()

        for name, image_file, time in movies:
            frame = CTkFrame(poster_frame)
            frame.pack(side="left", padx=10, pady=10)

            image_path = os.path.join(self.base_directory, image_file)
            img = Image.open(image_path)
            photo = CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 265))

            button = CTkButton(frame, image=photo, text='', command=lambda name=name, time=time: self.open_movie_page(name, time))
            button.image = photo
            button.pack()

            movie_info = f"{name} - \nHorário(s) Disponível(is): {time}"
            label = CTkLabel(frame, text=movie_info)
            label.pack()

    def open_movie_page(self, movie_name, time):
        self.clear_main_frame()
        movie_label = CTkLabel(self.main_frame, text=f"Página do {movie_name}", font=("Arial", 20))
        movie_label.grid(row=0, column=0, pady=20)
        seat_matrix = self.load_seat_matrix(movie_name, time)

        self.create_seat_interface(movie_name, time, seat_matrix)

    def create_seat_interface(self, movie_name, time, seat_matrix):
        seat_frame = CTkScrollableFrame(self.main_frame, width=700, height=400, orientation='horizontal')
        seat_frame.grid(row=0, column=0, pady=20)

        self.seat_buttons = []
        for row in range(5):
            row_buttons = []
            for col in range(10):
                button = CTkButton(seat_frame, text=f"{row * 10 + col + 1}",
                                    command=lambda r=row, c=col: self.toggle_seat(r, c, movie_name, time),
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

        save_button = CTkButton(self.main_frame, text="Salvar e Voltar", command=lambda: self.save_and_return(movie_name, time))
        save_button.grid(row=2, column=0, pady=10)
        return_button = CTkButton(self.main_frame, text="Voltar", command=self.show_movies)
        return_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def save_order(self, movie_name, time, seats):
        order = {
            "Cliente": self.user,
            "Filme": movie_name,
            "Sala": "PAT AT 085",
            "Horário": time,
            "Assentos": seats
        }
        self.orders.append(order)
        self.save_orders_to_file(order)

    def save_orders_to_file(self, order):
        pedidos_dir = os.path.join(self.base_directory, 'pedidos')
        if not os.path.exists(pedidos_dir):
            os.makedirs(pedidos_dir)

        file_path = os.path.join(pedidos_dir, f'{self.user}_pedidos.txt')
        with open(file_path, 'a') as file:
            file.write(f"{order['Cliente']}!{order['Filme']}!{order['Sala']}!{order['Horário']}!{','.join(order['Assentos'])}\n")

    def toggle_seat(self, row, col, movie_name, time):
        current_color = self.seat_buttons[row][col].cget("fg_color")
        
        # Não permite selecionar assentos cinzas (ocupados)
        if current_color == "gray":
            return

        new_color = "blue" if current_color == "green" else "green"
        self.seat_buttons[row][col].configure(fg_color=new_color)

        # Atualizar e salvar a matriz no arquivo
        seat_matrix = self.load_seat_matrix(movie_name, time)
        seat_matrix[row][col] = 2 if new_color == "blue" else 0
        self.save_seat_matrix(movie_name, time, seat_matrix)

    def save_and_return(self, movie_name, time):
        selected_seats = [f"{row * 10 + col + 1}" for row, row_buttons in enumerate(self.seat_buttons) for col, button in enumerate(row_buttons) if button.cget("fg_color") == "blue"]
        
        if not selected_seats:
            messagebox.showinfo("Aviso", "Nenhum assento selecionado para salvar.")
            return
        
        self.save_order(movie_name, time, selected_seats)
        
        # Atualizar matriz de assentos para marcar como ocupados (cinza)
        seat_matrix = self.load_seat_matrix(movie_name, time)
        for row in range(5):
            for col in range(10):
                if self.seat_buttons[row][col].cget("fg_color") == "blue":
                    seat_matrix[row][col] = 1  # Marcar como ocupado

        self.save_seat_matrix(movie_name, time, seat_matrix)
        self.show_movies()

    def show_my_orders(self):
        self.clear_main_frame()

        self.orders_label = CTkLabel(self.main_frame, text="Meus Pedidos", font=("Arial", 20))
        self.orders_label.pack(pady=20)

        self.scrollable_frame = CTkScrollableFrame(self.main_frame, width=800, height=500, orientation='vertical')
        self.scrollable_frame.pack(pady=20, fill="both", expand=True)

        self.inner_frame = CTkFrame(self.scrollable_frame, width=780)
        self.inner_frame.pack(pady=20, padx=20, fill="both", expand=True)

        pedidos_dir = os.path.join(self.base_directory, 'pedidos')
        file_path = os.path.join(pedidos_dir, f'{self.user}_pedidos.txt')

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    cliente, filme, sala, horario, assentos = line.strip().split('!')
                    if cliente == self.user:
                        order_text = f"Filme: {filme}\nSala: {sala}\nHorário: {horario}\nAssentos: {assentos}\n"
                        order_label = CTkLabel(self.inner_frame, text=order_text, font=("Arial", 16))
                        order_label.pack(pady=10, anchor="center")
        else:
            no_orders_label = CTkLabel(self.inner_frame, text="Nenhum pedido encontrado.", font=("Arial", 16))
            no_orders_label.pack(pady=10, anchor="center")

    def clear_seats(self, movie_name):
        seat_matrix = [[0 for _ in range(10)] for _ in range(5)]
        self.save_seat_matrix(movie_name, seat_matrix)
        self.open_movie_page(movie_name)

    def save_seat_matrix(self, movie_name, time, seat_matrix):
        file_path = os.path.join(self.base_directory, f"{movie_name}_{time}_seats.txt")
        with open(file_path, "w") as file:
            for row in seat_matrix:
                file.write("".join(map(str, row)) + "\n")

    def load_seat_matrix(self, movie_name, time):
        file_path = os.path.join(self.base_directory, f"{movie_name}_{time}_seats.txt")
        if not os.path.exists(file_path):
            return [[0 for _ in range(10)] for _ in range(5)]
        with open(file_path, "r") as file:
            return [list(map(int, line.strip())) for line in file]

    def show_my_data(self):
        self.clear_main_frame()
        self.data_label = CTkLabel(self.main_frame, text="Meus Dados", font=("Arial", 20))
        self.data_label.pack(pady=20)
        with open(self.usuarios_file, 'r') as file:
            lines = file.readlines()
            for i in lines:
                user_id, username, password, typeaccount, saldo = i.strip().split(',')
                if username == self.user:
                    break
        self.usrname = CTkLabel(self.main_frame, text=f"Olá, {username}! Seu id de usuário é ({user_id}) e seu tipo de conta é: {typeaccount}\n e você tem {saldo} de saldo.", font=("Arial", 25)).pack(padx=30, pady=70)

    def change_password(self):
        self.clear_main_frame()
        self.password_label = CTkLabel(self.main_frame, text="Alterar Senha", font=("Arial", 20))
        self.password_label.pack(pady=20)
        self.newpasswordl = CTkLabel(self.main_frame, text="Nova Senha:").pack(pady=10)
        self.newpw = CTkEntry(self.main_frame)
        self.newpw.pack(pady=10)
        self.newpasswordb = CTkButton(self.main_frame, width=4, height=8, text="Alterar", command=self.changepassword).pack(pady=10)

    def generate_movie_id(self):
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
            if not os.path.exists('data/filmes.txt'):
                with open('data/filmes.txt', 'w') as file:
                    pass
            with open('data/filmes.txt', 'r') as file:
                lines = file.readlines()
                if not lines:
                    return 1
                else:
                    last_line = lines[-1]
                    last_id = int(last_line.split(',')[0])
                    return last_id + 1
        except Exception as e:
            print(f"Erro ao gerar ID do filme: {e}")
            return None

    def save_movie_data(self, movie_id, movie_name, image_path, movie_time):
        try:
            with open('data/filmes.txt', 'a') as file:
                file.write(f"{movie_id},{movie_name},{image_path},{movie_time}\n")
            print("Dados do filme salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar dados do filme: {e}")

    def add_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png")]
        )
        if file_path:
            try:
                if not os.path.exists('images'):
                    os.makedirs('images')
                file_name = os.path.basename(file_path)
                dest_path = os.path.join('images', file_name)
                with open(file_path, 'rb') as src_file:
                    with open(dest_path, 'wb') as dest_file:
                        dest_file.write(src_file.read())
                self.image_path = dest_path
                print("Imagem adicionada com sucesso!")
            except Exception as e:
                print(f"Erro ao adicionar imagem: {e}")
        else:
            print("Nenhuma imagem foi selecionada.")

    def submit_movie(self):
        movie_name = self.nome_filme_entry.get()
        movie_time = self.horario_entry.get()
        movie_id = self.generate_movie_id()
        
        if movie_name and movie_time and hasattr(self, 'image_path') and movie_id:
            self.save_movie_data(movie_id, movie_name, self.image_path, movie_time)
        else:
            print("Todos os campos devem ser preenchidos e uma imagem deve ser selecionada.")

    def funcionario_properties(self):
        self.clear_main_frame()

        self.funcionario_frame = ctk.CTkFrame(self.main_frame)
        self.funcionario_frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.funcionario_frame, text="Nome do Filme:").pack(pady=5)
        self.nome_filme_entry = ctk.CTkEntry(self.funcionario_frame)
        self.nome_filme_entry.pack(pady=5, padx=10)

        ctk.CTkLabel(self.funcionario_frame, text="Imagem:").pack(pady=5)
        add_image_button = ctk.CTkButton(self.funcionario_frame, text="Adicionar Imagem", command=self.add_image)
        add_image_button.pack(pady=5, padx=10)

        ctk.CTkLabel(self.funcionario_frame, text="Horário:").pack(pady=5)
        self.horario_entry = ctk.CTkEntry(self.funcionario_frame)
        self.horario_entry.pack(pady=5, padx=10)
        self.horario_entry.insert(0, "00:00")

        submit_button = ctk.CTkButton(self.funcionario_frame, text="Salvar Filme", command=self.submit_movie)
        submit_button.pack(pady=20)

    def admin_properties(self):
        self.clear_main_frame()
        title_label = CTkLabel(self.main_frame, text="Funcionários", font=("Arial", 24))
        title_label.pack(pady=10)

        self.users_frame = CTkFrame(self.main_frame)
        self.users_frame.pack(pady=10, padx=15, fill="both", expand=True)

        users = self.read_users_from_file(self.usuarios_file)
        for user_id, user, passw, usertype, saldo in users:
            if usertype == 'Funcionario':
                user_info = f"ID: {user_id}, Usuário: {user}, Tipo: {usertype}"
                user_label = CTkLabel(self.users_frame, text=user_info, font=("Arial", 12), fg_color="#08253D")
                user_label.pack(pady=5)

        # aqui gerencia os funcionários
        manage_frame = CTkFrame(self.main_frame)
        manage_frame.pack(pady=20, padx=16, fill="x")

        manage_title = CTkLabel(manage_frame, text="Gerenciar Funcionários", font=("Arial", 20))
        manage_title.pack(pady=10)

        demitir_label = CTkLabel(manage_frame, text="ID:")
        demitir_label.pack(pady=5)

        self.demitir_entry = CTkEntry(manage_frame)
        self.demitir_entry.pack(pady=5, padx=10)

        demitir_button = CTkButton(manage_frame, text="Demitir", command=self.demitefuncionario)
        demitir_button.pack(pady=10)

    def demitefuncionario(self):
        demitido_id = self.demitir_entry.get()
    
        if not demitido_id:
            ctk.CTkMessagebox.show_info("Erro", "ID do funcionário não fornecido.")
            return
    
        updated_lines = []
        user_found = False

        # ler as linhas do código
        with open(self.usuarios_file, 'r') as file:
            lines = file.readlines()

        # atualizar a linha selecionada
        with open(self.usuarios_file, 'w') as file:
            for line in lines:
                user_id, username, pw, utype, saldo = line.strip().split(',')
                if user_id == demitido_id:
                    utype = 'Usuario'
                    user_found = True
                updated_line = f"{user_id},{username},{pw},{utype},{saldo}\n"
                file.write(updated_line)
    
    def changepassword(self):
        newpassword = self.newpw.get()
  
        if not newpassword:
            ctk.CTkMessagebox.show_info("Erro", "ID do funcionário não fornecido.")
            return
    
        updated_lines = []
        user_found = False

        # de novo lê as linhas do código
        with open(self.usuarios_file, 'r') as file:
            lines = file.readlines()

        # e seleciona a linha correspondente
        with open(self.usuarios_file, 'w') as file:
            for line in lines:
                user_id, username, pw, utype, saldo = line.strip().split(',')
                if user == username:
                    pw = newpassword
                    user_found = True
                updated_line = f"{user_id},{user},{pw},{utype}{saldo}\n"
                file.write(updated_line)

    def read_users_from_file(self, file_path):
        users = []
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    user_data = line.strip().split(",")
                    if len(user_data) == 5:  # tem que ter 5 partes cada linha
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
