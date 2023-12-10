
from domain.entitati import Student
from domain.validatori import ValidatorException
from repository.repository import RepositoryConflictException, RepositoryNotFoundException
from services.exception import ServiceException

import random
import string

class StudentService:
  """ Classa responsabila cu operatiile CRUD pt studenti
      GRASP controler
  """
  def __init__(self, repository, validator):
    """
      Initializeaza controlerul
      controlerul are nevoie de un validator și de un repository pentru a efectua operațiunile
      repo - InMemoryRepositoryStud()
      val - StudentValidator ()
    """
    self.__repository = repository
    self.__validator = validator
  
  def create(self, id, nume):
    """Creeaza un student valid si il memoreaza

    Args:
        id (_type_): Id ul studentului
        nume (_type_): Numele studentului

    Raises:
        ServiceException: Daca studentul mai exista
        ServiceException: Daca studentul nu este valid
        ServiceException: Ceva nu a functionat

    Returns:
        _type_: Student
    """
    try:
      student = Student(id, nume)
      self.__validator.validate(student)
      self.__repository.add(student)
    except RepositoryConflictException: 
      raise ServiceException("Nepermis! Student exista deja!")
    except ValidatorException as ex:
      raise ServiceException(ex)
    except Exception:
      raise ServiceException("Ceva nu a functionat")
    
    return student
  def update(self, id, nume):
    """
    Actualizeaza numele unui student, daca exista
    Args:
        id (_type_): Id ul studentului
        nume (_type_): Numele stduentului
    Raises:
        ServiceException: Daca studentul nu exista
    """
    try:
      student = Student(id, nume)
      self.__validator.validate(student)
      student_existent = self.__repository.get(student.get_id())
      if student_existent is None: 
        raise ServiceException("Studentul nu exista")
      self.__repository.update(student)
    except RepositoryNotFoundException:
      raise ServiceException("Nepermis! Student inexistent")
    
    
  def delete(self, id, nume):
    """Sterge studentul cu id ul id

    Args:
        id (_type_): Id-ul studentului
        nume (_type_): Numele studentului

    Raises:
        ServiceException: Studentul nu exista
    """
    try:
      student = Student(id, nume)
      self.__validator.validate(student)
      self.__repository.delete(student)
    except:
      raise ServiceException ("Studentul nu exista")
  
  def get_by_id(self, id):
    """ Retunreaza studentul cu id-ul id
    Args:
        id (_type_): Id ul studentului
        nume (_type_): Numele studentului
    Raises:
        ServiceException: Nu exista studentul

    Returns:
        _type_: Studentul cu id-ul id
    """
    studenti = self.__repository.get(id)
    if studenti == None:
      raise ServiceException("Nu exista studenti")
    return studenti
  
      
  
  def get_all(self):
    """
      Returneaza toti studenti 
    """
    studenti = self.__repository.get_all()
    if len(studenti) == 0:
      raise ServiceException("Nu exista studenti")
    return studenti
  
  
  def generate_students(self): 
    """
      Genereaza un student random
    """
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    cif = string.digits
    t = random.randint(0, 999)
    t = int(t)
    id = t
    t = random.randint(0, 7)
    t = int(t)  
    name = "".join(random.choice(upper))
    name += "".join(random.choices(lower,k =t))
    name = name +" "
    name += "".join(random.choice(upper))
    name += "".join(random.choices(lower, k =t))
      
    try:
      id = int(id)
      student = Student(id, name)
      self.__validator.validate(student)
      self.__repository.add(student)
      return student
    except RepositoryConflictException: 
      raise ServiceException("Nepermis! Student exista deja!")
    except ValidatorException as ex:
      raise ServiceException(ex)
    except Exception:
      raise ServiceException("Ceva nu a functionat")
    
      
    
      
  
    
    