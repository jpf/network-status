#filters output

input = [0, 2, 4, 6, 10, 3, 14, 6, 50, 30, 23, 40, 55, 34]

class cumulative_average:
    def __init__(self):
        self.count = 0
        self.value = 0.0
        
    def calculate(self, input):
        self.count += 1
        self.value = float(self.value + (input - self.value) / self.count)
        return self.value
        

class simple_average:
    def calculate(self, input):
        return float(sum(input)) / float(len(input))


if __name__ == '__main__':
    print "cnt\tsum\tavg\t\tma"
    simple = simple_average()
    cumulative = cumulative_average()
    for x in range(1,len(input)):
        if x == 1:
            continue
        slice = input[1:x]
        avg = simple.calculate(slice)
        i = x - 1
        cma = cumulative.calculate(input[i])
        print "% 3d % 3d \t%f \t%f" % (i, sum(slice), avg, cma)

