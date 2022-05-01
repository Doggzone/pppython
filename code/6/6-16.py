def find_2nd(filename,x):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(x)
    position = text.find(x,position+1)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(position) + " the 2nd time.\n")
    outfile.close()
    infile.close()
    print("Done")

# Test code
# find_2nd('article.txt','computer')    # at 3357 the 2nd time.
# find_2nd('article.txt','Whole Earth') # at 11280 the 2nd time.
# find_2nd('article.txt','Apple')       # at 4455 the 2nd time.
# find_2nd('article.txt','apple')       # not found.
