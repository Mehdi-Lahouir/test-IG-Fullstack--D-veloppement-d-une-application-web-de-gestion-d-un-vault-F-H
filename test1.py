true_inc = 0
true_dec = 0
incorrect = 0

f = open("test.txt", "r")
for line in f:
    line = line.strip()
    if line == "":
        incorrect += 1
        print("INCORRECT")
        continue

    parts = line.split()
    row = []
    i = 0
    while i < len(parts):
        row.append(int(parts[i]))
        i += 1

    if len(row) < 2:
        incorrect += 1
        print("INCORRECT")
        continue

    status = "UNKNOWN"
    bad = False

    j = 1
    while j < len(row):
        diff = row[j] - row[j - 1]

        if diff == 0:
            bad = True
            break

        if status == "UNKNOWN":
            if 1 <= diff <= 3:
                status = "INC"
            elif -3 <= diff <= -1:
                status = "DEC"
            else:
                bad = True
                break
        elif status == "INC":
            if not (1 <= diff <= 3):
                bad = True
                break
        else:
            if not (-3 <= diff <= -1):
                bad = True
                break

        j += 1

    if bad or status == "UNKNOWN":
        incorrect += 1
    elif status == "INC":
        true_inc += 1
    else:
        true_dec += 1

f.close()

print("TRUE INCREASING:", true_inc)
print("TRUE DECREASING:", true_dec)
print("INCORRECT:", incorrect)
print("TOTAL:", true_inc + true_dec)
