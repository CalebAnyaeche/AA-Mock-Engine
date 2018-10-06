from amadeus import Client, ResponseError

amadeus = Client(
    client_id='[YOUR_CLIENT_ID]',
    client_secret='[YOUR_CLIENT_SECRET]'
)

try:
    response = amadeus.reference_data.urls.checkin_links.get(airline='1X')
    print(response.data)
    # => [{'type': 'checkin-link', 'id': '1XEN-GBWeb', 'href': 'https://www....
except ResponseError as error:
    print(error)