# retrieve total number of votes cast
# list of candidates
# percentage of votes candidates won
# total number of votes per candidate
# winner of popular vote

import csv
import os

# read results file
openFilePath = os.path.join("resources", "election_results.csv")
with open(openFilePath) as electionData:

    print(electionData)

# write analysis file
writeFilePath = os.path.join("analysis", "election_analysis.txt")
with open(writeFilePath, "w") as outFile:
    outFile.write("Hello World!")

