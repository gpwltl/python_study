print(30%26)
print(chr(ord('E')))
print(ord('E'))

##1. rstrip() : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.('\n' 을 떼고 리스트 저장 가능)
for _ in range(2):
    arr = list(input().rstrip())
    print(arr)

##1-1. strip(): 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
##1-2. lstrip(): 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.

##2. 소문자 리스트 [string.ascii_lowercase]
import string
alpha_small = list(string.ascii_lowercase)
print(alpha_small)  #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alpha_small.index('a'))   #0
print(alpha_small.index('z'))   #25
print(alpha_small[24])  #y

##2-1. 동일한 방식의 대문자 리스트
alpha_bi = list(string.ascii_uppercase)
print(alpha_bi[4]) #E
print(alpha_bi.index('H'))  #7
print(alpha_bi[-19%26])

##3. ord('E'): 아스키 코드 번호 조회
print(ord('F')) #70
##3-1. chr(70) : 아스키코드 숫자의 문자열
print(chr(70))  #F