from time import sleep

DEBUG = True

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
        # Se estiver no modo de Depuração mostrar nome do professor
        for professor_item in QUERY_PROFESSORES:
            professor = professor_item.get("professor")
            if DEBUG:
                print(f"\n| -> Professor: {professor} {professor_item.get('ausente')}")

            # Criar lógica condicional saber se alunos devem ser avisados
            # Variavel devo_avisar_alunos
            devo_avisar_alunos = professor_item.get("ausente")

            # Criar logica condicional para saber se alunos ja foram avisados anteriormente
            # Variavel devo_avisar_alunos
            alunos_do_prof_ja_avisados = professor_item.get("avisado")

            condicao_para_envio = devo_avisar_alunos and not alunos_do_prof_ja_avisados
            if DEBUG:
                print(
                    f"| -> CONDIÇÃO({condicao_para_envio}): devo_avisar_alunos: {devo_avisar_alunos} "
                    f"alunos_do_prof_ja_avisados: {alunos_do_prof_ja_avisados}"
                )

            # Criar logica condicional para saber se alunos ja foram avisados anteriormente
            # Variavel devo_avisar_alunos
            if condicao_para_envio:
                # Adicionar professor a tabela de alunos avisados
                professor_item["avisado"] = True

                # Criar loop para pegar alunos do professor
                for aluno in professor_item.get("alunos"):

                    if DEBUG:
                        print(
                            f"| ---> Avisando professorAluno: {professor} alunos: {aluno}"
                        )

                    msg_text = mensagem_template.format(
                        aluno=aluno, professor=professor
                    )
                    print(f"Enviando SMS para {aluno}, msg ===> ({msg_text})")
        print(f"fim da interacao ({loopid}), aguardando...")
        sleep(2)


main()
