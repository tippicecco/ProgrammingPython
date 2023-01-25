import random #modulo = pcchetto casuale numero
class Person():
  pass
  def __init__(self, names, surnames):   #quello che scrivo in init lo istanzio
    self.name = names
    self.surname = surnames
    
  def __str__(self):
    return "Person : {} {}". format (self.name,self.surname)
  #def __repr__(self):
    #return 'person : {} {} '. format(self. name, self. surname )
  def say_hi(self):
    rand=random. randint(0,2)
    if rand == 0:
      print('Buongiorno, sono : "{}{}"' .format(self.name, self.surname))

    if rand == 1:
      print('Buongiorno, soi : "{}"' .format(self.name))
    if rand == 2:
      self.name = "checo"
      print('mandi, soy : "{}"' .format(self.name))

  
  
class Student(Person):
  def __str__(self):
    return 'Student: "{} {}"'.format(self.name, self.surname)

  def mettinota(self):
    print("Ai ciapat une note")
class Professor(Person):
  def __str__(self):
    return "Prof: '{}{}'".format(self.name, self.surname)
  def say_hi(self):
    print('Buongiorno, sono prof : "{}{}"' .format(self.name, self.surname))
  def or_say_hi(self):
    super().say_hi() #dico il say hi super della classe gerarch magg xk si salva non sovrascrive anche se nomi uguali
  
    



print("----------------------")
person = Person("mario", "il rosso")
print(person)
person.say_hi()
print("----------------------")
prof=Professor("Pippo","Baudo")
print(prof)
prof.say_hi()
prof.or_say_hi()
print("----------------------")
student = Student("gigio", "gigi")
print(student)
student.say_hi()
student.mettinota()
print("----------------------")

#print(person.name)
#print(person. surname)
mylist=[1,2,3,4,5]
mylist.reverse()
print(mylist)
print(mylist.reverse()) #stampa VUOTO
print(mylist)