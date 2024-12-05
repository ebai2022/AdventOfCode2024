from collections import defaultdict, deque


def part1(adj, pages):
    valid_pages = []
    invalid_pages = []
    for p in pages:
        seen = set()
        page_set = set(p)
        valid = True
        for page in p:
            # if it has parents that need to have been processed first, check
            if not check_validity(page, seen, adj, page_set):
                valid = False
                break
            seen.add(page)
        if valid:
            valid_pages.append(p)
        else:
            invalid_pages.append(p)
    # return middle numbers
    return valid_pages, invalid_pages


def part2(adj, reverse_adj, invalid_pages):
    valid_pages = []
    for pages in invalid_pages:
        new_page_order = []
        start_node = -1
        in_degrees = {}
        pages = set(pages)
        for page in pages:
            # find the in degree of the page. This is the number of nodes in its reverse_adj map that are also in the pages set
            in_degree = 0
            for parent in reverse_adj[page]:
                if parent in pages:
                    in_degree += 1
            in_degrees[page] = in_degree
            if in_degree == 0:
                start_node = page
        # perform topo sort
        q = deque([start_node])
        while q:
            curr = q.popleft()
            new_page_order.append(curr)
            for child in adj[curr]:
                if child in in_degrees:
                    in_degrees[child] -= 1
                    if in_degrees[child] == 0:
                        q.append(child)
        valid_pages.append(new_page_order)
    return valid_pages


def check_validity(page, seen, adj, page_set):
    prior_nodes = adj[page]
    for node in prior_nodes:
        if node not in seen and node in page_set:
            return False
    return True


def calculate_ans(pages):
    ans = 0
    for page in pages:
        ans += page[len(page) // 2]
    return ans


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    reverse_adj = defaultdict(set)  # tracks child -> parent
    adj = defaultdict(set)  # tracks parent -> child
    pages = []
    for line in data:
        if "|" in line:
            # process the rule
            parent, child = line.split("|")
            reverse_adj[int(child)].add(int(parent))
            adj[int(parent)].add(int(child))
        elif "," in line:
            # process the orders
            curr = line.split(",")
            int_line = [int(i) for i in curr]
            pages.append(int_line)
    valid_pages, invalid_pages = part1(reverse_adj, pages)
    ans = calculate_ans(valid_pages)
    print(f"part 1 answer: {ans}")
    new_valid_pages = part2(adj, reverse_adj, invalid_pages)
    ans = calculate_ans(new_valid_pages)
    print(f"part 2 answer: {ans}")
