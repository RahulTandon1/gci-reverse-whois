**About**
The task I took up was:

"Create a python script that uses https://viewdns.info to find domain names owned by an individual person or a company. Share the code in Pagure/GitHub and provide the Asciinema recording while executing the script. Give a brief description on what is WHOIS lookup."


Currently work for the Chrome browser
**Installation**
Run ```pip install -r requirements.txt```
You may also have to install the chrome browser driver from https://chromedriver.chromium.org/downloads and add it's location to the $PATH variable.

**Run & Test it!**
Run ```python3 index.py```
Sample input commands
- 'food' - should be too short an entry.
- 'lelelelelel' - should result in 0 results found. 
- 'viewdns', 'fedora' - should work just fine.

**Contents**
1. index.py - the heart of the program that ties everything together
2. definitions.py - consists of various functions used in the ```index.py```. This plays a great role in making the code in ```index.py``` readable.
3. table.py - has functions that help print a given nested list in a tabular form
4. requirements.txt - the requirements of the project in terms of python modules/libraries, all of which can be downloaded using the command mentioned in the Installation section above.
5. sample table - example of the table from which the main content is extracted (given that the entity name provided is fine)
6. log.md - a log of how I went about coding this entire thing. It just makes the project a little more **ME**.
7. what-is-who-is.md - an extremely minimanlistic explanation of WHOIS by me.

**Sources of Help**
- https://selenium-python.readthedocs.io/waits.html#implicit-waits
- https://stackoverflow.com/questions/44141316/can-any-one-explain-to-me-what-is-to-poll-the-dom-in-selenium
- https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
- https://www.whoisxmlapi.com/blog/finding-hacked-websites-2/ (for undertanding and not copying as it is)