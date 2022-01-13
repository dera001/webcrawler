# Web_Crawler 
***
 
 + Automated webscrapping program...
 
 + Scans through mavin.io search results and save retrieved information in an ordered format (.csv)
 
 + Built with passion @ Dera Mobile Legacy
 
 + Aurthor : CHIDERA C. ONWURAH
 
***

# complete results with 

a. products name, 
b. date sold, 
c. price sold, 
d. shipping cost and 
e. the pictures. 

All of the previous categories will be extracted to different columns in an csv


1. https://mavin.io/search?q=&amp;bt=sold&amp;cat=261332&amp;sort=EndTimeSoonest&amp;page=201    ( greater than 200 but less than 40,000) scraped
2. https://mavin.io/search?q=&cat=216 - results = 2,400,000 

# REQUIREMENT

1. Python3
2. beautifulsoup4 (bs4)
3. requests

# INSTALLATION

open cmd or terminal and run this command

~~~sh

pip install bs4, requests

~~~


# PROGRAM FLOW

- URLS
take for instance ;

https://mavin.io/search?q=&amp;bt=sold&amp;cat=261332&amp;sort=EndTimeSoonest&amp;page=201 [note] page starts from 201 
till n'th number of pages.. usually in range of 201 - 400,000 

- The program takes the item number [ self.num = 	("2956") ] input at [ line 11 ] in the main.py file .
And it scrapes all results corresponding to the said item number

- The only line that needs modification is [ line 11 ] .... 
Bcoz of the remaining items that needs to be scraped. so let the program scrape tons of information as its relates to a specific item, you can check the [ log.csv ] file if the number of items scraped are up to 7 million, kill the program by ;

~~~sh
Ctrl + C
~~~

- Don't worry there will not be any duplicate results

- Network issues wont affect the program, bcoz it keeps restarting itself anytime the signal is not strong enough.

- Contact [ mailto: deramobilelegacy@gmail.com ] for more enquiry

# EXECUTION

1. Open CMD or bash console in the project folder
2. Type in this command to run

~~~sh

python main.py

~~~

## ALL THE BEST
