# CAMBIBAR VISIBILIDAD DE REPOSITORIOS EN GITHUB #
# Script Name: GitVisibility
# Version : v1
# Author : PGX

from time import sleep as t
from colorama import Fore, Style, init
from dotenv import load_dotenv
from pyfiglet import Figlet
import os

init(autoreset=True)
so=os.name

#--------------- colors ------------- #
CYAN=f"{Fore.CYAN}{Style.BRIGHT}"
WHITE=f"{Fore.WHITE}{Style.BRIGHT}"
RED=f"{Fore.RED}{Style.BRIGHT}"
#------------------------------------#

from github import Github
load_dotenv()
token = os.getenv("GITHUB_TOKEN")
g = Github(token)
user = g.get_user()

def banner():
 print(CYAN + Figlet(font='small').renderText("GitVisibility"))

def chooseOneRepo(repoName):
 repo = user.get_repo(repoName)
 if repo.private:
  print(f" {CYAN}[+]{WHITE} el repositorio {CYAN} {repoName}{WHITE} ahora es {CYAN}[Publico]")
  repo.edit(private=False)
 else:
  print(f" {CYAN}[+]{WHITE} el repositorio {CYAN} {repoName}{WHITE} ahora es {CYAN}[Privado]")
  repo.edit(private=True)

def choose(number, from0, to, boolean0):
 repos = user.get_repos(visibility=f"{from0}")
 n=1
 for repo in repos:
  try:
   repo.edit(private=boolean0)
   print(f"  {CYAN}[+][{WHITE}{n}{CYAN}] {WHITE} Repositorio {CYAN}[{repo.name}]{WHITE} ahora es {CYAN}[{to}]{WHITE}")
   n+=1
  except Exception as e:
   print(f"[-] Error en '{repoName}': {e}")
 print("\nScript Finalizado...")


def consoleClear():
 if so != "nt":
  os.system("clear")
 else:
  os.system("cls")

def showOptions():
 print(f"""  {CYAN}[1]{WHITE} Cambiar todos los repositorios a Publico
  {CYAN}[2]{WHITE} Cambiar todos los repositorios a Privado
  {CYAN}[3]{WHITE} Cambiar visibilidad de un repositorio
 """)
def selOptions():
 opt=int(input(f" Seleccionar opcion ---> {CYAN}"))
 return opt

def conditionSel(opt):
 if opt == 1:
  choose(1, "private", "Publico", False)
 elif opt == 2:
  choose(2, "public", "Privado", True)
 elif opt == 3:
  repoName=input(f" {CYAN}[+]{WHITE} Nombre del repositorio: {CYAN}")
  chooseOneRepo(repoName)

def start():
 consoleClear()
 banner(); showOptions()
 conditionSel(selOptions())

if __name__ == "__main__":
 try:
  start()
 except KeyboardInterrupt:
  print(f"\n{WHITE}Script Interrumpido, {CYAN}[ADIOS]{WHITE}...")
  #t(2)
