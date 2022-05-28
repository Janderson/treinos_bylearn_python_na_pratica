from time import sleep

DEBUG = True

QUERY_PROFESSORES = [
    {
        "professor": "Rose",
        "ausente": False,
        "alunos": ["Rosangela", "Rosane"],
        "alunos_avisados": False
    },
    {
        "professor": "Roberto",
        "ausente": False,
        "alunos": ["Roberval", "Rogerio", "Romario"],
        "alunos_avisados": False
    },
    {
        "professor": "Jose",
        "ausente": True,
        "alunos": ["João", "Joaquim"],
        "alunos_avisados": False
    }
]


def main():
    autor = "Janderson"
    print(f"\n*** Prof SMS v1.1 *** (por {autor})\n")

    # criar template do sms
    template_sms = (
        "Olá {aluno} seu professor {professor} "
        "não comparecerá a aula hoje, desculpe o transtorno"
    )

    # + Criar uma variável 'repetir_loop' para controle de loops
    # + Criar um loop que executa x vezes
    repetir_loop = 5
    for loopid in range(repetir_loop):
        print(f"|> INICIO INTERAÇÃO: {loopid}")
        # Buscar todos os professores da querie de professores
        for professor in QUERY_PROFESSORES:
            # Se estiver no modo de depuração mostrar nome do professor
            professor_nome = professor.get("professor")
            if DEBUG:
                print(f"|-> {professor_nome}")

            # Criar lógica condicional saber se alunos devem ser avisados
            # ou se professor estará ausente
            # Variavel devo_avisar_alunos
            devo_avisar_alunos = professor.get("ausente")

            # Criar logica condicional para:
            # |--> Saber se alunos ja foram avisados anteriormente
            # |--> Variável alunos_do_prof_ja_avisados

            alunos_prof_ja_avisados = professor.get("alunos_avisados")

            # Criar lógica condição para saber se envia sms para professor
            # |--> Lógica deve saber se alunos já foram avisados anteriormente
            # |--> Váriavel condicao_envio
            condicao_envio = devo_avisar_alunos and not alunos_prof_ja_avisados

            # Mostrar debug (ou depuração) da condicao_para_envio
            if DEBUG:
                print(
                    f"!--> condicao_envio -> "
                    f"Avisar alunos? {devo_avisar_alunos} "
                    f"Alunos avisados? {alunos_prof_ja_avisados} "
                    f"enviar [{condicao_envio}]"
                )

            # Só enviar se condicao_para_envio=True
            if condicao_envio:

                # fazer UPDATE do professor a tabela de alunos avisados
                # para não enviar novamente na próxima interação
                professor["alunos_avisados"] = True

                # Criar loop para pegar alunos do professor
                for aluno in professor.get("alunos"):

                    # depuração -> nome do professor+aluno que será enviado
                    if DEBUG:
                        print(f"|---> enviando sms para aluno: {aluno}")

                    # montar template da msg, mudando
                    # nome do professor e nome do aluno
                    sms_texto = template_sms.format(professor=professor_nome,
                                                    aluno=aluno)

                    # Executar envio -> comando: print
                    print(f"\n|====> SMS: {sms_texto}\n\n")

        # print de fim da iteração + sleep
        print(f"|> FIM INTERAÇÃO: {loopid}")
        sleep(3.5)
        # ==> SEU CÓDIGO AQUI


main()
