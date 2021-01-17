cmd = input()
if cmd == '고무오리 디버깅 시작':
    stack = []
    cmd = input()
    while cmd != '고무오리 디버깅 끝':
        if cmd == '고무오리':
            if stack:
                stack.pop()
            else:
                stack.extend(['문제', '문제'])
        else:
            stack.append(cmd)
        cmd = input()

    print('힝구') if stack else print('고무오리야 사랑해')
