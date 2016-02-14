
###Parsing XML

'''
The findall method retrieves a Python list of subtrees that represent the user
structures in the XML tree. Then we can write a for loop that looks at each of
the user nodes, and prints the name and id text elements as well as the x attribute
from the user node.
'''

import xml.etree.ElementTree as ET

input = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print 'User count:', len(lst)

for item in lst:
	print 'Name', item.find('name').text
	print 'Id', item.find('id').text
	print 'Attribute', item.get('x')



###Parsing JSON

'''
We construct our JSON by nesting dictionaries (objects) and lists as needed. In
this example, we represent a list of users where each user is a set of key-value
pairs (i.e., a dictionary). So we have a list of dictionaries.
In the following program, we use the built-in json library to parse the JSON and
read through the data. Compare this closely to the equivalent XML data and code
above. The JSON has less detail, so we must know in advance that we are getting a
list and that the list is of users and each user is a set of key-value pairs. The JSON
is more succinct (an advantage) but also is less self-describing (a disadvantage).

We construct our JSON by nesting dictionaries (objects) and lists as needed. In
this example, we represent a list of users where each user is a set of key-value
pairs (i.e., a dictionary). So we have a list of dictionaries.
In the following program, we use the built-in json library to parse the JSON and
read through the data. Compare this closely to the equivalent XML data and code
above. The JSON has less detail, so we must know in advance that we are getting a
list and that the list is of users and each user is a set of key-value pairs. The JSON
is more succinct (an advantage) but also is less self-describing (a disadvantage).

If you compare the code to extract data from the parsed JSON and XML you will
see that what we get from json.loads() is a Python list which we traverse with a
for loop, and each item within that list is a Python dictionary. Once the JSON
has been parsed, we can use the Python index operator to extract the various bits
of data for each user. We don't have to use the JSON library to dig through the
parsed JSON, since the returned data is simply native Python structures.

'''

import json

input = '''
[
	{ "id" : "001",
		"x" : "2",
		"name" : "Chuck"
	} ,
	{ "id" : "009",
		"x" : "7",
		"name" : "Brent"
	}
]'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
	print 'Name', item['name']
	print 'Id', item['id']
	print 'Attribute', item['x']


###Google geocoding web service
'''
The following is a simple application to prompt the user for a search string, call
the Google geocoding API, and extract information from the returned JSON.

The program takes the search string and constructs a URL with the search string
as a properly encoded parameter and then uses urllib to retrieve the text from the
Google geocoding API. Unlike a fixed web page, the data we get depends on the
parameters we send and the geographical data stored in Google's servers.

Once we retrieve the JSON data, we parse it with the json library and do a few
checks to make sure that we received good data, then extract the information that
we are looking for.
'''

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1 : break

	url = serviceurl + urllib.urlencode({'sensor':'false',
			'address': address})
	print 'Retrieving', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'

	try: js = json.loads(str(data))
	except: js = None

	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ===='
		print data
		continue

	print json.dumps(js, indent=4)

	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lng"]
	print 'lat',lat,'lng',lng
	location = js['results'][0]['formatted_address']
	print location
