import customtkinter as ctk


ctk.set_appearance_mode("light")
# Função para mostrar a tela de login
def show_login():
    register_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

# Função para mostrar a tela de registro
def show_register():
    login_frame.pack_forget()
    register_frame.pack(fill="both", expand=True)

# Inicializa a janela principal
app = ctk.CTk()
app.geometry("400x300")
app.title("Login e Registro com customtkinter")

# Cria o frame de login
login_frame = ctk.CTkFrame(app)

# Conteúdo do frame de login
login_label = ctk.CTkLabel(login_frame, text="Tela de Login")
login_label.pack(pady=10)

username_label = ctk.CTkLabel(login_frame, text="Username:")
username_label.pack(pady=5)
username_entry = ctk.CTkEntry(login_frame)
username_entry.pack(pady=5)

password_label = ctk.CTkLabel(login_frame, text="Password:")
password_label.pack(pady=5)
password_entry = ctk.CTkEntry(login_frame, show="*")
password_entry.pack(pady=5)

login_button = ctk.CTkButton(login_frame, text="Login")
login_button.pack(pady=10)

register_button = ctk.CTkButton(login_frame, text="Cadastrar", command=show_register)
register_button.pack(pady=10)

# Cria o frame de registro
register_frame = ctk.CTkFrame(app)

# Conteúdo do frame de registro
register_label = ctk.CTkLabel(register_frame, text="Tela de Registro")
register_label.pack(pady=10)

new_username_label = ctk.CTkLabel(register_frame, text="Novo Username:")
new_username_label.pack(pady=5)
new_username_entry = ctk.CTkEntry(register_frame)
new_username_entry.pack(pady=5)

new_password_label = ctk.CTkLabel(register_frame, text="Novo Password:")
new_password_label.pack(pady=5)
new_password_entry = ctk.CTkEntry(register_frame, show="*")
new_password_entry.pack(pady=5)

confirm_password_label = ctk.CTkLabel(register_frame, text="Confirmar Password:")
confirm_password_label.pack(pady=5)
confirm_password_entry = ctk.CTkEntry(register_frame, show="*")
confirm_password_entry.pack(pady=5)

create_account_button = ctk.CTkButton(register_frame, text="Criar Conta")
create_account_button.pack(pady=10)

back_to_login_button = ctk.CTkButton(register_frame, text="Voltar ao Login", command=show_login)
back_to_login_button.pack(pady=10)

# Mostra o frame inicial (login)
show_login()

# Executa a aplicação
app.mainloop()
