requests.get('https://viewdns.info/reversewhois/?q=companyName') gives a 403
which means it's a valid url/query, but it's 'Forbidden'. 

So directly using the requests module ain't going to work. 

I could either research on trying to fake the clientSecret or whatever the front end of the site might be sending, but 
A. I have less time on my hands. 
B. Using Selenium's a safer option rn.
And the Request headers shows an ':authority: viewdns.info' and 'cookie:' which probably means that faking this would require a lot of work.
-------
Will need to check this text that comes,
"There are 0 domains that matched this search query."
to check if there were no results
-------
Can use 
tables = document.getElementsByTagName('table')
tables[3]
in case of presence of results
-------
Read up a bit about waiting in selenium. 
Lmao, I just spent like 30 mins trying to get a weird selector with js and css working like: 

```tables = document.getElementsByTagName('table')[2].tBodies[0].rows[2].innerText.split('domains', 1)[0]```

which returned:

```
Reverse Whois results for heroku
==============

There are 26
```

and I just read the bottom of this page [https://selenium-python.readthedocs.io/waits.html#implicit-waits]
and this stackoverflow page [https://stackoverflow.com/questions/44141316/can-any-one-explain-to-me-what-is-to-poll-the-dom-in-selenium]
turns out that implicitly waits is all that I needed, because, and i'm quoting the Stock Overflow page here: "It means to check the DOM repeatedly, on a set interval (every X milliseconds), to see if an element exists."
Which matches my needs in this case, because finding a proper selector on the pages of viewdns.info will be crazy hard, and I need to work efficiently rn.
-------

got the driver scraping and stuff
made a different file for printing the table out. 
got the idea of making a feature for printing 'headings' from the second response on this stack overflow question [https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data]

need to get the following things working:
- user input
- cases of errors
    - not enough text to get results
    - no results found

-------

after a whole lot of hacking around everything is working. 
I had to make a choice btw. repetitive input validation (inclusive of checking the webpage for no results or too short a search term).

Finally ended up making an ```index``` function, passing the drived in wherever required and what not. 
And for the extensive input validation  (which in the end after it worked turned out to require simpler code than I thought) I used a function which checked the page for error, and returned an ```errorObj```. 

1. If there were errors, the ```errorObj``` would have 2 key-value pairs:
- errorPresent
- errorMsg

2. If there were NO errors, the ```errorObj``` would have 2 key-value pairs:
- errorPresent
- tables - the original tables arg that was passed to it for checking the text.

If there are errors, ```index.py``` would call the ```getEntityName``` function and pass in the error message which would then be displayed. Hence, this way I'd keep going in this loop until there are no errors. 

Once there are no errors, the ```tables``` list that was "souped" in the latest 'request' (so to say) is returned and is used to print the -> Domain Name, Creation Date, Registrar in a tabular form.

Not sure how stuff is working anymore cause I hacked around and rearranged stuff in ```index.py``` so much that I'm kinda just too exhausted. 

I don't wanna write the readme......
And then I've also got to write about what is a 'WHOIS Lookup'
Shoot!
----
Okay, so the readme is done. 

Now getting to the 'whois lookup' part. Hot damn I'm getting riled up. (just for the melodrama XD. But seriously tho i'm tired more than a bit)

I've just stiched together a litttle something. I'm very very very sleepy.
I'm officialy not writing anymore code for this task. 
Hopefully I'll understand the use and meaning of a reverse-whois with the passage of time
rn just gn and submitting task. Do not want to work on this again rn. 
Let's move on!