def extractor(source="comped.jpg", destination="./"):
    sourceFile = open(source, 'r')
    content = sourceFile.readlines()
    customInfo = get_custom_info(content)
    if customInfo is None:
        return
    exts = get_dest_ext(customInfo)
    delimiter = get_delimiter(customInfo)
    fileNum = 0
    dFile = get_destination_file(fileNum, exts, destination)
    for line in content:
        if line.find("FTHKcdDL") != -1:
            dFile.write(line[:line.find("FTHKcdDL")])
            break
        if line.find(delimiter) == -1:
            dFile.write(line)
        else:
            dFile.write(line[:line.find(delimiter)])
            fileNum += 1
            dFile = get_destination_file(fileNum, exts, destination)
            dFile.write(line[line.find(delimiter) + len(delimiter):])




def get_custom_info(source):
    for line in reversed(source):
        if line.find("FTHKcdDL"):
            return line[line.find("FTHKcdDL"):]
    return None


def get_dest_ext(info):
    return eval(info[info.find("FTHKcdSE") + 8: info.find("FTHKcdEN")])

def get_delimiter(info):
    return info[info.find("FTHKcdDL") + 8: info.find("FTHKcdSE")]

def file_name(fileNum, exts):
    return "File" + str(fileNum+1) + "." + str(exts[fileNum])

def get_destination_file(fileNum, exts, dest):
    return open(dest + file_name(fileNum, exts), 'w')