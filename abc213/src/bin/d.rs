use proconio::{input, marker::Usize1};
use std::collections::BTreeSet;

fn main() {
    input! {
        n: usize,
        ab: [(Usize1, Usize1); n - 1],
    }

    let mut graph = vec![BTreeSet::new(); n];
    for &(a, b) in ab.iter() {
        graph[a].insert(b);
        graph[b].insert(a);
    }

    let mut res = vec![];
    dfs(0, None, &graph, &mut res);

    for v in res {
        println!("{}", v);
    }
}

fn dfs(vertex: usize, parent: Option<usize>, graph: &Vec<BTreeSet<usize>>, res: &mut Vec<usize>) {
    res.push(vertex + 1);
    for &ch in graph[vertex].iter() {
        if Some(ch) == parent {
            continue;
        }
        dfs(ch, Some(vertex), graph, res);
        res.push(vertex + 1);
    }
}
