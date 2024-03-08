# Faz uma pasta 📂 pra mixar entradas e uma pasta 📂 pros mashup
# Os efeitos eo loop vc vai saber a hora certa de usar basta vc confiar em você mesmo
# Quando tiver já na última música de entrada já pode usar pro mashup mas não esquece de preparar a música q vai encaixar no mashup antes da última música acabar de entrada acabar blz



import os
from helper import Helper
from datetime import datetime, timedelta
from typing import Iterable

class Musica:
    typeNotations = ['hotkey', 'transition', 'mashup', 'loop', 'starts']

    def __init__(self, nome, timeMusic = None) -> None:
        self.nome = nome
        self.timeMusic:timedelta = timeMusic
        self.anotations:Iterable[str] = []

        self.indexMaxInitNotation = 0
    
    def saveMusic(self):
        headerzinho = f'{self.nome}'
        if self.timeMusic != None:
            headerzinho += f' - {self.timeMusic}'

        headerAnotation = '** Anotações! **'
        bodyAnotation = [f'    *{anotation}'for anotation in self.anotations]
        fullAnotations = [headerAnotation] + bodyAnotation

        linesTxt = [headerzinho, ''] + fullAnotations
        
        with open(f'{self.nome}.txt', 'w') as txt:
            txt.write('\n'.join(linesTxt))

    def loadFromTxt(self, file_path):
        with open(file_path, 'r') as txt:
            lines = txt.readlines()
        
        header = lines[0].strip()
        if '-' in header:
            nome, time_str = header.split(' - ')
            horas, minutos, segundos = map(int, time_str.split(':'))
            self.timeMusic = timedelta(hours=horas, minutes=minutos, seconds=segundos)
        else:
            nome = header
            self.timeMusic = None
        self.nome = nome
        
        # Processa as anotações
        self.anotations = []
        in_anotations_section = False
        for line in lines[1:]:  # Ignora o cabeçalho já processado
            if '** Anotações! **' in line:
                in_anotations_section = True
                continue
            if in_anotations_section:
                # Remove espaços e o caractere '*' antes de adicionar à lista de anotações
                anotation = line.strip().lstrip('*')
                self.anotations.append(anotation)

    def setTimeMusic(self, segundos = 0, minutos = 0, horas = 0):
        self.timeMusic = timedelta( seconds=segundos, minutes=minutos,  hours=horas)
        return self.timeMusic
    
    def showNotationIndex(self):
        strRetorno = '\n'.join([f'{index} | {typeNot}' for index , typeNot in enumerate(self.typeNotations)])
        print(strRetorno)
        return strRetorno

    def showNotations(self, withIndex = True):
        if withIndex:
            strRetorno = '\n'.join([f'{index}.| {notation}' for index , notation in enumerate(self.anotations)])
        else:
            strRetorno = '\n'.join([f'{notation}' for  notation in self.anotations])
        print(strRetorno)
        return strRetorno




    def insertNotationMusic(self, notation:str = None, tipo:str = None, time = None):
        completeNotation = ''


        if time != None: 
            minuto = time.get('minutos', 0)
            segundos = time.get('segundos', 0)       

            while segundos >= 60:
                segundos = segundos - 60
                minuto = minuto + 1

            if segundos < 10:
                segundos = f'0{segundos}'
            completeNotation += f'|{minuto}:{segundos}'

        if tipo != None:
            if isinstance(tipo, int):
                tipoDaNotacao = self.typeNotations[tipo]
            else:
                tipoDaNotacao = tipo          

            completeNotation += f'|{tipoDaNotacao} '

        normalizeSpaces = self.normalizeTxt(completeNotation)

        completeNotation += f'{normalizeSpaces}| {notation}'     


        self.anotations.append(completeNotation)

    def normalizeTxt(self, str):
        diference = self.indexMaxInitNotation - len(str) 
        if diference < 0:
            self.indexMaxInitNotation = len(str) 
            self.updateAllIndex()
            return ''
        else:
            return ' ' * diference

    def updateAllIndex(self):
        updatedNotations = []
        for notation in self.anotations:
            splited = notation.split('|')
            notationPure = splited[-1]
            resto = '|'.join(splited[0:-1])
            
            normalizeSpaces = self.normalizeTxt(resto)
            notation = f'{resto}{normalizeSpaces}| {notationPure}'     
            updatedNotations.append(notation)
        self.anotations = updatedNotations

        pass



