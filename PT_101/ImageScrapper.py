from google_images_search import GoogleImagesSearch

# Replace with your own Google Custom Search API key and Google Search Engine ID
gis = GoogleImagesSearch('AIzaSyDCdpESdJy3FOeTWB1zngS153DqFRumw0w', '62af1a6d94d894ed6')

# Define search parameters
search_params = {
    'q': 'room interiors',
    'num': 10,
    'imgSize': 'large',
    'fileType': 'jpg',
    'safe': 'high'
}

# Search for images
gis.search(search_params)

# Download images
for image in gis.results():
    image.download('/home/ziyad/Projects/Python/images')
