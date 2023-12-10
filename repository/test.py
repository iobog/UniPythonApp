

import os
import unittest
from domain.entitati import Grade, Student, Disciplina
from repository.FILLErepository import DisciplineFileRepository, GradeFileRepository, StudentFileRepository
from repository.repository import InMemoryRepositoryGrade, InMemoryRepositoryStud,InMemoryRepositoryDisc, RepositoryConflictException, RepositoryException, RepositoryNotFoundException


# def test_add():
#   """Test functie de adaugarea in repository pentru studenti
#   """
#   student = Student('1', 'Anton')
#   repo = InMemoryRepositoryStud()
#   assert len(repo) == 0
#   repo.add(student)
#   assert len(repo) == 1
#   try:
#     repo.add(student)
#     assert False
#   except RepositoryConflictException:
#     assert True
#   except Exception:
#     assert False

# def test_get():
#   """Test functie de get din repository pentru studenti
#   """
#   student = Student('1', 'Anton')
#   repo = InMemoryRepositoryStud()
#   repo.add(student)
#   s = repo.get(student.get_id())
#   assert s == student



# def test_update():
#   """Test functie de actulaizare din repository pentru studenti
#   """
#   student = Student('1', 'Anton')
#   repo = InMemoryRepositoryStud()
#   repo.add(student)
#   student.set_nume('Vlad')
#   repo.update(student)
#   s = repo.get(student.get_id())
#   assert s.get_nume() == student.get_nume()
 

# def test_delete():
#   """Test functie de stergere din repository pentru studenti
#   """
#   student = Student('1', 'Anton')
#   repo = InMemoryRepositoryStud()
#   repo.add(student)
#   repo.delete(student)
#   assert repo.get(student.get_id()) == None
  

# def test_get_all():
#   """Test functie de get all din repository pentru studenti
#   """
#   repo = InMemoryRepositoryStud()
#   student = Student('1', 'Anton')
#   repo.add(student)
#   student = Student('2', 'Vlad')
#   repo.add(student)
  
#   studenti = repo.get_all()
#   assert len(studenti) == 2
  

# def test_add_disciplina():
#   """Test functie de adaugarea in repository pentru discipline
#   """
#   d = Disciplina(1,"matematica","Marius")
#   repo = InMemoryRepositoryDisc()
#   assert len(repo) == 0
#   repo.add(d)
#   assert len(repo) == 1
#   try:
#     repo.add(d)
#     assert False
#   except RepositoryConflictException:
#     assert True
#   except Exception:
#     assert False


# def test_get_disciplina():
#   """Test functie de get din repository pentru discipline
#   """
#   d = Disciplina(1,"matematica","Marius")
#   repo = InMemoryRepositoryDisc()
#   repo.add(d)
#   d_get = repo.get(d.get_id())
#   assert d == d_get


# def test_get_all_disciplina():
#   """Test functie de get all din repository pentru studenti
#   """
#   repo = InMemoryRepositoryDisc()
#   d  = Disciplina(1,"matematica","Marius")
#   repo.add(d)
#   d = Disciplina(2, "info", "virgil")
#   repo.add(d)
#   all_d = repo.get_all()
#   assert len(all_d) == 2



 
# def test_update_disciplina():
#   """Test functie de actulaizare din repository pentru discipline
#   """
#   d = Disciplina(1,"matematica","Marius")
#   repo = InMemoryRepositoryDisc()
#   repo.add(d)
#   d.set_nume("matematica")
#   d.set_prof("Virgil")
#   repo.update(d)
#   t = repo.get(d.get_id())
#   assert d.get_prof() == t.get_prof()

# def test_delete_disciplina():
#   """Test functie de actulaizare din repository pentru discipline
#   """
#   d = Disciplina(1,"matematica","Marius")
#   repo = InMemoryRepositoryDisc()
#   repo.add(d)
#   repo.delete(d)
#   assert repo.get(d.get_id()) == None

# def test_get_disciplina():
#   """Test functie de get din repository pentru discipline
#   """
#   d = Disciplina(1,"matematica","Marius")
#   repo = InMemoryRepositoryDisc()
#   repo.add(d)
#   d_get = repo.get(d.get_id())
#   assert d == d_get


# def test_add_grade():
#   g = Grade(1,1,1,10)
#   repo = InMemoryRepositoryGrade()
#   assert len(repo) == 0
#   repo.add(g)
#   assert len(repo) == 1
#   try:
#     repo.add(g)
#     assert False
#   except RepositoryConflictException:
#     assert True
#   except Exception:
#     assert False

