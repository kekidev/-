
 # 최빈값
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
# 중앙값
def center(List):
    if len(List) % 2 == 0: # 변량의 갯수가 홀수일 때
        index = (len(List) - 1) / 2
        return List[int(index)]
    else: # 변량의 갯수가 짝수일때
        return List[int(len(List) / 2)]

# 평균
def average(List):
    res = 0
    for i in List:
        res += i 

    return res / len(List)


li = [2,4,6,8,10,12, 14]
print(average(li))
