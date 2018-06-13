#!/bin/bash


#Initital list of groups extracted manually from
#https://www.rd-alliance.org/groups/working-groups

#Go over the list of groups. For each group open its website and get a list of members.
#adr has the link to the website of group
#name has the name of group

while IFS=';' read -r adr name;
do
        echo ================================================
        echo $name
        echo ===============================================
        curl -s $adr | grep "/user/[0-9]*\">[a-zA-Z -]*</a></span>" | grep -o "/user/[0-9]*\">[a-zA-Z -]*" | sed -e 's/">/;/g' | cut -d '/' -f3
done < $1

