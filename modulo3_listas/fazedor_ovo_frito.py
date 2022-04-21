from time import sleep

def fritar():
    print("fritando aguarde...")
    sleep(2.5)


def main():
    autor = "SEU NOME AQUI"
    print(f"\n*** Fazedor de OVO v1.0 *** (por {autor})\n")

    ingrediente1 = "OVO"
    ingrediente2 = "Azeite de Oliva"
    ingredientes = [ingrediente1, ingrediente2]

    ingredienteX = input("Informe seu ingrediente X:")
    ingredientes.append(ingredienteX)

    receita_str = ", ".join(ingredientes)
    print(f"ingredienteis => ({receita_str}) estão na panela")
    
    fritar()

    print("Feito!")


main()