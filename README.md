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
2. https://mavin.io/search?q=&amp;bt=sold&amp;cat=261333&amp;sort=EndTimeSoonest&amp;page=201    ( greater than 200 but less than 40,000) scraped 
3. https://mavin.io/search?q=&cat=261330 scraped 
4. https://mavin.io/search?q=&cat=261893 scraped
5. https://mavin.io/search?q=&cat=214  scraped
6. https://mavin.io/search?q=&cat=170134 scraped
7. https://mavin.io/search?q=&cat=2956 scraped
8. https://mavin.io/search?q=&cat=25583 scraped

* Note the page number at the end of the url !!
[ I call it the item number ] 
e.g 262055 in https://mavin.io/search?q=&cat=262055
9. https://mavin.io/search?q=&cat=262055 
10. https://mavin.io/search?q=&cat=2969 - results = 52,000 
11. https://mavin.io/search?q=&cat=183444 - results = 450,000 
12. https://mavin.io/search?q=&cat=43371 - results = 12,000 
13. https://mavin.io/search?q=&cat=183435 - results = 179,000 
14. https://mavin.io/search?q=&cat=217 - results = 47,000 
15. https://mavin.io/search?q=&cat=166107 - results = 3,000 
16. https://mavin.io/search?q=&cat=666 - results = 200,000 
17. https://mavin.io/search?q=&cat=213 - results = 20,300,000 
18. https://mavin.io/search?q=&cat=170131 - results = 450 
19. https://mavin.io/search?q=&cat=37795 - results = 24,000 
20. https://mavin.io/search?q=&cat=133072 - results = 4,300 
21. https://mavin.io/search?q=&cat=25579 - results = 300 
22. https://mavin.io/search?q=&cat=183715 - results = 100 
23. https://mavin.io/search?q=&cat=215 - results = 12,000,000 
24. https://mavin.io/search?q=&cat=4240 - results = 73,000 
25. https://mavin.io/search?q=&cat=43363 - results = 400 
26. https://mavin.io/search?q=&cat=261328 - results = 6,100,000 
27. https://mavin.io/search?q=&cat=216 - results = 2,400,000 
28. https://mavin.io/search?q=&cat=261331 - results = 12,000 

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
