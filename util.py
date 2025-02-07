def load_file(filename):
    with open(filename, 'r') as file:
        filetext = ''
        for row in file:
            filetext += row

        return filetext
