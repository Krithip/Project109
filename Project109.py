import pandas as pd
import statistics
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
df = pd.read_csv("C:/Users/Krithi/Desktop/Python/StudentsPerformance.csv")
readingScore = df["reading score"].to_list()

reading_mean = statistics.mean(readingScore)

reading_median = statistics.median(readingScore)

reading_mode = statistics.mode(readingScore)

print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))

reading_std_deviation = statistics.stdev(readingScore)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

readingScore_of_data_within_1_std_deviation = [result for result in readingScore if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
readingScore_of_data_within_2_std_deviation = [result for result in readingScore if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
readingScore_of_data_within_3_std_deviation = [result for result in readingScore if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

print("{}% of data for reading lies within 1 standard deviation".format(len(readingScore_of_data_within_1_std_deviation)*100.0/len(readingScore)))
print("{}% of data for reading lies within 2 standard deviations".format(len(readingScore_of_data_within_2_std_deviation)*100.0/len(readingScore)))
print("{}% of data for reading lies within 3 standard deviations".format(len(readingScore_of_data_within_3_std_deviation)*100.0/len(readingScore)))

fig = ff.create_distplot([readingScore], ["reading score"], show_hist = False)
fig.add_trace(go.Scatter(x = [reading_mean, reading_mean], y = [0, 0.2], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [reading_first_std_deviation_start, reading_first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "firstSd"))
fig.add_trace(go.Scatter(x = [reading_first_std_deviation_end, reading_first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "firstSd"))
fig.add_trace(go.Scatter(x = [reading_second_std_deviation_start, reading_second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "secondtSd"))
fig.add_trace(go.Scatter(x = [reading_second_std_deviation_end, reading_second_std_deviation_end], y = [0, 0.17], mode = "lines", name = "secondtSd"))
fig.add_trace(go.Scatter(x = [reading_third_std_deviation_start, reading_third_std_deviation_start], y = [0, 0.17], mode = "lines", name = "thirdSd"))
fig.add_trace(go.Scatter(x = [reading_third_std_deviation_end, reading_third_std_deviation_end], y = [0, 0.17], mode = "lines", name = "thirdSd"))
fig.show()