import uuid


def compress(sources, destination="comped", extension=None):
    destFileName = destination + "." + get_ext(sources[0])
    if extension is not None:
        destFileName = destination + "." + extension
    dest = open(destFileName, "w")
    sourcesExt = []
    delimiter = generate_delimiter()
    for source in sources:
        sourcesExt.append(get_ext(source))
        sFile = open(source, "r")
        dest.write(sFile.read())
        if source != sources[-1]:
            dest.write(delimiter)
        
    dest.write("FTHKcdDL")
    dest.write(delimiter)
    dest.write("FTHKcdSE")
    dest.write(str(sourcesExt))
    dest.write("FTHKcdEN")


def get_ext(filename):
    if filename.rfind('.') != -1:
        return filename[filename.rfind('.')+1:]
    return ""


def generate_delimiter():
    return str(uuid.uuid4())