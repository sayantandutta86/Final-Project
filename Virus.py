#seperate class for virus types
import random


class virus:

    def __init__(self):
        """ This is the method which intializes all the variables associated with virus class
                """
        self.type = random.choice(['C','FC','MC'])
        self.type_score = 100 #default value

    def get_type_score(self) -> int:
        """ Assign a pre-defined score based on how contagious the virus is.
        :return: type_score
                """
        if self.type == 'C':
            self.type_score = 100
        elif self.type == 'FC':
            self.type_score = 50
        else:
            self.type_score = 10

        return self.type_score
