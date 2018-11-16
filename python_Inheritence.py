class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self,firstName, lastName, id_num, scores):

        super().__init__(firstName, lastName, id_num)
        self.scores = scores

    def calculate(self):

        avg_Score = sum(self.scores)/ len(self.scores)

        if avg_Score >= 90 and avg_Score <= 100:

            return 'O'

        elif avg_Score >= 80 and avg_Score <= 90:

            return  'E'
            
        elif avg_Score >= 70 and avg_Score <= 80:

            return  'A'

        elif avg_Score >= 55 and avg_Score <= 70:

            return  'P'

        elif avg_Score >= 40 and avg_Score <= 55:

            return 'D'

        else:
            
            return 'T'
