# import o comando getpass do módulo getpass

um_texto_grande = """
What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""


def main():
    # Mostrar o titulo e o autor (tome propriedade do código)
    autor = "SEU NOME AQUI"
    print(f"\n*** Contador de Palavras *** (por {autor})\n")

    print("Olha o texto")
    palavra_para_contar = input("Informe a palavra que quer contar: ").strip()

    texto_quebrado = um_texto_grande.split(" ")

    contador = 0
    for palavra in texto_quebrado:
        print(palavra)
        if palavra.lower() == palavra_para_contar.lower():
            print(f"achei ->{contador}")
            contador+=1

    print(f"total de palavras no texto: {contador}")


main()