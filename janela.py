import tkinter as tk
import pymysql
import pymysql.cursors


class JanelaLogin():
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
            print(resultado_login)

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
        tk.Button(text="Cadastro",bg="orange2",width=10).grid(row=3,column=0,padx=10)
        tk.Button(text="Visualizar cadasotrs",bg="white",width=15).grid(row=4,column=0,columnspan=2)

        self.root.mainloop()

JanelaLogin()