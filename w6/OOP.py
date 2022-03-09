import re
import hashlib

class Account:
    
    def __init__(self , username , password , phonenumber , Email ) :
        if Account._is_username_valid(username):
            self.username = username
        if Account._is_password_valid(password):
            self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if Account._is_phonenumber_valid(phonenumber):
            if phonenumber.startswith('0'):
                self.phonenumber = phonenumber
            else:
                self.phonenumber = '0' + phonenumber[3:]
        if Account._is_Email_valid(Email):
            self.Email = Email

    @staticmethod
    def _is_username_valid(username):
        regex_pattern = re.compile(r'^[a-zA-Z]+_[a-zA-Z]+$')
        if re.fullmatch(regex_pattern , username):
            return True
        else:
            raise Exception('Invalid Username')

    @staticmethod
    def _is_password_valid(password):
        regex_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
        if re.fullmatch(regex_pattern , password):
            return True
        else:
            raise Exception('Invalid Password')

    @staticmethod
    def _is_phonenumber_valid(phonenumber):
        regex_pattern1 = re.compile(r'^09[\d]{9}$')
        regex_pattern2 = re.compile(r'^\+989[\d]{9}$')
        if re.fullmatch(regex_pattern1 , phonenumber) or re.fullmatch(regex_pattern2 , phonenumber):
            return True
        else:
            raise Exception('Invalid Phone Number')

    @staticmethod
    def _is_Email_valid(Email):
        regex_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,5}$')
        if re.fullmatch(regex_pattern , Email):
            return True
        else:
            raise Exception('Invalid Email')

class Site:

    def __init__(self , url):
        self.url = url
        self.register_users = []
        self.active_users = []

    def register(self , user):
        if user in self.register_users :
            raise Exception('user already registered')
        else:
            self.register_users.append(user)
            print('register successful')

    def login(self , *args):
        mark = 0
        for user in self.active_users:
            if len(args) == 3:
                if user.Email == args[0] and user.username == args[1] and user.password == hashlib.sha256(args[2].encode('utf-8')).hexdigest():
                    print('user already logged in')
                    mark = 2
            elif len(args) == 2:
                if (user.Email == args[0] or user.username == args[0]) and user.password == hashlib.sha256(args[1].encode('utf-8')).hexdigest():
                    print('user already logged in')
                    mark = 2
        if mark != 2:
            for user in self.register_users:
                if len(args) == 3:
                    if user.Email == args[0] and user.username == args[1] and user.password == hashlib.sha256(args[2].encode('utf-8')).hexdigest():
                        self.active_users.append(user)
                        print('login successful')
                        mark = 1
                elif len(args) == 2:
                    if (user.Email == args[0] or user.username == args[0]) and user.password == hashlib.sha256(args[1].encode('utf-8')).hexdigest():
                        self.active_users.append(user)
                        print('login successful')
                        mark = 1
        if mark == 0:
            print('invalid login')


    def logout(self , user):
        if user in self.active_users:
            self.active_users.remove(user)
            print('logout successful')
        else:
            print('user is not logged in')


