#lv2 전화번호부

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print("true ",p1, p2)
        if p2.startswith(p1):
            print("false ", p1, p2)
            return False

    return True

#phoneBook = {"119", "97674223", "11959524421"}
#phoneBook = {"123","456","789"}

phoneBook = {"12","123","1235","567","88"}
print(solution(phoneBook))