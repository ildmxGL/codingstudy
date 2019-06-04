def solution(priorities, location):
    num_print_out = 0
    while len(priorities):
        if priorities[0] == max(priorities):
            del priorities[0]
            num_print_out += 1
            if location:
                location -= 1
            else:
                return num_print_out
        else:
            priorities.append(priorities[0])
            del priorities[0]
            location = location - 1 if location else len(priorities) - 1

    return -1

