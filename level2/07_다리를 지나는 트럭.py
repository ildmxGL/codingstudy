def solution(bridge_length, weight, truck_weights):
    time = 0
    new = 0
    end = 0
    cross_length = [0 for i in range(len(truck_weights))]
    while end < len(truck_weights):
        time+=1
        if cross_length[end] == bridge_length:
            weight+=truck_weights[end]
            end+=1
        if new < len(truck_weights) and weight>=truck_weights[new]:
            weight-=truck_weights[new]
            new+=1
        for i in range(end, new):
            cross_length[i]+=1
    return time