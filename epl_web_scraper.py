from nerodia.browser import Browser
import pandas as pd
import time

browser = Browser('chrome', headless=True) # Set Headless to True so the physical GUI of Chrome doesn't have to be used ⚡️ 
browser.goto('https://www.premierleague.com/stats/top/players/goals?se=274') # Now use the browser to navigate to the EPL Stats Page

time.sleep(5) # Allow data time to load into HTML

goals = pd.read_html(browser.html)[0] # Use Pandas to fetch all the tables within the browser html, select the first table it finds ([0])

# When you've reached the end of the table, the Page Next button adds class 'inactive' to the page next element (div). Use browser tools to inspect the button on the last page to see for yourself.
# As we know this, we can keep clicking the page next button and scraping the table until the button is inactive. In Python we can use while loop:
while ((browser.div(class_name=["paginationBtn", "paginationNextContainer", "inactive"])).exists == False):
  browser.div(class_name=["paginationBtn", "paginationNextContainer"]).fire_event('onClick') # fire onClick event on page next element. If it was a button element (not a div element), we could simply use .click() 
  time.sleep(2)
  goals = goals.append(pd.read_html(browser.html)[0]) # append the table from this page with the existing goals dataframe.
  print("Next Page")

goals = goals[goals['Stat'] > 0] # Random Players at end of table wit 0 goals...

goals = goals.dropna(axis=1, how='all') # Random Unamed Column (all NaN elements, so clear columns where 'all' values are NaN)

goals.to_csv(r'data/epl_goals_19_20.csv', index=False) # Save dataframe to new csv file

browser.close() # Close Browser