from google_images_search import GoogleImagesSearch

# Replace with your own Google Custom Search API key and Google Search Engine ID
gis = GoogleImagesSearch('', '')

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
