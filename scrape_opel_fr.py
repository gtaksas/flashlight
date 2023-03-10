from selenium import webdriver 
from bs4 import BeautifulSoup 
import sql_insert


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
        driver.implicitly_wait(10) 
        
        # Get the page source of the new page using Selenium 
        new_page_source = driver.page_source 
        
        # Parse the new page source using BeautifulSoup 
        soup = BeautifulSoup(new_page_source, 'html.parser') 
        
        # Extract the desired data from the page 
        market = soup.find('span', class_='category-label', text='Marché:').next_sibling.strip() 
        brand = soup.find('span', class_='category-label', text='Marque:').next_sibling.strip() 
        model = soup.find('span', class_='category-label', text='Modèle:').next_sibling.strip() 
        entity = soup.find('span', class_='category-label', text='Entité:').next_sibling.strip() 
        engine = soup.find('span', class_='category-label', text='Moteur:').next_sibling.strip() 
        price = soup.find('span', class_='category-label', text='Prix (TTC):').next_sibling.strip() 
        horsepower = soup.find('span', class_='category-label', text='Puissance:').next_sibling.strip() 
        bodystyle = soup.find('span', class_='category-label', text='Carrosserie:').next_sibling.strip() 
        serie = soup.find('span', class_='category-label', text='Série:').next_sibling.strip() 
        fuel = soup.find('span', class_='category-label', text='Carburant:').next_sibling.strip() 
        consumption = soup.find('span', class_='category-label', text='Consommation:').next_sibling.strip() 
        emission_co2 = soup.find('span', class_='category-label', text='Émission CO2:').next_sibling.strip() 
        transmission = soup.find('span', class_='category-label', text='Boîte de vitesses:').next_sibling.strip() 
        transmission_type = soup.find('span', class_='category-label', text='Type de boîte de vitesses:').next_sibling.strip() 
        driveline = soup.find('span', class_='category-label', text='Chaîne cinématique:').next_sibling.strip() 
        reaperstring = soup.find('span', class_='reaperstring').text.strip() 
        matchstring = soup.find('span', class_='matchstring').text.strip() 
        datasource = soup.find('span', class_='datasource').text.strip() 
        datum = soup.find('span', class_='datum').text.strip() 
        
        # Print the extracted data for the current page - FOR TEST PURPOSES ONLY! - DELETE IT LATER!!!
        print(f'Market: {market}') 
        print(f'Brand: {brand}') 
        print(f'Model: {model}') 
        print(f'Entity: {entity}') 
        print(f'Engine: {engine}') 
        print(f'Price: {price}') 
        print(f'Horsepower: {horsepower}')
        print(f'{bodystyle}')
        print(f'{serie}')
        print(f'{fuel}')
        print(f'{consumption}')
        print(f'{emission_co2}')
        print(f'{transmission}')
        print(f'{transmission_type}')
        print(f'{driveline}')
        print(f'{reaperstring}')
        print(f'{matchstring}')
        print(f'{datasource}')
        print(f'{datum}')

        # Call store data in MySQL function
        sql_insert.store()

