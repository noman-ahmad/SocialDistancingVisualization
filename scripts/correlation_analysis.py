#reads edited dataset and calculates correlations

total_in_range = 0;

import csv;
cases_list = list();
encounter_list = list();
#finding the maximum correlation
with open('../data/edited/zip_park_crowd.csv') as file:
    parser = csv.reader(file);
    next(parser);
    for data in parser:
        #extract the subfields
        total_encounters = int(data[2]);
        total_cases = int(data[3]);
        if total_encounters > 5:
            cases_list.append(total_cases);
            encounter_list.append(total_encounters);

    cases_list.sort();
    encounter_list.sort();
    cases_list.reverse();
    encounter_list.reverse();
file.close();

write_file = open("../data/edited/zip_ranks.csv",'w');
write_file.write("ZIP,CaseRank,EncounterRank,Difference\n");

with open('../data/edited/zip_park_crowd.csv') as file:
    parser = csv.reader(file);
    next(parser);
    for data in parser:
        if int(data[2]) > 5:
            cases = int(data[3]);
            encounters = int(data[2]);
            rank_case = -1;
            rank_encounters = -1;
            for i in range(0,len(cases_list),1):
                if cases_list[i] == cases:
                    rank_case = i;
            for i in range(0,len(encounter_list),1):
                if encounter_list[i] == encounters:
                    rank_encounters = i;
            if abs(rank_encounters - rank_case) <= 8:
                total_in_range = total_in_range + 1;
            print(str(data[0]) + ": " + str(rank_case + 1) + "," + str(rank_encounters + 1) + "," + str(abs(rank_case - rank_encounters)));
            write_file.write(str(data[0])+","+str(rank_case+1)+","+str(rank_encounters+1)+","+str(abs(rank_case-rank_encounters))+'\n');
file.close();

print("Total ZIp-Codes In Range: " + str(total_in_range));
