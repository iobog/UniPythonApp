class SelectionSort():
  def __init__(self,*, key = None, reverse = False):
    self.__key = key
    self.__reverse = reverse
    
  def sellsort(self, lista):
       
    n = len(lista)
    something=[]
    for i in lista:
      something.append(list(i[:]))

    
    for i in range(n-1):
      poz = i
      for j in range(i+1, n):
        if self.__compare(something[j],something[poz]):
          poz = j
      
      something[i],something[poz]=something[poz],something[i]
    lista = something
    return something
  
  def __compare(self, a, b):
    if self.__key:
      a_key = self.__key(a)
      b_key = self.__key(b)
    else:
      a_key, b_key = a, b
      
    if self.__reverse:
      return a_key > b_key
    else:
      return a_key < b_key
    
      
      
      
class ShakeSort():
  def __init__(self,* ,key = None, reverse = False):
    self.__key = key
    self.__reverse = reverse
  
  
  def __compare(self, a, b):
    if self.__key:
      a_key = self.__key(a)
      b_key = self.__key(b)
    else:
      a_key, b_key = a, b
      
    if self.__reverse:
      return a_key < b_key
    else:
      return a_key > b_key
    
  
    
  def shasort(self, data):
    
    n = len(data)
    
    something=[]
    for i in data:
      something.append(list(i[:]))
    print (something)
    chg = True
    while chg:
      chg = False
      for i in range(n-1):
        if self.__compare(something[i],something[i+1]):
          something[i],something[i+1] = something[i+1], something[i]
          chg = True
          print (something)
          
      if not chg:
        break
      
      for i in range(n-1,1,-1):
        if not self.__compare(something[i],something[i-1]):
          something[i-1],something[i] = something[i],something[i-1]
          chg = True
          print (something)
          
    data = something

    return something

#       schimbat = True
#       for i in range(n-1,0,-1):
#         # if lista[i][by_what] > lista[i-1][by_what]:
#         if not cmp(key(lista[i]),key(lista[i+1])):
#         # if not self.__comparator_shake(self.__r(lista,i,by_what), self.__r(lista,i-1,by_what), True):
#           lista[i], lista[i-1] = lista[i-1], lista[i]
#           schimbat = True
#     print (lista)
    
#     return lista
    