# def test_get_nota():
#   g = Grade(1,1,1,10)
#   repo = InMemoryRepositoryGrade()
#   repo.add(g)
#   g_get = repo.get(g.get_id())
#   assert g == g_get
#   try:
#     g_get = repo.get(2)
#     assert g_get == None
#   except RepositoryNotFoundException:
#     assert True

# def test_delete_nota():
#   g = Grade(1,1,1,10)
#   repo = InMemoryRepositoryGrade()
#   repo.add(g)
#   t = Grade(2,1,1,5)
#   repo.add(t)
#   assert len (repo) == 2
#   repo.delete(g)
#   assert len(repo) == 1

#   try:
#     repo.delete(g)
#     assert False
#   except RepositoryNotFoundException:
#     assert True



# def test_update_nota():
#   g = Grade(1,1,1,10)
#   repo = InMemoryRepositoryGrade()
#   repo.add(g)
#   g.set_nota(7)
#   repo.update(g)
#   t = repo.get(1)
#   assert t.get_nota() == g.get_nota()
#   try:
#     g = Grade(10,1,1,10)
#     repo.update(g)
#     assert False
#   except RepositoryNotFoundException:
#     assert True

# def test_get_all_grades():
#   repo = InMemoryRepositoryGrade()
#   g1 = Grade(1, 1, 2, 10)
#   g2 = Grade(2, 1, 2, 3)
#   g3 = Grade(3, 2, 3, 10)
#   repo.add(g1)
#   repo.add(g2)
#   repo.add(g3)
#   all_grades = repo.get_all()
#   assert len (all_grades) == len(repo) 

    

#def test_repository():
  
  # test_add()
  # test_get()
  # test_get_all()
  # test_update()
  # test_delete()
  
  # test_add_disciplina()
  # test_get_disciplina()
  # test_update_disciplina()
  # test_get_all_disciplina()
  # test_delete_disciplina()

  # test_add_grade()
  # test_get_nota()
  # test_delete_nota()
  # test_update_nota()
  # test_get_all_grades()

  # testStore() 
  # test_store_disciplina()
  # test_store_grade

  # TestInMemoryRepositoryGrade()
  # TestInMemoryRepositoryDisc()
  # TestInMemoryRepositoryStud()


class TestInMemoryRepositoryStud(unittest.TestCase):

  def test_add(self):
    try:
      student = Student('1', 'Anton')
      repo = InMemoryRepositoryStud()
      self.assertEqual(len(repo), 0)
      repo.add(student)
      self.assertEqual(len(repo), 1)
      repo.add(student)
      self.fail("Expected RepositoryConflictException")
    except RepositoryConflictException:
      pass
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_get(self):
    try:
      student = Student('1', 'Anton')
      repo = InMemoryRepositoryStud()
      repo.add(student)
      s = repo.get(student.get_id())
      self.assertEqual(s, student)
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_update(self):
    try:
      student = Student('1', 'Anton')
      repo = InMemoryRepositoryStud()
      repo.add(student)
      student.set_nume('Vlad')
      repo.update(student)
      s = repo.get(student.get_id())
      self.assertEqual(s.get_nume(), student.get_nume())
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_delete(self):
    try:
      student = Student('1', 'Anton')
      repo = InMemoryRepositoryStud()
      repo.add(student)
      repo.delete(student)
      self.assertIsNone(repo.get(student.get_id()))
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_get_all(self):
    try:
      repo = InMemoryRepositoryStud()
      student = Student('1', 'Anton')
      repo.add(student)
      student = Student('2', 'Vlad')
      repo.add(student)
      studenti = repo.get_all()
      self.assertEqual(len(studenti), 2)
    except RepositoryNotFoundException as e:
      self.fail(f"Nu exista Studenti!: {e}")

if __name__ == '__main__':
    unittest.main()

