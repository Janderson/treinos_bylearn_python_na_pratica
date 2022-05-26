from time import sleep

DEBUG = False

QUERY_PROFESSORES = [
    {
        "professor": "Rose",
        "ausente": False,
        "alunos": ["Rosangela", "Rosane"],
        "avisado": False
    },
    {
        "professor": "Roberto",
        "ausente": False,
        "alunos": ["Roberval", "Rogerio", "Romario"],
        "avisado": False
    },
    {
        "professor": "Jose",
        "ausente": True,
        "alunos": ["João", "Joaquim"],
        "avisado": False
    }
]


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
        for professor_item in QUERY_PROFESSORES:
            professor = professor_item.get("professor")

            # Se estiver no modo de depuração mostrar nome do professor
            if DEBUG:
                print(f"\n| -> Professor: {professor} "
                      f"{professor_item.get('ausente')}")

            # Criar lógica condicional saber se alunos devem ser avisados
            # Variavel devo_avisar_alunos
            devo_avisar_alunos = professor_item.get("ausente")

            # Criar logica condicional para:
            # saber se alunos ja foram avisados anteriormente
            # Variavel devo_avisar_alunos
            alunos_do_prof_ja_avisados = professor_item.get("avisado")

            # Criar condição para saber se deve enviar sms para professor
            # + lógica deve saber se alunos já foram avisados anteriormente
            condicao_para_envio = all([
                devo_avisar_alunos,
                not alunos_do_prof_ja_avisados])

            # Mostrar debug da condicao_para_envio
            if DEBUG:
                print(
                    f"| -> CONDIÇÃO({condicao_para_envio}): "
                    f"devo_avisar_alunos: {devo_avisar_alunos} "
                    f"alunos_do_prof_ja_avisados: {alunos_do_prof_ja_avisados}"
                )

            if condicao_para_envio:
                # Adicionar professor a tabela de alunos avisados
                professor_item["avisado"] = True

                # Criar loop para pegar alunos do professor
                for aluno in professor_item.get("alunos"):

                    if DEBUG:
                        print(
                            f"| ---> Avisando professorAluno: {professor} "
                            f"alunos: {aluno}"
                        )
                    # montar template da msg
                    msg_text = mensagem_template.format(
                        aluno=aluno, professor=professor
                    )

                    # Executar envio -> mostrar print
                    print(f"Enviando SMS para {aluno}, msg ===> ({msg_text})")

        # print de fim da iteração + sleep
        print(f"fim da interacao ({loopid}), aguardando...")
        sleep(2)


main()
