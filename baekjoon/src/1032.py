# num=3
# arr=['config.sys', 'config.inf', 'configures']
num = int(input())
first_word = list(input())

for i in range(num-1):
    other_word = list(input())
    for j in range(len(first_word)):
        if first_word[j] != other_word[j]:
            first_word[j] = '?'

print(''.join(first_word))

## 계속 input 받아서 비교하는 구문은 굳이 모든 값을 받아서 리스트로 저장하지 않고,
## for문 돌리면서 원하는 값을 찾아가면 시간 단축 + 불필요한 변수 만들지 않아도 됨. + 모든 글자 길이가 같으므로 first_word에 저장해나간 것.