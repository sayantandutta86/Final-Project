import numpy as np
import random

#Class to create a person as per the population provided
class Person(object):
    def __init__(self):
        """ This is the method which intializes all the variables associated with Person class
        """
        self.time_diff = int(np.random.triangular(0,7,21)) #Time before the first case was reported
        self.dist_range = np.random.triangular(0, 3, 8) #Distance from the hospital
        self.gender = random.choice(['M','F']) #Gender of the person
        self.person_total_score = 0 #Total score assigned to each person based on the factors considered

    def get_tdif_score(self) -> int:
        """ Assign a pre-defined score based on time_diff value of an object
        The score for a person decreases as the number of days between this case and first case increases
        :return: time_diff_score
                """
        if self.time_diff < 7:
            self.time_diff_score = 100
        elif (self.time_diff >= 7) and (self.time_diff <= 14):
            self.time_diff_score = 100 - 10 * (self.time_diff - 7)
        else:
            self.time_diff_score = 30
        return self.time_diff_score

    def get_distance_score(self) -> int:
        """ Assign a pre-defined score based on dist_range value of an object
        The score for a person decreases as the distance from hospital increases as the cases can be reported to another hospital
            :return: dist_range_score """
        if self.dist_range <= 1:
            self.dist_range_score = 100
        elif (self.dist_range > 1) and (self.dist_range <= 4):
            self.dist_range_score = 100 - 10 * (self.dist_range - 1)
        else:
            self.dist_range_score = 30
        return self.dist_range_score

    def get_gender_score(self) -> int:
        """ Assign a pre-defined score based on gender value of an object
        We are defining the score as per immunity by gender.
        As per study, Female have higher immunity, so they are given a lower score and male is given a higher score
            :return: gender_score """
        if self.gender == 'M':
            self.gender_score = 100
        else:
            self.gender_score = 70
        return self.gender_score

    def get_total_score(self) -> int:
        """ Assign a pre-defined score based on all other parameters related to the object
        Summing all the scores from different factors to get an aggregate score.
            :return: person_total_score """
        self.person_total_score = self.get_distance_score() + self.get_distance_score()+ self.get_gender_score()
        return self.person_total_score



