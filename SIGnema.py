import subprocess
import customtkinter as ctk
import tkinter as tk
import os

class SIGnemaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("SIGnema")
        ctk.set_appearance_mode("light")

        # Diretório base do script
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(self.base_dir, "data")
        self.usuarios_file = os.path.join(self.data_dir, "usuarios.txt")
        self.pagina_principal_script = os.path.join(self.base_dir, "paginaprincipal.py")

        if not os.path.exists(self.usuarios_file):
            os.makedirs(self.data_dir, exist_ok=True)
            with open(self.usuarios_file, 'w') as file:
                pass

        
        self.login_frame = ctk.CTkFrame(self)
        self.register_frame = ctk.CTkFrame(self)

        # Inicializa os componentes da tela de login
        self.create_login_screen()

        # Inicializa os componentes da tela de registro
        self.create_register_screen()

        # Inicializa o rótulo de mensagem
        self.message_label = ctk.CTkLabel(self, width=0, height=0, text="")
        self.message_label.pack()

        # Mostra a tela de login inicialmente
        self.show_login()

    def clear_message(self):
        self.message_label.configure(text="", width=0, height=0)

    def show_login(self):
        self.clear_message()
        self.register_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def show_register(self):
        self.clear_message()
        self.login_frame.pack_forget()
        self.register_frame.pack(fill="both", expand=True)

    def create_login_screen(self):
        ctk.CTkLabel(self.login_frame, text="SIGnema").pack(pady=10)

        self.username_entry = ctk.CTkEntry(self.login_frame)
        ctk.CTkLabel(self.login_frame, text="Login:").pack(pady=5)
        self.username_entry.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self.login_frame, show="*")
        ctk.CTkLabel(self.login_frame, text="Senha:").pack(pady=5)
        self.password_entry.pack(pady=5)

        login_button = ctk.CTkButton(self.login_frame, text="Login", fg_color="#CA2E2E", hover_color="#CA3E3E", command=self.login_account)
        login_button.pack(pady=10)

        register_button = ctk.CTkButton(self.login_frame, text="Cadastrar", command=self.show_register, fg_color="#000000", hover_color="#000011")
        register_button.pack(pady=10)

    def create_register_screen(self):
        ctk.CTkLabel(self.register_frame, text="Tela de Registro").pack(pady=10)

        self.new_username_entry = ctk.CTkEntry(self.register_frame)
        ctk.CTkLabel(self.register_frame, text="Login:").pack(pady=5)
        self.new_username_entry.pack(pady=5)

        self.new_password_entry = ctk.CTkEntry(self.register_frame, show="*")
        ctk.CTkLabel(self.register_frame, text="Senha:").pack(pady=5)
        self.new_password_entry.pack(pady=5)

        self.confirm_password_entry = ctk.CTkEntry(self.register_frame, show="*")
        ctk.CTkLabel(self.register_frame, text="Confirmar Senha:").pack(pady=5)
        self.confirm_password_entry.pack(pady=5)

        # Criar e exibir o seletor de tipo de conta
        self.typecommon = ctk.StringVar(value="Usuario")
        self.typeaccount = ctk.CTkOptionMenu(self.register_frame, fg_color="black", button_color="red", button_hover_color="red", values=["Usuario", "Funcionario", "Gerente"], variable=self.typecommon)
        self.typeaccount.pack(pady=10)

        create_account_button = ctk.CTkButton(self.register_frame, text="Criar Conta", fg_color="#000000", hover_color="#000011", command=self.create_account)
        create_account_button.pack(pady=10)

        back_to_login_button = ctk.CTkButton(self.register_frame, text="Já possui conta?", command=self.show_login, fg_color="#000000", hover_color="#000022")
        back_to_login_button.pack(pady=10)

    def login_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open(self.usuarios_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                user_id, user, passw, usertype = line.strip().split(",")
                if username == user and password == passw:
                    self.show_message("Login realizado com sucesso", "success")
                    # Use lambda para passar os parâmetros corretamente
                    self.after(2900, lambda: self.abrir_pagina_principal(user, usertype))
                    return
        self.show_message("Usuário ou senha incorretos", "error")

    def abrir_pagina_principal(self, user, usertype):
        self.destroy()
        # Use subprocess.run para executar o comando com parâmetros
        subprocess.run(["python", self.pagina_principal_script, user, usertype])

    def create_account(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        account_type = self.typecommon.get()

        if new_username and new_password and new_password == confirm_password:
            with open(self.usuarios_file, 'r') as file:
                lines = file.readlines()
                user_id = len(lines) + 1

            with open(self.usuarios_file, 'a') as file:
                file.write(f"{user_id},{new_username},{new_password},{account_type}\n")
            self.show_message("Conta criada com sucesso", "success")
            self.show_login()
        else:
            self.show_message("Erro - Faltam dados ou senhas não coincidem", "error")

    def show_message(self, message, message_type):
        if message_type == "success":
            self.message_label.configure(text=message, width=10, height=25, fg_color="green")
        else:
            self.message_label.configure(text=message, width=10, height=25, fg_color="red")

if __name__ == "__main__":
    app = SIGnemaApp()
    app.mainloop()
