def solution(tickets):
    tickets.sort(key = lambda x: x[1], reverse = True)

    used_tickets = []
    stack = []

    stack.append([['', 'ICN'], 0])
    while stack and len(used_tickets) - 1 < len(tickets):
        ticket, idx = stack.pop()
        if ticket not in used_tickets:
            used_tickets = used_tickets[:idx]
            used_tickets.append(ticket)
            for t in tickets:
                if t[0] == ticket[1]:
                    stack.append([t, idx + 1])

    return [t[1] for t in used_tickets]

"""
def dfs(port, tickets, route, list_result):
    route = '{0} {1}'.format(route, port)

    if len(tickets) == 0:
        list_result.append(route)
        return

    for t in tickets:
        if t[0] == port:
            c_tickets = tickets.copy()
            c_tickets.remove(t)
            dfs(t[1], c_tickets, route, list_result)


def solution(tickets):
    list_result = []

    for t in tickets:
        c_tickets = tickets.copy()
        c_tickets.remove(t)
        dfs(t[1], c_tickets, t[0], list_result)

    list_result.sort()

    return list_result[0].split(' ')
"""

print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))
print(solution([['ICN', 'COO'], ['ICN', 'BOO'], ['COO', 'ICN']]))
