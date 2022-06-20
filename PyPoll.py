# retrieve total number of votes cast
# list of candidates
# percentage of votes candidates won
# total number of votes per candidate
# winner of popular vote

import csv
import os

# file paths
openFilePath = os.path.join("resources", "election_results.csv")
writeFilePath = os.path.join("analysis", "election_analysis.txt")

# read analysis file
with open(openFilePath) as electionData:
    fileReader = csv.reader(electionData)                   # initialize reader

    header = next(fileReader)                               # print header row
    print(header)

# write analysis file
with open(writeFilePath, "w") as electionAnalysis:
    electionAnalysis.write("Counties in the Election\n------------------\n")
    electionAnalysis.write("Arapahoe\nDenver\nJefferson")

