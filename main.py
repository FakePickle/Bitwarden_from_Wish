from file_transfer import file_Transfer
import time
from passwords import main,key
from encrypt_decrypt import encrypt_decrypt

class magic:
    def __init__(self,user_name_input,website):
        self.usr_name = user_name_input
        self.web = website
    
    def search_passwords(self):
        inline = open('passwords.txt')
        inline = eval(inline.read())
        for keys,values in inline.items():
            for k,v in values.items():
                if k == self.web:
                    temp_list = v
        email = temp_list[0]
        pwd = temp_list[1]
        with open('key.key','rb') as inline:
            data = inline.read().splitlines()
        key1 = data[0]
        key2 = data[1]
        decryption = encrypt_decrypt(key1,key2)
        mail = decryption.decrypt_file(email)
        password = decryption.decrypt_file(pwd)
        return str(mail),str(password)

class File_transfer:
    def __init__(self):
        self.file = file_Transfer()
    
    def main_time(self):
        run = True
        while run:
            role = 'host' if time.time() % 30 < 15 else 'client'
            if role == 'host':
                self.file.server_usr()
                print('HOST')
            elif role == 'client':
                self.file.client_usr()
                user_input_cl = input()
                print('CLIENT')
                if user_input_cl == 'recv': run = False
            time.sleep(15)
        if user_input_cl == 'recv':
            magic(input('Enter user name : '),input('Enter website : ')).search_passwords()
        if input() == 'kill':
            run = False
        else:
            run = True
        if run:
            File_transfer().main_time()
        else:
            print('Program killed !')

if __name__ == '__main__':
    print(magic(input('Enter user name '),input('Enter platform')).search_passwords())