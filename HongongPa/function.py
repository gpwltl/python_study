# 함수 
## 1. format() 

output_a = "{:d}".format(52)
output_b = "{:10d}".format(52)  # 앞에 공백 10칸 (특정 칸 출력)
output_c = "{:05d}".format(52)  # 빈칸 0으로 채우기
print(output_a)
print(output_b)
print(output_c)

output_d = "{:+d}".format(52)
output_e = "{:+d}".format(-52)  # 기호 부분 붙여줌
output_f = "{: d}".format(52)
output_g = "{: d}".format(-52)  # 기호 부분 공백 
print(output_d)
print(output_e)
print(output_f)
print(output_g)

output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)     # 공백 5칸 먼저, 기호 붙여줌  
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)    # 기호가 먼저, 공백 5칸 
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)    # 기호가 먼저, 0으로 5칸 채우기 
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

# 소수점 제거 
output_a1 = "{:f}".format(83.234)
output_b1 = "{:15f}".format(83.234)
output_c1 = "{:+f}".format(83.234)
output_d1 = "{:g}".format(83.23400)     # 의미없는 0 제거 (소수점을 제거하는 건 X)
print(output_a1)
print(output_b1)
print(output_c1)
print(output_d1)    

# 함축형 
print("{}".format(10))
print(f'{10}')

# 2. 공백 제거 
print("         안녕하세요.".strip())   # lstrip, rstrip

# 3. 문자열 구성 파악 
print("TrainA에이10".isalnum())     # isalpha, isdigit 등 

# 4. 문자열 있는지 체크 
print("안녕" in "안녕하셍")

# 5. 문자열 자르기 
print("10 20 30 40 50".split(" "))

