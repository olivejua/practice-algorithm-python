import collections

def get_letter(str: str) -> str:
    if len(str) == 1:
        return str

    p = collections.Counter(str)
    if p.most_common(2)[0][1] == p.most_common(2)[1][1]:
        return '?'
    else:
        return p.most_common(2)[0][0]

str = input().upper()
print(get_letter(str))