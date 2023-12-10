from domain.entitati import Disciplina, Grade, Student
from domain.validatori import DisciplinaValidator, GradeValidator, StudentValidator
from repository.repository import InMemoryRepositoryDisc, InMemoryRepositoryGrade, InMemoryRepositoryStud, RepositoryConflictException, RepositoryNotFoundException
from services.disciplineservices import DisciplineService
from services.gradeservice import GradeService
from services.studentservices import StudentService
import random
import unittest
# def test_create():
#   """ Testez functia pentru adaugare student
#   """
#   id = 1
#   nume = 'Vlad'
#   repo = InMemoryRepositoryStud()
#   val = StudentValidator()
#   serv = StudentService(repo, val)
#   serv.create(id, nume)
#   assert len(repo) == 1
  
# def test_update():
#   """ Testez functia pentru actualizare student
#   """
#   id = 1
#   nume = 'Vlad'
#   repo = InMemoryRepositoryStud()
#   val = StudentValidator()
#   serv = StudentService(repo, val)
#   serv.create(id, nume)
#   nume = "Vasile"
#   serv.update(id, nume)
#   get_student = serv.get_by_id(id)
#   assert get_student == Student(id, nume)

  
# def test_delete():
#   """ Testez functia pentru stergere student
#   """
#   id = 1
#   nume = 'Vlad'
#   repo = InMemoryRepositoryStud()
#   val = StudentValidator()
#   serv = StudentService(repo, val)
#   serv.create(id, nume)
#   serv.delete(id, nume)
#   assert len(repo) == 0
  
# def test_get_by_id():
#   """ Testez functia pentru cautare student dupa Id
#   """
#   id = 1
#   nume = 'Vlad'
#   repo = InMemoryRepositoryStud()
#   val = StudentValidator()
#   serv = StudentService(repo, val)
#   serv.create(id, nume)
#   st = serv.get_by_id(id)
#   assert st != None
#   # st = serv.get_by_id(2)
#   # assert st == None
  
# def test_get_all():
#   """ Test functia pentru get_all students
#   """
#   id = 1
#   nume = 'Vlad'
#   repo = InMemoryRepositoryStud()
#   val = StudentValidator()
#   serv = StudentService(repo, val)
#   serv.create(id, nume)
#   serv.create('2',"vasile")
#   students = serv.get_all()
#   assert len(students) == 2
  
# def test_random():
#   """ Test functia pentru generarea unui student aleatoriu
#   """
#   random.seed(123)
#   repo = InMemoryRepositoryStud()
#   val = StudentValidator()
#   serv = StudentService(repo, val)
#   st1 = serv.generate_students()
#   random.seed(123)
#   repo = InMemoryRepositoryStud()
#   val = StudentValidator()
#   serv = StudentService(repo, val)
  
#   st4 = serv.generate_students()
 
#   assert st1.get_id() == st4.get_id()
  
# def test_create_disciplina():
#   """ Test functia pentru adaugare disciplina
#   """
#   id = 1
#   nume = "matemtaica"
#   prof = "marius"
#   repo = InMemoryRepositoryDisc()
#   val = DisciplinaValidator()
#   serv = DisciplineService(repo, val)
#   serv.create_disc(id, nume, prof)
#   assert len(repo) == 1

# def test_update_disciplina():
#   """ Test functia pentru actualizare disciplina  
#   """
#   id = 1
#   nume = "matemtaica"
#   prof = "marius"
#   repo = InMemoryRepositoryDisc()
#   val = DisciplinaValidator()
#   serv = DisciplineService(repo, val)
#   serv.create_disc(id, nume, prof)
#   nume = "matematica"
#   prof = "Virgil"
#   serv.update_disciplina(id, nume, prof)
#   get_disciplina = serv.get_disciplina_by_id(id)
#   assert get_disciplina == Disciplina(id, nume, prof)

# def test_get_disciplina_by_id():
#   """ Test functia pentru determinarea unei discipline dupa id
#   """
#   id = 1
#   nume = "matemtaica"
#   prof = "marius"
#   repo = InMemoryRepositoryDisc()
#   val = DisciplinaValidator()
#   serv = DisciplineService(repo, val)
#   serv.create_disc(id, nume, prof)
  
