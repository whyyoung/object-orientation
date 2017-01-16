"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction - Hides complexity so users do not need to worry about details

   Encapsulation - Keeps necessary information together for easy accessibility

   Polymorphism - Compatible interchangeability

2. What is a class?
	A "type" of thing that has common attributes across it's subclasses and instance

3. What is an instance attribute?
	A condition that is set on an instance of a class, a "post-it" note that exists on that instance

4. What is a method?
	A method is like a function, but it is defined on a class

5. What is an instance in object orientation?
	An occurance of a class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   	A class attribute is shared amongst all occurances of a class (unless otherwise specified).
   	An instance attribute is assigned to a specific occurance of a class.
   	An example of a class attribute would be species "feline" for a cat class, since all cats are in the feline species.
   	An example of an instance attribute for a cat class instance would be the name of a cat since each cat has an individual name.



"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):
	"""Records a student's first and last name, along with address"""

	def __init__(self, first_name, last_name, address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address


class Question(object):
	"""Records a question and a corresponding correct answer."""

	def __init__(self, question, correct_answer):
		self.question = question
		self.correct_answer = correct_answer

	# asks user question and compares answer with correct answer; returns Boolean
	def ask_and_evaluate(self):
		user_answer = raw_input(self.question + ' > ')

		return user_answer == self.correct_answer


class Exam(object):

	def __init__(self, name, question = []):
		self.name = name
		self.question = question

	# adds question to exam
	def add_question(self, question, correct_answer):
		self.question.append(Question(question, correct_answer))

	# administers exam
	def administer(self):
		score = 0
		for question in self.question:
			if Question.ask_and_evaluate(question):
				score = score + 1
			else:
				score = score + 0

		return score


# administers test to student and returns test score
def take_test(exam, student):
	score = exam.administer()
	student.score = score
	print "Your score: {}".format(score)

# sets up an Exam and Student; administers Exam to Student
# The exercise did not specify if user was to input information for exam and student;
# when initially setting "stock" names for the exam and info for the student, the questions
# added together and began to repeat.
# Tried to solve this by adding user input for exam and student info...did not fix.
def example():
	exam_name = raw_input('What is this test called? > ')
	exam = Exam(exam_name)

	exam.add_question(
		'What is the method for adding an element to a set?',
		'.add()')
	exam.add_question(
		'Who is the author of Python?', 
		'Guido Van Rossum')
	exam.add_question(
		"What is Balloonicorn's favorite color?",
		"Sparkles")

	student_first_name = raw_input("What is the student's first name? > ")
	student_last_name = raw_input("What is the student's last name? > ")
	student_address = raw_input("Where does the student live? > ")
	student = Student(student_first_name, student_last_name, student_address)

	take_test(exam, student)



class Quiz(Exam):
	def __init__(self, name):
		super(Quiz, self).__init__(name)

	def administer(self):
		total_questions = 0
		score = 0
		for question in self.question:
			if Question.ask_and_evaluate(question):
				score = score + 1
				total_questions = total_questions + 1
			else:
				score = score + 0
				total_questions = total_questions + 1

		print 'Pass?'
		return score >= (total_questions/2.0)

