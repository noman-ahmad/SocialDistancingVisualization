# reads park dataset and outputs # of parks by zipcode
import csv;
# dictionary to store zip_code: # of parks within
zip_to_parks = dict();
#  open the park zone data set
with open('../data/original/park_zones.csv') as file:
    parser = csv.reader(file);
    next(parser); #ignore first line
    for data in parser:
        #extract current zip code
        current_zip = (data[18][0:5]);
        current_areaid = data[10];
        #initialize value in dict to 1 if first park in zip-code
        if current_zip not in zip_to_parks:
            zip_to_parks[current_zip] = [1];
        else: #increment # of parks per zip-code if already in dict
            zip_to_parks[current_zip][0]+=1;
        zip_to_parks[current_zip].append(current_areaid);
file.close(); # close the input file
# add a 0 value for number of incidents whitin that zip-code
for zips in zip_to_parks:
    zip_to_parks[zips].append(0);

#open the park crowds data set and store #of encounters in that zip-code
with open('../data/original/park_crowds.csv') as file:
    parser = csv.reader(file);
    next(parser);
    for data in parser:
        parkid = data[1];
        for zips in zip_to_parks:
            if parkid in zip_to_parks[zips]:
                zip_to_parks[zips][-1]+=1;
                break;
file.close(); #close the crowds file

for zips in zip_to_parks:
    zip_to_parks[zips].append(0);

with open('../data/original/covid_by_zip.csv') as file:
    parser = csv.reader(file);
    next(parser);
    for data in parser:
        zip = data[0];
        cases = int(data[3]);
        if zip in zip_to_parks:
            zip_to_parks[zip][-1] = cases;
        else:
            zip_to_parks[zip] = [0,0,cases];

file.close();
file = open('../data/edited/zip_park_crowd.csv','w');
file.write("ZIP,Park_Count,Encounters,Cases\n");

#final formatting, removes parks because they are no longer needed
for zips in zip_to_parks:
    num_of_parks = zip_to_parks[zips][0];
    num_of_encounters = zip_to_parks[zips][-2];
    num_of_cases = zip_to_parks[zips][-1];
    zip_to_parks[zips] = [num_of_parks,num_of_encounters,num_of_cases];
    file.write(zips+','+str(num_of_parks)+','+str(num_of_encounters)+','+str(num_of_cases)+'\n');

# input-loop runs indefinetely
while (1):
    inputted_zip = input("Enter Zip-Code (Q to quit): ");
    if inputted_zip == 'Q': #sentinel condition
        print("exiting");
        quit();
    elif inputted_zip in zip_to_parks: #zip-code exists in dict
        print(inputted_zip + ": " + str(zip_to_parks[inputted_zip]));
    else: #zip-code could not be found in dict (error condition)
        print("Zip-Code Could Not Be Found, Please Try Again");
