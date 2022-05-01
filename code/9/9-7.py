def store_members(members):
    file = open("members.csv","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + str(tries) + ',' + \
               str(wins) + "," + str(chips) + '\n'
        file.write(line)
    file.close()