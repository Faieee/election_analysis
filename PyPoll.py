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

    header = next(fileReader)

    for row in fileReader:
        totalVotes += 1

        candidateName = row[2]                                          # find candidate names
        if candidateName not in candidateList:
            candidateList.append(candidateName)
            candidateVotes[candidateName] = 0                           # start tracking candidate's votes

        candidateVotes[candidateName] += 1

    # print(candidateVotes)

with open(writeFilePath, "w") as electionAnalysis:                      # analyze/write analysis file
    electionSummary = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {totalVotes:,}\n"
        f"------------------------\n"
    )
    electionAnalysis.write(electionSummary)

    winningCandidate = ""                                               # find vote percentages and winner
    winningCount = 0
    winningPercentage = 0
    for candidateName in candidateVotes:
        votes = candidateVotes[candidateName]
        votePercentage = float(votes) / float(totalVotes) * 100
        electionAnalysis.write(f"{candidateName}: {votePercentage:.1f}% ({votes:,})\n")

        if candidateVotes[candidateName] > winningCount:
            winningCandidate = candidateName
            winningCount = votes
            winningPercentage = votePercentage

    winningSummary = (
        f"------------------------\n"
        f"Winner: {winningCandidate}\n"
        f"Winning Vote Count: {winningCount:,}\n"
        f"Winning Percentage: {winningPercentage:.1f}%\n"
        f"------------------------\n"
    )
    electionAnalysis.write(winningSummary)



