'''
#1:
    s = input()
    vowels = consonants = digits = spaces = others = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
        else:
            others += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Others:", others)


#2:
    s = input()
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()
    print(result)


#3:
    pw = input()
    if len(pw) < 8:
        print("WEAK")
        return

    has_upper = has_lower = has_digit = has_special = False
    for ch in pw:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch != " ":
            has_special = True

    kinds = has_upper + has_lower + has_digit + has_special
    if kinds == 4:
        print("STRONG")
    elif kinds >= 2:
        print("MODERATE")
    else:
        print("WEAK")


#4:
    s = input()
    c = input()
    count = 0
    positions = ""
    for i in range(len(s)):
        if s[i] == c:
            count += 1
            positions += str(i) + " "
    print("Count:", count)
    if count == 0:
        print("Positions: -1")
    else:
        print("Positions:", positions)


#5:
    words = input().split()
    for w in words:
        print(len(w), end=" ")
    print()


#6:
    p = input()
    ok = True
    if len(p) != 10:
        ok = False
    else:
        if p[0:2] != "RJ":
            ok = False
        for i in range(10):
            if i < 2 or (i >= 4 and i < 6):
                if not (p[i] >= 'A' and p[i] <= 'Z'):
                    ok = False
            else:
                if not p[i].isdigit():
                    ok = False
    print(ok)


#7:
    s = input()
    n = len(s)
    changes = 0
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            changes += 1
    print("Changes needed:", changes)


#8:
    s = input()
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    print(result)


#9:
    msg = input()
    k = int(input())
    result = ""
    for ch in msg:
        if ch == " ":
            result += ch
        else:
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    print(result)


#10:
    s = input()
    best_char = s[0]
    best_len = 1
    cur_len = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_len += 1
        else:
            cur_len = 1
        if cur_len > best_len:
            best_len = cur_len
            best_char = s[i]
    print(best_char, best_len)

'''











