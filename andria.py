with open("output.txt", "w", encoding="utf-8") as out:
    jami=0
    for i in range(500, 1001):
        out.write(str(i)+"\n")
        jami+=i
    out.write(str(jami))