client_id = '32496'
client_secret = 'fbdcb8c9c00a91b758d620ed03f17442e178c500'

## Wegschrijven client ID en Secret
with open('secret_client_id', 'w') as outfile:
    outfile.write( client_id ) 
    outfile.close

## Wegschrijven client ID en Secret
with open('secret_client_secret', 'w') as outfile:
    outfile.write( client_secret)
    outfile.close

