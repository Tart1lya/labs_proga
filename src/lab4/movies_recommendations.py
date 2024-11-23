import os
from typing import List, Dict


# Класс, представляющий фильм
class Movie:
    def __init__(self, movie_id: int, title: str):
        """Инициализация фильма."""
        self.movie_id = movie_id  # Идентификатор фильма
        self.title = title        # Название фильма


# Класс, представляющий историю просмотров одного пользователя
class UserHistory:
    def __init__(self, user_id: int, watched_movies: List[int]):
        """Инициализация истории просмотров пользователя."""
        self.user_id = user_id              # Уникальный ID пользователя
        self.watched_movies = watched_movies  # Список фильмов, просмотренных пользователем


# Класс системы рекомендаций
class RecommendationSystem:
    def __init__(self, movies_file: str, history_file: str):
        """Инициализация системы рекомендаций."""
        # Загрузка данных о фильмах и истории просмотров
        self.movies = self.load_movies(movies_file)            # Словарь с информацией о фильмах
        self.user_histories = self.load_user_histories(history_file)  # Список историй пользователей

    @staticmethod
    def load_movies(file_path: str) -> Dict[int, str]:
        """
        Загружает список фильмов из файла.
        Возвращает словарь: {id фильма: название фильма}.
        """
        movies = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                movie_id, title = line.strip().split(',', 1)
                movies[int(movie_id)] = title
        return movies

    @staticmethod
    def load_user_histories(file_path: str) -> List[UserHistory]:
        """
        Загружает историю просмотров из файла.
        Возвращает список объектов UserHistory.
        """
        histories = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for idx, line in enumerate(file, start=1):
                watched_movies = list(map(int, line.strip().split(',')))  # Преобразуем строку в список чисел
                histories.append(UserHistory(user_id=idx, watched_movies=watched_movies))
        return histories

    def recommend_movie(self, user_movies: List[int]) -> str:
        """
        Рекомендует фильм на основе списка фильмов, просмотренных пользователем.
        Возвращает название фильма или сообщение, что рекомендаций нет.
        """
        # Шаг 1: Найти похожих пользователей
        similar_users = self.get_similar_users(user_movies)

        # Шаг 2: Получить рекомендации из фильмов похожих пользователей
        recommended_movie_id = self.get_recommendations(user_movies, similar_users)

        # Возвращаем название фильма или сообщение, если рекомендаций нет
        return self.movies[recommended_movie_id] if recommended_movie_id else "Нет рекомендаций."

    def get_similar_users(self, user_movies: List[int]) -> List[UserHistory]:
        """
        Находит пользователей, которые посмотрели хотя бы половину фильмов из списка заданного пользователя.
        Возвращает отсортированный список похожих пользователей.
        """
        similar_users = []
        user_movies_set = set(user_movies)  # Преобразуем фильмы пользователя в множество для быстрого сравнения

        for history in self.user_histories:
            # Подсчитываем количество общих фильмов
            common_movies = len(user_movies_set.intersection(history.watched_movies))
            weight = common_movies / len(user_movies)  # Рассчитываем вес схожести

            # Если пользователь похож, добавляем его в список
            if weight >= 0.5:
                similar_users.append((weight, history))

        # Сортируем пользователей по убыванию веса (чем выше вес, тем больше схожесть)
        similar_users.sort(reverse=True, key=lambda x: x[0])
        return [user[1] for user in similar_users]  # Возвращаем только объекты UserHistory

    @staticmethod
    def get_recommendations(user_movies: List[int], similar_users: List[UserHistory]) -> int:
        """
        Собирает фильмы из списков похожих пользователей, исключая уже просмотренные.
        Возвращает ID фильма с максимальным количеством рекомендаций.
        """
        movie_counts = {}  # Словарь для подсчета частоты упоминаний фильмов
        user_movies_set = set(user_movies)  # Множество просмотренных фильмов пользователя

        for user in similar_users:
            for movie in user.watched_movies:
                # Учитываем только те фильмы, которые пользователь еще не видел
                if movie not in user_movies_set:
                    movie_counts[movie] = movie_counts.get(movie, 0) + 1

        # Если нет подходящих фильмов, возвращаем None
        if not movie_counts:
            return None

        # Возвращаем ID фильма с максимальным числом упоминаний
        return max(movie_counts, key=movie_counts.get)


# Константы для файлов
MOVIES_FILE = "movies.txt"  # Путь к файлу с фильмами
HISTORY_FILE = "history.txt"  # Путь к файлу с историей просмотров


if __name__ == "__main__":
    # Проверяем наличие файлов перед запуском
    if not os.path.exists(MOVIES_FILE) or not os.path.exists(HISTORY_FILE):
        print("Не найдены файлы с фильмами или историей просмотров.")
        exit(1)

    # Ввод списка просмотренных фильмов пользователя
    user_input = input("Введите идентификаторы фильмов через запятую: ")
    user_movies = list(map(int, user_input.strip().split(',')))

    # Инициализация системы рекомендаций
    recommendation_system = RecommendationSystem(MOVIES_FILE, HISTORY_FILE)

    # Получение рекомендации
    recommendation = recommendation_system.recommend_movie(user_movies)

    # Вывод результата
    print("Рекомендация:", recommendation)
