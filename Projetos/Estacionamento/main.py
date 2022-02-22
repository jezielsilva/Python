import sqlite3, os
os.system('cls')

def sql_create():
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    mycursor.execute
    ("""CREATE TABLE ESTACIONAMENTO( 
    CPF INTEGER NOT NULL PRIMARY KEY,
    NOME TEXT NOT NULL,
    PLACA TEXT NOT NULL,
    DATANASCIMENTO TEXT NOT NULL)""")
    mydb.commit()
    mydb.close()

def create(cpf, nome, placa, datanascimento):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções
    mycursor.execute
    (f"""
    INSERT INTO ESTACIONAMENTO (CPF ,NOME, PLACA, DATANASCIMENTO)
    VALUES({cpf},{nome},{placa},{datanascimento})
    """) 
    mydb.commit()
    mydb.close()


def delete(placa):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções
    mycursor.execute
    (f"""
    DELETE FROM ESTACIONAMENTO WHERE PLACA = {placa}
    """)
    mydb.commit()
    mydb.close()

def update(cpf, nome, placa, datanascimento):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções

    myCursor2 = mydb.cursor()
    myCursor2.execute(f"SELECT CPF ,NOME, DATANASCIMENTO FROM ESTACIONAMENTO WHERE PLACA = '{placa}'") 

    mycursor.execute
    (f"""
    UPDATE ESTACIONAMENTO SET 
    CPF = {cpf},
    NOME = {nome},
    DATANASCIMENTO = {datanascimento}
    WHERE {placa}
    """)
    mydb.commit()
    mydb.close()


def read(placa):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    mycursor.execute("""SELECT * FROM ESTACIONAMENTO""")
    mydb.commit()
    mydb.close()

def backup():
     mydb = sqlite3.connect("bancorecuperado.db") #conecta ou criA
     mybackup = sqlite3.connect("bancodedados.db") #tentativa
     mydb = mybackup
     mycursor = mydb.cursor() #chama funções
     mycursor.execute("""SELECT * FROM ESTACIONAMENTO""")
     mydb.commit()
     mydb.close()
