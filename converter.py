from grid import Grid

def convert_sdk(filestream):
    content: str = filestream.read()
    lines = content.replace('.', '0').split('\n')
    grid = [list(line) for line in lines]
    return Grid(grid)

converters = {
    'sdk': convert_sdk
}

def convert(file: str) -> Grid:
    filestream = open(file)
    type = file.split('.').pop()
    
    try:
       converter = converters[type]
       return converter(filestream)
    except KeyError:
        raise Exception(f'Invalid file type: {type}')