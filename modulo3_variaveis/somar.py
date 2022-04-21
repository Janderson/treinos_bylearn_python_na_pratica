def main():
    autor = "Janderson Ferreira"
    print(f"\n*** Calculadora de Soma v1.0 *** (por {autor})\n")

    # ENTRADA    
    entrada_valor1 = float(input("informe valor 1: "))
    entrada_valor2 = float(input("informe valor 2: "))

    # PROCESSAMENTO
    soma = entrada_valor1 + entrada_valor2

    
    saida_str = f"resultado da soma é: {soma}"

    # SAIDA
    print(saida_str)

main()