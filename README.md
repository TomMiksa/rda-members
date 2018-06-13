# rda-memebers

This repository provides scripts to parse the official website of the RDA to get:
- a list of WGs, IGs and coordination groups
- a list of users belonging to each group

This data can be later used to analyse the structure of the RDA, e.g. to find out connections between groups.

<b>scripts</b> folder contains two scrpits that needs to be called sequentially.

<b>inpit</b> folder contains 3 files with lists of groups for each type of group.
For example *input-WGs* was created by parsing https://www.rd-alliance.org/groups/working-group

<b>output</b> folder contains 3 files with lists of members for each group belonging to the given type of group.
For example, *result-WGs* contains all WGs and memebers belonging to each of them
The first column has the ID of the user. If you concatenate it with the https://www.rd-alliance.org/user/ then you get the profile of a person. The second column has user’s name.
