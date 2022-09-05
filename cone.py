import mysql.connector # importar a conexão com o mysql
mydb =  mysql.connector.connect( #criando a conexão com o mysql
            host ='localhost',
            user = 'root',
            password = '',
            database = 'hotel' )   