from time import sleep

DEBUG = False

QUERY_PROFESSORES = ["Jose", "Roberto", "Rose"]

QUERY_PROFESSORES_AUSENTES = [
    ["Rose",    False],
    ["Roberto", False], 
    ["Jose",    True]
]

QUERY_ALUNOS_PROFESSORES = [
    ["Rose",     ["Rosangela", "Rosane"]], 
    ["Roberto",  ["Roberval", "Rogerio", "Romario"]],
    ["Jose",     ["João", "Joaquim"]]
]

TABELA_ALUNOS_AVISADOS = []

TABELA_SMS_ENVIADOS = []


def main():
    autor = "Janderson"
    print(f"\n*** Prof SMS v1.0 *** (por {autor})\n")

    # criar mensagem de template

    # + Criar uma variável 'repetir_loop' para controle de loops
    # + Criar um loop que executa x vezes

        # Buscar todos os professores da querie de professores
        # Se estiver no modo de Depuração mostrar nome do professor

            # Criar lógica condicional saber se alunos devem ser avisados
            # Variavel devo_avisar_alunos


            # Criar logica condicional para saber se alunos ja foram avisados anteriormente
            # Variavel devo_avisar_alunos


            # Criar logica condicional para saber se alunos ja foram avisados anteriormente
            # Variavel devo_avisar_alunos


                # Adicionar professor a tabela de alunos avisados
            
                # Criar loop para pegar alunos do professor


                    # extrair professor_aluno e alunos na mesma linha

                    # Print MSG gerado apartir da template na parte superior


main()
