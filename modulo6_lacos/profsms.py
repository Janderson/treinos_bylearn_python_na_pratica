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


    mensagem_template = "Ola {aluno}, seu professor {professor} não comparecerá a aula hoje"

    repetir_loop = 2
    for i in range(repetir_loop):
        for professor in QUERY_PROFESSORES:
            if DEBUG: print(f"\n| -> Professor: {professor}")

            devo_avisar_alunos = all([esta_ausente 
                                      for prof, esta_ausente in QUERY_PROFESSORES_AUSENTES 
                                      if prof == professor])
            alunos_do_prof_ja_avisados = (professor in TABELA_ALUNOS_AVISADOS)

            if DEBUG: print(f"| -> devo_avisar_alunos: {devo_avisar_alunos} "
                            f"alunos_do_prof_ja_avisados: {alunos_do_prof_ja_avisados}")

            if devo_avisar_alunos and not alunos_do_prof_ja_avisados:
                if DEBUG: print(f"| --> Professor {professor} ==> irá faltar, avisar alunos")
                TABELA_ALUNOS_AVISADOS.append(professor)
            
                for query_item in QUERY_ALUNOS_PROFESSORES:
                    professor_aluno, alunos = query_item[0], query_item[1]
                    if DEBUG: print(f"| ---> ProfessorAluno: {professor_aluno} alunos: {alunos}")
                    if professor_aluno == professor:
                        for aluno in alunos:
                            msg_text = mensagem_template.format(aluno=aluno, professor=professor)
                            print(f"Enviando SMS para {aluno}, msg ===> ({msg_text})")


main()


def historia():
    # Repetir um loop simples algumas vezes, comando range
    for numero in range(10):
        print(f"Loop {numero}")


historia()
