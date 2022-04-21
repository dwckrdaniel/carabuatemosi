# KAMUS
# id_user :  integer
# username : string
# password : string
# input_username : string
# input_password : string 
# valid : boolean

def login(datas1): # F02-Login
    datas = datas1
    input_username = str(input("Masukan username: "))
    input_password = str(input("Masukan password: "))
    username = 2
    password = 3
    valid = False
    def findLength(string):
        count = 0
        for i in string:
            count+= 1
  
        return count

    for i in range(findLength(datas1)):
        id_user = datas[i][0]

    # VERIFIKASI LOGIN TERHADAP DATA
    def login_verif(username, password, input_username, input_password, valid):
        for i in range(findLength(datas1)):
            adminORuser = datas[i][4]
            if (datas[i][username] == input_username) and (datas[i][password] == input_password):
                valid = True
                break
            else:
                valid = False
        if valid == False:
            print("Password atau username salah atau tidak ditemukan.")
        else:
            print("Halo ",input_username,"! Selamat datang di Binomo")
        return [adminORuser,valid]

    loginverif = login_verif(username, password, input_username, input_password, valid)
    adminORuser = loginverif[0]
    valid = loginverif[1]
    return [id_user,username,adminORuser,valid]
