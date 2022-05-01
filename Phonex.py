#----------------------------------------------------------#
print('\033[1;33m'+'''

 /$$$$$$$  /$$                                                    
| $$__  $$| $$                                                    
| $$  \ $$| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$      
| $$$$$$$/| $$__  $$ /$$__  $$| $$__  $$ /$$__  $$|  $$ /$$/      
| $$____/ | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$ \  $$$$/       
| $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/  >$$  $$       
| $$      | $$  | $$|  $$$$$$/| $$  | $$|  $$$$$$$ /$$/\  $$      
|__/      |__/  |__/ \______/ |__/  |__/ \_______/|__/  \__/      
                                                                  
                                                                  ''')
#----------------------------------------------------------#
print('##### wait... #####')
#----------------------------------------------------------#
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
#----------------------------------------------------------#
while True :
    
    print('\ntype E to exit')
    a = input('\ntype phone number => ')
    if a == 'E':
        exit()
    b = input('\nselect your language by code en,fr,de,ja,ar ...==> ')
    if b == 'E':
        exit()
#----------------------------------------------------------#
    samNumber = phonenumbers.parse(a)

    yourlocation = geocoder.description_for_number(samNumber, b)
    print(yourlocation)

    service_provider = phonenumbers.parse(a)
    print(carrier.name_for_number(service_provider, b))

#country
#service provider

