import re


phone = re.compile('((\+?\(?[0-9]+\)?)'
                   '?[ -]?(([\d]{2}[ -]?[\d]{3}[ -]?[\d]{2}[ -]?[\d]{2})|'
                   '([\d]{3}[ -]?[\d]{3}[ -][\d]{3})))')


#Dict object. Change all listed (in sets) values to its keys:
output_keys = {
    'address': {'Address', 'adress'},
    'phone': {'tel', 'telephone', 'tel:', 'tel.'},
    'fax': {'fax:'},
    'website': {'www', 'wwww', "Strona WWW"},
    'facebook': {'Facebook'},
    'email': {},
    'bussines_hours': {}
}

#Dict object. Merge json objects values to its keys:
keys_to_merge = {'street': 'address'}

#extract everything from object with key to 'main' object:
keys_to_extract = {'Contacts:'}


#find common items with pattern value:
common_items_in_dicts = {
    'phone': phone,
    'email': None,
    'website': None
}
