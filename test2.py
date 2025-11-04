def is_safe(row):
    if len(row) < 2:
        return False

    status = "UNKNOWN"
    j = 1
    while j < len(row):
        diff = row[j] - row[j - 1]

        if diff == 0:
            return False

        if status == "UNKNOWN":
            if 1 <= diff <= 3:
                status = "INC"
            elif -3 <= diff <= -1:
                status = "DEC"
            else:
                return False
        elif status == "INC":
            if not (1 <= diff <= 3):
                return False
        else:  # DEC
            if not (-3 <= diff <= -1):
                return False
        j += 1

    return True


true_safe = 0
f = open("test.txt", "r")

for line in f:
    parts = line.strip().split()
    if not parts:
        continue
    row = [int(x) for x in parts]

    if is_safe(row):
        true_safe += 1
    else:
        fixed = False
        for i in range(len(row)):
            new_row = row[:i] + row[i+1:]
            if is_safe(new_row):
                true_safe += 1
                fixed = True
                break
        if not fixed:
            pass

f.close()

print("TOTAL SAFE:", true_safe)
