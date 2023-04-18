# Пишем инструмент, который позволит получать IP-адрес по доменному имени или адресу сайта!!!

import socket 

def get_ip_by_hostname():                
     hostname = input('Please, enter a website address (URL): ') #запросим у пользователя доменное имя

     # Пишем блок try (получаем IP-адресс) и except (обработаем и вернем сообщение о возможной ошибке при вводе не валидного имени):
     try: 
     # в блоке try первым делом вернем введенный домен, а затем и IP-адресс: 
     # обращаемся к модулю socket после чего к функции gethostbyname, в которую передаем полученный от пользователя домен
         return f'Hostname: {hostname}\nIP address: {socket.gethostbyname (hostname)}'
         
     except socket.gaierror as error:
         return f'Invalid Hostname - {error}' 


def main():                              # в этой функции вызываем нашу функцию
    print(get_ip_by_hostname())

if __name__=='__main__':                 #условие в котором вызываем функцию main
    main()



