function validPath(n: number, edges: number[][], source: number, destination: number): boolean {
    let graph: { [key: number]: number[] } = {};

    // Initialize the graph
    for (let i = 0; i < n; i++) {
        graph[i] = [];
    }

    // Populate the graph
    for (let edge of edges) {
        let u = edge[0];
        let v = edge[1];

        graph[u].push(v);
        graph[v].push(u);
    }

    const visited: Set<number> = new Set(); // Use a Set for visited nodes

    return dfs(graph, source, destination, visited);
}

function dfs(graph: { [key: number]: number[] }, source: number, destination: number, visited: Set<number>): boolean {
    if (source === destination) {
        return true;
    }

    visited.add(source); // Mark the current node as visited

    for (let neighbor of graph[source]) {
        if (!visited.has(neighbor)) { // Check using Set
            if (dfs(graph, neighbor, destination, visited)) {
                return true;
            }
        }
    }

    return false;
}
