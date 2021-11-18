# funktsioonide definitsioonid
def paranda_komavead(lause):
    # asendustehete tegemine
    lause = lause.lower()
    lause = lause.replace(" sest", ", sest")
    lause = lause.replace(" aga", ", aga")
    lause = lause.replace(" kuid", ", kuid")
    lause = lause.replace(" mis", ", mis")
    print(lause)
    
# põhiprogrammi algus
paranda_komavead()