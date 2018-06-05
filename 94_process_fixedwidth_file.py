wd = "C:\\Users\\bmareddy\\Documents\\PyLab"
dataFile = wd+"\\SamplePOSFile.txt"
itemFile = wd+"\\SampleItemFile.txt"
discountFile = wd+"\\SampleDiscountFile.txt"

fixed_width_delimiters = {49:(2,1,5,4,4,19,8,6),83:(2,1,14,10,10,10,1,2,7,12,14),112:(2,1,1,22,14,10,10,14,12,7,12,7),12:(2,10)}
line_type = {49: "Header",83:"Item",112:"Discount",12:"Trailer"}
lineitem = []
linediscount = []
header = ()
trailer = ()

itemdata = open(itemFile,'w',newline="\n")
discountdata = open(discountFile,'w',newline="\n")
rawdata = open(dataFile,'r',newline="\n")
for line in rawdata.read().splitlines():
    line_length = len(line)
    slicer = 0
    fields = ()
    for j in fixed_width_delimiters[line_length]:
        fields = fields + (line[slicer:slicer+j],)
        slicer = slicer+j
    if line_type[line_length] == "Header":
        header = fields
    if line_type[line_length] == "Item":
        lineitem.append(fields)
    if line_type[line_length] == "Discount":
        linediscount.append(fields)
    if line_type[line_length] == "Trailer":
        trailer = fields
        for li in lineitem:
            itemdata.write(",".join(str(s) for s in header+li+trailer) + "\n")
        for ld in linediscount:
            discountdata.write(",".join(str(s) for s in header+ld+trailer) + "\n")
        lineitem.clear()
        linediscount.clear()
rawdata.close()
itemdata.close()
discountdata.close()