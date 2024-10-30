import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')

    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])

print("Names ",names)
print("Status: ",status)

# with open('utilities/loanapp.csv','a') as wFile:
#     write = csv.writer(wFile)
#     write.writerow(["Bob","Rejected"])

