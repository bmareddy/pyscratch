import utilities as util

# Generate a fixed width file
trx = ""
for i in range(10):
    x = util.random.randint(3,6)
    trx = trx+util.random_x_digits(36)+"\n"
    while x > 2:
        trx = trx+util.random_x_digits(54)+"\n"
        x = x-1
    trx = trx+util.random_x_digits(12)
    if i < 9:
        trx = trx+"\n"


fixed_width_delimiters = ((4,4,3,6,7,12),(9,9,9,9,9,9),(8,8,8,8,8,14),(7,7,7,7,13,13),(6,6,6,12,12,12),(8,4))
onetrx = []

for line in trx.split():
    onetrx.append(line)
    if len(line) == 12:
        print(onetrx)
        for i in range(len(onetrx)):
            print("Fields for line: {}".format(i-1))
            slicer = 0
            for j in fixed_width_delimiters[i-1]:
                print(onetrx[i-1][slicer:slicer+j])
                slicer = slicer+j
        onetrx = []
print("End of All Things")