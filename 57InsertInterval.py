class Solution:
    def insert1(self, intervals, newInterval):
        if not intervals: return [newInterval]
        if not newInterval: return intervals
        retval = []
        for i in intervals:
            # very messy
            if (newInterval and (i[0] < newInterval[0] or i[0] > newInterval[1])) or (not newInterval and (not retval or i[0] > retval[-1][1])):
                retval.append(i)
            else:
                if retval and i[0]<= retval[-1][1
                ] :
                    retval[-1][1] = max(retval[-1][1],i[1])
                if not retval:
                    retval.append([min(i[0],newInterval[0]),max(i[1],newInterval[1])])
                    newInterval=[]

            if newInterval and retval[-1][1] >= newInterval[0] >= retval[-1][0] :
                retval[-1][1] = max(retval[-1][1],newInterval[1])
                newInterval=[]
        if newInterval:
            retval.append(newInterval)
        return retval

    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        if not newInterval: return intervals
        retval = []
        i = 0
        while i < len(intervals):
            if not newInterval or intervals[i][0] < newInterval[0]:
                retval.append(intervals[i])
                i+=1
            else:
                retval.append(newInterval)
                newInterval = []
        if newInterval:
            retval.append(newInterval)
        intervals = []
        for i in retval:
            if not intervals or i[0] > intervals[-1][1]:
                intervals.append(i)
            else:
                intervals[-1][1] = max(intervals[-1][1], i[1])
        return intervals


print(Solution.insert(Solution,[[1,3],[6,9]],[2,5]))
print(Solution.insert(Solution,[[1,5]],[2,7]))

print(Solution.insert(Solution,[[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
             
                