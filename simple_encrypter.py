from cryptography.fernet import Fernet
import base64
import hashlib
import getpass
import os

def start():
  while True:
    print('What do you want to do?')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Clear')
    print('4. Exit')

    selection = input()

    if selection == '1':
      text = input('\nEnter text to encrypt: ')
      password = getpass.getpass('Enter password: ')
      encrypt(text, password)
    elif selection == '2':
      text = input('\nEnter text to decrypt: ')
      password = getpass.getpass('Enter password: ')
      decrypt(text, password)
    elif selection == '3':
      os.system('clear')
    elif selection == '4':
      print('Exit')
      break

def convert_password(password):
  hash_pass = hashlib.sha256(password.encode()).hexdigest()[:32]
  return base64.urlsafe_b64encode(hash_pass.encode())

def encrypt(text, password):
  try:
    key = convert_password(password)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(text.encode())
    print('\nEncripted text: ' + encrypted.decode() + '\n')
  except:
    print('\nError, try again\n')

def decrypt(text, password):
  try:
    key = convert_password(password)
    fernet = Fernet(key)
    encrypted = fernet.decrypt(text.encode())
    print('\nDecrypted text: ' + encrypted.decode() + '\n')
  except:
    print('\nError, try again\n')

start()