from google_images_search import GoogleImagesSearch

# Replace with your own Google Custom Search API key and Google Search Engine ID
gis = GoogleImagesSearch('AIzaSyDCdpESdJy3FOeTWB1zngS153DqFRumw0w', '62af1a6d94d894ed6')

# Define search parameters
search_params = {
    'q': 'room interiors',
    'num': 10000,
    'imgSize': 'large',
    'fileType': 'jpg',
    'safe': 'high',
    'imgType': 'photo',
    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
    'siteSearch': 'https://www.zillow.com/ OR https://www.realtor.com/'
}

# Search for images
gis.search(search_params)

# Download images
for image in gis.results():
    image.download('/home/ziyad/Projects/Python/images')
