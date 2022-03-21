## Inlezen client_id
def read_client():
    with open('secret_client_id') as importfile:
        global client_id
        client_id = importfile.read()
        importfile.close()

    ## Inlezen Secret
    with open('secret_client_secret') as importfile:
        global client_secret
        client_secret = importfile.read()
        importfile.close()

