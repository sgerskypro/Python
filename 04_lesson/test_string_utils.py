from string_utils import StringUtils


class TestStringUtils:
    utils = StringUtils()

    # Тесты для capitalize()
    def test_capitalize_positive(self):
        assert self.utils.capitalize("skypro") == "Skypro"
        assert self.utils.capitalize("hello") == "Hello"

    def test_capitalize_negative(self):
        assert self.utils.capitalize("") == ""
        assert self.utils.capitalize("123") == "123"

    # Тесты для trim()
    def test_trim_positive(self):
        assert self.utils.trim("   skypro") == "skypro"
        assert self.utils.trim("  hello") == "hello"

    def test_trim_negative(self):
        assert self.utils.trim("") == ""
        assert self.utils.trim("skypro") == "skypro"

    # Тесты для contains()
    def test_contains_positive(self):
        assert self.utils.contains("SkyPro", "S") is True
        assert self.utils.contains("SkyPro", "y") is True

    def test_contains_negative(self):
        assert self.utils.contains("SkyPro", "U") is False
        assert self.utils.contains("", "S") is False

    # Тесты для delete_symbol()
    def test_delete_symbol_positive(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_negative(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"
        assert self.utils.delete_symbol("", "S") == ""
