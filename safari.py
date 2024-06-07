from selenium import webdriver

# Initialize the Safari driver
driver = webdriver.Safari()

# Open a webpage
driver.get("https://www.example.com")

# Interact with the webpage (e.g., find an element)
element = driver.find_element_by_tag_name("h1")

# Print the text of the element
print(element.text)

# Close the browser
driver.quit()
