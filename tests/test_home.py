from pages.home_page import HomePage

def test_homepage(driver):
    driver.get("http://localhost:5000")
    home = HomePage(driver)
    assert "Your Name" in home.get_text()
