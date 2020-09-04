import os 


if __name__ == "__main__":
    data = open('basics//file_data.txt')
    print(data.read())
    print(data.tell()) # tells about the pointer position

    print(data.seek(0))  # set the pointer position
    data.close()

    os.rename('basics//file_data.txt', 'basics//data.txt')

