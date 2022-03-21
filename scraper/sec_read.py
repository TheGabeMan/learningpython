## Inlezen client_id
with open('secret_client_id') as importfile:
    client_id = importfile.read()
    importfile.close()

## Inlezen Secret
with open('secret_client_secret') as importfile:
    client_secret = importfile.read()
    importfile.close()

