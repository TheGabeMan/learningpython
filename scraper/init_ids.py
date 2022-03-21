client_id = input('Your client ID: ')
client_secret = input('Your Client Secret: ')

## Wegschrijven client ID en Secret
with open('secret_client_id', 'w') as outfile:
    outfile.write( client_id ) 
    outfile.close

## Wegschrijven client ID en Secret
with open('secret_client_secret', 'w') as outfile:
    outfile.write( client_secret)
    outfile.close

