def parseFasta(file):
    df = open(file, "r")
    contents = df.read()
    df.close()
    strings = contents.split()
    seq = ''.join(strings[1:])
    return seq

def parseCodonTable(file):
    f = open(file,"r")
    contents = f.read()
    f.close()
    codonTable = {}
    strings = contents.split()
    codons = strings[0::2]
    aminoacids = strings[1::2]
    for i in range(0,len(codons),1):
        key = codons[i]
        value = aminoacids[i]
        codonTable[key] = value
    return codonTable

def parseFile(file):
    df = open(file, "r")
    contents = df.read()
    df.close()
    contents = int(contents)
    return contents
