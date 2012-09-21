#filters output

input = [0, 2, 3, 5, 10, 3, 14, 6, 50, 30, 23, 40, 55, 34]

print "cnt\tsum\tavg\t\tcma"
cma = 0.0
for x in range(1,len(input)):
    if x == 1:
        continue
    slice = input[1:x]
    avg = float(sum(slice)) / float(len(slice))
    i = x - 1
    cma = float(cma + (input[i] - cma) / i)
    
    print "% 3d % 3d \t%f \t%f" % (i, sum(slice), avg, cma)