#   d = serv.get_disciplina_by_id(id)
#   assert d == Disciplina(id, nume, prof)

# def test_delete_disciplina():
#   """Test functia de stergere a unei discipline
#   """
#   repo = InMemoryRepositoryDisc()
#   val = DisciplinaValidator()
#   serv = DisciplineService(repo, val)
#   serv.create_disc(0, "matematica", "marius A")
#   serv.create_disc(1, "informatica", "virgil A")
#   serv.create_disc(2, "geografie", "ioan B")
#   serv.delete_disciplina(1,"informatica","virgil A")
#   assert len(repo) == 2
  
# def test_get_all_dsciipline():
#   """Test functia de get all pentru discipline"""
#   repo = InMemoryRepositoryDisc()
#   val = DisciplinaValidator()
#   serv = DisciplineService(repo, val)
#   serv.create_disc(0, "matematica", "marius A")
#   serv.create_disc(1, "informatica", "virgil A")
#   serv.create_disc(2, "geografie", "ioan B")
#   discipline = serv.get_all_discipline()
#   assert len(discipline) == 3

# def test_random_disciplina():
#   """Test functia de genrat aleatoriu o disciplina"""
#   random.seed(123)
#   repo = InMemoryRepositoryDisc()
#   val = DisciplinaValidator()
#   serv = DisciplineService(repo, val)
#   disciplina1 = serv.generate_discipline()
#   random.seed(123)
#   repo = InMemoryRepositoryDisc()
#   val = DisciplinaValidator()
#   serv = DisciplineService(repo, val)
  
#   disciplina2 = serv.generate_discipline()
 
#   assert disciplina1.get_id() == disciplina2.get_id()
  


# def test_create_grade():
#   """ Test functie asignare nota
#   """
#   student_repository = InMemoryRepositoryStud()
#   student_service = StudentService(student_repository,StudentValidator())

#   disciplina_repository = InMemoryRepositoryDisc()
#   disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
#   student_service.create(1, "ioan")
#   disciplina_service.create_disc(1,"mate","marius")

#   grade_repository = InMemoryRepositoryGrade()
#   grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

#   grade = grade_service.create_grade(1,1,1,10)

#   assert grade.get_id() == 1
#   assert grade.get_student() == 1
#   assert grade.get_disciplina() ==1
#   assert grade.get_nota() == 10





# def test_update_grade():
#   """Test functia de actualizare a notei
#   """
#   student_repository = InMemoryRepositoryStud()
#   student_service = StudentService(student_repository,StudentValidator())

#   disciplina_repository = InMemoryRepositoryDisc()
#   disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
#   student_service.create(1, "ioan")
#   disciplina_service.create_disc(1,"mate","marius")

#   grade_repository = InMemoryRepositoryGrade()
#   grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

#   grade = grade_service.create_grade(1,1,1,10)

#   new_one = grade_service.update_grade(1,1,1,6)

#   assert grade.get_nota() != new_one.get_nota()


# def test_delete_grade():
#   """Test functia de stergere a unei note acordate
#   """
#   student_repository = InMemoryRepositoryStud()
#   student_service = StudentService(student_repository,StudentValidator())

#   disciplina_repository = InMemoryRepositoryDisc()
#   disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
#   student_service.create(1, "ioan")
#   disciplina_service.create_disc(1,"mate","marius")

#   grade_repository = InMemoryRepositoryGrade()
#   grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

#   grade = grade_service.create_grade(1,1,1,10)
#   assert len(grade_repository) == 1
#   grade_service.delete_grade(1,1,1,10)
#   assert len(grade_repository) == 0 



# def test_get_by_id_grade():
#   """Test functia de get pentu o singura nota
#   """
#   student_repository = InMemoryRepositoryStud()
#   student_service = StudentService(student_repository,StudentValidator())

#   disciplina_repository = InMemoryRepositoryDisc()
#   disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
#   student_service.create(1, "ioan")
#   disciplina_service.create_disc(1,"mate","marius")

