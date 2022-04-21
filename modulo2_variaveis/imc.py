def imc():
    # Desafio 2.3 = IMC
    # https://www.tuasaude.com/calculadora/imc/

    autor = "SEU NOME AQUI"
    print(f"\n*** Cálculo do IMC v1.0 *** (por {autor})\n")
    
    # ENTRADA    
    altura = float(input("altura (cm): "))
    peso_kg = float(input("peso (kg): "))

    IMC = peso_kg / (altura * altura)
    imc_fmt = IMC*100*100
    print(f"IMC ==> {imc_fmt:.1f}")


imc()