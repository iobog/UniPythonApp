
from repository.repository import RepositoryConflictException, RepositoryException, RepositoryNotFoundException
from services.studentservices import StudentService
from services.disciplineservices import DisciplineService
from services.gradeservice import GradeService
from domain.entitati import Student, Disciplina, Grade

class Console:
  def __init__(self, srv1,serv2, serv3):
    """Initializeaza UI

    Args:
        srv1 (_type_): Student service
        serv2 (_type_): Disciplina service
        serv3 : Grade service
    """
    self.__srvst = srv1
    self.__srvds = serv2
    self.__srvg = serv3
    
  
  def read(self, type, message):
    try:
      cmd_input = type(input(message))
      return cmd_input
    except ValueError as ex:
      print("Date incorecte!")

  def __add_students(self):
    """
    Citeste un student si il stocheaza in aplicatie

    Raises:
        RepositoryConflictException: Studentul mai exista
    """
    
    id = self.read(int,"Give id: ")
    name = self.read(str, "Give name: ")
    try:
      self.__srvst.create(id, name)
      print("Student Adaugat")
    except Exception as ex:
      print(ex)
  
  def __add_disciplina(self):
    """Citeste o disciplina si o stocheaza in aplicatie

    Raises:
        RepositoryConflictException: Disciplina mai exista
    """
    id = self.read(int,"Give id: ")
    name = self.read(str, "Name: ")
    prof = self.read(str, "Profesor: ")
    try:
      self.__srvds.create_disc(id, name, prof)
      print ("Disciplina adaugata")
    except Exception as ex:
      print(ex)
  
  def __add_nota(self):
    id = self.read(int,"Id: ")
    student = self.read(int, "Student: ")
    disciplina = self.read(int, "Disciplina: ")
    nota = self.read(int, "Nota: ")
    try:
      self.__srvg.create_grade(id, student, disciplina, nota)
      print("Nota adaugata")
    except Exception as ex:
      print(ex)
    
  
  
  def  __delete_students(self):
    """Citeste un student si il sterge

    Raises:
        RepositoryNotFoundException: Studentul nu exista
    """
    id = self.read(int,"Id: ")
    name = self.read(str, "Name: ")
    try:
      self.__srvst.delete(id, name)
      print("Student Sters")
    except Exception as ex:
      print(ex)

  def __delete_disciplina(self):
    """Citeste o disciplina si o sterge din lista

    Raises:
        RepositoryNotFoundException: Disciplina nu exista
    """ 
    id = self.read(int,"Id: ")
    name = self.read(str, "Name: ")
    prof = self.read(str, "Profesor: ")
    try:
      self.__srvds.delete_disciplina(id, name, prof)
      print("Disciplina Stearsa")
    except Exception as ex:
      print(ex)
  
  def __delete_grade(self):
    """ Citeste o nota deja acordata unui student si o sterge
    """
    id = self.read(int,"Id: ")
    student = self.read(int, "Student: ")
    disciplina = self.read(int, "Disciplina: ")
    nota = self.read(int, "Nota: ")
    try:
      self.__srvg.delete_grade(id, student, disciplina, nota)
      print("Nota stearsa")
    except:
      raise RepositoryNotFoundException
   
  def __update_students(self):
    """Actualizeaza studentul

    Raises:
        RepositoryNotFoundException: Studentul nu exista
    """
    id = self.read(int,"Give id: ")
    name = self.read(str,"Name: ")
    try:
      self.__srvst.update(id, name)
      print("Update facut")
    except Exception as ex:
      print(ex)
  
  def __update_disciplina(self):
    """Actualizeaza disciplina
     Raises:
        RepositoryNotFoundException: Studentul nu exista
    """
    id = self.read(int,"Id: ")
    name = self.read(str, "Name: ")
    prof = self.read(str, "Profesor: ")
    try:
      self.__srvds.update_disciplina(id, name, prof)
      print("Update facut")
    except Exception as ex:
      print(ex)
    
  def __update_grade(self):
    """ Citeste o nota deja acordata unui student si o sterge
    """
    id = self.read(int,"Id: ")
    student = self.read(int, "Student: ")
    disciplina = self.read(int, "Disciplina: ")
    nota = self.read(int, "Nota: ")
    try:
      self.__srvg.update_grade(id, student, disciplina, nota)
      print("Nota Actualizata")
    except:
      raise RepositoryNotFoundException
  
  def __view_student(self):
    """Afiseaza studentul cu id ul introdus
    """
    id = self.read(int,"Give id: ")
    try:
      student = self.__srvst.get_by_id(id)
      print(str(student.get_id())+ "   " + student.get_nume())
    except Exception as ex:
      print(ex)
  
  def __view_disciplina(self):
    """Afiseaza disciplina cu id ul introdus
    """
    id = self.read(int,"Give id: ")

    try:
      disciplina = self.__srvds.get_disciplina_by_id(id)
      print(str(disciplina.get_id())+ "   " + disciplina.get_nume()+"   " + disciplina.get_prof())
    except:
      raise RepositoryNotFoundException
    
  def __view_grade(self):
    """ Citeste un id al unei note si  afiseaza studentul, disciplina si nota
    """
    id = self.read(int,"Give id: ")
    try:
      rezultat = self.__srvg.get_grade_by_id(id)
      print(str(rezultat[0])+ " " + str(rezultat[1])+ " " +str(rezultat[2])) 
    except Exception as ex:
      print(ex)
  
  def __view_students(self):
    """Afiseaza toti studentii
    """
    students = self.__srvst.get_all()
    if len(students) == 0:
      print("Nu exista studenti")
    else:
      print ( "id     Nume")
      for st in students:
        print(str(st.get_id())+ "   " + st.get_nume())
  
  
  def __view_discinpline(self):
    """Afiseaza toate disciplinele
    """
    discipline = self.__srvds.get_all_discipline()
    if len(discipline) == 0:
      print("Nu exista Discipline")
    else:
      print ( "id     Nume         Prof")
      for d in discipline:
        print(str(d.get_id())+ "   " + d.get_nume()+"   " + d.get_prof())
  
  def __view__grades(self):
    grade = self.__srvg.get_all_grades()
    if len(grade) == 0:
      print("Nu exista Note")
    else:
      print("id   Student    Materie   Nota")
      for rezultat in grade:        
        print(str(rezultat[0])+" "+str(rezultat[1])+ " " + str(rezultat[2])+ " " +str(rezultat[3])) 


  def __add_random(self):
    """Genereaza un student random si il memoreaza
    """
    self.__srvst.generate_students()
  
  def __add_random_disciplina(self):
    """Genereaza o disciplina aleatorie si o memoreaza
    """
    self.__srvds.generate_discipline()
  
  
  def __top_20(self):
    pass

  def __lista_studenti_la_o_disciplina(self):
    """ Determina studenti si notele lor la o disicplina data
    """
    disciplina = self.read(int, "Disciplina: ")
    try:
      rezultate = self.__srvg.get_all_student_and_grade_specific_discipline(disciplina)
      print("Student       Note")
      for key, values in rezultate.items():
        print(key,   *values)
    except Exception as ex:
      print(ex)
    
  def __top20_studenti(self):
    """ Determina primi 20% cei mai buni studenti  si mediile lor 
    """
    try:
      rezultate = self.__srvg.top_20_studenti()
      print(" ID       Student       Medie")
      for key, values in rezultate.items():
        student = self.__srvst.get_by_id(int(key))
        print(str(student.get_id())+" " +student.get_nume()+ "  "   +str(*values))
    except Exception as ex:
      print(ex)
    
  def __top20_discipline(self):
    """ Determina primele 20% matrii cu mediile studentiilor cele mai mari 
    """
    try:
      rezultate = self.__srvg.top_20_discipline()
      print("ID     Disciplina  Profesor      Medie")
      for key, values in rezultate.items():
        disciplina = self.__srvds.get_by_id(int(key))
        print(str(disciplina.get_id())+" " +disciplina.get_nume()+ "  "+disciplina.get_prof()+"   "  +str(*values))
    except Exception as ex:
      print(ex)
    
    
  def show_ui(self):
    while True:
      cmd = self.read(str,"Command(student, discipline, note, raport):")
      if cmd == 'student':
        cmdst = self.read(str,"Command(add, update, delete, viewall, view, random): ")
        # add student
        if cmdst == "add":self.__add_students()
        # search one student
        if cmdst == "view":self.__view_student()
        # view all students
        if cmdst == "viewall":self.__view_students()
        # delete one student
        if cmdst == "delete":self.__delete_students()
        # update a student
        if cmdst == "update":self.__update_students()
        # un student random
        if cmdst == 'random':self.__add_random()
          
      if cmd == 'discipline':
        cmds = self.read(str,"Command(add, update, delete, viewall, view, random): ")
        # add discipline
        if cmds == "add":self.__add_disciplina()
        # search one discipline
        if cmds == "view":self.__view_disciplina()
        # view all discipline
        if cmds == "viewall":self.__view_discinpline()
        # delete one discipline
        if cmds == "delete":self.__delete_disciplina()
        # update a discipline
        if cmds == "update":self.__update_disciplina()
        # o discipline random
        if cmds == 'random':self.__add_random_disciplina()
      
      if cmd == 'note':
        cmd_g = self.read(str,"Command(add, update, delete, viewall, view): ")
        if cmd_g == "add": self.__add_nota()
        if cmd_g == "viewall": self.__view__grades()
        if cmd_g == "delete": self.__delete_grade()
        if cmd_g == "update": self.__update_grade()
        if cmd_g == "view": self.__view_grade()
      
      if cmd  == "raport":
        print("1. Lista studenti si notele lor la o disciplina")
        print("2. Top 20 studenti")
        print("3. Top 20 discipline")
        
        command = self.read(int,"Command(1, 2, 3): ")
        if command == 1: self.__lista_studenti_la_o_disciplina()
        if command == 2: self.__top20_studenti()
        if command == 3: self.__top20_discipline()
