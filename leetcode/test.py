class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:    	# 오름차순 정렬해서 간격을 확인하기 편하게 만든다.        
        intervals.sort(key = lambda x: x[0])        
        merged = []        
        for start, end in intervals:        	# 리스트에 값이 없으면 넣기.            
            if not merged:               
                merged.append([start, end])            # 리스트 마지막 끝값과 들어올 값의 시작점 비교해서 겹치지 않는 간격이면 리스트에 추가            
            elif merged[-1][1] < start:                
                merged.append([start, end])            # 겹치는 간격이면, 끝점끼리 비교해서 값 갱신            
                
            else:               
                merged[-1][1] = max(merged[-1][1], end)        
                return merged
