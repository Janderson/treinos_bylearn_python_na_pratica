# import o comando getpass do módulo getpass
from getpass import getpass


def main():
    # Mostrar o titulo e o autor (tome propriedade do código)
    autor = "SEU NOME AQUI"
    print(f"\n*** Jogo de Adivinhação v1.0 *** (por {autor})\n")

    # Pege o número SECRETO informado pelo usuário
    numero = getpass("[JOGADOR 1] -> diga número (que o mágico tentará acertar):")

    # Salve o numero de tentativas
    tentativas = 0

    # Crie um loop infinito
    while True:
        palpite = input("[JOGADOR 2] -> informe o número:")
        # crie um braço de decisao se o palpite for MAIOR que o numero
        if palpite > numero:
            tentativas+=1
            print("Vish, chutou muito alto!")
        # crie um braço de decisao se o palpite for MENOR que o numero
        elif palpite < numero:
            tentativas+=1
            print("Não, mais alto!")
        # crie um braço de decisao se o palpite ESTÁ CORRETO
        # Saia do loop
        elif palpite == numero:
            tentativas+=1
            print("Boa \o/ ! Acertou !!! ")
            break

    # mostra o número de tentativas 
    print(f"Você acertou em {tentativas} tentativas")

main()