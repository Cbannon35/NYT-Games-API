from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

nyt_connections_url = "https://www.nytimes.com/games/connections"
driver = webdriver.Chrome()
daily_connections = []

def main():
    driver.get(nyt_connections_url)
    assert "Connections:" in driver.title

    # Wait for the element with the 'board' id to be present
    board = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "board"))
    )
    # board = driver.find_element(By.ID, "board")
    board_html = board.get_attribute('outerHTML')

    # parse the html
    soup = BeautifulSoup(board_html, 'html.parser')
    items = soup.find_all(class_='item')
    for item in items:
        daily_connections.append(item.text)

    driver.close()
        
def debug(board):
    # Print the HTML content of the 'board' element
    print("Element HTML:", board.get_attribute('outerHTML'))
    
    # write driver page source
    with open('connections.html', 'w') as f:
        f.write(driver.page_source)

def print_connections():
    for connection in daily_connections:
        print(connection)


if __name__ == '__main__':
    main()