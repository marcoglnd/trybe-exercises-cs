# Defina uma classe Estatistica que calcule média, mediana e moda de uma lista de números.

class Estatistica():
    def __init__(self, number_list):
        self.number_list = number_list

    def media(self):
        return sum(self.number_list) / len(self.number_list)

    def mediana(self):
        sorted_list = self.number_list
        sorted_list.sort()
        length = len(sorted_list)
        if length % 2 == 1:
            return sorted_list[length // 2]
        return (sorted_list[length // 2] + sorted_list[(length // 2) - 1]) / 2

    def moda(self):
        result = 0
        for number in self.number_list:
            if self.number_list.count(number) > result:
                result = number
        return result
        

my_statistics = Estatistica([1, 1, 2, 2, 3, 3, 4, 5, 6])
print(my_statistics.moda())