import unittest
from src.lab4.movies_recommendations import RecommendationSystem


class TestRecommendationSystem(unittest.TestCase):
    def setUp(self):
        self.system = RecommendationSystem("test_movies.txt", "test_history.txt")

    def test_no_recommendations(self):
        self.assertEqual(self.system.recommend_movie([1, 2, 3, 4]), "Нет рекомендаций.")


if __name__ == "__main__":
    unittest.main()
