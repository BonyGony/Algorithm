

def solution(s):
    compression = []

    for length in range(1, len(s)+1):
        startIdx = 0
        newS = ''
        cnt = 1
        while startIdx < len(s):
            # print('length : ', length)
            # print('before : ', startIdx, startIdx +
            #       length, s[startIdx: startIdx+length])
            # print('after : ', startIdx+length, startIdx+2 *
            #       length, s[startIdx+length: startIdx+2*length])
            if s[startIdx: startIdx+length] == s[startIdx+length: startIdx+2*length]:
                cnt += 1
            else:
                if cnt == 1:
                    newS += s[startIdx: startIdx+length]
                else:
                    newS += str(cnt) + s[startIdx: startIdx+length]
                    cnt = 1
            startIdx = startIdx+length

        compression.append(len(newS))

    compression.sort()
    # print(sArr)

    return compression[0]

# def solution(s):
#     answer = 0
#     length = 1
#     startIdx = 0
#     newS_arr = []
#     newS = ''
#     cnt = 1

#     while startIdx < len(s):
#         print('length : ', length)
#         print('before : ', startIdx, startIdx +
#               length, s[startIdx: startIdx+length])
#         print('after : ', startIdx+length, startIdx+2 *
#               length, s[startIdx+length: startIdx+2*length])
#         if s[startIdx: startIdx+length] == s[startIdx+length: startIdx+2*length]:
#             cnt += 1
#             print(s[startIdx: length], s[startIdx+length:2*length])
#         else:
#             if cnt == 1:
#                 newS += s[startIdx: startIdx+length]
#             else:
#                 newS += str(cnt) + s[startIdx: startIdx+length]
#                 cnt = 1

#         startIdx = startIdx+length

#     print('new_S : ', newS)
#     return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
