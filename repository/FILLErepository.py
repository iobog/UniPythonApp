



from domain.entitati import Disciplina, Grade, Student
from repository.repository import InMemoryRepositoryDisc, InMemoryRepositoryGrade, InMemoryRepositoryStud
from repository.repository import RepositoryConflictException,RepositoryNotFoundException,RepositoryException

class StudentFileRepository(InMemoryRepositoryStud):
  """
    Store/retrieve students from file
  """
  def __init__(self, file):
    InMemoryRepositoryStud.__init__(self)
    self.__file_name = file
    self.__load_from_file()

  def __load_from_file(self):
    """Load student from file"""
    f = open(self.__file_name, "r")
    line = f.readline().strip()
    while line !="":
      atr = line.split(";")
      st = Student(int(atr[0]), atr[1])
      InMemoryRepositoryStud.add(self,st)
      line= f.readline().strip()
    f.close()
  
  def remove_all(self):
    """
    Remove all the students from the repository
    post: the repository is empty
    """
    InMemoryRepositoryStud.removeAll(self)
    self.__store_to_file()

  def delete(self, id):
    st= InMemoryRepositoryStud.get(self, id)
    self.__store_to_file()
    return st
  
  def update(self, st):
    InMemoryRepositoryStud.update(self,st)
    self.__store_to_file()

  def add(self, st):
    InMemoryRepositoryStud.add(self, st)
    self.__store_to_file()
    

  def __store_to_file(self):
    #open file (rewrite file)
    f = open(self.__file_name, "w")
    sts = InMemoryRepositoryStud.get_all(self)
    for st in sts:
      strf = str(st.get_id())+";"+st.get_nume()+";"
      strf = strf+"\n"
      f.write(strf)
    f.close()





class DisciplineFileRepository(InMemoryRepositoryDisc):
  """
    Store/retrieve discipline from file
  """
  def __init__(self, file):
    InMemoryRepositoryDisc.__init__(self)
    self.__file_name = file
    self.__load_from_file()

  def __load_from_file(self):
    """Load student from file"""
    
    f = open(self.__file_name,"r")
    
    line = f.readline().strip()
    while line !="":
      atr = line.split(";")
      disciplina = Disciplina(int(atr[0]), atr[1], atr[2])
      InMemoryRepositoryDisc.add(self, disciplina)
      line= f.readline().strip()
    f.close()
  
  def remove_all(self):
    """
    Remove all the students from the repository
    post: the repository is empty
    """
    InMemoryRepositoryDisc.removeAll(self)
    self.__store_to_file()

  def delete(self, id):
    st= InMemoryRepositoryDisc.get(self, id)
    self.__store_to_file()
    return st
  
  def update(self, disciplina):
    InMemoryRepositoryDisc.update(self,disciplina)
    self.__store_to_file()

  def add(self, disciplina):
    InMemoryRepositoryDisc.add(self, disciplina)
    self.__store_to_file()
    

  def __store_to_file(self):
    #open file (rewrite file)
    f = open(self.__file_name, "w")
    discipline = InMemoryRepositoryDisc.get_all(self)
    for disciplina in discipline:
      strf = str(disciplina.get_id())+";"+disciplina.get_nume()+";"+disciplina.get_prof()+";"
      strf = strf+"\n"
      f.write(strf)
    f.close()




class GradeFileRepository(InMemoryRepositoryGrade):
  """
    Store/retrieve discipline from file
  """
  def __init__(self, file):
    InMemoryRepositoryGrade.__init__(self)
    self.__file_name = file
    self.__load_from_file()

  def __load_from_file(self):
    """Load student from file"""
    
    f = open(self.__file_name,"r")
    
    line = f.readline().strip()
    while line !="":
      atr = line.split(";")
      disciplina = Grade(int(atr[0]),int( atr[1]), int(atr[2]),int(atr[3]))
      InMemoryRepositoryGrade.add(self, disciplina)
      line= f.readline().strip()
    f.close()
  
  def remove_all(self):
    """
    Remove all the students from the repository
    post: the repository is empty
    """
    InMemoryRepositoryGrade.removeAll(self)
    self.__store_to_file()

  def delete(self, id):
    st= InMemoryRepositoryGrade.get(self, id)
    self.__store_to_file()
    return st
  
  def update(self, grade):
    InMemoryRepositoryGrade.update(self,grade)
    self.__store_to_file()

  def add(self, grade):
    InMemoryRepositoryGrade.add(self, grade)
    self.__store_to_file()
    

  def __store_to_file(self):
    #open file (rewrite file)
    f = open(self.__file_name, "w")
    grades = InMemoryRepositoryGrade.get_all(self)
    for grade in grades:
      strf = str(grade.get_id())+";"+str(grade.get_student())+";"+str(grade.get_disciplina())+";"+str(grade.get_nota())+";"
      strf = strf+"\n"
      f.write(strf)
    f.close()
