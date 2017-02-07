import sys

def generate_paths(a, b, roadmap):
    paths = []
    
    for node in roadmap[a]:
        find_path(node, b, roadmap, [], paths)

    return paths
    


def find_path(curr_node, b, roadmap, visited, paths):    
    if curr_node == b:
        paths.append(visited)
        return

    if roadmap[curr_node] == None:
        return
    
    for node in roadmap[curr_node]:
        if node not in visited:
            visited.append(node)
            find_path(node, b, roadmap, visited, paths)
    
    
def find_cuts(paths):
    



num_towns, num_roads = sys.stdin.readline().split(' ')
s, t = sys.stdin.readline().split(' ')

roadmap = {}
roadcon = {}
roadweights = {}

count = 1

for line in sys.stdin:
    a, b, cost = line.split(' ')
    roadweights[count] = cost    
    
    if a in roadmap:
        roadmap[a].append(b)
    else:
        roadmap[a] = [b]

    if b in roadmap:
        roadmap[b].append(a)
    else:
        roadmap[b] = [a]

    if sorted((a,b)) in roadcon:
        roadcon.append(count)
    else:
        roadcon = [count]

    roadweights[m] = cost

paths = generate_paths(s, t, roadmap)
possible_cuts = find_cuts(paths)
optimal_cuts = find_opt(possible_cuts, roadweights)

