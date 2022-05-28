import os


def read_dependences_list(directory):
    # list to save all dependencies from all files
    content = []

    for r, d, f in os.walk(directory):
        for file in f:
            if file.endswith("requirements.txt"):
                print(os.path.join(r, file))
                file1 = open(os.path.join(r, file), "r+")
                print(file1.read())

                with open(os.path.join(r, file), 'r') as filehandle:
                    for line in filehandle:
                        # remove linebreak which is the last character of the string
                        current_place = line[:-1]

                        # add item to the list
                        content.append(current_place)

    # sorting list
    content.sort(key=str.casefold)
    print(content)
    print(len(content))

    # deleting empty spaces
    content = list(filter(None, content))
    print(content)
    print(len(content))

    # deleting duplicates
    content = list(dict.fromkeys(content))
    print(content)
    print(len(content))

    return content


def save_dependences_list(dep_list, export_dir):
    # saving in dependences.txt file
    with open("dependences.txt", "w") as output:
    #with open(export_dir + "\dependences.txt", "w") as output:
        for row in dep_list:
            output.write(str(row) + '\n')


if __name__ == '__main__':
    DIR = r'C:\Users\amondejar\Desktop\Mergulho\mergulho-ds\experimental'

    dep_list = read_dependences_list(DIR)

    save_dependences_list(dep_list, DIR)
