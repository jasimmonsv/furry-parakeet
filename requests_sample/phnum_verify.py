import requests
import json

api_key = ''
phone_number = ''
url = 'http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=US&format=1'.format(
    api_key=api_key,
    phone_number=phone_number
)