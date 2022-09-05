from typing import final
from cone import mydb
from cadastrocliente import Cliente
from cadastroQuarto import cadQuarto
from reserva import ReservaQ
from fim import Final, Acerto


class Menu():
    def men(self, e):
        print('''BIA'S HOTEL''')
        self.e = int(input('''Menu:
        1 - Cadastro Quarto
        2 - Cadastro Cliente
        3 - Reverva
        4 - Acerto de contas
        5 - Resultado final
        Escolha sua opção: '''))
        if e == 1:
            q = cadQuarto
            Menu.men()
        if e == 2:
            c = Cliente
            Menu.men()
        if e == 3:
            r = ReservaQ
            Menu.men()
        if e == 4:
            s = Acerto
            Menu.men()
        if e == 5:
            f = Final
            Menu.men()
            
  
Menu.men()