# Example!

# manual = Musica('Manual - rosy braids')
# manual.setTimeMusic(minutos=4, segundos=55)
# manual.insertNotationMusic('primeiro latido',time={'segundos':30} ) 
# manual.insertNotationMusic('virada beat e cantoria começa',4,time={'segundos':30} )
# manual.insertNotationMusic('latido e beat brabo', 'loop/hotkey', time={'minutos':4 , 'segundos':6 })  
# manual.insertNotationMusic('e fala baixo que o inimigo pode te ouvir', 'hotkey', time={'minutos':3 , 'segundos':40 })
# manual.showNotations()

# manual.saveMusic()

from time import sleep

class djNoterAnimations:
    def introducaoAnimation(self):
        djNoterAnimation = ['', 'd', 'dj', 'djN', 'djNo', 'djNot', 'djNote', 'djNoter ', 'DjNoter -']
        djNoterKarAnimation = ['dJnOTER - b', 'DjNoter - by:', 'DjNoter - by: k', 'djNoter - by: ka', 'DjNoter - by: kar'] 
        djKarLoading = ['djNoter - by: kar.', 'djNoter - by: kar..', 'djNoter - by: kar..' ]
        djKarMusicAnimation = ['DJNOTER ~ by: karM', 'DjNoter - by: karMu', 'DjNoter - by: karMu', 'DjNoter - by: karMus', 'DjNoter - by: karMus', 'DjNoter - by: karMusi','DjNoter - by: karMusic', 'DjNoter - by: karMusic.']
        
        timesLoading = djKarLoading * 2
        
        txtPresentationAnimation1 = djNoterAnimation + djNoterKarAnimation + timesLoading + djKarMusicAnimation
    
        for txt in txtPresentationAnimation1:
            print(txt)
            sleep(0.1)    

    def __init__(self) -> None:
        self.introducaoAnimation()

