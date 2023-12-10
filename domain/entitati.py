class Student:
  def __init__(self, id, nume):
    """Initializeaza un student cu id ul id si numele nume

    Args:
        id (_type_): Id ul studentului
        nume (_type_): Numele studentului
    """
    self.__id = id
    self.__nume = nume
  
  def get_id(self):
    """Returneaza id-ul studentului
    """    
    return self.__id
  
  def get_nume(self):
    
    return self.__nume
  
  def set_nume(self, nume):
    self.__nume = nume
  
  def __eq__(self, student):
    if student == None:
      return False
    return self.get_id() == student.get_id() and self.get_nume() == student.get_nume()
    
    


class Disciplina:
  def __init__(self, id_dis, nume, prof):
    """ Initializeaza o disciplina cu: id id_dis, numele nume si profesor cu prof

    Args:
        id_dis (_type_): Id- ul disciplinei
        nume (_type_): Numele disciplinei
        prof (_type_): Numele profesorului de la disciplina
    """
    self.__id_dis = id_dis
    self.__nume = nume
    self.__prof = prof
  
  def get_id(self):
    """ Returneaza id ul disciplinei
    """
    return self.__id_dis
  
  def get_nume(self):
    """ Returneaza numele disciplinei
    """
    return self.__nume
  
  def set_nume(self, nume):
    """ Seteaza numele disciplinei la nume
    """
    self.__nume = nume
    
  def set_prof(self, prof):
    """ Seteaza profesorul disciplinei cu prof
    """
    self.__prof = prof
  
  def get_prof(self):
    """ Returneaza numele profesorului din cadrul discipninei
    """
    return self.__prof
  
  def __eq__(self, disciplina):
    if disciplina == None:
      return False
    return self.get_id() == disciplina.get_id()
    



class Grade:
  
  def __init__(self, id, student, disciplina, nota):
    """ Initializeaza o nota cu: id id, id_student id_student id_disciplina id_disciplina si nota cu nota
    """
    self.__id = id
    self.__student = student
    self.__disciplina = disciplina
    self.__nota = nota
    
  def get_id(self):
    """Returneaza id-ul notei
    """
    return self.__id
  
  def get_disciplina(self):
    """Returneaza id ul disciplinei 
    """
    return self.__disciplina
  
  def get_student(self):
    """Returneaza id-ul studentului"""
    return self.__student
  
  def get_nota(self):
    """Returneaza nota"""
    return self.__nota
  
  def set_nota(self, nota):
    """Seteaza nota existenta cu nota"""
    self.__nota = nota
  
  def __eq__(self, grade):
    if grade == None:
      return False
    return self.get_id() == grade.get_id()
    

class StudentGrade:
  """
    Data transfer object
  """
  def __init__(self,student_id, discipline_id, grade):
    self.__stID = student_id
    self.__disciplineid = discipline_id
    self.__grade = grade
    self.__name = None

  def getStudentID(self):
    """
     Getter method
    """
    return self.__stID
  def getGrade(self):
    """
    Getter method
    """
    return self.__grade
  def getDisciplineID(self):
    """
    Getter method
    """
    return self.__disciplineid

  def getStudentName(self):
    """
    Getter method
    """
    return self.__name

  def setStudentName(self,n):
    self.__name = n

