# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

import string
def solution(new_id):
    test = list(string.ascii_lowercase + string.digits + "-_.")
    id = []
    id2 = []
    id3 = []
    #1
    for i in range(len(new_id)):
        id.append(new_id[i].lower())
    #2
    for i in range(len(id)):
        if id[i] in test:
        	id2.append(id[i])
    #3
    for i in range(len(id2)):
        #if i == 0:
        #    id3.append(id2[i])
        if not("." == id2[i] and id2[i-1] == ".") :#and id2[-1] != ".":
            id3.append(id2[i])    
    #4, 5
    if "." in id3 :
        if id3[0] == '.':
            del id3[0]
        elif id3[-1] == ".":
        	del id3[-1]
    if not id3:
        id3.append("a")
    #6
    if len(id3) >= 16:
        del id3[15:]
    if "." in id3 :
        if id3[0] == '.':
            del id3[0]
        elif id3[-1] == ".":
        	del id3[-1]
    #7
    if len(id3) < 3:
        while len(id3) < 3:
        	id3.append(id3[-1])

    return "".join(id3)