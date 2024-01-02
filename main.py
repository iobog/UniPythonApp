
from domain.validatori import DisciplinaValidator, StudentValidator, GradeValidator
# from domain.test import test_domain
from repository.FILLErepository import DisciplineFileRepository, GradeFileRepository, StudentFileRepository
from repository.repository import InMemoryRepositoryDisc, InMemoryRepositoryStud, InMemoryRepositoryGrade
# from repository.test import test_repository
from services.studentservices import StudentService
from services.disciplineservices import DisciplineService
from services.gradeservice import GradeService
# from services.test import test_services
from ui.console import Console

def test():
  # test_domain()
  # test_repository()
  # test_services()
  pass
  
def run():
  test()
  val = StudentValidator()
  val1 = DisciplinaValidator()
  val3 = GradeValidator()
  
  # repo = InMemoryRepositoryStud()
  # repo2 = InMemoryRepositoryDisc()
  # repo3 = InMemoryRepositoryGrade()

  # open("student.txt", "w").close()e
  # open("discipline.txt", "w").close()
  # open("note.txt", "w").close()
  
  repo = StudentFileRepository("student.txt")
  repo2 = DisciplineFileRepository("discipline.txt")
  repo3 = GradeFileRepository("note.txt")
  
  serv1 = StudentService(repo, val) 
  serv2 = DisciplineService(repo2,val1)
  serv3 = GradeService (repo, repo2, repo3, val3)
  
  ui = Console(serv1, serv2, serv3)
  
  ui.show_ui()
  


run()


# Este o copie a proiectului initialraport
