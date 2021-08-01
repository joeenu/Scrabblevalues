from rich.progress import track
import threading as t

from lib import calcScoreInRange

THREADS = 10


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
    
    packages = [i*len(lines)/THREADS for i in range(THREADS)]
    data = []
    threads = []
    calcScoreInRange(lines, 0, len(lines), data)
    """ for i in track(range(THREADS), description="Starting Threads"):
        threads.append(t.Thread(target=calcScoreInRange, args=(lines, int(packages[i]), int(packages[i]+len(lines)), data)))
        threads[i].start()
    for i in track(threads, description="Waiting for Threads"):
        i.join() """
    # Ensuring the same output as the other version
    data = "\n".join(data)
    data = data[-1].replace("\n", "")
    
    # Writing
    fi.writelines(data)
    fi.truncate()

# Sort the file
with open("words.txt", "r+") as fi:
    lines = fi.readlines()
    fi.seek(0)
    lines.sort(key = getscore,reverse =True)
    fi.writelines(lines)