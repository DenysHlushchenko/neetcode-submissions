class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {
        const adj = {};

        for (let edge of edges) {
            let [n1, n2] = edge;

            if (!adj[n1]) adj[n1] = new Set();
            if (!adj[n2]) adj[n2] = new Set();
            
            adj[n1].add(n2);
            adj[n2].add(n1);
        }

        let res = 0;
        let visited = new Set();
        
        for (let i=0; i<n; i++) {
            if (visited.has(i)) continue;

            res++;
            let stack = [i];

            while (stack.length > 0) {
                let node = stack.pop();

                if (!visited.has(node)) {
                    visited.add(node);

                    for (let neighb of adj[node] || []) {
                        if (!visited.has(neighb)) {
                            stack.push(neighb);
                        }
                    }
                }
            }
        }

        return res;
    }
}
