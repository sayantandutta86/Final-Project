import numpy as np
import matplotlib.pyplot as plt

aggregate_score_list = []
red_zone = []
def generate_score_for_patients():
    for i in range(1,100):
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
        if aggregate_score >= 250:
            red_zone.append(1)
        else:
            red_zone.append(0)
        aggregate_score_list.append(aggregate_score)
    #plt.plot(aggregate_score_list)
    #plt.show()
    return (aggregate_score_list, red_zone)

agg_scr_list, red_zone_list = generate_score_for_patients()
plt.plot(agg_scr_list)
plt.show()
#print(red_zone_list)
#plt.show()