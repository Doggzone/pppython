def radixsort(ds):
    if ds != []:
        length = len(ds[0])
        for i in range(length-1,-1,-1):
            distributed = [[] for _ in range(10)]
            # Write your for-loop (ds => distributed)
                
            ds = []
            # Write your for-loop (distributed => ds)
            
        return ds
    else:
        return []

# Test code
print(radixsort([])) # []
print(radixsort(["239"])) # ['239']
print(radixsort(["170",'045','075','090','002','024','802','066']))
# ['002', '024', '045', '066', '075', '090', '170', '802']
print(radixsort(["239",'234','879','878','123','358','416','317','137','225']))
# ['123', '137', '225', '234', '239', '317', '358', '416', '878', '879']
print(radixsort(["0505", "0515", "1225", "0915", "1111", "0101", "0318", "0301"]))
# ['0101', '0301', '0318', '0505', '0515', '0915', '1111', '1225']
print(radixsort(["01000", "00100", "00001", "10000", "00010"]))
# ['00001', '00010', '00100', '01000', '10000']