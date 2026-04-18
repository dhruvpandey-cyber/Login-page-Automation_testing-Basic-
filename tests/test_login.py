from pages.login_page import LoginPage
import os

def get_test_app_url():
    """Get the file URL for the test application"""
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_app.html'))
    return f'file:///{file_path}'

def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "admin123")

    assert "dashboard" in driver.page_source.lower()


def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("wrong", "wrong")

    assert "error" in driver.page_source


def test_empty_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("", "admin123")

    assert "username is required" in driver.page_source.lower()


def test_empty_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "")

    assert "password is required" in driver.page_source.lower()


def test_both_empty(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("", "")

    assert "username is required" in driver.page_source.lower()


def test_wrong_username_valid_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("wronguser", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_valid_username_wrong_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "wrongpass")

    assert "invalid credentials" in driver.page_source.lower()


def test_username_with_spaces(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login(" admin ", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_password_with_spaces(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", " admin123 ")

    assert "invalid credentials" in driver.page_source.lower()


def test_username_with_special_chars(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin@#$%", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_password_with_special_chars(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "admin123!@#")

    assert "invalid credentials" in driver.page_source.lower()


def test_very_long_username(setup):
    driver = setup
    login = LoginPage(driver)

    long_username = "a" * 1000
    login.open(get_test_app_url())
    login.login(long_username, "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_very_long_password(setup):
    driver = setup
    login = LoginPage(driver)

    long_password = "a" * 1000
    login.open(get_test_app_url())
    login.login("admin", long_password)

    assert "invalid credentials" in driver.page_source.lower()


def test_case_sensitive_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("Admin", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_case_sensitive_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "Admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_sql_injection_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin' OR '1'='1", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_sql_injection_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "admin123' OR '1'='1")

    assert "invalid credentials" in driver.page_source.lower()


def test_xss_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("<script>alert('xss')</script>", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_xss_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "<script>alert('xss')</script>")

    assert "invalid credentials" in driver.page_source.lower()


def test_numeric_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("12345", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_numeric_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "123456")

    assert "invalid credentials" in driver.page_source.lower()


def test_email_format_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin@example.com", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_leading_trailing_spaces_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("  admin  ", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_leading_trailing_spaces_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "  admin123  ")

    assert "invalid credentials" in driver.page_source.lower()


def test_unicode_characters_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("админ", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_unicode_characters_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "пароль123")

    assert "invalid credentials" in driver.page_source.lower()


def test_minimum_length_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("a", "admin123")

    assert "invalid credentials" in driver.page_source.lower()


def test_minimum_length_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open(get_test_app_url())
    login.login("admin", "a")

    assert "invalid credentials" in driver.page_source.lower()