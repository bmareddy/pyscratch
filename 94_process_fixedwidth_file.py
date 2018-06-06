import sys, os
from datetime import datetime as dt

wd = "C:\\Users\\bmareddy\\Documents\\PyLab"
dataFile = wd+"\\SamplePOSFile_1M.txt"
itemFile = wd+"\\SampleItemFile_1M.txt"
discountFile = wd+"\\SampleDiscountFile_1M.txt"

fixed_width_delimiters = {49:(2,1,5,4,4,19,8,6),83:(2,1,14,10,10,10,1,2,7,12,14),112:(2,1,1,22,14,10,10,14,12,7,12,7),12:(2,10)}
line_type = {49: "Header",83:"Item",112:"Discount",12:"Trailer"}
lineitem, linediscount = [], []
header, trailer = (), ()
try:
    start_time = dt.today()
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
    end_time = dt.today()
    run_time = end_time - start_time
    print("[Finished in {} days, {} secs]".format(run_time.days,run_time.seconds))
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("Error Type: {}, Line Number: {}, Message: {}".format(exc_type,exc_tb.tb_lineno,e))