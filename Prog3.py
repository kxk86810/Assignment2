def inctocms():
    inc = [150, 155, 145, 148]
    cm = []
    for item in inc:
        cm.append(item * 2.54)

    print("List in Inches", inc)
    print("List in cm's", [item * 2.54 for item in inc])

inctocms()