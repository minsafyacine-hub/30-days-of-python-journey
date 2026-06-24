class Statistics:
    def __init__(self, liste):
        self.liste = list(liste)
    def count(self):
        return len(self.liste)
    def sum(self):
        return sum(self.liste)
    def min(self):
        return min(self.liste)
    def max(self):
        return max(self.liste)
    def range(self):
        return self.max() - self.min()
    def mean(self):
        return self.sum() / self.count()
    def median(self):
        lsti = sorted(self.liste)
        n = len(lsti) // 2
        mediann = lsti[n]
        if len(self.liste) % 2 == 0:
            return ((lsti[n - 1] + lsti[n]) / 2)
        else:
            return mediann
    def mode(self):
        count = {}
        for number in self.liste:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        lamode = [(count, number) for number, count in count.items()]
        lemode = sorted(lamode, reverse=True)
        lemode = lemode[0]
        return f"'mode' : {lemode[1]}, 'count' : {lemode[0]}"
    def var(self):
        mean = self.mean()
        sde = sum(((number - mean)) ** 2 for number in self.liste)
        return sde / self.count() 
    def std(self):
        return self.var() ** 0.5
    def freq_dist(self):
        n = self.count()
        counts = {}
        for x in self.liste:
            counts[x] = counts.get(x, 0) + 1
        dist = [((c / n) * 100, num) for num, c in counts.items()]
        return sorted(dist, reverse=True) 
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) 
print('Sum: ', data.sum()) 
print('Min: ', data.min()) 
print('Max: ', data.max()) 
print('Range: ', data.range()) 
print('Mean: ', data.mean()) 
print('Median: ', data.median()) 
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.var()) 
print('Frequency Distribution: ', data.freq_dist())


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []
    def add_income(self, amount, description):
        self.incomes.append({'amount' : amount, 'description' : description})
        return self.incomes
    def add_expense(self, amount, description):
        self.expenses.append({'amount' : amount, 'description' : description})
        return self.expenses
    def total_incomes(self):
        return sum(income['amount'] for income in self.incomes)
    def total_expenses(self):
        return sum(exp['amount'] for exp in self.expenses)
    def account_info(self):
        return f"'name' : {self.firstname}, 'surname' : {self.lastname}, 'total of incomes' : {self.total_incomes()}, 'total of expenses' : {self.total_expenses()}, 'account balance' : {self.account_balance()}"
    def account_balance(self):
        return self.total_incomes() - self.total_expenses()
        

    