# retrieve total number of votes cast
# list of candidates
# percentage of votes candidates won
# total number of votes per candidate
# winner of popular vote

import csv
import os

openFilePath = os.path.join("resources", "election_results.csv")        # set file paths
writeFilePath = os.path.join("challengeAnalysis", "election_analysis.txt")

candidateList = []                                                      # track things we care about
candidateVotes = {}
totalVotes = 0

countyList = []                                                         # county tracking
countyVotes = {}

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

        countyName = row[1]                                             # find county names
        if countyName not in countyList:
            countyList.append(countyName)
            countyVotes[countyName] = 0

        countyVotes[countyName] += 1

    # print(candidateVotes)
    # print(countyVotes)

with open(writeFilePath, "w") as electionAnalysis:                      # analyze/write analysis file
    electionSummary = (
        f"\nElection Results\n"                                         # write general election data
        f"------------------------\n"
        f"Total Votes: {totalVotes:,}\n"
        f"------------------------\n"
    )
    electionAnalysis.write(electionSummary)                             # write election summary
    print(electionSummary)

    winningCandidate = ""                                               # find vote percentages and winner
    winningCount = 0
    winningPercentage = 0

    countyTurnout = ""                                                  # largest county turnout
    countyTurnoutVotes = 0
    countyTurnoutVotesPercentage = 0

    electionAnalysis.write("\nCounty Votes:\n")                         # formatting
    print("County Votes:")
    for countyName in countyList:                                       # find largest county turnout
        cVotes = countyVotes[countyName]
        cVotePercentage = float(cVotes) / float(totalVotes) * 100
        electionAnalysis.write(f"{countyName}: {cVotePercentage:.1f}% ({cVotes:,})\n")          # write county data
        print(f"{countyName}: {cVotePercentage:.1f}% ({cVotes:,})")

        if countyVotes[countyName] > countyTurnoutVotes:
            countyTurnout = countyName
            countyTurnoutVotes = cVotes
            countyTurnoutVotesPercentage = cVotePercentage
    electionAnalysis.write("\n")

    countySummary = (                                                   # format largest county turnout summary
        f"------------------------\n"
        f"Largest County Turnout: {countyTurnout}\n"
        # f"Largest County Turnout Count: {countyTurnoutVotes:,}\n"
        # f"Largest County Turnout Percentage: {countyTurnoutVotesPercentage:.1f}%\n"
        f"------------------------\n"
    )

    electionAnalysis.write(countySummary)
    print(countySummary)

    for candidateName in candidateVotes:                                # find winning candidate
        votes = candidateVotes[candidateName]
        votePercentage = float(votes) / float(totalVotes) * 100
        electionAnalysis.write(f"{candidateName}: {votePercentage:.1f}% ({votes:,})\n")         # write candidate data
        print(f"{candidateName}: {votePercentage:.1f}% ({votes:,})\n")

        if candidateVotes[candidateName] > winningCount:
            winningCandidate = candidateName
            winningCount = votes
            winningPercentage = votePercentage

    winningSummary = (                                                  # format winning candidate summary
        f"------------------------\n"
        f"Winner: {winningCandidate}\n"
        f"Winning Vote Count: {winningCount:,}\n"
        f"Winning Percentage: {winningPercentage:.1f}%\n"
        f"------------------------\n"
    )
    electionAnalysis.write(winningSummary)
    print(winningSummary)


