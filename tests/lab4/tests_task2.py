import unittest
from io import StringIO
import sys

# Импортируем классы, которые будем тестировать
from src.lab4.task2 import SurveyProcessor, AgeGroup


class TestSurveyProcessor(unittest.TestCase):

    def test_create_groups(self):
        # Тестируем создание групп возрастов
        age_bounds = [18, 25, 35, 45, 60, 80, 100]
        processor = SurveyProcessor(age_bounds)

        # Проверим количество групп
        self.assertEqual(len(processor.groups), 8)

        # Проверим корректность диапазонов возрастных групп
        self.assertEqual(processor.groups[0].min_age, 0)
        self.assertEqual(processor.groups[0].max_age, 18)

        self.assertEqual(processor.groups[1].min_age, 19)
        self.assertEqual(processor.groups[1].max_age, 25)

        self.assertEqual(processor.groups[-1].min_age, 101)
        self.assertEqual(processor.groups[-1].max_age, float('inf'))

    def test_add_respondent_to_group(self):
        # Тестируем добавление респондента в группу
        age_bounds = [18, 25, 35, 45, 60, 80, 100]
        processor = SurveyProcessor(age_bounds)
        processor.process_survey_data([
            "Соколов Андрей Сергеевич,15",
            "Егоров Алан Петрович,7"
        ])

        # Проверяем, что респонденты попали в правильные группы
        self.assertEqual(len(processor.groups[0].respondents), 2)  # Группа 0-18
        self.assertEqual(processor.groups[0].respondents[0], ("Соколов Андрей Сергеевич", 15))
        self.assertEqual(processor.groups[0].respondents[1], ("Егоров Алан Петрович", 7))


    def test_output_format(self):
        # Проверка вывода в консоль
        age_bounds = [18, 25, 35, 45, 60, 80, 100]
        processor = SurveyProcessor(age_bounds)
        processor.process_survey_data([
            "Соколов Андрей Сергеевич,15",
            "Егоров Алан Петрович,7",
            "Дьячков Нисон Иринеевич,88",
            "Иванов Варлам Якунович,88",
            "Кошельков Захар Брониславович,105",
            "Старостин Ростислав Ермолаевич,50",
            "Ярилова Розалия Трофимовна,29"
        ])

        # Перехватываем вывод в строковый поток
        captured_output = StringIO()
        sys.stdout = captured_output
        processor.print_results()
        sys.stdout = sys.__stdout__  # Восстанавливаем стандартный вывод

        expected_output = (
            "101+: Кошельков Захар Брониславович (105)\n"
            "81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)\n"
            "46-60: Старостин Ростислав Ермолаевич (50)\n"
            "26-35: Ярилова Розалия Трофимовна (29)\n"
            "0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)\n"
        )

        # Сравниваем захваченный вывод с ожидаемым
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
