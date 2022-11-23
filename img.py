from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('nikofigit99@gmail.com', 'November101121')

# GET a profile
profile = api.get_profile('adamrizananda')

# GET a profiles contact info
contact_info = api.get_profile_contact_info('adamrizananda')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('adamrizananda')


print(contact_info)