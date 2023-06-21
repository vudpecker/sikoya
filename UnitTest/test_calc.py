


class TestCalculateGrade(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(
            calculate_grade([90, 80, 70, 60]), 75.0, places=2
        )