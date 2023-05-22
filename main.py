from func import *


opcoes = {
    1: 'Apostar',
    2: 'Simular jogo',
    3: 'Listar sorteios anteriores',
    4: 'Verificar valor das apostas',
    5: 'Conferir o valor do prêmio',
    0: 'Sair'
}

valores = {
    6: 4.50,
    7: 31.50,
    8: 126,
    9: 378,
    10: 945,
    11: 2079,
    12: 4158,
    13: 7722,
    14: 13513.50,
    15: 22522.50
}


if __name__ == "__main__":
    s1 = Loteria(opcoes, valores=valores)
    s1.cabecalho('Bem-vindo')
    premio = s1.gerar_premio()
    s1.escolha_cliente = 1
    while s1.escolha_cliente != 0:
        s1.menu(opcoes)
        s1.escolher()
        match s1.escolha_cliente:
            case 0:
                print('Volte sempre!')
            case 1:
                n = s1.resultado(s1.jogo_principal(
                    s1.apostar(valores)), s1.sortear())
                print(s1.premios(n, premio))
                s1.escolha_cliente = 0
            case 2:
                print('Simulação do sorteio: ')
                print(s1.simular(s1.sortear()))
            case 3:
                pass
            case 4:
                for k, v in valores.items():
                    print(f'{k} números no valor de:'.ljust(
                        20, '.'), f'R${v:.2f}'.rjust(15, '.'))
            case 5:
                print(
                    f'O valor do prêmio total é de R${s1.mostrar_premio(premio):.2f}')
            case other:
                print('Opção inválida. Escolha uma das opções.')