class TestInMemoryRepositoryGrade(unittest.TestCase):

  def test_add_grade(self):
    try:
      g = Grade(1, 1, 1, 10)
      repo = InMemoryRepositoryGrade()
      self.assertEqual(len(repo), 0)
      repo.add(g)
      self.assertEqual(len(repo), 1)
      repo.add(g)
      self.fail("Expected RepositoryConflictException")
    except RepositoryConflictException:
      pass
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_get_nota(self):
    try:
      g = Grade(1, 1, 1, 10)
      repo = InMemoryRepositoryGrade()
      repo.add(g)
      g_get = repo.get(g.get_id())
      self.assertEqual(g, g_get)
      g_get = repo.get(2)
      self.assertIsNone(g_get)
    except RepositoryNotFoundException:
      pass
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_delete_nota(self):
    try:
      g = Grade(1, 1, 1, 10)
      repo = InMemoryRepositoryGrade()
      repo.add(g)
      t = Grade(2, 1, 1, 5)
      repo.add(t)
      self.assertEqual(len(repo), 2)
      repo.delete(g)
      self.assertEqual(len(repo), 1)
      repo.delete(g)
      self.fail("Expected RepositoryNotFoundException")
    except RepositoryNotFoundException:
      pass
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_update_nota(self):
    try:
      g = Grade(1, 1, 1, 10)
      repo = InMemoryRepositoryGrade()
      repo.add(g)
      g.set_nota(7)
      repo.update(g)
      t = repo.get(1)
      self.assertEqual(t.get_nota(), g.get_nota())
      g = Grade(10, 1, 1, 10)
      repo.update(g)
      self.fail("Expected RepositoryNotFoundException")
    except RepositoryNotFoundException:
      pass
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_get_all_grades(self):
    try:
      repo = InMemoryRepositoryGrade()
      g1 = Grade(1, 1, 2, 10)
      g2 = Grade(2, 1, 2, 3)
      g3 = Grade(3, 2, 3, 10)
      repo.add(g1)
      repo.add(g2)
      repo.add(g3)
      all_grades = repo.get_all()
      self.assertEqual(len(all_grades), len(repo))
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

if __name__ == '__main__':
    unittest.main()  

class TestInMemoryRepositoryDisc(unittest.TestCase):

  def test_add_disciplina(self):
    try:
      d = Disciplina(1, "matematica", "Marius")
      repo = InMemoryRepositoryDisc()
      self.assertEqual(len(repo), 0)
      repo.add(d)
      self.assertEqual(len(repo), 1)
      repo.add(d)
      self.fail("Expected RepositoryConflictException")
    except RepositoryConflictException:
      pass
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_get_disciplina(self):
    try:
      d = Disciplina(1, "matematica", "Marius")
      repo = InMemoryRepositoryDisc()
      repo.add(d)
      d_get = repo.get(d.get_id())
      self.assertEqual(d, d_get)
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_get_all_disciplina(self):
    try:
      repo = InMemoryRepositoryDisc()
      d = Disciplina(1, "matematica", "Marius")
      repo.add(d)
      d = Disciplina(2, "info", "virgil")
      repo.add(d)
      all_d = repo.get_all()
      self.assertEqual(len(all_d), 2)
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_update_disciplina(self):
    try:
      d = Disciplina(1, "matematica", "Marius")
      repo = InMemoryRepositoryDisc()
      repo.add(d)
      d.set_nume("matematica")
      d.set_prof("Virgil")
      repo.update(d)
      t = repo.get(d.get_id())
      self.assertEqual(d.get_prof(), t.get_prof())
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

  def test_delete_disciplina(self):
    try:
      d = Disciplina(1, "matematica", "Marius")
      repo = InMemoryRepositoryDisc()
      repo.add(d)
      repo.delete(d)
      self.assertIsNone(repo.get(d.get_id()))
    except Exception as e:
      self.fail(f"Unexpected exception: {e}")

if __name__ == '__main__':
    unittest.main()

class TestRepositories(unittest.TestCase):

  def setUp(self):
    self.file_names = ["test_student.txt", "test_disciplina.txt", "test_grade.txt"]

  def tearDown(self):
    for file_name in self.file_names:
      try:
        os.remove(file_name)
      except FileNotFoundError:
        pass

  def test_store_student(self):
        """Functie test pentru salvarea in fisier"""
        file_name = self.file_names[0]
        open(file_name, "w").close()
        repo = StudentFileRepository(file_name)
        repo.removeAll()

        st = Student(1, "ioan")
        repo.add(st)
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo.get(1), st)

        repo2 = StudentFileRepository(file_name)
        self.assertEqual(len(repo2), 1)
        self.assertEqual(repo2.get(1), st)

  def test_store_disciplina(self):
        """Functie test pentru salvarea in fisier"""
        file_name = self.file_names[1]
        
        open(file_name, "w").close()
        repo = DisciplineFileRepository(file_name)
        repo.removeAll()

        ds = Disciplina(1, "mate", "marius")
        repo.add(ds)
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo.get(1), ds)
        
        repo2 = DisciplineFileRepository(file_name)
        self.assertEqual(len(repo2), 1)
        self.assertEqual(repo2.get(1), ds)

  def test_store_grade(self):
        """Functie test pentru salvarea in fisier"""
        file_name = self.file_names[2]
        
        open(file_name, "w").close()
        repo = GradeFileRepository(file_name)
        repo.removeAll()

        st = Grade(1, 1, 1, 10)
        repo.add(st)
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo.get(1), st)

        repo2 = GradeFileRepository(file_name)
        self.assertEqual(len(repo2), 1)
        self.assertEqual(repo2.get(1), st)

if __name__ == '__main__':
    unittest.main()