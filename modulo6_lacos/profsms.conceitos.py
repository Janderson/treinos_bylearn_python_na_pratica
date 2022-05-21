def main():

    # Crie um loop até 10 print o loop numerico
    #
    for numero in range(10):
        print(f"iterar sobre um loop numerico {numero}")

    # iterar em um lista de objetos
    professores = ["Jose", "Joaquim"]
    for professor in professores:
        print(f"iterar sobre um objeto {professor}")

    # logica condiconal
    debug = True
    if debug:
        print("Estou em depuração....")

    # logica de estar em uma lista
    professor_esta_na_lista = "Joaquim" in professores
    print(f"Professor esta na lista {professor_esta_na_lista}")

    # todas as regras de uma lista sao verdadeiras - comando all
    avisar_professor = True
    professor_esta_na_lista = True
    lista_regras = [avisar_professor, professor_esta_na_lista, debug]
    todas_sao_verdadeiras = all(lista_regras)
    print(f"\n\nTodas as regras sao verdadeiras: {todas_sao_verdadeiras}")

    # loop dentro de uma lista
    professor = "Jose"

    # query professores (PODE COPIAR E COLAR PARA NÃO DAR DOR DE CABEÇA)
    query_professores = [["Rose", False], ["Roberto", False], ["Jose", True]]

    # saber se o professor X, Y, Z estará ausente
    # compreensão de listas - list comprehension
    prof_esta_ausente = [
        esta_ausente for prof, esta_ausente in query_professores if prof == professor
    ]
    print(f"prof {professor} esta ausente {prof_esta_ausente}")

    nomes_dos_ausentes = [
        prof for prof, esta_ausente in query_professores if esta_ausente
    ]
    print(f"nomes dos ausentes: {nomes_dos_ausentes}")

    # É o mesmo que o anterior, num formato mais padrão
    so_ausentes = []
    for prof, esta_ausente in query_professores:
        if prof == professor:
            so_ausentes.append(esta_ausente)
    print(f"só professores ausentes: {so_ausentes}")

    # extrair duas variaveis de uma lista, em uma linha só
    item1, item2 = ["Valor do item 1", "Valor do item 2"]
    print(f"Extrair duas variaveis de uma lista: \nitem1={item1}\nitem2={item2}")

    # for com continue
    professores = ["Tais", "Tiago", "Tomas", "Tailor"]
    prof_vai_faltar = "Tais"
    for index, prof in enumerate(professores):
        if prof_vai_faltar != prof:
            print(f"{prof} não é o professor que eu quero")
            continue

        if index >= 2:
            print("chega..")
            break

        print(f"===> esse professor eu quero: {prof}")


main()
