def find_last(filename,x):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    # Write your code here.
    
    

    

    
    outfile.close()
    infile.close()
    print("Done")

# Test code
# find_last('article.txt','computer')    # at 10975 the last time.
# find_last('article.txt','Whole Earth') # at 11280 the last time.
# find_last('article.txt','Apple')       # at 6604 the last time.
# find_last('article.txt','apple')       # not found.
