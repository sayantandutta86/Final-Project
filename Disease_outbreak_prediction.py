import numpy as np
import matplotlib.pyplot as plt
from Person import Person
from Virus import virus

def generate_score_for_patients():
    aggregate_score_list = []
    red_zone = 0
    total_count = 0
    for i in range(1,1000001, 100):
        person1 = Person()
        virus1 = virus()

        aggregate_score = person1.get_total_score() + virus1.get_type_score()

        if aggregate_score >= 250:
            red_zone = red_zone+1
        total_count = total_count + 1
        aggregate_score_list.append(aggregate_score)
    #plt.plot(aggregate_score_list)
    #plt.show()
    return (aggregate_score_list, red_zone, total_count)

probability_list = []
for i in range (1, 1000, 100):
    probability = 0
    agg_scr_list, red_zone_count, total_count = generate_score_for_patients()
    probability = red_zone_count/total_count
    probability_list.append(probability)
print(sum(probability_list)/len(probability_list))
plt.plot(probability_list)
plt.show()
#print(red_zone_list)
#plt.show()