class djNoterKarmusic(djNoterAnimations):
    def __init__(self):
        self.musicas = []
        self.carregarMusicas()
        self.introducaoAnimation()
        self.menuPrincipal()

    def carregarMusicas(self):
        for arquivo in os.listdir('.'):
            if arquivo.endswith('.txt'):
                with open(arquivo, 'r') as f:
                    nome = f.readline().strip()
                    self.musicas.append(Musica(nome))


    def menuPrincipal(self):
        while True:
            print("\nBiblioteca")
            print("1 - Criar nova música")
            print(f"2 - Visualizar música ({len(self.musicas)})")
            print("3 - Carregar música")
            print("4 - Voltar")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.criarNovaMusica()
            elif escolha == '2':
                self.abrirMusica()
            elif escolha == '3':
                self.carregarMusicas()
            elif escolha == '4':
                break
            else:
                print("Opção inválida. Tente novamente.")
        
    def menuBiblioteca(self):
        # while True:
        #     print("\nMenu KarMusic.")
        #     print("1 - Biblioteca")
        #     print("2 - Música")
        #     print("3 - Sair")
        #     escolha = input("Escolha uma opção: ")

        #     if escolha == '1':
        #         self.menuBiblioteca()
        #     elif escolha == '2':
        #         self.menuMusica()
        #     elif escolha == '3':
        #         print("Saindo do programa...")
        #         break
        #     else:
        #         print("Opção inválida. Tente novamente.")
        pass



    def menuMusica(self):
        pass
        # Implemente o menu Música aqui, onde o usuário pode interagir com as funções da classe Musica


    def criarNovaMusica(self):
        nome = input("Digite o nome da nova música: ")
        novaMusica = Musica(nome)
        print("Música criada com sucesso!")
        print('digite "help" caso tenha dúvida em como fornecer dados')
        escolha = input("Conhece a duração da musica?")
        if escolha == 'help':
            Helper.helpMusicDuration()
            escolha = input("agora que ja aprendeu... quer me contar a duração da musica?")
        if escolha not in ['não', 'nao', 'no', 'n', '', '0']:
            horas, minutos, segundos = 0
            if 'h' in escolha:
                horas = int(escolha.split('h')[0])
                escolha = escolha.split('h')[-1]
            if 'm' in escolha:
                minutos = int(escolha.split('m')[0])
                escolha = escolha.split('m')[-1]
            if 's' in escolha:
                segundos = int(escolha.split('h')[0])     
                escolha = escolha.split('s')[-1]
            novaMusica.setTimeMusic(segundos, minutos, horas) 

        print('prooonto, cabeçalho da musica definido')
        print('1 |criar anotações na musica atual')
        print('2 |Adicionar outra musica')
        print('3 |Voltar ao menu')

        self.musicas.append(novaMusica)
        if escolha == '1':
            self.adicionarAnotacao(novaMusica)
        elif escolha == '2':
            self.criarNovaMusica()
        elif escolha == '3':
            self.menuMusica()
        else:
            print("Opção inválida. Tente novamente.")
 
    def adicionarAnotacao(self, musica:Musica):
        while True:
            Helper.helpAnotation()
            escolha = input("Escreva a anotação da música ou 'sair' para finalizar: ")
            if escolha.lower() == 'sair':
                break
            else:
                # Aqui você deve chamar a função que analisa a string de escolha
                # e preenche corretamente a função insertNotationMusic
                self.parseAndInsertNotation(musica, escolha)

            print('Anotação adicionada. O que gostaria de fazer agora?')
            print('1 | Criar anotações na música atual')
            print('2 | Adicionar outra música')
            print('3 | Ir para a biblioteca')
            print('4 | Voltar ao menu')
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                continue  # Continua adicionando anotações
            elif opcao == '2':
                self.criarNovaMusica()
                break  # Sai do loop após criar nova música
            elif opcao == '3':
                self.menuPrincipal()
                break  # Sai do loop após ir para a biblioteca
            elif opcao == '4':
                self.menuMusica()
                break  # Sai do loop e volta ao menu
            else:
                print("Opção inválida. Tente novamente.")

    def parseAndInsertNotation(self, musica:Musica, escolha:str):
        # Inicializa as variáveis
        time_data = {}
        tipo = None
        notation = None

        # Divide a entrada em partes com base no '|'
        parts = escolha.split('|')

        # Processa cada parte para extrair tempo, tipo e comentário
        for part in parts:
            # Remove espaços em branco extras
            part = part.strip()

            # Verifica se é uma parte de tempo
            if 'h' in part or 'm' in part or 's' in part:
                # Extrai horas, minutos e segundos
                h, m, s = 0, 0, 0
                if 'h' in part:
                    h, part = part.split('h')
                    h = int(h)
                if 'm' in part:
                    m, part = part.split('m')
                    m = int(m)
                if 's' in part:
                    s = int(part.replace('s', ''))

                # Converte tudo para minutos e segundos
                total_seconds = h * 3600 + m * 60 + s
                time_data['minutos'] = total_seconds // 60
                time_data['segundos'] = total_seconds % 60

            # Verifica se é uma parte de tipo
            elif part.isdigit() or part.endswith('*t'):
                tipo = part.replace('*t', '')

            # Caso contrário, assume que é um comentário
            else:
                notation = part

        # Chama a função de inserção com os dados coletados
        musica.insertNotationMusic(notation=notation, tipo=tipo, time=time_data)


# Certifique-se de implementar as funções criarNovaMusica, irParaBiblioteca e menuMusica.


    def abrirMusica(self):
        if self.musicas:
            print("\nMúsicas disponíveis:")
            for i, musica in enumerate(self.musicas, 1):
                print(f"{i} - {musica.nome}")
            escolha = int(input("Escolha uma música para abrir: "))
            if 1 <= escolha <= len(self.musicas):
                musica_escolhida = self.musicas[escolha - 1]
                # Aqui você pode chamar um método para mostrar detalhes da música ou editar
            else:
                print("Número inválido. Tente novamente.")
        else:
            print("Não há músicas disponíveis.")

# Inicialização da aplicação
djNoterKarmusic()