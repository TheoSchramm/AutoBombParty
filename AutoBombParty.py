from random import choice
from subprocess import check_call
from requests import get

def copy2clip(txt):
    cmd=f'echo {txt.strip()}|clip'
    return check_call(cmd, shell=True)

def create_list(user_input,dic):
    return [i for i in dic if user_input in i.lower() and len(i) < 9]

def get_words():
    try:
        print('>> Conectando-se ao dicionário online...')
        return get('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt').text.split('\n')

    except:
        print('>> Erro! Abrindo arquivo local...')
        try:
            with open("br-sem-acentos.txt", "r") as fp:
                return fp.read().split('\n')
        except:
            print('>> Erro! Arquivo local não encontrado.\n')
            exit()

def __main__():
    dic = get_words()
    print()
    while True:
        menu = input('.\n├─> Insira as letras ou digite 0 para sair: ')
    
        match menu:
            case '0':
                print('└──> Saindo...')
                exit()
            
            case _:
                try:
                    escolhida = choice(create_list(menu,dic))
                    copy2clip(escolhida)
                    print(f'└──> Copiei \033[4m{escolhida.upper()}\033[0m para a sua área de transferência! \n')
                except:
                    print('└──> Ops! Não encontrei nenhuma palavra com essas letras :(\n')

if __name__ == '__main__':
    __main__()
