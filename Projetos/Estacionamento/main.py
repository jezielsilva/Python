from ast import While
import sqlite3, os
from datetime import datetime
from datetime import date, time, datetime, timedelta
os.system('cls')

def sql_createCliente():
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    mycursor.execute("""CREATE TABLE "CLIENTE" (
	"NOME"	TEXT NOT NULL,
	"USERID"	NUMERIC NOT NULL PRIMARY KEY AUTOINCREMENT,
	"CPF"	TEXT NOT NULL,
	"PLACA"	TEXT NOT NULL,
	"DATANASCIMENTO"	TEXT NOT NULL)""")
    mydb.commit()

def sql_createValoresDiarios():
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    mycursor.execute("""CREATE TABLE "VALORESDIARIOS" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"DATAENTRADA"	TEXT,
	"DATASAIDA"	TEXT,
	"CPF"	TEXT NOT NULL,
	"PLACA"	TEXT NOT NULL,
	"VALORTOTAL"	TEXT,
	"PAGO"	INTEGER,
	FOREIGN KEY("PLACA") REFERENCES "CLIENTE"("PLACA"),
	FOREIGN KEY("CPF") REFERENCES "CLIENTE"("CPF"))""")
    mydb.commit()

def sql_createFinancas():
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    mycursor.execute("""CREATE TABLE "FINANCAS" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"DATA"	TEXT,
	"VALORTOTAL"	TEXT,
	FOREIGN KEY("DATA") REFERENCES "VALORESDIARIOS"("DATASAIDA"))""")
    mydb.commit()

def sql_createTaxas():
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    mycursor.execute("""CREATE TABLE "TAXAS" (
	"VALORHORA"	TEXT,
	"VALORDIARIA"	TEXT)""")
    mydb.commit()

