import unittest
from l_converters import FromMDtoHTML


class TestFromMDtoHTML(unittest.TestCase):
    def setUp(self):
        self.converter = FromMDtoHTML()

    def test_text_to_text(self):
        self.assertEqual(self.converter.text_to_text('''# gg ### ggg'''), '<h1>gg ### ggg</h1>')


if __name__ == '__main__':
    unittest.main()
