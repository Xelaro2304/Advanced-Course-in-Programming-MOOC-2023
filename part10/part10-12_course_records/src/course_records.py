# tee ratkaisusi tänne
class Course:
    def __init__(self, course, grade, credits):
        self.__course = course
        self.__grade = grade
        self.__credits = credits
        
    def course(self):
        return self.__course
    
    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits

class Record:
    def __init__(self):
        self.__courses = []

    def add_course(self, course, grade, credits):
        course_check = self.search_course(course)
        if course_check == None:
            pass
        else:
            if course_check.grade() < grade:
                self.__courses.remove(course_check)
            else:
                return
        self.__courses.append(Course(course, grade, credits))

    def get_course(self, course_name):
        course = self.search_course(course_name)
        if course == None:
            return None
        if course.course() == course_name:
            return f'{course.course()} ({course.credits()} cr) grade {course.grade()}'
    
    def search_course(self, course_name):
        for course in self.__courses:
            if course_name == course.course():
                return course
        return None
    
    def get_statistics(self):
        total_grades = 0
        total_credits = 0
        grades = []
        for course in self.__courses:
            grades.append(course.grade())
            total_grades += course.grade()
            total_credits += course.credits()
        print(f'{len(self.__courses)} completed courses, a total of {total_credits} credits')
        print(f'mean {(total_grades/len(self.__courses)):.1f}')
        print(f'grade distribution')
        print(f'5: {"x"*grades.count(5)}')
        print(f'4: {"x"*grades.count(4)}')
        print(f'3: {"x"*grades.count(3)}')
        print(f'2: {"x"*grades.count(2)}')
        print(f'1: {"x"*grades.count(1)}')

class RecordTracking:
    def __init__(self):
        self.__record = Record()

    def instructions(self):
        print('1 add course')
        print('2 get course data')
        print('3 statistics')
        print('0 exit')

    def add_course(self):
        course = input('course: ')
        grade = int(input('grade: '))
        credits = int(input('credits: '))
        self.__record.add_course(course, grade, credits)

    def get_course(self):
        course = input('course: ')
        course_information = self.__record.get_course(course)
        if course_information == None:
            print('no entry for this course')
        else:
            print(course_information)

    def statistics(self):
        self.__record.get_statistics()

    def execute(self):
        self.instructions()
        while True:
            command = int(input('command: '))
            if command == 0:
                break
            if command == 1:
                self.add_course()
            if command == 2:
                self.get_course()
            if command == 3:
                self.statistics()

record_track = RecordTracking()
record_track.execute()