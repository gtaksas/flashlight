from selenium import webdriver 
from bs4 import BeautifulSoup 
import sql_insert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class scrape:
    # Create a new instance of the web driver 
    driver = webdriver.Chrome('C:/Program Files/chrome webdriver/chromedriver.exe') 

    # Navigate to the webpage 
    driver.get('https://store.opel.fr/trim/configurable/corsa-citadine') 

    # Check if an cookie page is present
    try:
        accept_my_choice = driver.find_element_by_xpath('//span[text()="Sauvegarder mes choix"]')

        # Click the span element
        accept_my_choice.click()
    except:
        pass

    # Find all the buttonWrapper divs on the page 
    button_divs = driver.find_elements_by_css_selector('div.buttonWrapper') 

    # Loop through each buttonWrapper div 
    for div in button_divs: 
        # Click the div to go to the corresponding page 
        div.click() 

        # Wait for the page to load 
        #driver.implicitly_wait(10) 
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inner')))
        
        # Get the page source of the new page using Selenium 
        new_page_source = driver.page_source 
        
        # Parse the new page source using BeautifulSoup 
        soup = BeautifulSoup(new_page_source, 'html.parser') 
        
        # Find and store all the div elements that contain the desired data
        inner = soup.find_all('div', class_='inner')

        # Extract the desired data from the page 
        for line in inner:
            engine_span = line.find('span', class_='engineTitle')
            engine_desc_span = line.find('span', class_='engineDescription')
            engine_price = line.find('span', class_='enginePrice').find('span', class_='formatMoney')
            if engine_span is not None:
                engineTitle = engine_span.text.strip()
                engineTitle_list = engineTitle.split()
                # Print the extracted data for the current page - FOR TEST PURPOSES ONLY! - DELETE IT LATER!!!
                print(f'engineTitle_list: {engineTitle_list}')
            if engine_desc_span is not None:
                engineDescription = engine_desc_span.text.strip()
                engineDescription_list = engineDescription.split(', ')
                # Print the extracted data for the current page - FOR TEST PURPOSES ONLY! - DELETE IT LATER!!!
                print(f'engineDescription_list: {engineDescription_list}')
            if engine_price is not None:
                enginePrice = engine_price.text.strip()
                price = enginePrice
                # Print the extracted data for the current page - FOR TEST PURPOSES ONLY! - DELETE IT LATER!!!
                print('Price: ' + price)

            #market = soup.find('span', class_='category-label', text='Marché:').next_sibling.strip() 
            #brand = soup.find('span', class_='category-label', text='Marque:').next_sibling.strip() 
            #model = soup.find('span', class_='category-label', text='Modèle:').next_sibling.strip() 
            #entity = soup.find('span', class_='category-label', text='Entité:').next_sibling.strip() 
            #engine = soup.find('span', class_='category-label', text='Moteur:').next_sibling.strip() 
            #price = soup.find('span', class_='category-label', text='Prix (TTC):').next_sibling.strip() 
            #horsepower = soup.find('span', class_='category-label', text='Puissance:').next_sibling.strip() 
            #bodystyle = soup.find('span', class_='category-label', text='Carrosserie:').next_sibling.strip() 
            #serie = soup.find('span', class_='category-label', text='Série:').next_sibling.strip() 
            #fuel = soup.find('span', class_='category-label', text='Carburant:').next_sibling.strip() 
            #consumption = soup.find('span', class_='category-label', text='Consommation:').next_sibling.strip() 
            #emission_co2 = soup.find('span', class_='category-label', text='Émission CO2:').next_sibling.strip() 
            #transmission = soup.find('span', class_='category-label', text='Boîte de vitesses:').next_sibling.strip() 
            #transmission_type = soup.find('span', class_='category-label', text='Type de boîte de vitesses:').next_sibling.strip() 
            #driveline = soup.find('span', class_='category-label', text='Chaîne cinématique:').next_sibling.strip() 
            #reaperstring = soup.find('span', class_='reaperstring').text.strip() 
            #matchstring = soup.find('span', class_='matchstring').text.strip() 
            #datasource = soup.find('span', class_='datasource').text.strip() 
            #datum = soup.find('span', class_='datum').text.strip() 
            
            # Print the extracted data for the current page - FOR TEST PURPOSES ONLY! - DELETE IT LATER!!!
            #print(f'Market: {market}') 
            #print(f'Brand: {brand}') 
            #print(f'Model: {model}') 
            #print(f'Entity: {entity}') 
            #print(f'Engine: {engine}') 
            #print(f'Price: {price}') 
            #print(f'Horsepower: {horsepower}')
            #print(f'{bodystyle}')
            #print(f'{serie}')
            #print(f'{fuel}')
            #print(f'{consumption}')
            #print(f'{emission_co2}')
            #print(f'{transmission}')
            #print(f'{transmission_type}')
            #print(f'{driveline}')
            #print(f'{reaperstring}')
            #print(f'{matchstring}')
            #print(f'{datasource}')
            #print(f'{datum}')

            # Call store data in MySQL function  __WE WILL NEED THIS ONE LATER ON!!!__ (DON'T FORGET IT)
            #sql_insert.store()

    # Close all chrome windows
    driver.quit()

# Test
scrape()