def validaCpf(cpf):
    # Verifica a formatação do CPF
    while (verificaCpf != True):
        if (r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            verificaCpf = True
        else:
            verificaCpf = False
            cpf = input("Insira um cpf válido: ")
    
    verificaCpf = False
    while (verificaCpf != True):
        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(cpf) != 11 or len(set(cpf)) == 1:
            verificaCpf = False
            cpf = input("Insira um cpf válido: ")
        else:
            verificaCpf = True

    verificaCpf = False
    while (verificaCpf != True):
         # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(cpf[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if cpf[9] != expected_digit:
            verificaCpf = False
            cpf = input("Insira um cpf válido: ")
        else:
            verificaCpf = True

    verificaCpf = False
    while (verificaCpf != True):
        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(cpf[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if cpf[10] != expected_digit:
            return False
            cpf = input("Insira um cpf válido: ")
        else:
            verificaCpf = True
    return cpf

def validaPlaca(placa):
    while placa.upper() != 'X':
        contLetra = 0
        contNum = 0
        #Verifica se a placa contém 7 caracteres
        if len(placa) == 7:
            #Verificar se a posição dos caracteres está correta, ou seja, letras e números no seu devido lugar.
            for i, item in enumerate(placa):
                #isalpha = manipulação de string
                if item.isalpha() and (i == 0 or i == 1 or i == 2 or i ==4):
                    contLetra += 1
                elif item.isdigit() and (i == 3 or i == 4 or i == 5 or i == 6):
                    contNum += 1

            if (contLetra == 3 and contNum == 4) or (contLetra == 4 and contNum == 3):
                print('Placa válida!')
                break;                    
            else:
                print('')
                placa = input('Placa inválida. Por favor, insira uma placa válida: ')
                
        else:
            placa = input('Placa inválida. Por favor, insira uma placa válida: ')
    return placa

def validaNascimento(datanascimento):
    verificaNascimento = False
    while verificaNascimento == False: 
        if(len(datanascimento) == 8):
            datanascimento = datetime.strptime(datanascimento, "%d/%m/%Y")
            verificaNascimento = True
            break
        else:
            datanascimento = input("Data informada está incorreta, digite somente os números e data completa: ")
            verificaNascimento = False
    return datanascimento

def formataNome(nome):
    nome = nome.upper()
    return nome

def criarCliente(cpf, nome, placa, datanascimento):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções

    verificaCpf = False
    
    nome = formataNome(nome)
    cpf = validaCpf(cpf)
    placa = validaPlaca(placa)
    datanascimento = validaNascimento(datanascimento)

    mycursor.execute
    (f"""
    INSERT INTO CLIENTE (CPF ,NOME, PLACA, DATANASCIMENTO)
    VALUES({cpf},{nome},{placa},{datanascimento})
    """) 
    mydb.commit()
    mydb.close()

def deletarCliente(placa, cpf):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções
    placa = validaPlaca(placa)
    cpf = validaCpf(cpf)

    mycursor.execute
    (f"""
    DELETE FROM CLIENTE WHERE PLACA = {placa} and CPF = {cpf}
    """)
    mydb.commit()
    mydb.close()

def deletarCarro(id, cpf, placa):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções
    placa = validaPlaca(placa)
    cpf = validaCpf(cpf)

    mycursor.execute
    (f"""
    DELETE FROM VALORESDIARIOS WHERE PLACA = {placa}, CPF = {cpf} AND ID = {id}
    """)
    mydb.commit()
    mydb.close()

def atualizarCliente(cpf, nome, placa, datanascimento):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções

    nome = formataNome(nome)
    cpf = validaCpf(cpf)
    placa = validaPlaca(placa)
    datanascimento = validaNascimento(datanascimento)

    myCursor2 = mydb.cursor()
    myCursor2.execute(f"SELECT CPF ,NOME, DATANASCIMENTO FROM CLIENTE WHERE PLACA = '{placa}'") 

    mycursor.execute
    (f"""
    UPDATE CLIENTE SET 
    CPF = {cpf},
    NOME = {nome},
    DATANASCIMENTO = {datanascimento}
    WHERE {placa}
    """)
    mydb.commit()
    mydb.close()

def buscarCliente(id_usuario, cpf):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções

    cpf = validaCpf(cpf)

    mycursor.execute("""SELECT * FROM CLIENTE WHERE USER_ID = {id_usuario} and CPF = {cpf}""")
    mydb.commit()
    mydb.close()

def atualizarPrecoHora(valor_hora):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções

    myCursor2 = mydb.cursor()
    myCursor2.execute(f"SELECT VALOR_HORA FROM PRECOS") 

    mycursor.execute
    (f"""
    UPDATE PRECOS SET 
    VALOR_HORA = {valor_hora}
    """)
    mydb.commit()
    mydb.close()

def atualizarPrecoDiaria(valor_diaria):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou cria
    mycursor = mydb.cursor() #chama funções

    myCursor2 = mydb.cursor()
    myCursor2.execute(f"SELECT VALOR_DIARIA FROM PRECOS") 

    mycursor.execute
    (f"""
    UPDATE PRECOS SET 
    VALOR_DIARIA = {valor_diaria}
    """)
    mydb.commit()
    mydb.close()

def inserirCarro(cpf, data_entrada, placa):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    data_entrada = datetime.now()
    cpf = validaCpf(cpf)
    placa = validaPlaca(placa)
    
    mycursor.execute
    (f"""
    INSERT INTO VALORES_DIARIOS (DATA_ENTRADA, CPF, PAGO)
    VALUES({data_entrada},{cpf},{0})
    """) 
    mydb.commit()
    mydb.close()

def atualizarCarro(cpf, data_entrada, placa):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    data_entrada = datetime.now()
    cpf = validaCpf(cpf)
    placa = validaPlaca(placa)

    mycursor.execute
    (f"""
    UPDATE VALORES_DIARIOS SET
    DATA_ENTRADA = {data_entrada}, 
    CPF = {cpf}, 
    PLACA = {placa}
    WHERE PLACA = {placa}
    """) 
    mydb.commit()
    mydb.close()

def calcularTotal(id_usuario, cpf):
    mydb = sqlite3.connect("bancodedados.db") #conecta ou criA
    mycursor = mydb.cursor() #chama funções
    cpf = validaCpf(cpf)
    data_entrada = mycursor.execute("""SELECT DATA_ENTRADA FROM VALORES_DIARIOS WHERE ID = {id_usuario} AND CPF = {cpf}""")
    data_saida = mycursor.execute("""SELECT DATA_SAIDA FROM VALORES_DIARIOS WHERE ID = {id_usuario} AND CPF = {cpf}""")
    taxa = mycursor.execute("""SELECT VALOR_HORA FROM TAXAS""")
    tempoTotal = data_saida - data_entrada
    valor_total = taxa * tempoTotal
    mycursor.execute
    (f"""
    UPDATE VALORES_DIARIOS SET(DATA_ENTRADA ,DATA_SAIDA, CPF, VALOR_TOTAL, PAGO)
    VALUES({data_entrada},{data_saida},{cpf},{valor_total}, {1} WHERE ID = {id_usuario})
    """) 
    mydb.commit()
    mydb.close()

def backup():
     mydb = sqlite3.connect("bancorecuperado.db") #conecta ou cria
     mybackup = sqlite3.connect("bancodedados.db") #tentativa
     mydb = mybackup
     mycursor = mydb.cursor() #chama funções
     mycursor.execute("""SELECT * FROM ESTACIONAMENTO""")
     mydb.commit()
     mydb.close()

def relatorio():
    return True

def createBanco():
    sql_createCliente()
    sql_createValoresDiarios()
    sql_createFinancas()
    sql_createTaxas()

def funcaoEscolhida(opcao):
    switcher = {
        1: criarCliente(),
        2: deletarCliente(),
        3: atualizarCliente(),
        4: buscarCliente(),
        5: inserirCarro(),
        6: atualizarCarro(),
        7: deletarCarro(),
        8: relatorio(),
        9: calcularTotal(),
        0: exit()
    }


def inicio():
    print(">> ESTACIONAMENTO <<")
    print("Escolha a opção desejada: ")
    print("1 - CADASTRAR CLIENTE")
    print("2 - DELETAR CLIENTE")
    print("3 - ATUALIZAR DADOS DO CLIENTE")
    print("4 - BUSCAR CLIENTE")
    print("5 - CADASTRAR VEÍCULO")
    print("6 - ATUALIZAR DADOS DO VEÍCULO")
    print("7 - DELETAR VEÍCULO")
    print("8 - RELATÓRIO")
    print("9 - EMISSÃO DE COBRANÇA")
    print("0 - SAIR")
    opcao = input("Digite a opção escolhida: ")
    funcaoEscolhida(opcao)


