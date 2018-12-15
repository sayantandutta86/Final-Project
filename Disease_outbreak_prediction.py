import numpy as np
import matplotlib.pyplot as plt
import math
from Person import Person
from Virus import virus
from ExceptionClass import PopulationSizeException,VirusTypeException,ThresholdValueException,FloatException


def generate_score_for_patients()-> tuple:
    """ This function calculate the aggregate of the scores for a person according to the variables associated
        with person class and virus class. Then, it further increases the count of the person in the red_zone
        and return the results.
        Since the doctest here depends on the user input for population size, and it varies according to the input
        the user gives, it is not possible to write doctests here.
        :return aggregate_score, red_zone, total_count

    """
    aggregate_score_list = []
    red_zone = 0
    total_count = 0
    for i in range(1,population_size):
        person1 = Person()
        virus1 = virus(virus_type)

        #aggregate score is calculated as the sum of the patient's total score plus 
        #the score based on the virus he is infected with.
        aggregate_score = person1.get_total_score() + virus1.get_type_score()
        #If the aggregate score exceeds a threshold level the patient is considered in red-zone.
        if aggregate_score >= 300:
            red_zone = red_zone+1
        total_count = total_count + 1
        aggregate_score_list.append(aggregate_score)
    return (aggregate_score, red_zone, total_count)


if __name__ == '__main__':
    flag = True
    #Handling the user input errors and raising required exceptions
    #We have created custom exceprion in the ExceptionClass
    while flag == True :
        try:
            print("\n Types of virus:")
            print("1. Highly contagious")
            print("2. Fairly contagious")
            print("3. Mildly contagious")
            virus_type = int(input("Please select a virus type(1,2,3):"))
            if virus_type not in [1,2,3]:
                raise VirusTypeException

            population_size = int(input("Insert the number of people:"))
            if population_size <= 0:
                raise PopulationSizeException

            threshold_value = int(input("Insert the threshold percentage:"))
            if isinstance(threshold_value,float):
                raise FloatException
            if threshold_value > 100 or threshold_value < 0:
                raise ThresholdValueException

            flag = False

        #Printing the error details and re-prompting for the user input
        except VirusTypeException as e:
            print(e)
            flag = True
        except PopulationSizeException as e:
            print(e)
            flag = True
        except FloatException as e:
            print(e)
            flag = True
        except ThresholdValueException as e:
            print(e)
            flag = True
        except Exception as e:
            print('Error Occured, Details:')
            print(e)
            flag = True

    probability_list = [] #This list will store the probability coing out of each run in a defined number of simulations
    #Designing different number of monte carlo simulations
    monte_carlo_simulations = [101, 1001, 10001, 100001, 1000001]
    iter_prob_list = [] #Storing the average probability of each simulation
    #Running simulations for different number to achieve steady state and check the Law of Large Numbers
    for i in monte_carlo_simulations:
        for j in range (1, i):
            probability = 0
            agg_scr, red_zone_count, total_count = generate_score_for_patients()
            #Detecting the probability spread of red-zone patients to assess possibility of outbreak
            probability = red_zone_count/total_count
            probability_list.append(probability)
        avg_prob = math.ceil((sum(probability_list) / len(probability_list)) * population_size)
        print('Number of people infected in the population of {p} is {x} based on {i} iterations'.format(p=population_size, x = avg_prob,i=i-1))
        iter_prob_list.append(sum(probability_list)/len(probability_list))
        #Showing the variations in probability range on a graph for different simulations
        plt.plot(probability_list)
        plt.title("Probaility range for {i} iterations".format(i=i-1))
        plt.show()
    #Comparing with the threshold value provided by the user and raising an error accordingly
    if(iter_prob_list[-1]*100 > threshold_value):
        print("Based on the threshold value provided, intervention is required")
    else:
        print("No major intervention required. Some measures can be taken")
    #Showing the achievement of steady state value with the increase in the number of iterations.
    plt.plot(iter_prob_list)
    plt.title("Variabilty in probability with the increase in number of iterations")
    plt.show()
