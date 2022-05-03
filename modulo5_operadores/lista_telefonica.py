def main():
    # Mostrar o titulo e o autor (tome propriedade do código)
    autor = "SEU NOME AQUI"
    print(f"\n*** Lista telefonica v2.0 *** (por {autor})\n")

    # criaçao da lista
    lista_telefonica = []
    
    # Ler o nome1 digitado pelo usuario (comando=>input)
    # + Adicionar na lista
    nome1 = input("nome #1:")
    lista_telefonica.append(nome1)

    # Ler o nome2 digitado pelo usuario 
    # + detectar se já existe na lista (comando=>if)
    # + adicionar na lista
    nome2 = input("nome #2:")
    if nome2 in lista_telefonica:
        print(f"{nome2} já existe na lista, nao adicionado")
    else:
        lista_telefonica.append(nome2)

    # Ler o nome3 digitado pelo usuario
    # + detectar se já existe na lista 
    # + adicionar na lista (comando=>append)
    nome3 = input("nome #3:")
    if nome3 in lista_telefonica:
        print(f"{nome3} já existe na lista, nao adicionado")
    else:
        lista_telefonica.append(nome3)

    # Ordenar a lista telefonica 
    # mostrar para o usuario a lista final (string format)
    lista_ordenada = sorted(lista_telefonica)
    print(f"lista final: {lista_ordenada}")


main()