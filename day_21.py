class Statistics:
    def __init__(self, liste):
        self.liste = ages
    def count(self):
        return len(self.liste)
    def sum(self):
        return sum(self.liste)
    def min(self):
        return min(self.liste)
    def max(self):
        return(self.liste)
    def range(self):
        return max(self.liste) - min(self.liste)
    def mean(self):
        return sum(self.liste) / len(self.liste)
    def median(self):
        lsti = sorted(self.liste, reverse=True)
        la_median = len(self.liste) / 2
        mediann = lsti[la_median]
        la_mediane = la_median + 1
        if len(self.liste) % 2 == 0:
            return la_median
        else:
            return la_mediane
    def mode(self):
        count = {}
        for number in self.liste:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        lamode = [(count, number) for number, count in count.items()]
        lemode = sorted(lamode, reverse=False)
        lemode = lemode[:0]
        return "'mode' : {lemode[0]}, 'count' : {lemode[1]}"
    def std(self):
        mean = sum(self.liste) / len(self.liste)
        for number in self:
            eac = sum((number - mean)) ** 2
            mdeac = eac / len(self)
        return mdeac ** 0.5
    def var(self):
        mean = sum(self.liste) / len(self.liste)
        for number in self.liste:
            eac = sum((number - mean)) ** 2
            mdeac = eac / len(self.liste)
        return mdeac
    def freq_dist(self):
        for number in self.liste:
            fql = {number / len(self.liste)}
        fqll = [(fql, number) for number, fql in fql.items()]
        fqlu = sorted(fqll, reverse=True)
        return fqlu
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.var()) 
print('Frequency Distribution: ', data.freq_dist())
    
