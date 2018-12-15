import numpy as np
import matplotlib.pyplot as plt
from Person import Person
from Virus import virus


def generate_score_for_patients()-> tuple:
    """ This function calculate the aggregate of the scores for a person according to the variables associated
        with person class and virus class. Then, it further increases the count of the person in the red_zone
        and return the results
        :return aggregate_score_list, red_zone, total_count

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
        if aggregate_score >= 250:
            red_zone = red_zone+1
        total_count = total_count + 1
        aggregate_score_list.append(aggregate_score)
    #plt.plot(aggregate_score_list)
    #plt.show()
    return (aggregate_score_list, red_zone, total_count)


if __name__ == '__main__':
    print("\n Options:")
    print("1. Highly contagious")
    print("2. Fairly contagious")
    print("3. Mildly contagious")
    virus_type = int(input("Please select a virus type:"))
    population_size = int(input("Insert the number of people:"))
    probability_list = []
    #Designing different number of monte carlo simulations
    monte_carlo_simulations = [101, 1001, 10001, 100001, 1000001]
    for i in monte_carlo_simulations:
        for i in range (1, i):
            probability = 0
            agg_scr_list, red_zone_count, total_count = generate_score_for_patients()
            #Detecting the probability spread of red-zone patients to assess possibility of outbreak
            probability = red_zone_count/total_count
            probability_list.append(probability)
        print(sum(probability_list)/len(probability_list))
        plt.plot(probability_list)
        plt.show()
    #print(red_zone_list)
    #plt.show()
