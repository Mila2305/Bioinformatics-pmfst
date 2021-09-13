def string_spelled(genome_path):
    """Find the string spelled by genome path"""
    result=genome_path[0]
    for i in range(1,len(genome_path)):
                   result=result+genome_path[i][-1]
    return result

x="""ACCGA
CCGAA
CGAAG
GAAGCT"""
inlines=x.split()
print(string_spelled(inlines))
