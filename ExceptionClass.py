'''
Created on Nov 24, 2015

@author: sayed.hussain
'''


class VirusTypeException(Exception):
    def __init__(self):
        super().__init__('Enter valid virus type input. Value can be 1, 2 or 3')


class PopulationSizeException(Exception):
    def __init__(self):
        super().__init__('Population size should be greater than 0')

