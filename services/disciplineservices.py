


from domain.entitati import Disciplina
from repository.repository import RepositoryConflictException, RepositoryNotFoundException
from services.exception import ServiceException
from domain.validatori import ValidatorException

import random
import string



class DisciplineService:
 
  def __init__(self, repository, validator):
    """
      Initializeaza controlerul
        controlerul are nevoie de un validator și de un repository pentru a efectua operațiunile
        repo - InMemoryRepositoryDisc()
        val - DisciplinaValidator ()
    """
    self.__repository = repository
    self.__validator = validator
    
  def create_disc(self, id, nume, prof):
    """Creeaza o disciplina valida si o memoreaza

    Args:
        id : Id ul disciplinei
        nume : Numele disciplinei
        prof : Numele cadrului didactic

    Raises:
        ServiceException: Daca disciplina mai exista 
        ServiceException: Daca disciplina nu este valida
        ServiceException: Ceva nu a functionat
    Returns:
        _type_: Disciplina
    """
    try:
      disc = Disciplina(id, nume, prof)
      self.__validator.validate(disc)
      self.__repository.add(disc)
    except RepositoryConflictException: 
      raise ServiceException("Nepermis! Disciplina exista deja!")
    except ValidatorException as ex:
      raise ServiceException(ex)
    except Exception:
      raise ServiceException("Ceva nu a functionat")
    return disc

  def update_disciplina(self, id, nume, prof):
    """
    Actualizeaza o disciplina cu nume si prof, daca exista
    Args:
        id (_type_): Id ul disciplinei
        nume (_type_): Numele disciplinei
        prof (_type_): Profesorul diisciplinei

    Raises:
        ServiceException: Daca disciplina nu exista
    """
    try:
      disciplina = Disciplina(id, nume, prof)
      self.__validator.validate(disciplina)
      discpilina_existenta = self.__repository.get(disciplina.get_id())
      if discpilina_existenta is None: 
        raise ServiceException("Disciplina nu exista")
      self.__repository.update(disciplina)
    except RepositoryNotFoundException:
      raise ServiceException("Nepermis! Disciplina inexistenta")
  
  
  def get_disciplina_by_id(self, id):
    """ Retunreaza disciplina cu id ul id

    Args:
        id (_type_): Id ul disciplinei
        nume (_type_): Numele disciplinei
        prof (_type_): Profesorul disciplinei

    Raises:
        ServiceException: Nu exista disciplina

    Returns:
        _type_: Disciplina cu id-ul id
    """
    disciplina = self.__repository.get(id)
    if disciplina == None:
      raise ServiceException ("Nu exista disciplina")
    return disciplina

  def delete_disciplina(self, id, nume, prof):
    """Sterge disciplina cu id-ul id 

    Args:
        id (_type_): Id-ul disciplinei
        nume (_type_): Numele disciplinei
        prof (_type_): Profesorul disciplinei

    Raises:
        ServiceException: _description_
    """
    try:
      disciplina = Disciplina(id, nume, prof)
      self.__validator.validate(disciplina)
      self.__repository.delete(disciplina)
    except:
      raise ServiceException("Disciplina nu exista")
    
  def get_all_discipline(self):
    """
      Returneaza toate disciplinele 
    """
    discipline = self.__repository.get_all()
    if len(discipline) == 0:
      raise ServiceException("Nu exista discipline")
    return discipline
    
  def generate_discipline(self):
    """Genereaza o disciplina aleatorie
    """
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    t = random.randint(0, 999)
    t = int(t)
    id = t
    t = random.randint(3, 8)
    t = int(t)  
    name = "".join(random.choice(upper))
    name += "".join(random.choices(lower,k =t))
    name = name +" "
    name += "".join(random.choice(upper))
    name += "".join(random.choices(lower, k =t))
    
    t = random.randint(3, 8)
    t = int(t)  
    prof = "".join(random.choice(upper))
    prof += "".join(random.choices(lower,k =t))
    prof = prof +" "
    prof += "".join(random.choice(upper))
    prof += "".join(random.choices(lower, k =t))
     
    try:
      id = int(id)
      disciplina = Disciplina(id, name, prof)
      self.__validator.validate(disciplina)
      self.__repository.add(disciplina)
      return disciplina
    except RepositoryConflictException: 
      raise ServiceException("Nepermis! Disciplina existenta!")
    except ValidatorException as ex:
      raise ServiceException(ex)
    except Exception:
      raise ServiceException("Ceva nu a functionat")
    
  # def list_id_discipline_with_same_id(self, nume):
  #   """Returneaza o lista de id uri ale disciplinelor care au numele nume
  #   """
  #   all_discipline = self.__repository.get_all()
  #   id_list = {}
  #   for disciplina in all_discipline :
  #     if nume == disciplina.get_nume():
  #       id_list[disciplina.get_id()] = disciplina.get_id()

  #   return id_list

