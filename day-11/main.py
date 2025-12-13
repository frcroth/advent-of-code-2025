import os


def parse_graph(path):
    with open(path) as f:
        input = f.readlines()
    adj = dict()

    all_nodes = []
    for line in input:
        line = line.strip()
        name = line.split(": ")[0]
        all_nodes.append(name)
        connections = line.split(": ")[1].split(" ")
        adj[name] = connections

    if "out" not in all_nodes:
        all_nodes.append("out")
        adj["out"] = []

    return all_nodes, adj


def do_topo_sort(adj, all_nodes):
    def visit(n):
        if n not in unvisited:
            return
        if n in visited_tmp:
            print("CYCLE")
            return
        visited_tmp.add(n)
        for c in adj.get(n, []):
            visit(c)
        unvisited.remove(n)
        l.insert(0, n)

    l = []

    visited_tmp = set()
    unvisited = set(all_nodes)

    while len(unvisited) > 0:
        n = next(iter(unvisited))
        visit(n)

    return l


def part_1(parsed):
    all_nodes, adj = parsed

    ordered = do_topo_sort(adj, all_nodes)

    path_count = dict()
    path_count["you"] = 1

    for n in ordered:
        current_path_count = path_count.get(n, 0)
        for c in adj.get(n, []):
            path_count[c] = path_count.get(c, 0) + current_path_count

    return path_count["out"]


def part_2(parsed):
    all_nodes, adj = parsed

    ordered = do_topo_sort(adj, all_nodes)

    def count_paths(start):
        paths = {node: 0 for node in all_nodes}
        paths[start] = 1
        for node in ordered:
            for connection in adj[node]:
                paths[connection] += paths[node]
        return paths

    path_count = {node: 0 for node in all_nodes}
    path_count["out"] = 1

    for node in reversed(ordered):
        for connection in adj[node]:
            path_count[node] += path_count[connection]

    from_svr = count_paths("svr")
    from_dac = count_paths("dac")
    from_fft = count_paths("fft")

    via_dac_and_fft = from_svr["dac"] * from_dac["fft"] * path_count["fft"]
    via_fft_and_dac = from_svr["fft"] * from_fft["dac"] * path_count["dac"]

    return via_dac_and_fft + via_fft_and_dac


if __name__ == "__main__":
    example_input = parse_graph("example.txt")
    assert 5 == part_1(example_input)

    example_2_input = parse_graph("example_2.txt")
    assert 2 == part_2(example_2_input)

    if not os.getenv("SKIP_INPUT"):
        input = parse_graph("input.txt")
        print(part_1(input))
        print(part_2(input))
