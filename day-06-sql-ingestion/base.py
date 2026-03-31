import sqlite3

def criar_banco_pronto():
    conn = sqlite3.connect('corporativo.db')
    cursor = conn.cursor()

    # Criando tabelas
    cursor.execute("CREATE TABLE IF NOT EXISTS departamentos (id INTEGER PRIMARY KEY, nome TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios (id INTEGER PRIMARY KEY, nome TEXT, cargo TEXT, salario REAL, dept_id INTEGER)")

    # Inserindo dados prontos
    depts = [(1, 'TI'), (2, 'RH'), (3, 'Financeiro')]
    funcs = [
        (101, 'Suzana', 'Data Engineer', 12000.0, 1),
        (102, 'Joao', 'Analista de RH', 5000.0, 2),
        (103, 'Maria', 'Gerente Financeiro', 15000.0, 3),
        (104, 'Carlos', 'Software Engineer', 11000.0, 1)
    ]

    cursor.executemany("INSERT OR REPLACE INTO departamentos VALUES (?,?)", depts)
    cursor.executemany("INSERT OR REPLACE INTO funcionarios VALUES (?,?,?,?,?)", funcs)

    conn.commit()
    conn.close()
    print("✅ Banco 'corporativo.db' gerado com sucesso!")

if __name__ == "__main__":
    criar_banco_pronto()