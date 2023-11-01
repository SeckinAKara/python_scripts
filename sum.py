weights = [105, 100, 207, 2013, 2390, 100, 703, 79, 109,
           308, 543, 429, 2801, 4893, 390, 4381, 4839,
           940, 894, 112, 804, 903, 328, 541, 4371, 3321,
           289, 904, 584, 389, 274, 333, 214, 442, 390,
           105, 100, 207, 2013, 2390, 100, 703, 79, 109,
           308, 543, 429, 2801, 4893, 390, 4381, 4839,
           940, 894, 112, 804, 903, 328, 541, 4371, 3321,
           289, 904, 584, 389, 274, 333, 214, 442, 390,
           105, 100, 207, 2013, 2390, 100, 703, 79, 109,
           308, 543, 429, 2801, 4893, 390, 4381, 4839,
           940, 894, 112, 804, 903, 328, 541, 4371, 3321,
           289, 904, 584, 389, 274, 333, 214, 442, 390]
maximum = 120000

def isSummable(values, sum_to_check):
    values = sorted(values)
    length = len(values)
    if length == 1:
        return values[0] == sum_to_check
    if sum_to_check in values:
        return True
    else:
        for n, i in enumerate(values):
            if n == 0:
                remaining = values[1:]
            elif n == length:
                remaining = values[:-1]
            else:
                remaining = values[:n] + values[n+1:]
            return isSummable(remaining, sum_to_check - i)


for i in range(maximum, 1, -1):
    if isSummable(weights, i):
        print "Maximum sum is " + str(i)
        break
