def solution(places):
    answer = []

    for place in places:
        # 이제 시작
        row_answer = 1

        length = len(place)
        Ps = []
        Os = []
        for x in range(length):
            for y in range(length):
                if 'P' == place[x][y]:
                    Ps.append((x, y))
                elif 'O' == place[x][y]:
                    Os.append((x, y))

        for x, y in Ps:
            # 상하좌우
            if (x-1, y) in Ps or \
                (x, y+1) in Ps or \
                (x+1,y) in Ps or \
                (x, y-1) in Ps:
                row_answer = 0
                break
        for x, y in Os:
            cnt = 0
            if (x-1, y) in Ps: cnt+=1
            if (x, y+1) in Ps: cnt+=1
            if (x+1, y) in Ps: cnt+=1
            if (x, y-1) in Ps: cnt+=1

            if 2 <= cnt:
                row_answer = 0
                break

        answer.append(row_answer)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))