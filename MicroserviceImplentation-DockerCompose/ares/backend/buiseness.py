def get_data():
    with open('names.txt') as f:
      names = f.read()
      nameList = names.split()
    return nameList