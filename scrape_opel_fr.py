from selenium import webdriver 
from bs4 import BeautifulSoup 
#import sql_insert
import connect_db
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date, datetime


def scrape():
    # Create a new instance of the web driver 
    driver = webdriver.Chrome('C:/Program Files/chrome webdriver/chromedriver.exe') 

    # Navigate to the webpage 
    url = 'https://store.opel.fr/trim/configurable/corsa-citadine'
    driver.get(url) 

    # Check if an cookie page is present
    try:
        accept_my_choice = driver.find_element_by_xpath('//span[text()="Sauvegarder mes choix"]')

        # Click the span element
        accept_my_choice.click()
    except:
        pass

    # Find all the buttonWrapper divs on the page 
    button_divs = driver.find_elements_by_css_selector('div.buttonWrapper') 
    print(button_divs)
    print(len(button_divs))
    counter = len(button_divs)
    while counter > 1:
        counter -= 1
        button_divs = driver.find_elements_by_css_selector('div.buttonWrapper') 

    # Loop through each buttonWrapper div 
    #for div in button_divs: 
        #print(div)
        # Click the div to go to the corresponding page 
        button_divs[counter].click() 

        # Wait for the page to load 
        #driver.implicitly_wait(10) 
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inner')))
            
        # Get the page source of the new page using Selenium 
        new_page_source = driver.page_source 
            
        # Parse the new page source using BeautifulSoup 
        soup = BeautifulSoup(new_page_source, 'html.parser') 

        # Find market
        market = "?"

        # Find brand
        brand_title = soup.find('p', class_='title-primary').text.strip().split()
        brand = brand_title[0]
        
        # Find model
        model = soup.find('span', class_='title').text.strip()

        # Find bodystyle
        bodystyle = "?"

        # Find serie
        serie_line = soup.find('span', class_='specs-title').text.strip().split()
        serie = serie_line[0]
        
        # Find and store all the div elements that contain the desired data
        inner = soup.find_all('div', class_='inner')

        # Extract the desired data from the page 
        for line in inner:
            engine_span = line.find('span', class_='engineTitle')
            engine_desc_span = line.find('span', class_='engineDescription')
            engine_price_line = line.find('span', class_='enginePrice')
            if engine_price_line is not None:
                engine_price = engine_price_line.find('span', class_='formatMoney')
                if engine_price is not None:
                    enginePrice = engine_price.text.strip()
                    price = enginePrice

            if engine_span is not None:
                engineTitle = engine_span.text.strip()
                engineTitle_list = engineTitle.split()
                # Print the extracted data for the current page - FOR TEST PURPOSES ONLY! - DELETE IT LATER!!!
                print(f'engineTitle_list: {engineTitle_list}')
                # set entity
                entity = ' '.join(engineTitle_list[0: 4])
                # set engine
                engine = ' '.join([engineTitle_list[0], engineTitle_list[engineTitle_list.index('ch')-1]])
                # set horsepower
                horsepower = ' '.join([engineTitle_list[engineTitle_list.index('ch')-1], 'ch'])

            if engine_desc_span is not None:
                engineDescription = engine_desc_span.text.strip()
                engineDescription_list = engineDescription.split(', ')
                # Print the extracted data for the current page - FOR TEST PURPOSES ONLY! - DELETE IT LATER!!!
                print(f'engineDescription_list: {engineDescription_list}')
                # set fuel
                fuel = engineDescription_list[0]
                # set transmission_type
                transmission_type = engineDescription_list[1]


            if engine_span is not None:


                # We will need to click each inner element first (after the inner for loop!)!!!!!!!
                # Find consumption
                consumption = soup.find('div', {'data-testid':'TESTING_TECH_INFO_CONSUMPTION'}).text.strip()

                # Find emission_co2
                emission_co2 = soup.find('div', class_='emmisions-value').text.strip() 

                # set transmission
                featureList = soup.find_all('ul', class_='featureList featureListWithValue')
                featureInfos = [rep.next_sibling.strip() for rep in featureList if rep.find('span', text_='Nombre de rapports')]
                num_of_reports = featureList[-2].find('span', class_='featureValue').text
                transmission = transmission_type + num_of_reports

                # set driveline
                driveline = "?"
                
                # set reaperstring
                reaperstring = market + brand + model + serie + entity.replace(' ', '') + transmission + driveline

                #set matchstring
                ismatch = reaperstring
                matchstring = ismatch == reaperstring
                #matchsql = sql_insert.cur.execute('SELECT reaperstring form cars')
                #ismatch = matchsql.fetchall()
                #for match in matchsql:
                    #matchstring = ismatch == reaperstring
                #if matchstring == True: UPDATE SET WHERE else: INSERT

                # set source
                datasource = url.split('/')
                datasource = datasource[datasource.index('trim')+1]

                # Get the current date
                datum = date.today()
                #datum = datetime.now()
                
                # Print the extracted data for the current page - FOR TEST PURPOSES ONLY! - DELETE IT LATER!!!
                print(f'Market: {market}') 
                print(f'Brand: {brand}') 
                print(f'Model: {model}') 
                print(f'Entity: {entity}') 
                print(f'Engine: {engine}') 
                print(f'Price: {price}') 
                print(f'Horsepower: {horsepower}')
                print(f'Bodystyle: {bodystyle}')
                print(f'Serie: {serie}')
                print(f'Fuel: {fuel}')
                print(f'Consumption: {consumption}')
                print(f'Emission: {emission_co2}')
                print(f'Transmittion: {transmission}')
                print(f'Transmittion type: {transmission_type}')
                print(f'Driveline: {driveline}')
                print(f'Reaperstring: {reaperstring}')
                print(f'Matchstring: {matchstring}')
                print(f'Datasource: {datasource}')
                print(f'Datum: {datum}')

                # Call store data in MySQL function  __WE WILL NEED THIS ONE LATER ON!!!__ (DON'T FORGET IT)
                #sql_insert.store()
                sql = """INSERT INTO cars 
                (market, brand, model, entity, engine, price, horsepower, bodystyle, serie, fuel, consumption, emission_co2, transmission, transmission_type, driveline, reaperstring, matchstring, datasource, datum)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                val = (market, brand, model, entity, engine, price, horsepower, bodystyle, serie, fuel, consumption, emission_co2, transmission, transmission_type, driveline, reaperstring, matchstring, datasource, datum)
                connect_db.mycursor.execute(sql, val)

                connect_db.db1.commit()
            
        driver.get(url)
        driver.implicitly_wait(10)

    # Close all chrome windows
    driver.quit()

# Test
#scrape()