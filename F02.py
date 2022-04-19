# KAMUS
# new_user_idx :  integer
# new_user_name : string
# new_user_username : string 
# new_user_password : string
# new_user_role : string
# saldo : integer
# new_user : array

def register(datas1,header1,dir):
  # INISIALISASI KEUNIKAN USERNAME
  Alphabeth_uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  Alphabeth_undercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  numerical = ["0","1","2","3","4","5","6","7","8","9"]
  symbol = ["-","_"]
  # INISIALISASI NEW USER
  new_users = []
  isUnik = False
  new_user_idx = datas1[-1][0] + 1 # PENAMBAHAN DATA PADA ELEMEN TERAKHIR

  new_user_name = input("Masukan nama: ")
  new_user_username = input("Masukan username: ")
  new_user_password = input("Masukkan password: ")
  
  def findLength(string):
      count = 0
      for i in string:
          count+= 1

      return count
  # VALIDASI TIDAK DAPAT MEMBUAT AKUN ADMIN DAN USERNAME YANG SAMA
  if new_user_username == "admin":
    print("Tidak bisa membuat admin, coba username lain.")
    exit()
  elif datas1[i][2] == new_user_username:
    print("Username", new_user_username, "sudah terpakai, silakan menggunakan username lain.")
    exit()
  while isUnik == False: # membaca keunikan username
    for i in range(findlenght(datas1)):
      if (datas1[i][2] != new_user_username) or new_user_username == Alphabet_uppercase or new_user_username == Alphabeth_undercase or new_user_username == numerical or new_user_username == symbol :
        isUnik = True
      else:
        isUnik = False
        new_user_username = input("Username harus unik, masukan username lain: ")

  print("")
  # PENAMBAHAN USER KE DALAM DATA
  new_user_role = "user"
  saldo = 0
  new_user = [new_user_idx, new_user_name, new_user_username, new_user_password, new_user_role, saldo]
  new_users = new_users + new_user

  datas1 += new_users

  print("Username", new_user_username, 'telah berhasil register ke dalam "Binomo"')

  def convert_datas_to_string(header,datas):
    string_data = ";".join(header) + "\n"
    for arr_data in datas:
      arr_data_all_string = [str(var) for var in arr_data]
      string_data += ";".join(arr_data_all_string)
      string_data += "\n"
    return string_data

  # AUTOSAVE DATA USER PADA USER.CSV
  datas_as_string = convert_datas_to_string(header1,datas1)
  f1 = open("./"+dir+"/user.csv", "w")
  f1.write(datas_as_string)
  f1.close()
  return datas1
