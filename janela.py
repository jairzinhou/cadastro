import tkinter as tk
from tkinter import messagebox
import pymysql
import pymysql.cursors

class Janela_autenticado():
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Admin")
        self.root.geometry("500x500")

        self.root.mainloop()

class JanelaLogin():
    def cadastro(self):
        self.root=tk.Toplevel()
        self.root.title("Cadastro")

        tk.Label(self.root,text="Cadastrar Usuário").grid(row=0,column=0,columnspan=2,pady=5)

        tk.Label(self.root,text="Usuario").grid(row=1,column=0)
        self.login_cadastro = tk.Entry(self.root)
        self.login_cadastro.grid(row=1,column=1)

        tk.Label(self.root,text="Senha").grid(row=2,column=0)
        self.senha_cadastro = tk.Entry(self.root)
        self.senha_cadastro.grid(row=2,column=1)

        tk.Label(self.root,text="Chave de segurança").grid(row=3,column=0,padx=5)
        self.chave_seguranca = tk.Entry(self.root)
        self.chave_seguranca.grid(row=3,column=1,padx=5,pady=5)

        tk.Button(self.root,text="Cadastrar",width=10).grid(row=4,column=0,pady=20)

        self.root.mainloop()

    def VerficaLogin(self):
        autenticado = False
        user_master = False
        
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print("erro ao conectar com o banco de dados")

        usuario = self.login.get()
        senha = self.senha.get()

        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM cadastros WHERE nome=%s AND senha=%s",(usuario,senha))
            resultado_login = cursor.fetchone()
            if resultado_login:
                if resultado_login["nivel"] == 2:
                    user_master = True
                    autenticado=True
                else:
                    user_master = False
                    autenticado = True
                    
        if not autenticado:
            messagebox.showinfo("login","usuario nao atenticado")
        else:
            self.root.destroy()
            if user_master:
                Janela_autenticado()
        

    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Login")

        tk.Label(self.root,text="Login").grid(row=0,column=0,columnspan=2)

        tk.Label(self.root,text="Usuario:").grid(row=1,column=0)
        self.login=tk.Entry(self.root)
        self.login.grid(row=1,column=1,padx=5,pady=5)

        tk.Label(self.root,text="Senha:").grid(row=2,column=0)
        self.senha=tk.Entry(self.root,show="*")
        self.senha.grid(row=2,column=1,padx=5,pady=5)

        tk.Button(text="Login",bg="green2",width=10,command=self.VerficaLogin).grid(row=3,column=1,pady=10)
        tk.Button(text="Cadastro",bg="orange2",width=10,command=self.cadastro).grid(row=3,column=0,padx=10)
        tk.Button(text="Visualizar cadastros",bg="white",width=15).grid(row=4,column=0,columnspan=2)

        self.root.mainloop()

JanelaLogin()