import matplotlib.pyplot as plt;
import csv;

rank_cases = list();
rank_encounters = list();

with open('../data/edited/zip_ranks.csv') as file:
    parser = csv.reader(file);
    next(parser);
    for data in parser:
        rank_cases.append(data[1]);
        rank_encounters.append(data[2]);

file.close();


plt.plot(rank_cases, rank_encounters);
plt.show();
