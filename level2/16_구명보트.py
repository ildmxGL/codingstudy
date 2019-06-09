from collections import deque

def solution(people, limit):
    answer = len(people)
    people_min = min(people)
    people = [x for x in people if x + people_min <= limit]
    
    people = deque(sorted(people, reverse = True))
    while people:
        x = people.pop()
        for i in range(len(people)):
            if x + people[i] <= limit:
                [people.popleft() for _ in range(i + 1)]
                answer -= 1
                break
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([40, 50, 60, 70, 80, 90, 100], 120))
print(solution([40, 70, 90, 110, 150], 160))
print(solution([40, 40, 40, 110, 80, 120], 120))
print(solution([40, 50, 40, 40, 50, 60], 100))
print(solution([40, 40, 40, 40, 40], 70))
print(solution([40, 40, 40, 40, 40], 80))