#   grade_repository = InMemoryRepositoryGrade()
#   grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

#   grade = grade_service.create_grade(1,1,1,10)
#   rezultat = grade_service.get_grade_by_id(1)
#   assert rezultat[0] == "ioan"
#   assert rezultat[1] == "mate"
#   assert rezultat[2] == 10
#   # assert get_grade == Grade(id, id_student, id_disciplina, grade)

# def test_get_all_grades():
#   """Test functia de get all pentru note
#   """
#   student_repository = InMemoryRepositoryStud()
#   student_service = StudentService(student_repository,StudentValidator())

#   disciplina_repository = InMemoryRepositoryDisc()
#   disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
#   student_service.create(1, "ioan")
#   disciplina_service.create_disc(1,"mate","marius")

#   grade_repository = InMemoryRepositoryGrade()
#   grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

#   grade = grade_service.create_grade(1,1,1,10)
#   rezultat = grade_service.get_all_grades()

#   assert len(rezultat) == 1

#   grade = grade_service.create_grade(2,1,1,5)
#   rezultat = grade_service.get_all_grades()
#   assert len(rezultat) == 2

#   grade = grade_service.create_grade(3,1,1,5)
#   rezultat = grade_service.get_all_grades()
#   assert len(rezultat) == 3

#   # assert get_grade == Grade(id, id_student, id_disciplina, grade)

# def test_get_all_student_and_grade_specific_discipline():
#   """ Test functia 
#   """
#   student_repository = InMemoryRepositoryStud()
#   student_service = StudentService(student_repository,StudentValidator())

#   disciplina_repository = InMemoryRepositoryDisc()
#   disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
#   student_service.create(1, "ioan")
#   student_service.create(2, "andrei")
#   disciplina_service.create_disc(1,"mate","marius")

#   grade_repository = InMemoryRepositoryGrade()
#   grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

#   grade = grade_service.create_grade(1,1,1,10)
#   grade = grade_service.create_grade(2,2,1,10)

#   rezultate = grade_service.get_all_student_and_grade_specific_discipline(1)
#   # expected order
#   expected_order = ["andrei", "ioan"]

#   # Convert dictionary keys to a list
#   actual_order = list(rezultate.keys())

#   assert actual_order == expected_order
  

# def test_top20_studenti():
#   """ Test functia 
#     """
#   student_repository = InMemoryRepositoryStud()
#   student_service = StudentService(student_repository,StudentValidator())

#   disciplina_repository = InMemoryRepositoryDisc()
#   disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
#   student_service.create(1, "ioan")
#   student_service.create(2, "andrei")
#   student_service.create(3, "stefan")
#   student_service.create(4, "virgil")
#   student_service.create(5, "anotn")
#   disciplina_service.create_disc(1,"mate","marius")

#   grade_repository = InMemoryRepositoryGrade()
#   grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

#   grade = grade_service.create_grade(1,1,1,10)
#   grade = grade_service.create_grade(2,2,1,5)
#   grade = grade_service.create_grade(3,3,1,6)
#   grade = grade_service.create_grade(4,4,1,7)
#   grade = grade_service.create_grade(5,5,1,8)
  
#   rezultate = grade_service.top_20_studenti()
#   assert len(rezultate) == 1
#   assert 1 in rezultate.keys()
#   assert rezultate[1] == 10



# def test_top_20_dicipline():
#   """ Test functia 
#     """
#   student_repository = InMemoryRepositoryStud()
#   student_service = StudentService(student_repository,StudentValidator())

#   disciplina_repository = InMemoryRepositoryDisc()
#   disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
#   student_service.create(1, "ioan")
#   disciplina_service.create_disc(1,"mate","marius")
#   disciplina_service.create_disc(2,"info","andrei")
#   disciplina_service.create_disc(3,"fizica","filip")
#   disciplina_service.create_disc(4,"engleza","david")
#   disciplina_service.create_disc(5,"istorie","ioan")

#   grade_repository = InMemoryRepositoryGrade()
#   grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

