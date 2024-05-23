# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

import socket, sys


HOST = '192.168.0.137'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados


def main(argv): 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Servidor executando!")
            while(True):       
                texto = input("Digite o texto a ser enviado ao servidor:\n")
                s.send(texto.encode()) #texto.encode - converte a string para bytes
                data = s.recv(BUFFER_SIZE)

                texto_recebido = repr(data) #converte de bytes para um formato "printável"
                print('Texto recebido do servidor, invertido:', texto_recebido)
                texto_string = data.decode('utf-8') #converte os bytes em string
                
                
                qntdV = s.recv(1024).decode()
                num1 = repr(qntdV)
                print('Quantidade de vogais:', num1)
                

                qntdC = s.recv(1024).decode()
                num2 = repr(qntdC)
                print('Quantidade de consoantes:', num2)
                

                if (texto_string == 'bye'):
                    print('vai encerrar o socket cliente!')
                    s.close()
                    break
    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":   
    main(sys.argv[1:])