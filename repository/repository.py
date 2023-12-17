class RepositoryException(Exception):
  def __init__(self):
    Exception.__init__(self)
  
class RepositoryConflictException(RepositoryException):
  def __init__(self):
    RepositoryException.__init__(self)
  
class RepositoryNotFoundException(RepositoryException):
  def __init__(self):
    RepositoryException.__init__(self)
  
  
  
class InMemoryRepositoryStud:
  """
  Clasa responsabilă cu gestionarea unei liste de studenți (stocare, get, get all, stergere, actualizare etc.)
  
  """
  def __init__(self):
    self.__entitati = {}
    
  def add(self, entitate):
    """
      Memoreaza un student
      entitate - student
    Raises:
        RepositoryConflictException: studentul cu acelasi id mai exista 
    """

    if entitate.get_id() in self.__entitati.keys():
      raise RepositoryConflictException()
    self.__entitati[entitate.get_id()] = entitate
    
  def get(self, id):
    """Returneaza un studentul cu id-ul id, daca existata"""
    lis = list(self.__entitati.items())
    t = self.__recursive_get(lis, id)
    return t
    

  def __recursive_get(self, lista, element):
    """verifica daca element se afla in lista disc"""
    if lista == [] : 
      return None
    if lista[0][0] == element: 
      return (lista[0][1])
    return self.__rec(lista[1:], element)



  # def get(self, id):
  #   """Returneaza un studentul cu id-ul id, daca exusta
  #   """
  #   if id not in self.__entitati.keys():
  #     # raise RepositoryNotFoundException()
  #     return None
  #   return self.__entitati[id]
  
  def get_all(self):
    """Returneaza toti studentii
    """
    return self.__entitati.values()
    
  def update(self, entitate):
    """Actualizeaza stidentul  cu entitate
    enitatete - studentul cu datele actualizate
    """
    if entitate.get_id() not in self.__entitati.keys():
      raise RepositoryNotFoundException()
    self.__entitati[entitate.get_id()] = entitate
  
  def delete(self, entitate):
    """Sterge entitatea, daca exista
    """
    if entitate.get_id() not in self.__entitati.keys():
      raise RepositoryNotFoundException()
    self.__entitati.pop(entitate.get_id())
    
  
  def __len__(self):
    """
      Returneaza nr de studenti din repository
    """
    return len(self.__entitati.keys())
   
  # def removeAll(self):
  #   """Sterge toti studentii"""
  #   self.__entitati={}
   
  def removeAll(self):
    """Sterge toti studentii"""
    self.__entitati = self.__recRemoveAll(list(self.__entitati.items()))

  def __recRemoveAll(self, disc):
    """Sterge toate elementele din lista disc"""
    if not disc:  
      return {}

    return self.__recRemoveAll(disc[1:])
    

class InMemoryRepositoryDisc:
  """
  Clasa responsabilă cu gestionarea unei liste de discipline (stocare, get, get all, stergere, actualizare etc.)
  
  """
  def __init__(self):
    self.__entitati = {}
    
  def add(self, entitate):
    """
      Memoreaza o disciplina
      entitate - disciplina
    Raises:
        RepositoryConflictException: Disciplina cu acelasi id mai exista 
    """
    if entitate.get_id() in self.__entitati.keys():
      raise RepositoryConflictException()
    self.__entitati[entitate.get_id()] = entitate
    
  def get(self, id):
    """Returneaza disciplina cu id-ul id, daca exusta

    Args:
        id (_type_): Id disciplina

    Returns:
        _type_: _description_
    """
    if id not in self.__entitati.keys():
      # raise RepositoryNotFoundException()
      return None
    return self.__entitati[id]
  
  def get_all(self):
    """Returneaza toate disciplinele
    """
    return self.__entitati.values()
    
  def update(self, entitate):
    """Actualizeaza disciplina  cu entitate
    enitatete - disciplina cu datele actualizate
    """
    if entitate.get_id() not in self.__entitati.keys():
      raise RepositoryNotFoundException()
    self.__entitati[entitate.get_id()] = entitate
  
  def delete(self, entitate):
    """Sterge entitatea, daca exista
    """
    if entitate.get_id() not in self.__entitati.keys():
      raise RepositoryNotFoundException()
    self.__entitati.pop(entitate.get_id())
    
  def removeAll(self):
    """Sterge toate disciplinele
    """
    self.__entitati={}

  def __len__(self):
    return len(self.__entitati.keys())
  




class InMemoryRepositoryGrade():
  def __init__(self):
    self.__entitati ={}
    
  def add(self, entitate):
    """
      Memoreaza o nota
      entitate - nota
    Raises:
        RepositoryConflictException: Nota cu acelasi id mai exista 
    """
    
    if entitate.get_id() in self.__entitati.keys():
      raise RepositoryConflictException()
    self.__entitati[entitate.get_id()] = entitate
    
  def get(self, id):
    """Returneaza nota cu id-ul id, daca exista

    Args:
        id (_type_): Id nota

    Returns:
        Nota: Nota cu id ul id
    """
    if id not in self.__entitati.keys():
      # raise RepositoryNotFoundException()
      return None
    return self.__entitati[id]
  
  def get_all(self):
    """Returneaza toate notele
    """
    return self.__entitati.values()
    
  def update(self, entitate):
    """Actualizeaza nota  cu entitate
    enitatete - nota cu datele actualizate
    """
    if entitate.get_id() not in self.__entitati.keys():
      raise RepositoryNotFoundException()
    self.__entitati[entitate.get_id()] = entitate
  
  def delete(self, entitate):
    """Sterge entitatea, daca exista
    """
    if entitate.get_id() not in self.__entitati.keys():
      raise RepositoryNotFoundException()
    self.__entitati.pop(entitate.get_id())

  def removeAll(self):
    """Sterge toate disciplinele
    """
    self.__entitati={}
  def __len__(self):
    return len(self.__entitati.keys())
  

    