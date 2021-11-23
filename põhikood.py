def paranda_komavead(lause):
    lause = lause.lower()
    lause = lause.replace(" sest", ", sest")
    lause = lause.replace(" aga", ", aga")
    lause = lause.replace(" kuid", ", kuid")
    lause = lause.replace(" mille", ", mille")
    lause = lause.replace(" kuna", ", kuna")
    return lause

fail = open("vigane.txt", encoding = "UTF-8")

õige = open("parandatud.txt", "w", encoding = "UTF-8")

for rida in fail:
    õiged = paranda_komavead(rida)
    õige.write(õiged)

fail.close()

õige.close()