#   grade = grade_service.create_grade(1,1,1,10)
#   grade = grade_service.create_grade(2,1,2,5)
#   grade = grade_service.create_grade(3,1,3,6)
#   grade = grade_service.create_grade(4,1,4,7)
#   grade = grade_service.create_grade(5,1,5,8)
  
#   rezultate = grade_service.top_20_discipline()
#   assert len(rezultate) == 1
#   assert 1 in rezultate.keys()
#   assert rezultate[1] == 10



# def test_services():
  # TestDisciplinaService()
  # TestGradeService()
  # TestStudentService()
  # # test_create()
  # test_update()
  # test_delete()
  # test_get_by_id()
  # test_random()
  # test_get_all()
  
  # test_create_disciplina()
  # test_update_disciplina()
  # test_delete_disciplina()
  # test_get_disciplina_by_id()
  # test_get_all_dsciipline()
  # test_random_disciplina()
  
  # test_create_grade()
  # test_update_grade()
  # test_delete_grade()
  # test_get_by_id_grade()
  # test_get_all_grades()

  # test_get_all_student_and_grade_specific_discipline()
  # test_top20_studenti()
  # test_top_20_dicipline()



class TestDisciplinaService(unittest.TestCase):

  def test_create_disciplina(self):
    id = 1
    nume = "matematica"
    prof = "marius"
    repo = InMemoryRepositoryDisc()
    val = DisciplinaValidator()
    serv = DisciplineService(repo, val)
    try:
      serv.create_disc(id, nume, prof)
      self.assertEqual(len(repo), 1)
    except Exception as e:
      self.fail(f"Exception occurred: {e}")

  def test_update_disciplina(self):
    id = 1
    nume = "matematica"
    prof = "marius"
    repo = InMemoryRepositoryDisc()
    val = DisciplinaValidator()
    serv = DisciplineService(repo, val)
      
    try:
      serv.create_disc(id, nume, prof)
      nume = "matematica"
      prof = "Virgil"
      serv.update_disciplina(id, nume, prof)
      get_disciplina = serv.get_disciplina_by_id(id)
      self.assertEqual(get_disciplina, Disciplina(id, nume, prof))
    except Exception as e:
      self.fail(f"Exception occurred: {e}")

  def test_get_disciplina_by_id(self):
    id = 1
    nume = "matematica"
    prof = "marius"
    repo = InMemoryRepositoryDisc()
    val = DisciplinaValidator()
    serv = DisciplineService(repo, val)
        
    try:
      serv.create_disc(id, nume, prof)
      d = serv.get_disciplina_by_id(id)
      self.assertEqual(d, Disciplina(id, nume, prof))
    except Exception as e:
      self.fail(f"Exception occurred: {e}")

  def test_delete_disciplina(self):
    repo = InMemoryRepositoryDisc()
    val = DisciplinaValidator()
    serv = DisciplineService(repo, val)
        
    try:
      serv.create_disc(0, "matematica", "marius A")
      serv.create_disc(1, "informatica", "virgil A")
      serv.create_disc(2, "geografie", "ioan B")
      serv.delete_disciplina(1, "informatica", "virgil A")
      self.assertEqual(len(repo), 2)
    except Exception as e:
      self.fail(f"Exception occurred: {e}")

  def test_get_all_discipline(self):
    repo = InMemoryRepositoryDisc()
    val = DisciplinaValidator()
    serv = DisciplineService(repo, val)
        
    try:
      serv.create_disc(0, "matematica", "marius A")
      serv.create_disc(1, "informatica", "virgil A")
      serv.create_disc(2, "geografie", "ioan B")
      discipline = serv.get_all_discipline()
      self.assertEqual(len(discipline), 3)
    except Exception as e:
      self.fail(f"Exception occurred: {e}")

  def test_random_disciplina(self):
    random.seed(123)
    repo = InMemoryRepositoryDisc()
    val = DisciplinaValidator()
    serv = DisciplineService(repo, val)
        
    try:
      disciplina1 = serv.generate_discipline()
      random.seed(123)
      repo = InMemoryRepositoryDisc()
      val = DisciplinaValidator()
      serv = DisciplineService(repo, val)
      disciplina2 = serv.generate_discipline()
      self.assertEqual(disciplina1.get_id(), disciplina2.get_id())
    except Exception as e:
      self.fail(f"Exception occurred: {e}")

