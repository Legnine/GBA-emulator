myfile = open("file\\filenames.txt", "r")
myline = myfile.readline()
gameType = "gba-alt"
while myline:
    print(myline)
    myline = myfile.readline()
    myline1 = myline.replace("\n", "',")
    with open("Cat\gen.txt", "a") as f:
        f.write(f"'../gba-host/{gameType}/{myline1}\n")