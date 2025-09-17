import pyautogui
import pandas

# entra no site da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pyautogui.write() -> escreve um texto
# pyautogui.press() -> aperta uma tecla
# pyautogui.hotkey() -> aperta uma combinação de teclas
# pyautogui.click() -> clicar em algum lugar da tela
# pyautogui.position() -> mostra a posição do mouse na tela
# pyautogui.sleep() -> espera um tempo
# pyautogui.PAUSE = 1 -> adiciona uma pausa de 1 segundo entre cada comando do pyautogui
# pyautogui.alert() -> mostra uma mensagem na tela
# pyautogui.confirm() -> mostra uma mensagem na tela com as opções OK e Cancelar
# pyautogui.prompt() -> mostra uma mensagem na tela com um campo para o usuário digitar algo
# pyautogui.locateOnScreen() -> localiza uma imagem na tela
# pyautogui.locateCenterOnScreen() -> localiza o centro de uma imagem na tela
# pyautogui.screenshot() -> tira um print da tela
# pyautogui.scroll() -> rola a tela para cima ou para baixo
# pyautogui.moveTo() -> move o mouse para uma posição específica na tela


pyautogui.PAUSE = 0.8

# abrir o navegador chrome

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")


# entrar no site da empresa
pyautogui.sleep(2)
# pyautogui.click(x=1020, y=481)


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.sleep(3)

# fazer login
pyautogui.click(x=923, y=363)
pyautogui.write("victorevolts@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
pyautogui.sleep(3)

# entrar no menu produtos

# ler aquivo csv com pandas dentro da pasta do projeto
tabela = pandas.read_csv('Python\produtos.csv')
print(tabela)
# cadastrar produtos


pyautogui.sleep(1)

for linha in tabela.index:

# buscar as informações dentro da base de dados e preencher o formulário

    pyautogui.click(x=783, y=241)    
    codigo = tabela.loc[linha,"codigo"] 
    pyautogui.write(codigo)
    
    pyautogui.press("tab")
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    
    pyautogui.press("tab")
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    
    pyautogui.press("tab")
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    
    
    pyautogui.press("tab")
    obs = str(tabela.loc[linha,"obs"])
    if obs != 'nan':
       pyautogui.press("enter")   
    
    
    pyautogui.press("tab")
    pyautogui.press("enter")