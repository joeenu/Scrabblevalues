def calcScore(line):
    """
    calcScore Calculate the scrabble score of the word in the line

    :param line: the line/word to calculate the score from
    :type line: str
    :return: The scrabble score of the word
    :rtype: int
    """
    a = line.count("a")
    b = line.count("b")
    c = line.count("c")
    d = line.count("d")
    e = line.count("e")
    f = line.count("f")
    g = line.count("g")
    h = line.count("h")
    i = line.count("i")
    j = line.count("j")
    k = line.count("k")
    l = line.count("l")
    m = line.count("m")
    n = line.count("n")
    o = line.count("o")
    p = line.count("p")
    q = line.count("q")
    r = line.count("r")
    s = line.count("s")
    t = line.count("t")
    u = line.count("u")
    v = line.count("v")
    w = line.count("w")
    x = line.count("x")
    y = line.count("y")
    z = line.count("z")
    ä = line.count("ä")
    ö = line.count("ö")
    ü = line.count("ü")
    return (e+ n+ s+ i+ r+ t+ u+ a+ d) + (h+ g+ l+ o)*2 + (m+ b+ w+ z)*3 + (c+ f+ k+ p)*4 + (ä+ j+ ü+ v)*6 + (ö+ x)*8 + (q+ x)*10


def calcScoreInRange(arr, pack, data):
    values = []
    for i in pack:
        try:
            l = i.lower()
            l = l.replace("\n", "")
            values.append(l + " " + str(calcScore(l)))
        except Exception:
            import threading
            print("Error in: " + threading.current_thread().getName(), i)
            return

    # Couldn't concatinate lists with + because of passing the value through reference
    for i in values:
        data.append(i)
    

# Array spliting code from: https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
# Author: tixxit
def splitList(arr, n):
    k, m = divmod(len(arr), n)
    return [arr[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]
        