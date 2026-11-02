def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    size = len(s1)
    s1_count = {}
    window_count = {}

    for i in range(size):
        s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
        window_count[s2[i]] = window_count.get(s2[i], 0) + 1

    if s1_count == window_count:
        return True

    for i in range(size, len(s2)):
        new_char = s2[i]
        window_count[new_char] = window_count.get(new_char, 0) + 1

        old_char = s2[i - size]
        window_count[old_char] -= 1

        if window_count[old_char] == 0:
            del window_count[old_char]

        if s1_count == window_count:
            return True

    return False