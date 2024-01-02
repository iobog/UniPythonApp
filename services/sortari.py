 

class Sort(object):

    def identitate(self):
        return object

    def negatie(self):
        return not object

    def sort(self, lista,*, key=lambda x: x, cmp= lambda x,y: x<y , reverse=False):
        pass



class ShakeSort(Sort):
  
  def shake_sort(self, lista, key, cmp, operatie):
    """Functie de sortare """

    n = len(lista)

    schimbat = True

    while schimbat:
      schimbat = False
      for i in range(0, n-1):
        #if lista[i][by_what] < lista[i+1][by_what]:
        if cmp(key(lista[i]),key(lista[i+1])):
        # if self.__comparator_shake(self.__r(lista,i,by_what),self.__r(lista,i,by_what), True):
          lista[i], lista[i+1] = lista[i+1], lista[i]
          schimbat = True
      
      if not schimbat:
        break 

      schimbat = True
      for i in range(n-1,0,-1):
        # if lista[i][by_what] > lista[i-1][by_what]:
        if not cmp(key(lista[i]),key(lista[i+1])):
        # if not self.__comparator_shake(self.__r(lista,i,by_what), self.__r(lista,i-1,by_what), True):
          lista[i], lista[i-1] = lista[i-1], lista[i]
          schimbat = True
    print (lista)
    
    return lista

  def sort(self, lista, *, key=lambda x: x, cmp=lambda x, y: x < y, reverse=False):
    if reverse:
      operatie=self.negatie()
    else:
      operatie=self.identitate()
    self.shake_sort(lista,key,cmp,operatie)

class SelectionSort(Sort):
  
  def selection_sort(self, lista, key, cmp, operatie, reverse = False):
    """Algoritm de sortare 
      
    """

    something=[]
    for i in lista:
      something.append(i[:])

    for i in range(0,len(lista)-1):
      poz_max= i
      for j in range(i+1,len(lista)):
       
        # sortare dupa nume -- numele fiind pe pozitia 0
        #if self.__comparator_selection(self.__r(lista, j, by_what), self.__r(lista, poz_max,by_what)):
        if cmp(key(lista[j]),key(lista[poz_max])):
          poz_max = j
      
      #self.____swp(lista[i],lista[poz_max])
      lista[i],lista[poz_max] = lista[poz_max],lista[i]
    print (lista)
    if reverse: 
        lista.reverse()
    print (lista)
    return lista
  

  
  def sort(self, lista, *, key = lambda x: x[1], cmp=lambda x, y: x < y, reverse=False):
    lista = list(lista)
    if reverse:
      operatie = self.negatie()
    else:
      self.identitate()
    self.selection_sort(lista, key, cmp, operatie)

