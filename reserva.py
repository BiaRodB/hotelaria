from datetime import datetime
from cadastroQuarto import cadQuarto
from cone import mydb
class ReservaQ: #classe para reservar o quarto
    def __init__(self, idCliente, datai:datetime.date, dataf:datetime.date, numQ, status, idreserva): 
        self.idreserva =idreserva
        self.idcliente = idCliente  #informações necessaria para a reserva do quarto: Id do cliente
        self.datai = datai          #data que o cliente comparecera para da entrada no quarto
        self.dataf = dataf          # data prevista para o cliente sair do quarto   
        self.numQ = numQ            #numero do quarto  
        self.status = status        # Status do quarto: ocupado ou vago
        

dadosr = ReservaQ #chamando a classe reserva
q = cadQuarto
q.tipoquart

#adicionado as informações por meio do input
dadosr.idreserva = input('ID da reserva: ')
dadosr.idcliente = input('ID do Cliente: ') 
dadosr.datai = input('Data Inicial: ')    
dadosr.dataf = input('Data Final: ')  
q.tipoquart = input('''Tipo do quarto: 
    1 - Simples (1 cama)
    2 - Duplo (2 camas)
    3 - Casal
    4 - Luxo 
    Escolha: ''')
dadosr.numQ =  input('Numero do quarto: ')
dadosr.status = input('O quarto está: ')

mycursor = mydb.cursor()
sql = "INSERT INTO reserva (idreserva, idcliente, dataI, dataF, tipoQ, numQ,status ) VALUES ("+dadosr.idreserva+","+dadosr.idcliente+","+dadosr.datai+","+dadosr.dataf+","+q.tipoquart+","+q.numero+""+dadosr.status+")"
mycursor.execute(sql)
mydb.commit()
mycursor == True
print('inserido com sucesso')

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM reserva")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)