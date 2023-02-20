'''
Exercise (4 points)

a) Write a class that represents a course. The class should represent the
   following information:

- title

- day

- start time  

- end time

  (Assume for simplicity that meetings for courses take place just once a week)


b) Write a class that represents employees of a university.

The class should contain attributes representing the following information:

- Employees have a first name, a last name and a birth date

- Employees might be teaching one ore more courses (a collection of course objects). 
  Initially, i.e., when an Employee object is created, no courses should
  be assinged to the employee.

Plus at least the following methods:

- add_course: assign a course to the employee

- is_avalailble: returns True if the Employee is available for a meeting.
  Assume that the employee is available at all times where they do not 
  give a course.

- a __str__ method the returns a string where all information is nicely 
  presented 
'''

class Course:

  def __init__(self, title, day, start_time, end_time) -> None:
    self.title = title
    self.day = day
    self.start_time = start_time
    self.end_time = end_time


class Employee:
  def __init__(self, first_name, last_name, birth_date) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.birth_date = birth_date
    self.courses = []
  
  def __str__(self):
    res = self.first_name 
    res += self.first_name + " " + self.last_name 
    res +=  ", born " + self.birth_date
    res += ", teaches "
    for index,item in enumerate(self.courses):
      res += item.title
      if index!=len(self.courses)-1:
        res += ", "
      

    #more pretty print but this isnt what was in the sample output and hence commented. 
    # res = "First name: " + self.first_name + "\n"
    # res += "Last name: " + self.last_name + "\n"
    # res += "Birth date: " + self.birth_date + "\n"
    # res += "Courses: " +  "\n"
    # for i in self.courses:
    #   res += i.title + " : on " + i.day + " from " + str(i.start_time) + " to " + str(i.end_time) +  "\n"

    return res

  def add_course(self,course):
    self.courses.append(course)

  def is_available(self, day, time):
    '''
    checking if the time is within the listed courses time and if its then employee is busy
    '''
    for i in self.courses:
      if i.day == day:    # both if conditions can be written as one statement but i am writing them seperately for easines of reading 
        if time > i.start_time and time < i.end_time: # i am not setting <= or >= intentionally because i dont think the task is asking me to do that but obviously if thats not the case then that can be changed easily
          return False
    
    #if its here then we didnt find any conflict and hence employee is available
    return True



if __name__ == "__main__":
    print("Create employee 'John Doe', born January 1st, 1990")
    john = Employee('John', 'Doe', '1990-01-01')
    print('  Created:', john)

    print("Create employee 'Jane Doe', born August 10, 1992")
    jane = Employee('Jane', 'Doe', '1992-08-10')
    print('  Created:', jane)

    print("Add 'Python I' to John Doe's courses")
    python1 = Course('Python I', 'Tuesday', 12, 14)
    john.add_course(python1)
    print('  John:', john)

    print("Add 'Introduction to Semantics' to John Doe's courses")
    semantics = Course('Introduction to Semantics', 'Monday', 10, 12)
    john.add_course(semantics)
    print('  John:', john)

    print("Add 'Python I' to Jane Doe's courses")
    jane.add_course(python1)
    print('  Jane:', jane)

    print("Is John avaliable for a meeting on Monday at 11h?")
    print(john.is_available('Monday', 11))

    print("Is Jane avaliable for a meeting on Monday at 11h?")
    print(jane.is_available('Monday', 11))

    print("Is John avaliable for a meeting on Tuesday at 13h?")
    print(john.is_available('Tuesday', 13))
    
    print("Is John avaliable for a meeting on Tuesday at 15h?")
    print(john.is_available('Tuesday', 15))
    
