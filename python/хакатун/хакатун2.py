class TriangleChecker:
    def __init__(self, list):
        self.list = list
    def is_triangle(self):
        if all(isinstance(i, (int, float))for i in self.list):
            if all(i > 0 for i in self.list):
                sorted_i = sorted(self.list)
                if sorted_i[0] + sorted_i[1] > sorted_i[2]:
                    return 'Ура можно построить треугольник!'
                return 'Жаль, но из этого ничего не получится'
            return 'С отрицательными цифрами не получится'
        return 'нужно вводить только числа'
a, b , c = map(float, input(' пример 2 3 4:').split())
triangle1 = TriangleChecker([a , b, c])
print(triangle1.is_triangle())