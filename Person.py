#class for a person

import numpy as np
import random


class Person:
    def __init__(self):
        """ This is the method which intializes all the variables associated with Person class
        """
        self.time_diff = np.random.randint(0, 21)
        self.dist_range = np.random.randint(0, 16)
        self.gender = random.choice(['M','F'])
        self.person_total_score = 0

    def get_tdif_score(self):
        """ Assign a pre-defined score based on time_diff value of an object
        :return: time_diff_score
                """
        if self.time_diff < 7:
            self.time_diff_score = 100
        elif (self.time_diff >= 7) and (self.time_diff <= 14):
            self.time_diff_score = 100 - 10 * (self.time_diff - 7)
        else:
            self.time_diff_score = 30
        return self.time_diff_score

    def get_distance_score(self):
        """ Assign a pre-defined score based on dist_range value of an object
            :return: dist_range_score """
        if self.dist_range <= 1:
            self.dist_range_score = 100
        elif (self.dist_range > 1) and (self.dist_range <= 8):
            self.dist_range_score = 100 - 10 * (self.dist_range - 1)
        else:
            self.dist_range_score = 30
        return self.dist_range_score

    def get_gender_score(self):
        """ Assign a pre-defined score based on gender value of an object
            :return: gender_score """
        if self.gender == 'M':
            self.gender_score = 100
        else:
            self.gender_score = 70
        return self.gender_score

    def get_total_score(self):
        """ Assign a pre-defined score based on all other parameters related to the object
            :return: total_score """
        self.person_total_score = self.get_distance_score() + self.get_distance_score()+ self.get_gender_score()
        return self.person_total_score




