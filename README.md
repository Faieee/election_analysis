## Overview of Election Audit
The PyPoll_Challenge.py script takes raw election data located in [resources/election_results.csv](resources) and outputs formatted results on per-candidate vote counts, per-county vote counts, election winner, and county with highest response rate to both the console and text file at [challengeAnalysis/election_analysis.txt](challengeAnalysis).
## Election-Audit Results
- 369,711 votes were cast in total
- Election results by county:
  - Jefferson County: 10.5% (38,855 votes)
  - Denver County: 82.8% (306,055 votes)
  - Arapahoe County: 6.7% (24,801 votes)
- Highest voter turnout was observed in Denver County
- Election results by candidate:
  - Charles Casper Stockham: 23.0% (85,213 votes)
  - Diana DeGette: 73.8% (272,892 votes)
  - Raymon Anthony Doane: 3.1% (11,606 votes)
- Diana DeGette won the election with 73.8% of the vote (272,892 votes)
## Election-Audit Summary
The included script already has capability for handling any number of candidates, votes, or counties, but aditional functionality can be easily added to handle things such as state-wide elections with more subdivisions or ranked-choice voting.
- To handle election result files with more columns for subdivisions, lines 28 and 35 need to have their row numbers checked, and an entire new block of code can be added in the style of lines 28-33 or 35-40 to account for a new category (the writing of these results is shown in example in lines 63-79.
- Ranked-choice voting support can be implemented by replacing line 33 with a code block that tallies the results in 5 new lists, one for each candidate.
