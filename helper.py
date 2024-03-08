class Helper:
    @staticmethod
    def helpMusicDuration():
        print("caso não saiba apenas pressione enter ou digite 'não', 'nao' ou 'no") 
        print("exemplo esperado '2m23s' aquilo q vem antes de 'm' são minutos, 's' segundos, 'h' horas")
        print("caso a faixa tem 34 segundos deveria ser '34s")
        print("caso a faixa tenha 22 minutos deveria ficar '22m'")
    
    @staticmethod
    def helpAnotation():
        print('podemos guardar 3 informações na anotação, tempo, tipo e anotação, nenhuma delas é obrigatória')
        print('exemplo técnico " <tempo> | <tipo> | <comentario> "')
        print('exemplo técnico2 " <comentario> "')
        print('exemplo técnico3 " <tempo> | <tipo>  "')
        print('exemplo pratico1 " 2m23s | 1 | lembrar de eliminar as vozes, aumentar a bateria e brincar com efeitos "')
        print('exemplo pratico2 " 4m46s | loop  "')
        print('exemplo pratico1 " mashup | primeira metade grave forte médio médio -> depois da parte calma usar a voz "')
        print('<tempo> -> 2m23s padrão do tempo temos as letras "h" , "m", "s" para indicar horas, minutos, segundos')
        print('<tipo> -> pode ser nome da categoria ou numero do indice, caso tenha dúvida das categorias existentes e os indices digite (help listaDicas). útil para categorizar as anotações.')
        print('caso queira anotar somente o tipo exemplo "mashup" sem sinalizar tempo ou algum comentario escreva "*t" ou "*tipo* exemplo "mashup*t"')
        print('caso se esqueça ele irá salvar como se fosse um comentario, quando visualizar o bloco da musica não vai mudar muito, a informação vai continuar la, mas quando pesquisar por categoria dentro da biblioteca, não vai encontrar')
        print('<comentario> por fim o comentario, é basicamente um texto, não tem limite de caracteres')
        print('')