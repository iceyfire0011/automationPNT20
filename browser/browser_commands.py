from selenium import webdriver

driver = webdriver.Firefox()


driver.get("https://google.com")

website_title = driver.title
print(website_title)

website_url = driver.current_url
print(website_url)

# driver.close()
