import sys
from collections import deque

# Cycle detection on a Graph representation of the problem
# Overall Runtime = 0(V * (V+E)), where V is the number of unique locks
# and E is the number of threads


# Graph of lock dependencies in form {Lock : Path: Set of Lock Deps}
# so {Lock1: Path2: (Lock3, Lock2)}
# implies that Lock1 can be dependent on Lock3 or lock2 when 
# path2 is executing
def create_graph(paths):
    dependent_on = {}
    locks = set()
    
    for path in paths:
        name, path = path.split(" ")
        path = path.split(",")
        for i in range(len(path) - 1):
            if path[i] != path[i+1]:
                locks.add((name, path[i], path[i+1]))
               
    for lock_tuple in locks:
        path, lock1, lock2 = lock_tuple[0], lock_tuple[1], lock_tuple[2]
        if lock1 not in dependent_on:
            dependent_on[lock1] = {}
        if path not in dependent_on[lock1]:
            dependent_on[lock1][path] = set()
        dependent_on[lock1][path].add(lock2)
        
    return dependent_on


# If you can find a cycle, starting from a lock 
# it means that there exists a lock A s.t the start 
# lock is depending on A, and A is depending on the start
# (i.e) a deadlock. We can use BFS to find the cycles for each lock
# if it exists
def bfs(start, graph):
    all_paths = set(graph[start].keys())
    cycles = set()
    
    for path in all_paths:
        queue = deque([(set(), start)])
        while len(queue) > 0:
            curr_node = queue.popleft()
            if curr_node[1] not in graph:
                continue
                
            next_paths = set(graph[curr_node[1]].keys()) - curr_node[0]
            if len(next_paths) < 0:
                continue
                
            for p in next_paths:
                new_used_paths = set(curr_node[0])
                new_used_paths.add(p)
                for x in graph[curr_node[1]][p]:
                    if start == x:
                        cycles.add(frozenset(new_used_paths))
                    else:
                        queue.append((new_used_paths, x))   
    return cycles
    
def solve():
    lines = [line.rstrip() for line in sys.stdin]
    graph = create_graph(lines)
    solutions = set()
    
    for lock in graph.keys():
        sols = bfs(lock, graph)
        solutions.update(sols)
        for sol1 in sols:
            best_sol = sol1
            new_solutions = set()    
            # we need to ensure that this solution is the
            # only solution which uses this exact subset of paths
            # otherwise there will be redundancies
            for sol2 in solutions:
                if best_sol & sol2 == best_sol:
                    best_sol = best_sol
                elif best_sol & sol2 == sol2:
                    best_sol = sol2
                else:
                    new_solutions.add(sol2)
            new_solutions.add(best_sol)
            solutions = new_solutions
    
    solutions = [tuple(sorted(list(x))) for x in solutions]
    print_sol(solutions)
    
def print_sol(solutions):
    sol_list = [",".join(list(sol)) for sol in solutions]
    sol_list.sort()
    for s in sol_list:
        print s
    
solve()
