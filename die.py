import requests
import random
import string

scam_form_url = 'http://eg.detector-million.t500track12.com/join'

## Random line in txt file function
def random_line(file_name):
    lines = open(file_name).read().splitlines()
    return random.choice(lines)

## Generate a number/character sequence
def id_generator(size=32, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


resp = requests.post(scam_form_url)
print("Scam website still live")


while resp.status_code == 200:

    first_name = random_line('first_names.txt')
    last_name = random_line('last_names.txt')
    e_mail = first_name.lower() + id_generator(4) + random_line('email_providers.txt')
    session_id = id_generator()
    affiliate_id = id_generator(4, string.digits)
    phone = id_generator(8, string.digits)
    phonecc = "%2B" + random_line('phone_areas.txt')

    form = {
        'first_name': first_name,
        'last_name': last_name,
        'email': e_mail,
        'phone': phone,
        'session_id': session_id,
        'affiliate_id': affiliate_id,
        'phonecc': phonecc,
        'password': 'fg6W92Db',
        'fpp': 1,
        'current_url': 'eg.detector-million.t500track12.com'
    }

    print("New sign up: {} {} with phone number: {} and e-mail: {}".format(first_name, last_name, phone, e_mail))

    resp = requests.post(scam_form_url, form)
