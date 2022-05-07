def main():
    autor = "Janderson FFerreira @janderson.fferreira"
    print(f"\n*** Marculina Lyrics v1.0 *** (por {autor})\n")

    # criar string com multiplas linhas = marculina_lyrics com novas linhas
    marculina_lyrics = """
A minha Marculina só me enchia o saco
Gritava buraco e eu fiquei azedo
Me fui pro praiedo me raparo os troco
Mas bebi que nem loco com tudo o chinedo
Borracho e sem dinheiro pra casa de vorta
Meti o pé na porta e me esbarrei c'oa china
Entrei trupicando de ganhá pitoco
E já levei um soco da minha Marculina
    """

    # criar string com multiplas linhas = marculina_lyrics
    marculina_lyrics = """A minha Marculina só me enchia o saco
Gritava buraco e eu fiquei azedo
Me fui pro praiedo me raparo os troco
Mas bebi que nem loco com tudo o chinedo
Borracho e sem dinheiro pra casa de vorta
Meti o pé na porta e me esbarrei c'oa china
Entrei trupicando de ganhá pitoco
E já levei um soco da minha Marculina"""


    # mostrar letra da musica
    print(marculina_lyrics)

    # quebrar marculina_lyrics em palavras (comando: da banana ...)
    palavras_marculina_lyrics = marculina_lyrics.split(" ")

    # identificar os "novas linhas" contra barras
    print(f"\n\nPalavras na Marculina:\n{palavras_marculina_lyrics}")

    # remover as novas linhas do texto => (comando:replace)
    marculina_lyrics_sem_nl = marculina_lyrics.replace("\n", " ")
    # TESTE: experimente  fazer replace ao inves de espaço, sem nada ""

    marculina_palavras_sem_nl = marculina_lyrics_sem_nl.split(" ")
    print(f"\n\nPalavras na Marculina (Sem Nova Linha):\n{marculina_palavras_sem_nl}")
 
    # quebrar a marculina_lyrics em frases / estrofes
    marculina_lyrics_frases = marculina_lyrics.split("\n")
    print(f"\n\nMarculina Frase: {marculina_lyrics_frases}")
    print(f"tipo ==> {type(marculina_lyrics_frases)}")

    # pegar a primeira frase da música (conceito: uso de indice na lista)
    primeira_frase = marculina_lyrics_frases[0]
    print(f"\n\nPrimeira Frase: {primeira_frase}")

    # pegar a segunda frase da música (conceito: uso de indice na lista)
    segunda_frase = marculina_lyrics_frases[1]
    print(f"\n\nSegunda Frase: {segunda_frase}")

    # pegar a última frase da música
    ultima_frase = marculina_lyrics_frases[-1]
    print(f"\n\nPrimeira Frase: {ultima_frase}")


    # Pegar a última frase da música (conceito: slice ou "fatia maior" de lista)
    # OBS: No slice, primeiro índice está dentro, segundo indice não
    duas_primeiras_frases = marculina_lyrics_frases[0:2]
    print(f"\n\nAs duas primeiras frases (listas): {duas_primeiras_frases}")

    # Desafio: Indices negativos (Trazer perguntas)

    # Juntas as duas_primeiras_frases e fazer "voltar" para uma string
    duas_primeiras_frases_texto = " ".join(duas_primeiras_frases)
    print(f"\n\nDuas primeiras frases ageitadas: {duas_primeiras_frases_texto}")

    # pegar duas frases e adicionar ao marculina_lyrics_frases
    marculina_lyrics_frases.append("Não me judia...eu não tô bebendo só mais ou menos")
    marculina_lyrics_frases.append("Eu quero durmi, minha nega agora, me leva pra cama")

    print(f"\n\nMarculina Frase: {marculina_lyrics_frases}")

    # pegar strofe 2 colocar na variavel marculina_lyrics_strofe_2
    marculina_lyrics_strofe_2 = """Parou e ficou falando num tom de piedade:
- Que barbaridade! Quê que deu no meu macho
De chegar borracho pos eu me parpita
Que tu tava nas tipa e bebeu que nem guaxo
Borracho e chateado e a nega falando
As veis quase chorando me olhava e pruguntava:
- Me conta onde tu tava, meu amor que eu não me zango
E onde tu botou o mango a cousa que eu mas gostava"""


    # Quebrar em palavras marculina_lyrics_strofe_2_frases removendo os "nova_linha"
    marculina_lyrics_strofe_2_frases = marculina_lyrics_strofe_2.replace("\n", "").split("\n")
    print(f"\n\nPalavras na Marculina (Strofe #2):\n {marculina_lyrics_strofe_2_frases}")

    # juntar strofe1 + strofe2 colocar na variavel marculina_lyrics_frases
    marculina_lyrics_frases.extend(marculina_lyrics_strofe_2_frases)
    estrofe_1_estrofe_2 = "".join(marculina_lyrics_frases)
    
    print(f"\n\nPalavras na Marculina (Strofe #1+#2):\n {estrofe_1_estrofe_2}")


    print(f"\n\n\n\nEu {autor} já sei trabalhar com listas no python! \o/")
main()
