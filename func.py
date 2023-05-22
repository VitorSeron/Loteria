from __future__ import annotations
from random import randint


class Loteria:

    def __init__(self, opcoes: dict, *escolha: int, valores: dict) -> None:
        self.opcoes = opcoes
        self.escolha = escolha
        self.valores = valores
        self.escolha_cliente: int
        self.acertos: int = 0

    def escolher(self) -> int:
        self.escolha_cliente = int(input('Digite sua escolha: '))
        return self.escolha_cliente

    def cabecalho(self, cabecalho: str) -> None:
        print('-' * 40)
        print(cabecalho.center(40).title())
        print('-' * 40)

    def menu(self, opcoes: dict) -> None:
        print('Opções: ')
        for k, v in opcoes.items():
            print(k, '-', v)

    def apostar(self, valores: dict) -> int:
        for k, v in valores.items():
            print(f'{k} números no valor de:'.ljust(
                20, '.'), f'R${v:.2f}'.rjust(15, '.'))
        self.escolha_cliente = self.escolher()
        print(
            f'Você escolheu jogar com {self.escolha_cliente} '
            f'números pelo valor de R${self.valores[self.escolha_cliente]:.2f}.')
        return self.escolha_cliente

    def sortear(self) -> list:
        self.sorteio: list = []
        i = 1
        while i in range(1, 7):
            n = randint(1, 60)
            if n not in self.sorteio:
                self.sorteio.append(n)
                i += 1
            else:
                pass
        self.sorteio.sort()

        return self.sorteio

    def simular(self, n_sorteados: list) -> list:
        return n_sorteados

    def jogo_principal(self, qtd_num: int) -> list:
        print(f'Jogando com {qtd_num}...')
        self.numeros_escolhidos: list = []
        i = 1
        while i in range(1, self.escolha_cliente + 1):
            n = int(input(f'Digite o {i}º número escolhido: '))
            if n >= 1 and n <= 60 and n not in self.numeros_escolhidos:
                self.numeros_escolhidos.append(n)
                i += 1
            else:
                print('Digite um número válido entre 1 e 60.')
        self.numeros_escolhidos.sort()
        print(f'Seus números foram:             {self.numeros_escolhidos}')
        return self.numeros_escolhidos

    def resultado(self, n_escolhidos: list, n_sorteados: list) -> int:
        self.acertos = 0
        self.lista_acertos: list = []
        for n in n_escolhidos:
            if n in n_sorteados:
                self.lista_acertos.append(n)
                self.acertos += 1
        print(f'Os números sorteados foram:     {self.sorteio}')
        if self.lista_acertos == []:
            print(f'Você não acertou nehum número.')
        else:
            print(
                f'Você acertou o(s) número(s) {self.lista_acertos}, totalizando {self.acertos} acerto(s).')
        return self.acertos

    def premios(self, num_acertos: int, valor_premio: int) -> str:
        ganhadores = 0
        quadra = 0.19
        quina = 0.19
        sena = 0.60
        match num_acertos:
            case 4:
                ganhadores = randint(5000, 10000)
                premio = (valor_premio * quadra) / (ganhadores + 1)
                return f'Parabéns, você acertou {self.acertos} números e ganhou um prêmio'\
                    f' de R${premio:.2f}'
            case 5:
                ganhadores = randint(50, 100)
                premio = (valor_premio * quina) / (ganhadores + 1)
                return f'Parabéns, você acertou {self.acertos} númerose ganhou um prêmio'\
                    f' de R${premio:.2f}'
            case 6:
                ganhadores = randint(0, 2)
                premio = (valor_premio * sena) / (ganhadores + 1)
                return f'VOCÊ ACERTOU A MEGA SENA E GANHOU UM PRÊMIO DE R${premio:.2f}!!'
            case other:
                return 'Infelizmente você não ganhou. Mais sorte na próxima vez!'

    def gerar_premio(self) -> int:
        self.premio = randint(20000000, 40000000)
        return self.premio

    def mostrar_premio(self, valor: int) -> int:
        valor = self.premio
        return valor
