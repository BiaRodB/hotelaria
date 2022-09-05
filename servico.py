from cone import mydb
from cadastroQuarto import cadQuarto
class Servico: #classes serviços
    def __init__(self,tiposerv,nomeserv,custo_serv, idservico):
        self.tiposerv = tiposerv
        self.nomeserv = nomeserv
        self.custo_serv = custo_serv
        self.idservico = idservico

s = Servico
q = cadQuarto
q.numero
q.valorq
s.idservico = input('ID do Serviço: ')
s.tiposerv = input('Tipo de serviço (1- passar, 2 - lavar ou 3 - combo): ')
s.nomeserv = input('Nome do serviço: ')
s.custo_serv = input('Custo do serviço: ')

mycursor = mydb.cursor()
sql = "INSERT INTO servico (idservico, tiposerv, nomeServico, custo_serv) VALUES ("+s.idservico+","+s.tiposerv+",'"+s.nomeserv+"',"+s.custo_serv+")"
mycursor.execute(sql)
mydb.commit()
mycursor == True
print('inserido com sucesso')

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM servico")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)