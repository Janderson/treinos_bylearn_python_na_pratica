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

    mensagem_template = (
        "Ola {aluno}, seu professor {professor} " 
        "não comparecerá a aula hoje"
    )

    # + Criar uma variável 'repetir_loop' para controle de loops
    # + Criar um loop que executa x vezes
    repetir_loop = 5
    for loopid in range(repetir_loop):

        # Buscar todos os professores da querie de professores
        # Se estiver no modo de Depuração mostrar nome do professor
        for professor in QUERY_PROFESSORES:
            if DEBUG:
                print(f"\n| -> Professor: {professor}")

            # Criar lógica condicional saber se alunos devem ser avisados
            # Variavel devo_avisar_alunos
            devo_avisar_alunos = all([
                    esta_ausente
                                      for prof, esta_ausente in QUERY_PROFESSORES_AUSENTES 
                    if prof == professor
                ])

            # Criar logica condicional para saber se alunos ja foram avisados anteriormente
            # Variavel devo_avisar_alunos
            alunos_do_prof_ja_avisados = professor in TABELA_ALUNOS_AVISADOS

            if DEBUG:
                print(
                    f"| -> devo_avisar_alunos: {devo_avisar_alunos} "
                    f"alunos_do_prof_ja_avisados: {alunos_do_prof_ja_avisados}"
                )

            # Criar logica condicional para saber se alunos ja foram avisados anteriormente
            # Variavel devo_avisar_alunos
            if devo_avisar_alunos and not alunos_do_prof_ja_avisados:
                if DEBUG:
                    print(f"| --> Professor {professor} ==> irá faltar, avisar alunos")

                # Adicionar professor a tabela de alunos avisados
                TABELA_ALUNOS_AVISADOS.append(professor)
            
                # Criar loop para pegar alunos do professor
                for query_item in QUERY_ALUNOS_PROFESSORES:

                    # extrair professor_aluno e alunos na mesma linha
                    professor_aluno, alunos = query_item[0], query_item[1]

                    if DEBUG:
                        print(
                            f"| ---> ProfessorAluno: {professor_aluno} alunos: {alunos}"
                        )

                    if professor_aluno != professor:
                        continue

                    # Print MSG gerado apartir da template na parte superior
                    for aluno in alunos:
                        msg_text = mensagem_template.format(
                            aluno=aluno, professor=professor
                        )
                        print(f"Enviando SMS para {aluno}, msg ===> ({msg_text})")
        print(f"fim da interacao ({loopid}), aguardando...")
        sleep(2)


main()
