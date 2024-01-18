print("hello")
print("hi")
print("안녕하세요")

print(type("hi"), type(123))

print("hi\nhello")
print("안녕\t하세요")

print("""이렇게도 출력이
가능하지~""")

print("안녕하세요"[0:2])    # 안녕 -> '마지막 숫자를 포함하지 않음'

# 연산자 
print("3/2=", 3/2)
print("3//2=", 3//2)

# 입력 <error 유의>
inp = input("입력 >> ")
# print(inp + 300)
print(int(inp)+300)