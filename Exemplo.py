import pyautogui
import time

def exemplo_basico():
    print("Começando em 3 segundos...")
    time.sleep(3)  # tempo pra você posicionar a tela

    # 1. Mover o mouse até uma posição (x, y)
    pyautogui.moveTo(500, 400, duration=0.5)

    # 2. Clicar
    pyautogui.click()

    # 3. Digitar algo
    pyautogui.write("Olá, Arthur! Estou digitando via PyAutoGUI.", interval=0.05)

    # 4. Pressionar ENTER
    pyautogui.press("enter")

    # 5. Achar um botão por imagem (opcional)
    botao = pyautogui.locateCenterOnScreen("botao_ok.png", confidence=0.8)
    if botao:
        pyautogui.click(botao)
    else:
        print("Botão não encontrado.")

