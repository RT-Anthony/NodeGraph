def contains_cycle(node):
    visited_ids = []
    nodes_to_visit = [node]
    for node in nodes_to_visit:
        if node.id in visited_ids:
            return node.id
        else:
            for input in node.inputs:
                pass

    return None
