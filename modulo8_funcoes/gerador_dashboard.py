import csv
from copy import deepcopy

def extrair_dados_alocacoes():
    # Arquivo
    # Banco de Dados
    # Fila
    # Topico Kafka
    # Excel
    ASSESSORES_ALOCACOES = [
        {
            "assessor": "Lucas",
            "fundo": "PLAZA",
            "qtd": 1,
            "valor_cota": 100
        },
        {
            "assessor": "Lucas",
            "fundo": "PLAZA",
            "qtd": 3,
            "valor_cota": 100
        },
        {
            "assessor": "Roberto",
            "fundo": "PLAZA",
            "qtd": 3,
            "valor_cota": 100
        },
        {
            "assessor": "Janderson",
            "fundo": "PLAZA",
            "qtd": 8,
            "valor_cota": 100
        }
    ]
    return ASSESSORES_ALOCACOES


def extrair_dados_times():
    ASSESSOR_TIMES = [
        {"assessor": "Janderson", "time": "Warriors"},
        {"assessor": "Lucas", "time": "Champions"},
        {"assessor": "Roberto", "time": "Champions"}]
    return ASSESSOR_TIMES


def encontrar_assessor_em_time(assessor, times):
    it = filter(lambda it: it["assessor"] == assessor, times)
    return list(it)[0]


def juntar_times_alocacoes(times, alocacoes):
    times_alocacoes = deepcopy(alocacoes)
    for item in times_alocacoes:
        assessor = item["assessor"]
        time_item = encontrar_assessor_em_time(assessor, times)
        print(f"{assessor} --> {time_item} -> {item}")
        item.update(time_item)
        #alocacoes[]
    
    for item in times_alocacoes:
        print(f"item==> {item}")
    return times_alocacoes


def filtrar_alocacao_time(time, times_alocacoes):
    items = filter(lambda it: it["time"] == time, times_alocacoes)
    return list(items)


def distinct_times(times):
    nomes = [t["time"] for t in times]
    diferentes = set(nomes)
    nomes = list(diferentes)
    print(f"nomes:{nomes}")
    return nomes

def soma_quantidades(times_alocacoes):
    quantidades = [it["qtd"] for it in times_alocacoes]
    return sum(quantidades, start=0)


def calcular_alocacao_time(times, times_alocacoes):
    time_somas = []
    for time in distinct_times(times):
        so_alocacoes_dotime = filtrar_alocacao_time(time, times_alocacoes)
        soma_qtd = soma_quantidades(so_alocacoes_dotime)
        print(f"alocacoes_time: {time}->{so_alocacoes_dotime} ===> {soma_qtd}")
        soma_item = {"time": time, "soma": soma_qtd}
        time_somas.append(soma_item)
    return time_somas


# Testes/Treinos ==> Salvar em Json
# Testes/Treinos ==> Salvar em CSV usando pandas
def mandar_para_arquivo(times_alocacoes):
    with open("banco_dados.txt", "w") as txt_file:
        txt_file.write(str(times_alocacoes))
        

def main():
    autor = "Janderson"
    print(f"\n*** Gerador Dashboard v1.0 *** (por {autor})\n")
    # conceito ETL = Extrair ==> Transformar ==> Carregar
    # conceito pipeline => cada etapa, pega o seu resultado e entrega para a próxima

    # Etapa Extrair
    alocacoes = extrair_dados_alocacoes()
    times = extrair_dados_times()

    # Etapa Transformar
    times_alocacoes = juntar_times_alocacoes(times,
                                             alocacoes)

    time_somas = calcular_alocacao_time(times, times_alocacoes)

    # Etapa Carregar
    mandar_para_arquivo(time_somas)

    # Clean Code
    # Função que fazem apenas 1 coisa
    # conceito pipeline => cada etapa, pega o seu resultado e entrega para a próxima





main()