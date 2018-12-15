# Custom Exception class to handle in program exceptions


class VirusTypeException(Exception):
    '''This type of exception will occur when the user chooses value other than 1,2 or 3 for virus type when
    prompted'''
    def __init__(self):
        super().__init__('Enter valid virus type input. Value can be 1, 2 or 3')


class PopulationSizeException(Exception):
    '''This type of exception will occur when the user inputs value less than 0 of negative for the population
    variable'''
    def __init__(self):
        super().__init__('Population size should be greater than 0')


class ThresholdValueException(Exception):
    '''This type of exception will occur when the user inputs value less than 0 or more than 100 for threshold
    variable'''
    def __init__(self):
        super().__init__('Threshold value should be between 0 and 100')


class FloatException(Exception):
    '''This type of exception will occur when the user inputs value as float for threshold
    variable'''
    def __init__(self):
        super().__init__('Threshold value should be an integer value')

