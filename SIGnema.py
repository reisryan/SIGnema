import customtkinter as ctk

class SIGnemaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("SIGnema")
        ctk.set_appearance_mode("light")

        # Cria os frames
        self.login_frame = ctk.CTkFrame(self)
        self.register_frame = ctk.CTkFrame(self)

        # Inicializa os componentes da tela de login
        self.create_login_screen()

        # Inicializa os componentes da tela de registro
        self.create_register_screen()

        # Mostra a tela de login inicialmente
        self.show_login()

    def show_login(self):
        self.register_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def show_register(self):
        self.login_frame.pack_forget()
        self.register_frame.pack(fill="both", expand=True)

    def create_login_screen(self):
        login_label = ctk.CTkLabel(self.login_frame, text="SIGnema")
        login_label.pack(pady=10)

        username_label = ctk.CTkLabel(self.login_frame, text="Login:")
        username_label.pack(pady=5)
        username_entry = ctk.CTkEntry(self.login_frame)
        username_entry.pack(pady=5)

        password_label = ctk.CTkLabel(self.login_frame, text="Senha:")
        password_label.pack(pady=5)
        password_entry = ctk.CTkEntry(self.login_frame, show="*")
        password_entry.pack(pady=5)
        global p, u
        p, u = password_entry.get(), username_entry.get()
        login_button = ctk.CTkButton(self.login_frame, text="Login", fg_color="#CA2E2E", hover_color="#CA3E3E", command=self.login_account)
        login_button.pack(pady=10)

        register_button = ctk.CTkButton(self.login_frame, text="Cadastrar", command=self.show_register, fg_color="#000000", hover_color="#000011")
        register_button.pack(pady=10)

    def create_register_screen(self):
        register_label = ctk.CTkLabel(self.register_frame, text="Tela de Registro")
        register_label.pack(pady=10)

        new_username_label = ctk.CTkLabel(self.register_frame, text="Login:")
        new_username_label.pack(pady=5)
        new_username_entry = ctk.CTkEntry(self.register_frame)
        new_username_entry.pack(pady=5)

        new_password_label = ctk.CTkLabel(self.register_frame, text="Senha:")
        new_password_label.pack(pady=5)
        new_password_entry = ctk.CTkEntry(self.register_frame, show="*")
        new_password_entry.pack(pady=5)

        confirm_password_label = ctk.CTkLabel(self.register_frame, text="Confirmar Senha:")
        confirm_password_label.pack(pady=5)
        confirm_password_entry = ctk.CTkEntry(self.register_frame, show="*")
        confirm_password_entry.pack(pady=5)

        create_account_button = ctk.CTkButton(self.register_frame, text="Criar Conta", fg_color="#000000", hover_color="#000011")
        create_account_button.pack(pady=10)

        back_to_login_button = ctk.CTkButton(self.register_frame, text="Já possui conta?", command=self.show_login, fg_color="#000000", hover_color="#000022")
        back_to_login_button.pack(pady=10)

    def login_account(self):
        with open("data/usuarios.txt", 'r') as file:
            lines = file.readlines()
            for i in lines:
                if u == (i.split(","))[1] and p == (i.split(","))[2]:
                    print("ok", u, p)
                else:
                    print((i.split(","))[1], ((i.split(","))[2]), u, p)

    def create_account(self):
        if new_username_entry.get() != null and new_password_entry.get() == confirm_password_entry.get():
            with open("data/usuarios.txt", 'r') as file:
                lines = file.readlines()
                id = len(lines) + 1
            with open("data/usuarios.txt", 'w') as file:
                file.write(id+","+new_username_entry.get()+","+new_password_entry.get()+","+ "aqui tipo" + "\n")
        else:
            self.textbox = ctk.CTkTextbox(master=self, width=400, corner_radius=0)
            self.textbox.grid(row=0, column=0, sticky="nsew")
            self.textbox.insert("0.0", "Erro - faltam dados!\n" * 50)

if __name__ == "__main__":
    app = SIGnemaApp()
    app.mainloop()
