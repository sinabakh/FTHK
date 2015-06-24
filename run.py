# First we Compress 3 files
# Note that the desired file should be added first
# So here we want the final file looks like "aks.jpg"

import Compressor

sources = []
sources.append('aks.jpg')
sources.append('aks2.jpg')
sources.append('music.mp3')
Compressor.compress(sources) # This generate file "comped.jpg"
Compressor.compress(sources, 'fileName') # This generate file "fileName.jpg"


# Then we Extract Thems

import Extractor

Extractor.extractor(source='filename.jpg') # This extract files in current folder
Extractor.extractor(source='filename.jpg', destination = './dest/') # This extract files in 'dest' folder
