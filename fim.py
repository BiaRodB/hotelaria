from cone import mydb
from reserva import ReservaQ
from cadastroQuarto import cadQuarto, frigo
from cadastrocliente import Cliente


class Final:
    def __init__(self, datasaida, numQuarto,custoTotal):
        self.datasaida = datasaida
        self.numQuarto = numQuarto
        self.custoTotal = custoTotal

class Acerto(Final):
  def __init__(self,valorquar, frib, quant, servc,multa,pagou,func):    
    self.valorquar = valorquar
    self.frib = frib
    self.quant = quant
    self.servc = servc
    self.multa = multa
    self.pagou = pagou
    self.func = func

'''
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
        fb.valorp = 5'''


fb = frigo
fb.quantidade
fb.valorp
q = cadQuarto
q.numero
q.valorq

fa = Final
fa.custoTotal
fa.datasaida 

a = Acerto
a.multa
a.valorquar
a.frib
a.servc
a.pagou
a.func

dadosr = ReservaQ
c = Cliente
c.cpf
mycursor = mydb.cursor()
sql = "INSERT INTO frigobar (idQua, produto, preco, quantidade) VALUES ("+q.numero+",'"+fb.tipop+"',"+fb.valorp+","+fb.quantidade+")"
mycursor.execute(sql)
mydb.commit()
mycursor == True
print('inserido com sucesso')

fa.numQuarto = input('Número do quarto: ')
fa.datasaida = input('Data da Saida: ')
a.func = input('Funcionario responsável: ')
a.pagou = input('Sim ou Não: ')

mycursor = mydb.cursor()
sql = "INSERT INTO datasaida (idquarto, datasaida) VALUES ("+q.numero+","+fa.datasaida+")"
mycursor.execute(sql)
mydb.commit()
mycursor == True
print('inserido com sucesso')

if  dadosr.dataf > fa.datasaida:
    a.multa = a.valorq * 0.1
    a.resu = a.valorq * a.multa
    print(f'Você recebeu a diaria com multa foi: {a.resu}')
    a.custoTotal = q.valorq + a.valorquar + a.resu + (fb.quantidade + fb.valorp)
else:
    a.custoTotal = q.valorq + a.valorquar + (fb.quantidade + fb.valorp)


mycursor = mydb.cursor()
sql = "INSERT INTO saida (multa, custototal, idcliente, numeroq, pagou, funcioranioRe ) VALUES ("+a.multa+","+fa.custoTotal+","+c.cpf+",'"+a.pagou+"','"+a.func+"')"
mycursor.execute(sql)
mydb.commit()
mycursor == True
print('inserido com sucesso')

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cadastrocliente")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)