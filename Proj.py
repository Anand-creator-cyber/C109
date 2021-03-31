import pandas as pd 
import plotly.express as px
import csv 
import plotly.figure_factory as ff
import statistics

df = pd.read_csv(r"C:\Users\91814\OneDrive\Desktop\Whitehat\Class 109\StudentsPerformance.csv")
score_list = df["reading score"].tolist()

score_mean = statistics.mean(score_list)
score_median = statistics.median(score_list)
score_mode = statistics.mode(score_list)
score_std = statistics.stdev(score_list)

print("Mean, Median, Mode and Standard Deviation of Reading Score is {}, {}, {} and {}".format(score_mean, score_median, score_mode, score_std))

score_first_start, score_first_end = score_mean-score_std, score_mean+score_std
score_second_start, score_second_end = score_mean-(2*score_std), score_mean+(2*score_std)
score_third_start, score_third_end = score_mean-(3*score_std), score_mean+(3*score_std)

score_list_of_data_within_1_std_deviation = [result for result in score_list if result > score_first_start and result < score_first_end]
score_list_of_data_within_2_std_deviation = [result for result in score_list if result > score_second_start and result < score_second_end]
score_list_of_data_within_3_std_deviation = [result for result in score_list if result > score_third_start and result < score_third_end]

print("{}% of data for score lies within 1 standard deviation".format(len(score_list_of_data_within_1_std_deviation)*100.0/len(score_list)))
print("{}% of data for score lies within 2 standard deviation".format(len(score_list_of_data_within_2_std_deviation)*100.0/len(score_list)))
print("{}% of data for score lies within 3 standard deviation".format(len(score_list_of_data_within_3_std_deviation)*100.0/len(score_list)))


