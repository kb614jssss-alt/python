#1~100 까지 의 합계
tot=0 
for j in range(1, 101):
    tot +=j #tot=toto+j (j를 누적해서 tot)

print(tot)

#2~100 짝수 합계
tot=0 
for j in range(2, 101 , 2):
    tot +=j

print(tot)

#1~99 홀수 합계
tot=0 
for j in range(1, 100 , 2):
    tot +=j

print(tot)