if __name__ == '__main__':
  unittest.main()

class TestGradeService(unittest.TestCase):

  def setUp(self):
    self.student_repository = InMemoryRepositoryStud()
    self.disciplina_repository = InMemoryRepositoryDisc()
    self.grade_repository = InMemoryRepositoryGrade()

    self.student_service = StudentService(self.student_repository, StudentValidator())
    self.disciplina_service = DisciplineService(self.disciplina_repository, DisciplinaValidator())
    self.grade_service = GradeService(self.student_repository, self.disciplina_repository, self.grade_repository, GradeValidator())
    self.student_service.create(1, "ioan")
    self.student_service.create(2, "andrei")
    self.disciplina_service.create_disc(1, "mate", "marius")

  def test_create_grade(self):
    grade = self.grade_service.create_grade(1, 1, 1, 10)
    self.assertEqual(grade.get_id(), 1)
    self.assertEqual(grade.get_student(), 1)
    self.assertEqual(grade.get_disciplina(), 1)
    self.assertEqual(grade.get_nota(), 10)

  def test_update_grade(self):
    grade = self.grade_service.create_grade(1, 1, 1, 10)
    new_grade = self.grade_service.update_grade(1, 1, 1, 6)
    self.assertNotEqual(grade.get_nota(), new_grade.get_nota())

  def test_delete_grade(self):
    self.grade_service.create_grade(1, 1, 1, 10)
    self.assertEqual(len(self.grade_repository), 1)
    self.grade_service.delete_grade(1, 1, 1, 10)
    self.assertEqual(len(self.grade_repository), 0)

  def test_get_by_id_grade(self):
    self.grade_service.create_grade(1, 1, 1, 10)
    result = self.grade_service.get_grade_by_id(1)
    self.assertEqual(result[0], "ioan")
    self.assertEqual(result[1], "mate")
    self.assertEqual(result[2], 10)

  def test_get_all_grades(self):
    self.grade_service.create_grade(1, 1, 1, 10)
    results = self.grade_service.get_all_grades()
    self.assertEqual(len(results), 1)

    self.grade_service.create_grade(2, 1, 1, 5)
    results = self.grade_service.get_all_grades()
    self.assertEqual(len(results), 2)

    self.grade_service.create_grade(3, 1, 1, 5)
    results = self.grade_service.get_all_grades()
    self.assertEqual(len(results), 3)

  def test_get_all_student_and_grade_specific_discipline(self):
    """ Test functia 
    """
    student_repository = InMemoryRepositoryStud()
    student_service = StudentService(student_repository,StudentValidator())

    disciplina_repository = InMemoryRepositoryDisc()
    disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
    student_service.create(1, "ioan")
    student_service.create(2, "andrei")
    disciplina_service.create_disc(1,"mate","marius")

    grade_repository = InMemoryRepositoryGrade()
    grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

    grade = grade_service.create_grade(1,1,1,10)
    grade = grade_service.create_grade(2,2,1,10)

    rezultate = grade_service.get_all_student_and_grade_specific_discipline(1)
    # expected order
    expected_order = ["andrei", "ioan"]

    # Convert dictionary keys to a list
    actual_order = list(rezultate.keys())

    assert actual_order == expected_order

  def test_top20_studenti(self):
    """ Test functia 
    """
    student_repository = InMemoryRepositoryStud()
    student_service = StudentService(student_repository,StudentValidator())

    disciplina_repository = InMemoryRepositoryDisc()
    disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
    student_service.create(1, "ioan")
    student_service.create(2, "andrei")
    student_service.create(3, "stefan")
    student_service.create(4, "virgil")
    student_service.create(5, "anotn")
    disciplina_service.create_disc(1,"mate","marius")

    grade_repository = InMemoryRepositoryGrade()
    grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

    grade = grade_service.create_grade(1,1,1,10)
    grade = grade_service.create_grade(2,2,1,5)
    grade = grade_service.create_grade(3,3,1,6)
    grade = grade_service.create_grade(4,4,1,7)
    grade = grade_service.create_grade(5,5,1,8)
    
    rezultate = grade_service.top_20_studenti()
    assert len(rezultate) == 1
    assert 1 in rezultate.keys()
    assert rezultate[1] == 10

  def test_top_20_dicipline(self):
    student_repository = InMemoryRepositoryStud()
    student_service = StudentService(student_repository,StudentValidator())

    disciplina_repository = InMemoryRepositoryDisc()
    disciplina_service = DisciplineService(disciplina_repository,DisciplinaValidator())
    student_service.create(1, "ioan")
    disciplina_service.create_disc(1,"mate","marius")
    disciplina_service.create_disc(2,"info","andrei")
    disciplina_service.create_disc(3,"fizica","filip")
    disciplina_service.create_disc(4,"engleza","david")
    disciplina_service.create_disc(5,"istorie","ioan")

    grade_repository = InMemoryRepositoryGrade()
    grade_service = GradeService(student_repository,disciplina_repository,grade_repository, GradeValidator())

    grade = grade_service.create_grade(1,1,1,10)
    grade = grade_service.create_grade(2,1,2,5)
    grade = grade_service.create_grade(3,1,3,6)
    grade = grade_service.create_grade(4,1,4,7)
    grade = grade_service.create_grade(5,1,5,8)
    
    rezultate = grade_service.top_20_discipline()
    assert len(rezultate) == 1
    assert 1 in rezultate.keys()
    assert rezultate[1] == 10

