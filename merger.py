import os
import io
import csv
files = os.listdir(os.curdir)
# print(files)


fields = [] 
rows = [] 
for i in range(0,len(files)):
    if((".csv" in str(files[i])) and ("result" not in str(files[i]))):
        # reading csv file 
        with io.open(files[i], 'r', encoding="utf8") as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
      
            # extracting field names through first row 
            fields = next(csvreader) 

            # extracting each data row one by one 
            for row in csvreader:
                data = [row for row in csv.reader(csvfile)]
                # print(data)
                # print("files   "+files[i])
                for j in range(0,len(data)):
                    data[j].insert(0,str(str(files[i]).split("#")[1].split(".")[0]))
                    data[j].insert(0,str(str(files[i]).split("#")[0]))
                    # print(data[0])
                rows.append(data)
    print(i)

filename = "result.csv"
# print("------------------------")
# print(rows[0])
# print("---------------------")
# print(rows[1])
fields.insert(0,"Search Term")
fields.insert(0,"Company Name")

    
# writing to csv file  
with io.open(filename, 'w', encoding="utf8", newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
    for i in range(0,len(rows)):
        csvwriter.writerows(rows[i]) 
