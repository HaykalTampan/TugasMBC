database = {
    'haykal': 'azriel',
    'Lolos': 'rekruitasi',
    'asisten': 'MBC',
    'aamiin': 'yaallah'
}

def login():
    username = input("Username: ")
    password = input("password: ")

    if username in database and database[username] == password:
        print("Anda berhasil Login")
    else:
        print("Password dan Username anda salah")

login()

