from data_reader import read


class Diagnostician:
    def __init__(self, file):
        self.file = file
        self.symptoms = []
        self.possible_diseases = []
        self.symptoms_per_disease = []
        self.consistency = []
        self.diseases_percentage = []
        self.counter = 0
        self.iterator = 0

        self.all_symptoms = []
        self.all_diseases = []

        for keys, values in read(self.file).items():
            self.all_diseases.append([keys, values])
            for i in values:
                if i not in self.all_symptoms:
                    self.all_symptoms.append(i)

    def ask_question(self):
        return self.all_symptoms[self.counter]

    def positive(self):
        if self.counter >= 0:
            self.symptoms.append(self.all_symptoms[self.counter])
            if self.counter < len(self.all_symptoms)-1:
                self.counter += 1
            else:
                self.counter = -1
        else:
            pass

    def negative(self):
        if self.counter >= 0:
            if self.counter < len(self.all_symptoms)-1:
                self.counter += 1
            else:
                self.counter = -1
        else:
            pass

    def diagnose(self):
        itr = 0
        ctr = 0
        while self.iterator < len(self.all_diseases):
            for item in self.symptoms:
                if item in self.all_diseases[self.iterator][1]:
                    self.possible_diseases.append(self.all_diseases[self.iterator][0])
            self.iterator += 1
        res = [*set(self.possible_diseases)]
        self.possible_diseases = res
        self.possible_diseases.sort()
        while itr < len(self.all_diseases):
            for item in self.possible_diseases:
                if item in self.all_diseases[itr][0]:
                    match = [set(self.symptoms) & set(self.all_diseases[itr][1])]
                    self.symptoms_per_disease.append([len(match[0]), len(self.all_diseases[itr][1])])
            itr += 1

        for x in self.symptoms_per_disease:
            percentage = x[0]/x[1]*100
            percentage = float("{:.2f}".format(percentage))
            self.consistency.append(percentage)

        while ctr < len(self.possible_diseases):
            self.diseases_percentage.append([self.possible_diseases[ctr], self.consistency[ctr]])
            ctr += 1
        self.diseases_percentage.sort(reverse=True, key=lambda a: a[1])

        # b_set = set(tuple(val) for val in self.diseases_percentage)
        # b = [list(var) for var in b_set]
        # self.diseases_percentage = b
        # self.diseases_percentage.sort(reverse=True, key=lambda a: a[1])



