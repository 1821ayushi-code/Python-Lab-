'''
#1
n=input()
rev=''
for i in n:
    rev=i+rev
print(rev)


#2
n=input()
rev=''
count=0
for i in  n:
    rev=i+rev
for j in rev:
    if j!=' ':
        count+=1
    elif j==' ':
        break
print(count)


#3 inbuilt
sentence=input()
word=input()
if word in sentence:
    print('Yes')
else:
    print('No')
print(sentence.count(word))

#3 non-inbuilt
sentence=input()+' '
word=input()
wnew=''
count=0
for i in sentence:
    if i!=' ':
        wnew+=i
    else:
        if wnew==word:
            count+=1
            wnew=''
if count>0:
    print('Yes')
    print(count)
else:
    print('No')


#4
n=input().lower()
main='abcdefghijklmnopqrstuvwxyz'
mnew=''
for i in n:
    if i in main and i not in mnew:
        mnew+=i
if len(mnew)==len(main):
    print('Pangram')
else:
    print('Not a Pangram')


#5
text = input("Enter string: ")
shift = int(input("Enter shift: "))
result = ""
for ch in text:
    if ch >= 'a' and ch <= 'z':
        result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    elif ch >= 'A' and ch <= 'Z':
        result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
print("Cipher text:", result)


#6:
counts = [0, 0, 0, 0, 0]          # groups: 1-2, 3-4, 5-6, 7-8, 9-10
total = 0
while True:
    n = int(input("Enter number (1-10, -1 to stop): "))
    if n == -1:
        break
    if n >= 1 and n <= 10:
        counts[(n - 1) // 2] += 1
        total += 1
        else:
        print("Out of range, ignored")
if total == 0:
    print("No valid input")
    return
labels = ["1 - 2", "3 - 4", "5 - 6", "7 - 8", "9 - 10"]
for i in range(5):
    percent = counts[i] * 100 / total
    hashes = "# " * int(percent / 5 + 0.5)
    print(labels[i] + ":", hashes + format(percent, ".2f") + " %")


#7:
    s = input("Enter string: ")
    n = len(s)
    is_pal = True
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            is_pal = False
            break
    if is_pal:
        print("Palindrome")
    else:
        print("Not a palindrome")


#8:
    nums = read_list()

    total = 0
    for x in nums:
        total += x
    print("Sum =", total)

    prod = 1
    for x in nums:
        prod *= x
    print("Product =", prod)

    smallest = nums[0]
    for x in nums:
        if x < smallest:
            smallest = x
    print("Smallest =", smallest)


#9:
    nums = read_list()
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print("Descending:", nums)


#10:
    words = input("Enter words separated by hyphen: ").split("-")
    n = len(words)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]
    print("-".join(words))

#11:
    para = input("Enter paragraph: ")
    digits = alpha = upper = lower = special = 0
    for ch in para:
        if ch.isdigit():
            digits += 1
        elif ch.isalpha():
            alpha += 1
            if ch.isupper():
                upper += 1
            else:
                lower += 1
        elif ch != " ":
            special += 1
    print("Digits:", digits)
    print("Alphabets:", alpha)
    print("Uppercase:", upper)
    print("Lowercase:", lower)
    print("Special characters:", special)


#12:
    s = input("Enter sentence: ")
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    print("After removing duplicates:", result)
'''































