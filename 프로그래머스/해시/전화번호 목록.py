def solution(phone_book):
    answer = True
    hash = {}
    for phone_number in phone_book:
        hash[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_book:
            temp += number
            if temp in hash and temp != phone_number:
                answer = False

    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution([["123","456","789"]]))
print(solution(["12","123","1235","567","88"]))