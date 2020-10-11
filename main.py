choseong = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jungseong = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongseong = ['', 'ㄱ', 'ㄲ', ('ㄱ','ㅅ'), 'ㄴ', ('ㄴ','ㅈ'), ('ㄴ','ㅎ'), 'ㄷ', 'ㄹ', ('ㄹ','ㄱ'), ('ㄹ','ㅁ'), ('ㄹ','ㅂ'), ('ㄹ','ㅅ'), ('ㄹ','ㅌ'), ('ㄹ','ㅍ'), ('ㄹ','ㅎ'), 'ㅁ', 'ㅂ', ('ㅂ','ㅅ'), 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

eng = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
kor = ['ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ', 'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', 'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ', 'ㅃ', 'ㅉ', 'ㄸ', 'ㄲ', 'ㅆ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅒ', 'ㅖ', 'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', 'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ']


def cho(char):
    global choseong
    return list(choseong[(char-44032) // 588])

def jung(char):
    global jungseong
    return list(jungseong[((char-44032) % 588) // 28])

def jong(char):
    global jungseong
    return list(jongseong[((char-44032) % 588) % 28])

def hangulSplit(a):
    if ord(a) >= ord('가') and ord(a) <= ord('힣'):
        return cho(ord(a))+jung(ord(a))+jong(ord(a))
    elif ord(a) >= ord('ㄱ') and ord(a) <= ord('ㅣ'):
        return list(a)

# def hangulJoin(a):
#     for i in len(a):
#         if i==0 and (ord(a[i]) >= ord('ㅏ') and ord(a[i]) <= ord('ㅣ')):

def kor2eng(string):
    result = list()
    for i in string:   
        result += hangulSplit(i)
    for j in result:
        print(eng[kor.index(j)], end = "")
    print()

toChange = input()
kor2eng(toChange)