interface Node {
    connections: Node[];
    parents: Node[];
    children: Node[];
    id: string;
}

function node(): Node {
    return {
        connections: [],
        parents: [],
        children: [],
        id: crypto.randomUUID()
    };
}

interface Move {
    from: Node;
    to: Node;
    reparent: Node[];
}

const nodes: Node[] = Array.from({ length: 2 }, node);

/* a node is dead when it has 3 connections */
const isDead = (node: Node) => {
    console.assert(node.connections.length <= 3, `Node ${node.id} has more than 3 connections`);
    return node.connections.length >= 3;
}

function possibleMoves(nodes: Node[]): Move {
    const moves: Move[] = [];

    for (const node of nodes) {
        if (isDead(node)) {
            continue;
        }

        // if the node has 1 connection, it can be connected to itself
        if (node.connections.length === 1) {
            moves.push({
                from: node,
                to: node,
                reparent: []
            });

            // now we can talk about parenting nodes - since this node has 1 connection, we can connect it to itself while trrapping a node
        }

        // since the node has 1 or more connections remaining, it can be connected to any other node.
        // since that's the case, we'll check if it's a child or parent of any node and see if it can
        // be connected to that node's parent or child.
        for (const childNode of node.children) {
            if (isDead(childNode)) {
                continue;
            }

            moves.push({
                from: node,
                to: childNode,
                // we aren't adding new parents to the child node
                // since the child node is already connected to the parent node
                reparent: []
            });
        }

        for (const parentNode of node.parents) {
            if (isDead(parentNode)) {
                continue;
            }

            moves.push({
                from: node,
                to: parentNode,
                // we aren't adding new children to the parent node
                // since the parent node is already connected to the child node
                reparent: []
            });
        }
    }
}