if __name__ == '__main__':
    unittest.main()

class TestStudentService(unittest.TestCase):

  def test_create(self):
    try:
      id = 1
      nume = 'Vlad'
      repo = InMemoryRepositoryStud()
      val = StudentValidator()
      serv = StudentService(repo, val)
      serv.create(id, nume)
      self.assertEqual(len(repo), 1)
    except RepositoryConflictException as e:
      self.fail(f"Existent: {e}")

  def test_update(self):
    try:
      id = 1
      nume = 'Vlad'
      repo = InMemoryRepositoryStud()
      val = StudentValidator()
      serv = StudentService(repo, val)
      serv.create(id, nume)
      nume = "Vasile"
      serv.update(id, nume)
      get_student = serv.get_by_id(id)
      self.assertEqual(get_student, Student(id, nume))
    except RepositoryNotFoundException as e:
      self.fail(f"Inexistent: {e}")

  def test_delete(self):
    try:
      id = 1
      nume = 'Vlad'
      repo = InMemoryRepositoryStud()
      val = StudentValidator()
      serv = StudentService(repo, val)
      serv.create(id, nume)
      serv.delete(id, nume)
      self.assertEqual(len(repo), 0)
    except RepositoryNotFoundException as e:
      self.fail(f"Inexistent: {e}")

  def test_get_by_id(self):
    try:
      id = 1
      nume = 'Vlad'
      repo = InMemoryRepositoryStud()
      val = StudentValidator()
      serv = StudentService(repo, val)
      serv.create(id, nume)
      st = serv.get_by_id(id)
      self.assertIsNotNone(st)
    except RepositoryNotFoundException as e:
      self.fail(f"Inexistent: {e}")

  def test_get_all(self):
    try:
      id = 1
      nume = 'Vlad'
      repo = InMemoryRepositoryStud()
      val = StudentValidator()
      serv = StudentService(repo, val)
      serv.create(id, nume)
      serv.create('2', "vasile")
      students = serv.get_all()
      self.assertEqual(len(students), 2)
    except RepositoryNotFoundException as e:
      self.fail(f"Inexistent: {e}")

  def test_random(self):
    try:
      random.seed(123)
      repo = InMemoryRepositoryStud()
      val = StudentValidator()
      serv = StudentService(repo, val)
      st1 = serv.generate_students()

      random.seed(123)
      repo = InMemoryRepositoryStud()
      val = StudentValidator()
      serv = StudentService(repo, val)
      st4 = serv.generate_students()

      self.assertEqual(st1.get_id(), st4.get_id())
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

if __name__ == '__main__':
    unittest.main()