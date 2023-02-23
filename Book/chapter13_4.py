def balanceCheck(s):
    left = 0
    right = 0

    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        elif s[i] == ')':
            right += 1

    if left != 0 and right != 0 and left == right:
        return True
    else:
        return False


def rightCheck(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif len(stack) != 0 and s[i] == ')':
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


def makeUV(p):
    u = ''
    v = ''

    for i in range(len(p)+1):
        if (balanceCheck(p[:i]) and balanceCheck(p[i:])) or (balanceCheck(p[:i]) and p[i:] == ''):
            u = p[:i]
            v = p[i:]
            break

    return u, v


def changeBracket(s):
    st = ''

    for i in range(len(s)):
        if s[i] == '(':
            st += ')'
        elif s[i] == ')':
            st += '('

    return st


def makeRightS(p):
    if p == '':
        return ''

    u, v = makeUV(p)

    if rightCheck(u):
        return u+makeRightS(v)
    else:
        return '(' + makeRightS(v) + ')' + changeBracket(u[1:len(u)-1])


def solution(p):
    answer = ''

    answer = makeRightS(p)

    return answer


# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))
