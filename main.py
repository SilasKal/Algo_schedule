n = int(input())
if n == 0:
    print("0")
else:
    S = []
    F = []
    for i in range(n):
        s, f = map(int, input().split())  # liest die zweite Zeile
        S.append(s)
        F.append(f)
    index_S_F = [*range(n)]
    index_S_F.sort(key=lambda i: F[i]) # Index nach F sortieren
    counter = 1
    endzeit = F[index_S_F[0]]
    for i in index_S_F[1:]:
        if endzeit <= S[i]:
            endzeit = F[i]
            counter +=1
    print(counter)
