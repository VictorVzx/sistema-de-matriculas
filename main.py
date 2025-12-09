import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT UNIQUE,
    telefone TEXT
)""")


print("------Matricular Alunos------")

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu numero de telefone: ")

dados_do_aluno = (nome, email, telefone)

cursor.execute("""
INSERT INTO alunos(nome, email, telefone)
VALUES (?, ?, ?)               
""", dados_do_aluno)


conexao.commit()