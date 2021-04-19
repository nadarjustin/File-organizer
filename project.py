import os

i = 1
paths = "J:/iphone pics test"
for root, dirs, files in os.walk("J:/Iphone pics"):
    for loc in dirs:
        path = "J:/Iphone pics/" + str(loc)
        files1 = os.listdir(path)

        for index, file in enumerate(files1):
            os.rename(os.path.join(path, file), os.path.join(paths, ''.join([str(i), '.jpg'])))
            i += 1

print("Done")
