# --------------------- IMPORTS ---------------------
# used to parse normal text into a query string
import urllib.parse


# returns the name of an entity taken from the user
def getEntityName(errorPresent=False, errorMsg='Error with entity name'):

    if not errorPresent:

        # printing about
        print('Reverse WHOIS Lookup')

    # error present
    # (will only execute when we've already executed this function once,
    # found an error and are no re-executing to launch a new request)
    else:

        # padding above error message with 1 blank line
        print()

        # printing error message
        print(errorMsg)

        # padding below error message with 1 blank line
        print()

    # temporarily assigning 'name' an empty string
    name = str()

    # getting name of company and performing input validation
    while len(name) == 0:       # while name is empty

        # message to display
        # did not type across mulitple lines becuase it resulted in it getting
        # messed up while printing.
        # And i'm too lazy to google alternatives :P.
        msg = '''Please enter the name of the individual person or a company to look up: '''

        # getting name
        name = str(input(msg))

    # returning name
    return name


# takes input the baseURL and user's input string
# returns the url that can be used to 'request' the webpage
def getURL(base, userInput):
    # storing query string.
    # passing a dictionary to 'urlencode' that is parsed and finally returns
    # the query string
    queryString = str(urllib.parse.urlencode({
        'q': userInput
    }))

    # attaching query string to base url and storing a final variable
    # called 'url'
    url = base + queryString

    # returning the final url
    return url


'''
given the list of tables, returns an errorObject
which can be in 2 'states' so to say.
1. An error state where there will be 2 keys:
- errorPresent [boolean]
- errorMsg [str]

2. A non-error state where there will also be 2 keys
- errorPresent [boolean]
- tables [a beautiful soup object list that was originally passed to the
function to check for existence of errors. Is used afterwards for getting
a 2D List of all the information]
'''


def checkForErrors(tablesList):
    # the table where error message are found if present is the 3rd table
    # i.e. 2nd index
    potentialErrorTxt = str(tablesList[2].text)

    # there are 2 types of possible errors that i've come across.
    # In both cases no main content is returned.
    # Instead the certain exact text comes every single time.
    # I used that 2 make 2 types of errors,
    # and I search for the exact text using the 'in' operator

    # first type of error: no domains found for given search
    errType1 = 'There are 0 domains that matched this search query.'

    # second type fo error: search term is too short
    # I let the string be inline and long on purpose,
    # because otherwise it would've gotten messed up while
    # trying to identify the errors [search for them on the page]
    errType2 = 'Search term is too short.  Please be more specific in your search term.'
    # --------NOTE: The double space here ^ is on purpose.
    # It's the exact text that's present on the webpage.
    # ** THIS CAN BE THE REASON FOR A FUTURE ISSUE. **
    # But, for now we'll leave it hardcoded.

    if errType1 in potentialErrorTxt:
        return {
            'errorPresent': True,
            'errorMsg': str('Error: ' + errType1)
        }

    elif errType2 in potentialErrorTxt:
        return {
            'errorPresent': True,
            'errorMsg': str('Error: ' + errType2)
        }

    else:
        return {
            'errorPresent': False,
            'tables': tablesList
        }


# extracts the table data, like in the `sample table` file
# into a 2D Array
def getTableData(tables):

    # always located in 3rd table
    reqdTable = tables[3]

    # list of <tr> elements
    rows = reqdTable.findAll('tr')
    '''
    example of rows obj->
    [
    <tr>
        <td>Domain Name</td>
        <td>Creation Date</td>
        <td>Registrar</td>
    </tr>,
    <tr>
        <td>cheescake.moscow</td>
        <td>2016-01-27</td>
        <td>JSC "RU-CENTER"</td>
    </tr>
    .....]
    '''

    # Now, we cycle through each <tr> obj
    # and get all the <td> which are in the following order:
    # Domain Name
    # Creation Date
    # Registrar

    # list in which we'll store all the tuples of 'site's
    data = []

    for row in rows:
        '''
        e.g. of row:
        <tr>
            <td>Domain Name</td>
            <td >Creation Date</td>
            <td>Registrar</td>
        </tr>
        '''

        # converint row obj (tr tag) to list of td tags
        tdList = row.findAll('td')
        '''
        e.g. of tdlist:
        [<td>Domain Name</td>, <td>Creation Date</td>, <td>Registrar</td>]
        '''

        # extracting text from each element of the 'tdList'
        # and storing it in a temporary tuple
        tempSiteTuple = (tdList[0].text, tdList[1].text, tdList[2].text)

        # appending the tuple to the main data object
        data.append(tempSiteTuple)

    return data
