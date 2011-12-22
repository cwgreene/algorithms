def partitions(n):
    results = []
    if n <=0:
        results.append([])
        return results
    for p in partitions(n-1):
        results.append([1]+p)
        if p != [] and ((len(p) < 2) or p[1] > p[0]):
            results.append([p[0]+1]+p[1:])
    return results

import sys
print len(partitions(int(sys.argv[1])))
