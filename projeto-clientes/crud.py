from conexao import conectar

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            idade INTEGER
        )
    """)
    
    conn.commit()
    conn.close()

def inserir_cliente(nome, email, idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO clientes (nome, email, idade)
    VALUES (?, ?, ?)
    """, (nome, email, idade))

    conn.commit()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    conn.close()
    return clientes

def atualizar_cliente(id_cliente, nome, email, idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE clientes
    SET nome = ?, email = ?, idade = ?
    WHERE id = ?
    """, (nome, email, idade, id_cliente))

    conn.commit()
    conn.close()

def excluir_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM clientes WHERE id = ?",
        (id_cliente,)
    )

    conn.commit()
    conn.close()
    