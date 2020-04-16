from configparser import ConfigParser

config = ConfigParser()
config.read('parametros.ini')
default_config = dict(config['Dados'])
default_config = dict(config['HoradeEntrada'])

import webbrowser
import pyautogui
import time

webbrowser.open('https://iqoption.br.com/reg?aff=97684&afftrack=IQ_BRCOM_main_SignIn_Header&clickid=98f824ffaac781d44ef107bf5e24bc84')

time.sleep(10)

pyautogui.moveTo(752, 405, duration=0.25)
pyautogui.click(752, 405, button='left', duration=0.25)
pyautogui.moveTo(602, 486, duration=0.25)
pyautogui.click(602, 482, button='left', duration=0.25)
pyautogui.typewrite(config.get('Dados', 'Email'))
pyautogui.hotkey('tab')
pyautogui.typewrite(config.get('Dados', 'Senha'))
pyautogui.hotkey('enter')

time.sleep(1.5)

pyautogui.moveTo(675, 678, duration=0.25)
pyautogui.click(675, 678, button='left', duration=0.25)#botão entrar negociação

time.sleep(45)

pyautogui.moveTo(117, 183, duration=0.75)
pyautogui.click(117, 183, button='left', duration=0.25)#clica na escolha do par de moedas
time.sleep(2)
pyautogui.moveTo(198, 142, duration=0.75)
pyautogui.click(198, 142, button='left', duration=0.25)#click 2 na escolha do par de moedas
time.sleep(2)
pyautogui.moveTo(195, 240, duration=0.75)
pyautogui.click(195, 240, button='left', duration=0.25)#click 3 na escolha do par de moedas
time.sleep(2)
pyautogui.moveTo(370, 135, duration=0.75)
pyautogui.click(370, 135, button='left', duration=0.25)#click 4 na escolha do par de moedas
time.sleep(6)
pyautogui.moveTo(552, 133, duration=1.5)
pyautogui.click(552, 133, button='left', duration=0.25)#clica para escrever o par de moedas
pyautogui.typewrite(config.get('Dados', 'Moeda'))
time.sleep(6)
pyautogui.moveTo(582, 230, duration=1.5)
pyautogui.click(582, 230, button='left', duration=0.25)#confirma a escolha do par de moedas
time.sleep(6)
pyautogui.moveTo(95, 539, duration=2)
pyautogui.click(95, 539, button='left', duration=0.25)#seleção de candles
pyautogui.moveTo(194, 524, duration=2)
pyautogui.click(194, 524, button='left', duration=0.25)#confirma candles
pyautogui.moveTo(94, 580, duration=2)
pyautogui.click(94, 580, button='left', duration=0.25)#seleção de 5M
pyautogui.moveTo(316, 423, duration=2)
pyautogui.click(316, 423, button='left', duration=0.25)#confirma 5M
pyautogui.moveTo(1302, 177, duration=2)
pyautogui.click(1302, 177, button='left', duration=0.25)#alinhamento 5M
pyautogui.moveTo(1188, 268, duration=2)
pyautogui.click(1188, 268, button='left', duration=0.25)#confirma alinhamento 5M
pyautogui.moveTo(1296, 256, duration=2)
pyautogui.click(1296, 256, button='left', duration=0.25)#clica no campo valor de entrada
pyautogui.hotkey('backspace')#limpa o campo valor de entrada
time.sleep(1)
pyautogui.typewrite(config.get('Dados', 'ValordeEntrada'))#digita valor de entrada
time.sleep(5)

import sched, time, threading, sys

triggerA = time.mktime((2020, 4, 14, 16, 23, 8, 0, 0, 0))
triggerB = time.mktime((2020, 4, 14, 16, 23, 8, 0, 0, 0))
triggerC = time.mktime((2020, 4, 14, 16, 23, 8, 0, 0, 0))

def taskA(triggerA):
    sys.stdout.write(" Entrada A realizada "+ str(time.time() - triggerA) + ' segundos\n')
    sys.stdout.read(pyautogui.click())

def taskB(triggerB):
    sys.stdout.write(" Entrada B realizada "+ str(time.time() - triggerB) + ' segundos\n')
    sys.stdout.read(pyautogui.click())

