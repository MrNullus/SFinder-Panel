import requests
from colorama import Fore
import time
import os
from platform import system as device
import random


def time_oc():
        final = time.time()
        counter = round(final - inicio, 2)
        conver = time.strftime("%Mm:%Ss", time.gmtime(counter))
        segundos = time.strftime("%S", time.gmtime(counter))
        minutos = counter / 60
        verificar = int(minutos)
        if verificar == 0:
                print(f"{Fore.YELLOW}Duração de execução: {segundos}s")
        else:
                print(f"{Fore.YELLOW}Duração de execução: {conver}m")
                input()

def vali(): #Criando a função que irá formatar os dados encontrados
        if valid_directs != []:
                print(f"{Fore.GREEN}Páginas encontradas")
                for i in range(len(valid_directs)):
                        print(f"{Fore.GREEN}[{i+1}]{valid_directs[i]}")
        else:
                print(f"{Fore.RED}Nenhuma página foi encontrada")


def verifify_cl(): #função que irá verificar o sistema operacional
        sys = device()
        if sys == "Windows":
                os.system("cls")
        elif sys == "Linux":
                os.system("clear")


def create_valid(): #função que irá criar o arquivo txt
                choice = str(input("Deseja salvar os diretórios encontrados?S/n ")).lower()
                if choice == "s":
                        archive_n = open(input("Nome do arquivo "), "w+")
                        if valid_directs == []:
                                print(f"{Fore.RED}Não existe páginas para salvar!!")
                                print(Fore.RESET)  # Resetar a cor padrão do terminal deixada pela script.
                                exit()
                        else:        
                                for i in valid_directs:
                                        archive_n.write(f"{i}\n")
                                archive_n.close()






agents = {} #dicionario que irá armazenar os user-agents
valid_directs = [] #lista que irá armazenar os diretórios encontrados
valid_redirect = []

verifify_cl()
print("[1]Http\n[2]Https\n[3]Sair")

try:
        protocol = input("==> ")
        if protocol == "1":
                protocol = "http://"

        elif protocol == "2":
                protocol = "https://"

        elif protocol == "3":
                exit()
        else:
                print(f"{Fore.RED}Erro na entrada de dados!!")
                print(Fore.RESET)  # Resetar a cor padrão do terminal deixada pela script.
                exit()
except KeyboardInterrupt:
        print(f"\n{Fore.RED}Programa interrompido!")
        print(Fore.RESET)  #Resetar a cor padrão do terminal deixada pela script.
        exit(0)


url = str(input("Url: "))
inicio = time.time()

try:
        while True:
                with open("pages.txt", "r") as direct: #acessando o arquivo que contém os diretórios
                        for i in direct.readlines(): #passando pelo objeto que possui os diretórios
                                if i[0] == "/": #verificando se o diretório possui "/"(isso causa erro na requisição)
                                        content = protocol + url + i
                                elif i[0] != "/": 
                                        content = protocol + url + "/" + i

                                with open("user-agents.txt", "r") as ag_list: #abrindo o arquivo que possui os agents
                                        #for ag in ag_list.readlines(): #passando pelo objeto que contém os agents
                                        ag = ag_list.readlines()
                                        ag = random.choice(ag)
                                        agents["User-Agent"] = ag.rstrip("\n") #adicionando no dicinario agents e excluindo a quebra de linha com regex
                                        try:                                 
                                                r = requests.get(content, headers=agents)
                                        except requests.exceptions.ConnectionError:
                                                print(f"{Fore.RED}Url inválida!!")
                                                print(Fore.RESET)  # Resetar a cor padrão do terminal deixada pela script.
                                                exit()

                                        stats = r.status_code
                                        if stats == 200:
                                                valid_directs.append(content) #adicionando os direótios válidos na lista
                                                print(f"{Fore.GREEN}Página encontrada!! >>> {content}")
                                                        
                                        elif stats == 302:
                                                valid_redirect.append(content)
                                                print(f"{Fore.YELLOW}Redirecionamento de página >>> {content}")

                                        elif stats == 404:
                                                print(f"{Fore.RED}Página não encontrada!![X] => {content}")
                        ag_list.close() 
                direct.close()
                break
        create_valid() #chamando função que gera o txt
        vali() #chamando a função que formata os dados
except KeyboardInterrupt:
        print(f"{Fore.RED}Programa interrompido!")
        vali()
        time_oc()
        print(Fore.RESET)  #Resetar a cor padrão do terminal deixada pela script.
        pass