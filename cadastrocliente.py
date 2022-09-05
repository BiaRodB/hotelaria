from cone import mydb

class Cliente: #cadastro do cliente
    def __init__(self, nome,contato,cpf,email):
      try:
        self.nome = nome
        self.contato = contato
        self.cpf = cpf #ou documento
        self.email = email
      except(NameError, ValueError):
            print('Invalido, tente novamente.')

c = Cliente #chamando a função cliente
 


c.nome = input('Nome: ')
c.contato = input('Contato: ')
c.cpf = input('Documento: ')
c.email = input('Email: ')
mycursor = mydb.cursor() #conexão com o mysql

sql = "INSERT INTO cadastrocliente (nome, contato, documento, email ) VALUES ('"+c.nome+"',"+c.contato+","+c.cpf+",'"+c.email+"')"
mycursor.execute(sql)
mydb.commit()
mycursor == True
print('inserido com sucesso')

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cadastrocliente")
myresult = mycursor.fetchall()
for x in myresult:
   print(x)