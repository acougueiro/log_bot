#!/usr/bin/python3
#teste

##MODULOS#################################################################################################################################################################
import time
import sys
import pexpect
import os
import getpass
import datetime
import glob
##VARIAVEIS###############################################################################################################################################################
user="a0095769"
senha="!H3nr1qu51"
jump ="200.204.1.4"
ssh=("ssh -l " + user + " " + jump )
os.path.dirname(os.path.abspath(__file__))

##CONTROLE DE RESULTADOS##################################################################################################################################################
sem_cnx1 = open('sem_cnx.txt','w')
sem_cnx1.close()

remover = glob.glob('result/*')
for arquivos in remover:
    os.remove(arquivos)

##JUMP####################################################################################################################################################################
child = pexpect.spawn ( ssh, encoding='utf-8')

try:
    child.expect (['sword:', 'sword: '])
    child.sendline (senha)
except:
    child.expect([':~]', ':~] '])
    child.sendline (' ')

##CONTROLE DE FLUXO#######################################################################################################################################################
lista_equips = open('lista_equips.txt','r')
for linha_equip in lista_equips:
    linha_equip = linha_equip.rstrip()
    host = linha_equip.split(" ")[1]
    tipo = linha_equip.split(" ")[2]
    host = str(host)
    tipo = str(tipo)
    now = datetime.datetime.now()
    data_e_hora = now.strftime("%d/%m/%Y %H:%M:%S")
    aviso = str("Executado as " + data_e_hora + " " + host + " " + tipo )
    arquivo_resultado = ("result/" + host + ".txt")
    print (aviso)

##COMANDOS################################################################################################################################################################
    try:
        child.logfile = open(arquivo_resultado,"w")
        child.expect([':~]', ':~] '])
        child.sendline ('ssh ' + host )
        try:
            child.expect(['yes', 'yes: '])
            child.sendline ("y")
        except:
            print (' ')
        child.expect (['sword:', 'sword: '])
        child.sendline (senha)

        open(arquivo_resultado, 'w').close()
        vendor = open(tipo,'r')
        for cmd in vendor:
            cmd = cmd.rstrip()
            child.expect(['>','#','~]$','> ','# ','~]$ '])
            child.sendline (cmd)
        vendor.close()
        child.expect([':~]', ':~] '])
        child.sendline (" ")


        #resultado = open(arquivo_resultado,"a")
        #resultado.write(host + "\n")
        #resultado.write(resultado + "\n")
        #resultado.close()


    except Exception:
        child.expect('.*')
        time.sleep(2)
        child.sendline (' ')
        sem_cnx2 = open("sem_cnx.txt","a")
        sem_cnx2.write(host + " " + tipo + "\n")
        sem_cnx2.close()

##FECHAR SSH##############################################################################################################################################################
child.expect(':~]')
child.sendline ('exit')
child.expect(pexpect.EOF)

