import pyautogui
import time

time.sleep(4)
print(pyautogui.position())

# x=499, y=353 = posiçao do grift/ x=442, y=355 poder que upa o grift
# x=588, y=358 = posição do gerador de dinheiro
# x=553, y=525 = posição do jinwu vai proteger o cavaleiro
# x=554, y=505 = posição do cavaleiro dos glifos para o boss
# x=505, y=617 = posição de recomeçar a fase
# x=775, y=171 = posiçao botaõ de começar a partida
# Detalhes da fase:
#  Cada onda dura 20s e o apocalipse dura 1min ent:
#  depois dos primeiros 22s colocar o gerador de dinheiro dps mais 22s colocar o grift depois de 1,05min clicar no ponto denovo para ativar a abilidade e dps de 2s colocar Jinwu logo em seguida dps de mais 1.02min colocar as duas ultimas unidades que faltam e upar todas de 21s a 21s 
pyautogui.moveTo()
pyautogui.press("t")


# x=719, y=367 = bruxa e hollow knigth
# x=557, y=352
# botão tentar novamente modo infinito = x=649, y=616