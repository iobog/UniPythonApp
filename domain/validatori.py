
from domain.entitati import Student, Disciplina, Grade
class ValidatorException(Exception):
  def __init__(self, erori) :
    self.__erori = erori
    
  def __str__(self):
    #return "\n".join(self.__erori)
    return self.__erori
  def __len__(self):
      return len(self.__erori) 


class StudentValidator():
  
  def validate(self, student):
    erori = []
    if student.get_id() == None: erori.append("Id nu poate sa lipseasca")
    if student.get_nume() == None :erori.append("Numele nu poate sa lipsasca")

    if len(erori) > 0 :
      raise ValidatorException(erori)
    
class DisciplinaValidator():
  
  def validate(self, disciplina):
    erori = []
    if disciplina.get_id() == None:
      erori.append("Id nu poate sa lipseasca! Trebuie sa fie un numar mai mare decat 1!")
    if disciplina.get_nume() == None :erori.append("Numele nu poate sa lipsasca")
    if disciplina.get_prof() == None :erori.append("Profesorul nu poate sa lipsasca")
            
    if len(erori) > 0:
      raise ValidatorException(erori) 


class GradeValidator():
  
  def validate(self, grade):
    
    erori = []
    if grade.get_id() == None:
      erori.append("Id nu poate sa lipseasca! Trebuie sa fie un numar mai mare decat 1!")
    if grade.get_disciplina() == None:
      erori.append("Disciplina nu poate sa lipseasca!")
    if grade.get_student() == None:
      erori.append("Studentul nu poate sa lipseasca!")
    if int(grade.get_nota()) < 1 or int(grade.get_nota() > 10):
      erori.append("Nota invalida")
    
    if len(erori) > 0:
      raise ValidatorException(erori) 

    
      