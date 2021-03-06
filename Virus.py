#seperate class for virus types
import random


class virus:

    def __init__(self, virus_type):
        """ This is the method which intializes all the variables associated with virus class
                """
        self.type = virus_type
        self.type_score = 0 #default value

    def get_type_score(self) -> int:
        """ Assign a pre-defined score based on how contagious the virus is.
        Virus type 1 - is the most contagious
        Virus type 3 - is the least contagious
        :return: type_score
        >>> v_list= [1,2,3]
        >>> v= virus(random.choice(v_list))
        >>> v.type in [1,2,3]
        True
        >>> 10 <= v.get_type_score() <= 100
        True
                """
        if self.type == 1:
            self.type_score = 100
        elif self.type == 2:
            self.type_score = 50
        else:
            self.type_score = 10

        return self.type_score
