import os


def CreateRequirementsList(directoryPath: str):
    '''
    Makes a list of requirements libraries given a Python project path

            Parameters:
                    directoryPath (str): A string path

            Returns:
                    content (list): A list with all requirements libraries
    '''
    # list to save all dependencies from all files
    content = []

    for r, d, f in os.walk(directoryPath):
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


def SaveRequirementsList(requirementsList: list, exportList: str):
    '''
    Saves the list of requirements.txt to a specified path.

            Parameters:
                    requirementsList (list): A string list
                    exportList (str): A string path

            Returns:
                    Saves the requirements.txt file 
    '''
    # saving in requirements.txt file
    with open(exportList + "\\requirements.txt", "w") as output:
        for row in requirementsList:
            output.write(str(row) + '\n')


if __name__ == '__main__':
    DIR = r'C:\Users\abelg\GoDev\My Drive\Github'
    EXPORT_DIR = r'C:\Users\abelg\GoDev\My Drive\Github\UnifyRequirements'

    requirementsList = CreateRequirementsList(DIR)
    SaveRequirementsList(requirementsList, EXPORT_DIR)
