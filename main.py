class Statics:
    def __init__(self, li: list):
        self.List = li 
    
    # 최빈값
    def most_frequent(self):
        counter = 0
        num = self.List[0]
        
        for i in self.List:
            curr_frequency = self.List.count(i)
            if(curr_frequency > counter):
                counter = curr_frequency
                num = i
    
        print("최빈값: " + num)
    
    # 중앙값
    def center(self):
        if len(self.List) % 2 == 0: # 변량의 갯수가 홀수일 때
            index = (len(self.List) - 1) / 2
            print("중앙값: " + self.List[int(index)])
        else: # 변량의 갯수가 짝수일때
            print("중앙값: " + self.List[int(len(self.List) / 2)])

    # 평균
    def average(self):
        res = 0
        for i in self.List:
            res += i 

        print("평균: " + res / len(self.List))

# 사용법 예시
Statics([12,21,3,123,12,3,312,3,123]).center()
