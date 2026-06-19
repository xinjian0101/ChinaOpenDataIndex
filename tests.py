import unittest
import main


class CatalogTest(unittest.TestCase):
    def test_validation(self):
        missing = main.validate_entry({"id": "demo"})
        self.assertTrue(len(missing) > 0)


if __name__ == "__main__":
    unittest.main()
