    
import unittest
from domain.entitati import Disciplina, Student ,Grade, StudentGrade
from domain.validatori import DisciplinaValidator, GradeValidator, StudentValidator, ValidatorException


# def test_creare_Student():
#   """
#     Testam crearea unui student
#   """
#   student = Student('1','Popescu Prenume')
#   assert student.get_id() == '1'
#   assert student.get_nume() == 'Popescu Prenume'

  
# def test_egalitate():
#   student_1 = Student ('1','Pop Vasile')
#   student_2 = Student ('1','Pop Vasile')
#   assert student_1 == student_2
  




# def test_validare_student():
#   validator = StudentValidator()
#   student = Student("", "")
#   try:
#     validator.validate(student)
#     assert False
#   except ValidatorException:
#     assert True
    
#     student = Student("1", "")
#     try:
#       validator.validate(student)
#       assert False
#     except ValidatorException:
#       assert True
    
#     st = Student("2", "Antonio Vasile")
#     try:
#       validator.validate(st)
#       assert True
#     except ValidatorException:
#       assert False

# def test_validare_disciplina():
#   validator = DisciplinaValidator()
#   disciplina = Disciplina(None, "","")
#   try:
#     validator.validate(disciplina)
#     assert False
#   except ValidatorException:
#     assert True
    
#   disciplina = Disciplina( 1, "", "")
#   try:
#     validator.validate(disciplina)
#     assert False
#   except ValidatorException:
#     assert True
    
#   disciplina = Disciplina(1,"matematica", "marius")
#   try:
#     validator.validate(disciplina)
#     assert True
#   except ValidatorException:
#     assert False
  
# def test_existenta_disciplina():
#     """
#       Testam daca nu mai exista aceeasi disciplina 
#     """
    
#     dis1 = Disciplina('1', "informatica", 'Nume Antonio')
#     dis2 = Disciplina('1', "informatica", 'Nume Antonio')
#     assert dis1 == dis2
    

# def test_creare_Disciplina():
  
#   """
#     Testam crearea unei discipline
#   """
#   disciplina = Disciplina('1', "informatica", 'Nume Antonio')
  
#   assert disciplina.get_id() == '1'
#   assert disciplina.get_nume() == 'informatica'
#   assert disciplina.get_prof() == 'Nume Antonio'

# def testStudentGrade():
#     sg = StudentGrade("1","1",9)
#     assert sg.getStudentID()=="1"
#     assert sg.getDisciplineID()=="FP"
#     assert sg.getGrade()==9

# testStudentGrade()


# def test_domain_entitati():
#   test_egalitate()
#   test_creare_Student()
    
#   test_creare_Disciplina()
#   test_existenta_disciplina()

# def test_domain_validator():
#   test_validare_student()
#   test_validare_disciplina()

# def test_domain():
#   test_domain_entitati()
#   test_domain_validator()

# class TestDisciplina(unittest.TestCase):

#   def test_validate(self):
#     validator = DisciplinaValidator()
#     invalid_disciplina1 = Disciplina(None, "Math", "Prof. Smith")
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_disciplina1)
#     self.assertIn("Id nu poate sa lipseasca", str(context.exception))

  
#     invalid_disciplina2 = Disciplina(1, "", "Prof. Smith")
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_disciplina2)
#     self.assertIn("Numele nu poate sa lipsasca", str(context.exception))

#     invalid_disciplina3 = Disciplina(1, "Math", "")
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_disciplina3)
#     self.assertIn("Profesorul nu poate sa lipsasca", str(context.exception))

#     valid_disciplina = Disciplina(1, "Math", "Prof. Smith")
#     self.assertIsNone(validator.validate(valid_disciplina))

#   def test_existenta_disciplina(self):
#         dis1 = Disciplina('1', "informatica", 'Nume Antonio')
#         dis2 = Disciplina('1', "informatica", 'Nume Antonio')
#         self.assertEqual(dis1, dis2)

#   def test_creare_Disciplina(self):
#         disciplina = Disciplina('1', "informatica", 'Nume Antonio')
#         self.assertEqual(disciplina.get_id(), '1')
#         self.assertEqual(disciplina.get_nume(), 'informatica')
#         self.assertEqual(disciplina.get_prof(), 'Nume Antonio')

# if __name__ == '__main__':
#   unittest.main()


# class TestStudentValidator(unittest.TestCase):

#   def test_validate(self):
#     validator = StudentValidator()

       
#     invalid_student1 = Student(None, "John Doe")
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_student1)
#     self.assertEquals("Id nu poate sa lipseasca", str(context.exception))

       
#     invalid_student2 = Student("1", None)
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_student2)
#     self.assertIn("Numele nu poate sa lipsasca", (context.exception))

       
#     valid_student = Student("1", "John Doe")
#     self.assertIsNone(validator.validate(valid_student))

# if __name__ == '__main__':
#     unittest.main()

# class TestGradeValidator(unittest.TestCase):
#   def test_validate(self):
#     validator = GradeValidator()
#     invalid_grade1 = Grade(None, 1, 2, 8)
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_grade1)
#     self.assertIn("Id nu poate sa lipseasca", str(context.exception))
#     invalid_grade2 = Grade(1, None, 2, 8)
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_grade2)
#     self.assertIn("Disciplina nu poate sa lipseasca", str(context.exception))
#     invalid_grade3 = Grade(1, 1, None, 8)
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_grade3)
#     self.assertIn("Studentul nu poate sa lipseasca", str(context.exception))

#     invalid_grade4 = Grade(1, 1, 2, 11)
#     with self.assertRaises(ValidatorException) as context:
#       validator.validate(invalid_grade4)
#     self.assertIn("Nota invalida", str(context.exception))

#     valid_grade = Grade(1, 1, 2, 8)
#     self.assertIsNone(validator.validate(valid_grade))

# if __name__ == '__main__':
#     unittest.main()


class TestGrade(unittest.TestCase):

    def test_init(self):
        grade = Grade(1, 2, 3, 8)
        self.assertEqual(grade.get_id(), 1)
        self.assertEqual(grade.get_student(), 2)
        self.assertEqual(grade.get_disciplina(), 3)
        self.assertEqual(grade.get_nota(), 8)

    def test_set_nota(self):
        grade = Grade(1, 2, 3, 8)
        grade.set_nota(9)
        self.assertEqual(grade.get_nota(), 9)

    def test_eq(self):
        grade1 = Grade(1, 2, 3, 8)
        grade2 = Grade(1, 2, 3, 8)
        grade3 = Grade(2, 3, 4, 9)

        self.assertEqual(grade1, grade2)
        self.assertNotEqual(grade1, grade3)

if __name__ == '__main__':
    unittest.main()