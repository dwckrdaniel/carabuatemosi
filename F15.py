# F15 - Load Data
def load1(dir):
  dir = "./"+dir+"/user.csv"
  with open(dir, "r") as f1:
      raw_lines1 = f1.readlines()
  f1.close()

  lines1 = [raw_line.replace("\n", "") for raw_line in raw_lines1] # hapus spasi

  def convert_array_data_to_real_values1(array_data):
    arr_cpy = array_data[:]
    for i in range(5):    # ubah id ke integer           
      if(i == 0):
        arr_cpy[i] = int(arr_cpy[i])
      elif(i==5):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil = [temp]+hasil
              temp = ""
          else:
              temp += words
      hasil= [temp]+hasil
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  
  def my_pop(l):
    new = []
    l = list(l)
    for i in l:
        if l[-1] == i:
            pass
        else:
            new = [i]+new
    return new
  raw_header1 = lines1.my_pop(0)

  header1 = convert_line_to_data(raw_header1)

  datas1 = []

  for line in lines1:
    array_of_data = convert_line_to_data(line)
    real_values1 = convert_array_data_to_real_values1(array_of_data)
    datas1 = [real_values1] + datas1
  return [header1,datas1]

def load2(dir):
  dir = "./"+dir+"/game.csv"
  with open(dir, "r") as f2:
      raw_lines2 = f2.readlines()
  f2.close()

  lines2 = [raw_line.replace("\n", "") for raw_line in raw_lines2] # hapus spasi

  def convert_array_data_to_real_values2(array_data):
    arr_cpy = array_data[:]
    for i in range(5):    # ubah id ke integer           
      if(i == 3):
        arr_cpy[i] = int(arr_cpy[i])
      elif(i==4):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil = [temp]+hasil
              temp = ""
          else:
              temp += words
      hasil= [temp]+hasil
      return hasil
    
  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  
  def my_pop(l):
    new = []
    l = list(l)
    for i in l:
        if l[-1] == i:
            pass
        else:
            new = [i]+new
    return new
  raw_header2 = lines2.my_pop(0)

  header2 = convert_line_to_data(raw_header2)

  datas2 = []

  for line in lines2:
    array_of_data = convert_line_to_data(line)
    real_values2 = convert_array_data_to_real_values2(array_of_data)
    datas2=[real_values2]+datas2
  return [header2,datas2]

def load3(dir):
  dir = "./"+dir+"/riwayat.csv"
  with open(dir, "r") as f3:
      raw_lines3 = f3.readlines()
  f3.close()

  lines3 = [raw_line.replace("\n", "") for raw_line in raw_lines3] # hapus spasi

  def convert_array_data_to_real_values3(array_data):
    arr_cpy = array_data[:]
    for i in range(4):    # ubah id ke integer           
      if(i == 2): 
        arr_cpy[i] = int(arr_cpy[i])
      if(i == 3): 
        arr_cpy[i] = int(arr_cpy[i])

    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil = [temp]+hasil
              temp = ""
          else:
              temp += words
      hasil= [temp]+hasil
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  
  def my_pop(l):
    new = []
    l = list(l)
    for i in l:
        if l[-1] == i:
            pass
        else:
            new = [i]+new
    return new
  raw_header3 = lines3.my_pop(0)

  header3 = convert_line_to_data(raw_header3)

  datas3 = []

  for line in lines3:
    array_of_data = convert_line_to_data(line)
    real_values3 = convert_array_data_to_real_values3(array_of_data)
    datas3=[real_values3]+datas3
  return [header3,datas3]

def load4(dir):
  dir = "./"+dir+"/kepemilikan.csv"
  with open(dir, "r") as f4:
      raw_lines4 = f4.readlines()
  f4.close()

  lines4 = [raw_line.replace("\n", "") for raw_line in raw_lines4] # hapus spasi

  def convert_array_data_to_real_values4(array_data):
    arr_cpy = array_data[:]
    for i in range(1):    # ubah id ke integer           
      if(i == 1):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil = [temp]+hasil
              temp = ""
          else:
              temp += words
      hasil= [temp]+hasil
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  
  def my_pop(l):
    new = []
    l = list(l)
    for i in l:
        if l[-1] == i:
            pass
        else:
            new = [i]+new
    return new
  raw_header4 = lines4.my_pop(0)

  header4 = convert_line_to_data(raw_header4)

  datas4 = []

  for line in lines4:
    array_of_data = convert_line_to_data(line)
    real_values4 = convert_array_data_to_real_values4(array_of_data)
    datas4= [real_values4]+datas4
  return [header4,datas4]
