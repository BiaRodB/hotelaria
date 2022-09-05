from cone import mydb
#from enum import Enum

class cadQuarto(): #cadastro do quarto
    def __init__(self, numero, tipoquart, valorq, itens, frigobar):
        self.numero = numero
        self.tipoquart = tipoquart
        self.valorq = valorq
        self.itens = itens
        self.frigobar = frigobar


q = cadQuarto

q.numero = input('Numero do quarto: ')
q.tipoquart = input(''''Tipo do quarto:  
    1 - Simples (1 cama)
    2 - Duplo (2 camas)
    3 - Casal
    4 - Luxo 
    Escolher tipo de Quarto: ''') #escolher o tipo do quarto
q.valorq = input('Qual o valor do quarto: ')
q.itens = input("Quais são os itens que tem no quarto: ")

mycursor = mydb.cursor()
sql = "INSERT INTO cadastroQuarto (numero, tipoQuarto, valorQuarto, itens) VALUES ("+q.numero+","+q.tipoquart+","+q.valorq+",'"+q.itens+"')"
mycursor.execute(sql)
mydb.commit()
mycursor == True
print('inserido com sucesso')


print('Cadastro Quarto:')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cadastroQuarto")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#from enum import Enum

class frigo(): #coisas que está no frigobar
   def __init__(self, quantidade, tipop, valorp):
       self.tipop = tipop
       self.quantidade = quantidade
       self.valorp = valorp
   
   def simples_simple(self):
    if q.tipoquart == 1:
        fb.tipop = 'água'
        fb.quantidade = 10
        fb.valorp = 5
   def quarto_duplo():
    if q.tipoquart == 2:
        fb.tipop = 'água, suco'
        fb.quantidade = 15
        fb.valorp = 5
   def quarto_casal():
     if q.tipoquart == 3:
        fb.tipop ='água, suco, refri'
        fb.quantidade = 25
        fb.valorp = 5
   def quarto_luxo():
    if q.tipoquart == 4:
        fb.tipop = 'água, suco, café, refri'
        fb.quantidade = 30
        fb.valorp = 5


fb = frigo
fb.quantidade = input("digite quantidade de itens no figobar: ")
fb.valorp = input('valor dos produtos: ')
fb.tipop = input('Tipo de produto no frigobar: ')
q = cadQuarto
q.numero
q.valorq



mycursor = mydb.cursor()
sql = "INSERT INTO frigobar (idQua, produto, preco, quantidade) VALUES ("+q.numero+",'"+fb.tipop+"',"+fb.valorp+","+fb.quantidade+")"
mycursor.execute(sql)
mydb.commit()
mycursor == True
print('inserido com sucesso')

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM frigobar")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)