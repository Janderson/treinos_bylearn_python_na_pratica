def imc():
    # Desafio 2.3 = IMC
    # https://www.tuasaude.com/calculadora/imc/

    autor = "SEU NOME AQUI"
    print(f"\n*** Cálculo do IMC v1.0 *** (por {autor})\n")
    
    # ENTRADA
    altura = float(input("altura (cm): ")) / 100
    peso_kg = float(input("peso (kg): "))
    # Experimentar ==> altura em Metros

    IMC = peso_kg / (altura * altura)
    imc_fmt = IMC
    print(f"IMC ==> {imc_fmt:.1f}")


imc()