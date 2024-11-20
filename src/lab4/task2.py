import sys

# Основной класс для обработки данных опроса
class SurveyProcessor:
    def __init__(self, age_bounds):
        # Конструктор, принимает список возрастных границ
        self.age_bounds = age_bounds
        self.groups = self._create_groups(age_bounds)  # Создаем возрастные группы

    def _create_groups(self, age_bounds):
        # Метод для создания возрастных групп на основе переданных границ
        groups = []
        prev_bound = 0
        for bound in age_bounds:
            # Для каждой границы создаем группу от prev_bound до текущей границы
            groups.append(AgeGroup(prev_bound, bound))
            prev_bound = bound + 1  # Обновляем нижнюю границу для следующей группы
        # Последняя группа для всех возрастов от prev_bound (например, от 101+) до бесконечности
        groups.append(AgeGroup(prev_bound, float('inf')))
        return groups

    def process_survey_data(self, survey_data):
        # Метод для обработки данных опроса и распределения респондентов по возрастным группам
        for data in survey_data:
            name, age = data.split(',')  # Разделяем строку на имя и возраст
            age = int(age)  # Преобразуем возраст в целое число
            for group in self.groups:
                # Для каждой возрастной группы проверяем, входит ли возраст в диапазон этой группы
                if group.is_within_group(age):
                    group.add_respondent(name, age)  # Добавляем респондента в группу

    def print_results(self):
        # Метод для вывода результатов
        for group in reversed(self.groups):  # Перебираем группы в обратном порядке (от старшей к младшей)
            if group.respondents:
                group.print_group()  # Выводим только те группы, которые содержат респондентов

# Класс для представления одной возрастной группы
class AgeGroup:
    def __init__(self, min_age, max_age):
        # Конструктор, принимает минимальный и максимальный возраст для группы
        self.min_age = min_age
        self.max_age = max_age
        self.respondents = []  # Список для хранения респондентов в этой группе

    def is_within_group(self, age):
        # Проверка, входит ли возраст в диапазон текущей группы
        return self.min_age <= age <= self.max_age

    def add_respondent(self, name, age):
        # Добавляем респондента в группу
        self.respondents.append((name, age))

    def print_group(self):
        # Сортируем респондентов по возрасту (по убыванию), а затем по имени (по возрастанию)
        self.respondents.sort(key=lambda x: (-x[1], x[0]))
        # Формируем название возрастной группы
        group_label = f'{self.min_age}-{self.max_age}' if self.max_age != float('inf') else '101+'
        # Выводим строку с группой и респондентами
        print(f'{group_label}: ', end="")
        print(', '.join([f'{name} ({age})' for name, age in self.respondents]))


if __name__ == "__main__":
    # Чтение возрастных границ и данных опроса из командной строки
    age_bounds = list(map(int, sys.argv[1:]))  # Чтение границ возрастных групп из командной строки
    survey_data = []

    # Чтение данных опроса из стандартного ввода
    while True:
        try:
            line = input().strip()  # Чтение строки
            if line == "END":  # Если встречаем строку "END", завершаем ввод
                break
            survey_data.append(line)  # Добавляем респондента в список
        except EOFError:
            break  # Завершаем ввод при окончании данных (например, при EOF)

    # Обработка данных с использованием созданных возрастных групп
    processor = SurveyProcessor(age_bounds)
    processor.process_survey_data(survey_data)  # Распределяем респондентов по группам
    processor.print_results()  # Печатаем результаты
