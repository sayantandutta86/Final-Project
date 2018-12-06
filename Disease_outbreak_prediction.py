import numpy as np
import matplotlib.pyplot as plt

#List to store the aggregate score for all the patients
aggregate_score_list = []

def generate_score_for_patients(num):
    """
    The function calculates the aggregate score for num (number of patients/sample size) to be considered
    :param num: number of cases to be considered (cases reported in the real-life scenario)
    :return: a list of aggregate scores for all the cases.
    """
    for i in range(1,num):
        time_diff = np.random.random_integers(0, 28)
        if time_diff < 7:
            time_diff_score = 100
        elif (time_diff >= 7) and (time_diff <= 14):
            time_diff_score = 100-10*(time_diff-7)
        else:
            time_diff_score = 30

        dist_range = np.random.random_integers(0, 16)
        if dist_range <= 1:
            dist_range_score = 100
        elif (dist_range > 1) and (dist_range <= 8):
            dist_range_score = 100 - 10 * (dist_range - 1)
        else:
            dist_range_score = 30

        virus_type = [10,50,100]
        contagious_score = np.random.choice(virus_type)

        aggregate_score = time_diff_score + dist_range_score + contagious_score
        aggregate_score_list.append(aggregate_score)
    return(aggregate_score_list)

aggr_score = generate_score_for_patients(100)
plt.plot(aggr_score)
plt.show()