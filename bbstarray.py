def GenerateBBSTArray(source):
    if len(source) < 2:
        return source
    sorted_src = sorted(source)
    middle = len(sorted_src) // 2
    depth = 0
    cutoff = 2 ** depth
    levels = [(cutoff, middle)]
    while middle > 0:
        middle //= 2
        depth += 1
        cutoff += 2 ** depth
        levels.append((cutoff, middle))

    result = list(0 for x in range(len(sorted_src)))
    current_depth = 0

    for dst_index, prev_src_index in enumerate(result):
        if dst_index == levels[current_depth][0]:
            current_depth += 1
        src_index = prev_src_index + levels[current_depth][1]
        is_not_last_depth = current_depth < len(levels) - 1
        if is_not_last_depth:
            result[dst_index * 2 + 1] += prev_src_index
            result[dst_index * 2 + 2] += src_index + 1
        result[dst_index] = sorted_src[src_index]

    return tuple(result)
