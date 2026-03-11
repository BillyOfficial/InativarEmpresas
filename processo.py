'''Cala a boca ai pylint, eu sei o que eu to fazendo!'''

from time import sleep
import pyautogui
import pandas as pd

# Ler planilha
planilha = pd.read_excel(r'Relatório\Relação de Empresas por Franquia.xlsx')
Base_codigo = planilha.iloc[:, 0].dropna().astype(int).tolist()

# Listas de imagens
home = ['Home1.png', 'HomenotCF.png']
ativo = ['Ativowhite.png', 'Ativoblack.png']
inativo = ['Inativowhite.png', 'Inativoblack.png', 'InativoblackCF.png']

def puxar(lista, conf=0.8):
    for img in lista:
        try:
            pos = pyautogui.locateOnScreen(img, confidence=conf)
            if pos:
                return pos
        except:
            pass
    return None

# ---------------------------------------------------------------------
# 1) PRIMEIRO: ir para o Home (única coisa que faz sentido procurar agora)
# ---------------------------------------------------------------------

print("Procurando botão Home...")
painel_inicial = puxar(home)

if not painel_inicial:
    print("Erro: Não achei o botão Home na tela!")
    exit()

pyautogui.click(painel_inicial)
sleep(2)

print(f"\nProcessando empresa: {Base_codigo[0]}")

# ---------------------------------------------------------------------
# 2) ABRIR BUSCA E COMEÇAR O PROCESSO
# ---------------------------------------------------------------------

pyautogui.press('f8')
sleep(4)

verificando_filtro = 'filtro em apelido.png'

if verificando_filtro:
    print("Filtro aplicado em apelido, alterando para código.")
    pyautogui.click(verificando_filtro)
else:
    exit()

# escrever código
pyautogui.write(str(Base_codigo[0]))
sleep(2)

pyautogui.click('Dados da empresa2.png')
sleep(4)

for codigo in Base_codigo:

    empresa_ativa = puxar(ativo)
    empresa_inativa = puxar(inativo)

    if empresa_ativa:
        print(f"{codigo} -> Empresa Ativa! Inativando...")
        pyautogui.click(empresa_ativa)
        sleep(2)
        pyautogui.click('Inativar Empresa.png')
        sleep(2)
        pyautogui.click('Gravar.png')
        sleep(4)

    elif empresa_inativa:
        print(f"{codigo} -> Já está inativa.")

    else:
        print(f"{codigo} -> Situação desconhecida: não achei ativo nem inativo.")

    # Ir para editar para a próxima empresa
    editar = ['Editar.png', 'Editar2.png', 'Editar3.png']
    editar_empresa = puxar(editar)

    pyautogui.click(editar_empresa)
    sleep(4)
    pyautogui.write(str(codigo))
    sleep(1)
    pyautogui.press('tab')
    sleep(2)
