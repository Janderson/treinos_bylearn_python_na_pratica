def imc():
    # https://www.tuasaude.com/calculadora/imc/
    # http://www.unimed.coop.br/pct/index.jsp?cd_canal=49146&cd_secao=-1&cd_materia=299005

    autor = "SEU NOME AQUI"
    print(f"\n*** Cálculo do IMC v1.0 *** (por {autor})\n")
    
    # ENTRADA
    altura = float(input("altura (cm): ")) / 100
    peso_kg = float(input("peso (kg): "))
    # Experimentar ==> altura em Metros

    # CÁLCULO - IMC
    IMC = peso_kg / (altura * altura)
    imc_fmt = IMC

    # CALCULO DA FAIXA
    if IMC < 18.5:
        faixa = "Magreza"
    elif (IMC >= 18.5) and (IMC < 24.9):
        faixa = "Saudável"
    elif (IMC >= 25) and (IMC < 29.9):
        faixa = "Sobrepeso"
    elif (IMC >= 30) and (IMC < 34.9):
        faixa = "Obesidade Grau I"
    elif (IMC >= 35) and (IMC < 39.9):
        faixa = "Obesidade Grau II (severa)"
    elif (IMC >= 40):
        faixa = "Obesidade Grau III (morbidade)"
    else:
        faixa = "fora de qualquer faixa"

    # SAÍDA
    print(f"IMC ==> {imc_fmt:.1f} -> faixa: ({faixa})")


imc()