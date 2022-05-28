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

    # criar template do sms 
    # ==> SEU CÓDIGO AQUI

    # + Criar uma variável 'repetir_loop' para controle de loops
    # + Criar um loop que executa x vezes
    # ==> SEU CÓDIGO AQUI

        # Buscar todos os professores da querie de professores
        # ==> SEU CÓDIGO AQUI

            # Se estiver no modo de depuração mostrar nome do professor
            # ==> SEU CÓDIGO AQUI

            # Criar lógica condicional saber se alunos devem ser avisados
            # Variavel devo_avisar_alunos
            # ==> SEU CÓDIGO AQUI

            # Criar logica condicional para:
            # saber se alunos ja foram avisados anteriormente
            # Variavel devo_avisar_alunos
            # ==> SEU CÓDIGO AQUI

            # Criar lógica condição para saber se deve enviar sms para professor
            # + lógica deve saber se alunos já foram avisados anteriormente
            # variavel condição_envio
            # ==> SEU CÓDIGO AQUI

            # Mostrar debug da condicao_para_envio
            # ==> SEU CÓDIGO AQUI

            # Só enviar se condicao_para_envio=True
            # ==> SEU CÓDIGO AQUI

                # Adicionar professor a tabela de alunos avisados
                # ==> SEU CÓDIGO AQUI

                # Criar loop para pegar alunos do professor
                # ==> SEU CÓDIGO AQUI

                    # depuração -> nome do professor+aluno que será enviado
                    # ==> SEU CÓDIGO AQUI

                    # montar template da msg, mudando nome do professor + aluno
                    # ==> SEU CÓDIGO AQUI

                    # Executar envio -> mostrar print
                    # ==> SEU CÓDIGO AQUI

        # print de fim da iteração + sleep
        # ==> SEU CÓDIGO AQUI


main()
