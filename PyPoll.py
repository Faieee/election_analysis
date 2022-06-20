# retrieve total number of votes cast
# list of candidates
# percentage of votes candidates won
# total number of votes per candidate
# winner of popular vote

import csv
import os

openFilePath = os.path.join("resources", "election_results.csv")        # set file paths
writeFilePath = os.path.join("analysis", "election_analysis.txt")

candidateList = []                                                      # track things we care about
candidateVotes = {}
totalVotes = 0

with open(openFilePath) as electionData:                                # read analysis file
    fileReader = csv.reader(electionData)                               # initialize reader

    header = next(fileReader)                                           # print header row
    print(header)

    for row in fileReader:
        totalVotes += 1

        candidateName = row[2]                                          # find candidate names
        if candidateName not in candidateList:
            candidateList.append(candidateName)
            candidateVotes[candidateName] = 0                           # start tracking candidate's votes

        candidateVotes[candidateName] += 1

    print(candidateVotes)

winningCandidate = ""
winningCount = 0
winningPercentage = 0
for candidateName in candidateVotes:                                    # find vote percentages and winner
    votes = candidateVotes[candidateName]
    votePercentage = float(votes) / float(totalVotes) * 100
    print(f"{candidateName} received {votePercentage:.1f}% of the votes.")

    if candidateVotes[candidateName] > winningCount:
        winningCandidate = candidateName
        winningCount = votes
        winningPercentage = votePercentage

print(f"\nWinner is {winningCandidate} with {winningPercentage:.1f}% of the votes ({winningCount})")

with open(writeFilePath, "w") as electionAnalysis:                      # write analysis file
    exit(0)
