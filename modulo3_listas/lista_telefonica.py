def main():
    autor = "SEU NOME AQUI"
    print(f"\n*** Lista telefonica v1.0 *** (por {autor})\n")

    # criaçao da lista
    lista_telefonica = []
    
    nome1 = input("nome #1:")
    lista_telefonica.append(nome1)

    nome2 = input("nome #2:")
    lista_telefonica.append(nome2)

    nome3 = input("nome #3:")
    lista_telefonica.append(nome3)

    lista_ordenada = sorted(lista_telefonica)

    print("mostrando lista")
    print


main()