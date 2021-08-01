from rich.progress import track


def getscore(ele):
    """
    getscore Gets the scrabble score of each line in the elements

    :param ele: The line
    :type ele: str
    :return: The score
    :rtype: int
    """
    return int(ele.split(" ")[-1])


# Remove words which are two words
with open("words.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    for line in track(lines):
        if "_" not in line:
            f.write(line)
    f.truncate()

# Calculate score for each word
with open("words.txt", "r+") as fi:
    lines = fi.readlines()
    fi.seek(0)
    for ii in track(range(len(lines))):
        data = lines[ii].lower()
#        print(repr(data))
        data = data.replace("\n","")
#        print(repr(data))
        a = data.count("a")
        b = data.count("b")
        c = data.count("c")
        d = data.count("d")
        e = data.count("e")
        f = data.count("f")
        g = data.count("g")
        h = data.count("h")
        i = data.count("i")
        j = data.count("j")
        k = data.count("k")
        l = data.count("l")
        m = data.count("m")
        n = data.count("n")
        o = data.count("o")
        p = data.count("p")
        q = data.count("q")
        r = data.count("r")
        s = data.count("s")
        t = data.count("t")
        u = data.count("u")
        v = data.count("v")
        w = data.count("w")
        x = data.count("x")
        y = data.count("y")
        z = data.count("z")
        ä = data.count("ä")
        ö = data.count("ö")
        ü = data.count("ü")
        value = (e+ n+ s+ i+ r+ t+ u+ a+ d) + (h+ g+ l+ o)*2 + (m+ b+ w+ z)*3 + (c+ f+ k+ p)*4 + (ä+ j+ ü+ v)*6 + (ö+ x)*8 + (q+ x)*10
        fi.write(data + " " + str(value) + "\n")
    fi.truncate()

# Sort the file
with open("words.txt", "r+") as fi:
    lines = fi.readlines()
    fi.seek(0)
    lines.sort(key = getscore,reverse =True)
    fi.writelines(lines)