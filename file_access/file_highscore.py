#
#
#
#
import random

# Konfiguration
FILENAME = "highscore_test.txt"

def readHighscore():
    fh = open(FILENAME, "r")
    data = []
    for line in fh:
        line = line.rstrip("\n")
        tmp = line.split(",")
        d = {
            "name": tmp[0],
            "score": int(tmp[1]),
            "games": int(tmp[2])
        }
        data.append(d)
    fh.close()
    return data


def writeHighscore(data):
    content = ""
    for row in data:
        line = ",".join([
            row["name"],
            str(row["score"]),
            str(row["games"])
        ])
        content += line + "\n"

    # in Datei schreiben
    fh = open(FILENAME, "w")
    fh.write(content)
    fh.close()


def saveHighscore(username, score):
    data = readHighscore()

    # Daten manipulieren wenn eintrag vorhanden
    found = False
    for i in range(0, len(data)):
        if data[i]["name"] == username:
            data[i]["score"] += score
            data[i]["games"] += 1
            found = True

    # Falls noch nicht vorhanden -> anhängen
    if not found:
        row = {
            "name": username,
            "score": score,
            "games": 1
        }
        data.append(row)

    writeHighscore(data)


username = input("Bitte Name eingeben: ")
saveHighscore(username, 80)


"""
data = [
    {'name': 'Susi', 'score': 1000, 'games': 3},
    {'name': 'Moritz', 'score': 40, 'games': 2},
    {'name': 'Hans', 'score': 200, 'games': 10}
]
"""
#writeHighscore(data)

#test = readHighscore()
#print(test)





