
from domain.entitati import Grade
from domain.validatori import GradeValidator, ValidatorException
from repository.repository import RepositoryConflictException, RepositoryNotFoundException
from services.exception import ServiceException

import random
import string

class GradeService:
  
  def __init__(self, student_repository, disciplina_repository, repository_garade, validator):
   
    self.__repository_grade = repository_garade
    self.__repository_student = student_repository
    self.__repository_disciplina= disciplina_repository
    self.__validator = validator
  
  def create_grade(self, id, student, disciplina, nota):
    """ Asigneaza unui student o nota la o disciplina
    """
    try:
      st = self.__repository_student.get(student)
      disc = self.__repository_disciplina.get(disciplina)
      if disc == None:
        raise RepositoryNotFoundException
      if st == None:
        raise RepositoryNotFoundException
      
      one_grade = Grade(id, student, disciplina, nota)
      self.__validator.validate(one_grade)
      self.__repository_grade.add(one_grade)
    except RepositoryConflictException: 
      raise ServiceException("Nepermis! Student exista deja!")
    except ValidatorException as ex:
      raise ServiceException(ex)
    except Exception:
      raise ServiceException("Ceva nu a functionat")
    return one_grade
  
  def update_grade(self, id, student, disciplina, nota):
    """
    Actualizarea unei note oferite studentului la materie
    """
    try:
      if self.__repository_student.get(student) == None or self.__repository_disciplina.get(disciplina) == None:
        raise ServiceException("Student sau disciplina inexistenta")
      grade = Grade(id, student, disciplina, nota)
      self.__validator.validate(grade)
      student_existent = self.__repository_student.get(grade.get_id())
      if student_existent is None: 
        raise ServiceException("Studentul nu exista")
      self.__repository_grade.update(grade)
    except RepositoryNotFoundException:
      raise ServiceException("Nepermis! Student inexistent")
    
    return grade
    
  def delete_grade(self, id, student, disciplina, nota):
    """Sterge nota cu id ul id
    """
    try:
      if self.__repository_student.get(student) == None or self.__repository_disciplina.get(disciplina) == None:
        raise ServiceException("Student sau disciplina inexistenta")
      grade = Grade(id, student, disciplina, nota)
      self.__validator.validate(grade)
      self.__repository_grade.delete(grade)
    except:
      raise ServiceException ("Studentul nu exista")
  
  def get_grade_by_id(self, id):
    """ Retunreaza Nota cu id-ul id
    """
    grade = self.__repository_grade.get(id)
    if grade == None:
      raise ServiceException("Nu exista Nota")
    rezultat =[]
    # grade =(id, id student, id disciplina, nota)
    # numele studentului
    student = self.__repository_student.get(grade.get_student())
    disciplina = self.__repository_disciplina.get(grade.get_disciplina())
    rezultat.append(student.get_nume())
    rezultat.append(disciplina.get_nume())
    rezultat.append(grade.get_nota())
    return rezultat
  
      
  
  def get_all_grades(self):
    """
      Returneaza toate notele 
    """
    rezultate =[]
    note = self.__repository_grade.get_all()
    if len(note) == 0:
      raise ServiceException("Nu exista note")
    for grade in note:
      rezultat =[]
      # grade =(id, id student, id disciplina, nota)
      # numele studentului
      student = self.__repository_student.get(grade.get_student())
      disciplina = self.__repository_disciplina.get(grade.get_disciplina())
      rezultat.append(grade.get_id())
      rezultat.append(student.get_nume())
      rezultat.append(disciplina.get_nume())
      rezultat.append(grade.get_nota())
      rezultate.append(rezultat)
    return rezultate
    
  # def get_all_Disc(self, lista_iduri_discipline):
  #   """ Returneaza toate notele pentru toti studenti de la disciplina disc
  #   """

  #   rez= []
  #   note = self.__repository.get_all()
  #   for nota in note:
  #     if nota.get_id_disciplina() in lista_iduri_discipline.values():
  #       new_list = []
  #       new_list.append(nota.get_id_student())
  #       new_list.append(nota.get_nota())
  #       rez.append(new_list)
  #   rez.sort(key = lambda x:(x[0], -x[1]))
  #   # sortez rezultate
  
  def get_all_student_and_grade_specific_discipline(self, disciplina):
    """Returneaza toati studenti si notele lor la disciplina disciplina ordonati alfabetic
    """
    if self.__repository_disciplina.get(disciplina) == None:
      raise RepositoryNotFoundException("Disciplina Inexistenta")
    
    rezultate = {}
    all_grades = self.__repository_grade.get_all()
    for grade in all_grades:
      if grade.get_disciplina() == disciplina:
        
        student = self.__repository_student.get(grade.get_student())
        student_name = student.get_nume()
        if student_name in rezultate:
          rezultate[student_name].append(grade.get_nota())
        else:
          rezultate[student_name] = [grade.get_nota()]
    
    # sortat alfabetic dupa nume
    rezultate_sortate = dict(sorted(rezultate.items()))
    return rezultate_sortate
  
  def top_20_studenti(self):
    """Returneaza 20% dintre cei mai buni studenti"""
    rezultate = {}
    number = (len(self.__repository_student)) // 5
    all_grades = self.__repository_grade.get_all()

    for grade in all_grades:        
      student = self.__repository_student.get(grade.get_student())
      student_id = student.get_id()
      if student_id in rezultate:
        rezultate[student_id].append(grade.get_nota())
      else:
        rezultate[student_id] = [grade.get_nota()]
    
    sums = {}
    for key, values in rezultate.items():
        sums[key] = sum(values)/len(values)
        
    rezultat_sortat = dict(sorted(sums.items(), key = lambda item: item[1],reverse = True ))
    rezultate={}
    for key in rezultat_sortat.keys():
      rezultate[key] = rezultat_sortat[key]
      if number == 1: 
        return rezultate
      number -= 1

  def top_20_discipline(self):
    """Returneaza cele mai bune 20% discipline
    """
    rezultate = {}
    number = (len(self.__repository_disciplina)) // 5
    all_grades = self.__repository_grade.get_all()

    for grade in all_grades:        
      disciplina = self.__repository_disciplina.get(grade.get_disciplina())
      disciplina_id = disciplina.get_id()

      if disciplina_id in rezultate:
        rezultate[disciplina_id].append(grade.get_nota())
      else:
        rezultate[disciplina_id] = [grade.get_nota()]
    
    sums = {}
    for key, values in rezultate.items():
        sums[key] = sum(values)/len(values)
    rezultat_sortat = dict(sorted(sums.items(), key = lambda item: item[1],reverse = True ))

    rezultate={}
    for key in rezultat_sortat.keys():
      rezultate[key] = rezultat_sortat[key]
      if number == 1: 
        return rezultate
      number -= 1