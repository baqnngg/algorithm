# heapq 모듈 가져오기
import heapq
# 큐로 사용할 리스트 선언하기
heap = [] 
# 우선순위 큐에 data 삽입하기
heapq.heappush(heap, (-5,'L'))
heapq.heappush(heap, (3,'C'))
heapq.heappush(heap, (4,'D'))
heapq.heappush(heap, (1,'A'))
heapq.heappush(heap, (2,'B'))

#최대로 할려면 저 1,2,3,4를 -로 바꿔서 넣으면 됨

# 우선순위 큐에서 data 꺼내기
for i in range(5):
 result = heapq.heappop(heap)
 print(result[1], end=' ')