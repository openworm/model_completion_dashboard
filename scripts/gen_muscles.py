import sys
import csv



input_file = open("C. elegans Cell List - WormBase.csv")
file_reader = csv.DictReader(input_file)

def getbodywallmuscles(file_reader):
    bwmuscle = open("bodywallmuscles.csv",'w')
    writer = csv.writer(bwmuscle, delimiter=',')
    writer.writerow(["Body wall muscles"]);
    for row in file_reader:
        if (row["Body wall muscles"]=='1'):
            writer.writerow([row['Cell']])

    bwmuscle.close()


def getpharynxmuscles(file_reader):
    phymuscle = open("pharynxmuscles.csv",'w')
    writer = csv.writer(phymuscle, delimiter=',')
    writer.writerow(["Pharynx muscles"]);
    for row in file_reader:
        if (row["Pharynx muscles"]=='1'):
            writer.writerow([row['Cell']])

    phymuscle.close()

getbodywallmuscles(file_reader)
input_file.seek(0)
getpharynxmuscles(file_reader)