def taskC(triggerC):
    sys.stdout.write(" Entrada C realizada "+ str(time.time() - triggerC) + ' segundos\n')
    sys.stdout.read(pyautogui.click())

def taskD(triggerD):
    sys.stdout.write(" Entrada D realizada "+ str(time.time() - triggerD) + ' segundos\n')
    sys.stdout.read(pyautogui.click())

def taskE(triggerE):
    sys.stdout.write(" Entrada E realizada "+ str(time.time() - triggerE) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskF(triggerF):
    sys.stdout.write(" Entrada F realizada "+ str(time.time() - triggerF) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskG(triggerG):
    sys.stdout.write(" Entrada G realizada "+ str(time.time() - triggerG) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskH(triggerH):
    sys.stdout.write(" Entrada H realizada "+ str(time.time() - triggerH) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskI(triggerI):
    sys.stdout.write(" Entrada I realizada "+ str(time.time() - triggerI) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskJ(triggerJ):
    sys.stdout.write(" Entrada J realizada "+ str(time.time() - triggerJ) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskK(triggerK):
    sys.stdout.write(" Entrada K realizada "+ str(time.time() - triggerK) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskL(triggerL):
    sys.stdout.write(" Entrada L realizada "+ str(time.time() - triggerL) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskM(triggerM):
    sys.stdout.write(" Entrada M realizada "+ str(time.time() - triggerM) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskN(triggerN):
    sys.stdout.write(" Entrada N realizada "+ str(time.time() - triggerN) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskO(triggerO):
    sys.stdout.write(" Entrada O realizada "+ str(time.time() - triggerO) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskP(triggerP):
    sys.stdout.write(" Entrada P realizada "+ str(time.time() - triggerP) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskQ(triggerQ):
    sys.stdout.write(" Entrada Q realizada "+ str(time.time() - triggerQ) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskR(triggerR):
    sys.stdout.write(" Entrada R realizada "+ str(time.time() - triggerR) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskS(triggerS):
    sys.stdout.write(" Entrada S realizada "+ str(time.time() - triggerS) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))

def taskT(triggerT):
    sys.stdout.write(" Entrada T realizada "+ str(time.time() - triggerT) + ' segundos\n')
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))#entrada CALL
    sys.stdout.read(pyautogui.click(1300, 599, button='left', duration=0.25))#entrada PUT

def taskU(triggerU):
    sys.stdout.write(" Entrada U realizada "+ str(time.time() - triggerU) + ' segundos\n')
    CALL = int(config.get(''))
    if
    sys.stdout.read(pyautogui.click(1300, 486, button='left', duration=0.25))

s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)
s = sched.scheduler(time.time, time.sleep)

s.enterabs(triggerA, 1, taskA, argument=(triggerA,))
s.enterabs(triggerB, 2, taskB, argument=(triggerB,))
s.enterabs(triggerC, 3, taskC, argument=(triggerC,))
s.enterabs(triggerD, 4, taskD, argument=(triggerD,))
s.enterabs(triggerE, 1, taskE, argument=(triggerE,))
s.enterabs(triggerF, 2, taskF, argument=(triggerF,))
s.enterabs(triggerG, 3, taskG, argument=(triggerG,))
s.enterabs(triggerH, 4, taskH, argument=(triggerH,))
s.enterabs(triggerI, 1, taskI, argument=(triggerI,))
s.enterabs(triggerJ, 2, taskJ, argument=(triggerJ,))
s.enterabs(triggerK, 3, taskK, argument=(triggerK,))
s.enterabs(triggerL, 4, taskL, argument=(triggerL,))
s.enterabs(triggerM, 1, taskM, argument=(triggerM,))
s.enterabs(triggerN, 2, taskN, argument=(triggerN,))
s.enterabs(triggerO, 3, taskO, argument=(triggerO,))
s.enterabs(triggerP, 4, taskP, argument=(triggerP,))
s.enterabs(triggerQ, 1, taskQ, argument=(triggerQ,))
s.enterabs(triggerR, 2, taskR, argument=(triggerR,))
s.enterabs(triggerS, 3, taskS, argument=(triggerS,))
s.enterabs(triggerT, 4, taskT, argument=(triggerT,))
s.enterabs(triggerU, 4, taskU, argument=(triggerU,))

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

t = threading.Thread(target=s.run)
t.start()

while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
while t.is_alive(): pass
