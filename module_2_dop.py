for n in range(3, 21):
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if i + j == n:
                pairs.append(str(i) + str(j))
    password = ''.join(pairs)
    print(f"{n} - {password}")