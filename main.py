import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':

    print('hello Sumana')
    # Opening JSON file
    f = open('./resource/swagger.json')

    # Loading json content
    data = json.load(f)

    # Iterating API under paths
    for i in data['paths']:
        print(i)

    # Closing file
    f.close()

##Adding this line just for tag release1.2

