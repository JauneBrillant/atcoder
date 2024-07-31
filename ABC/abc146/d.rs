use proconio::{input, marker::Usize1};

#[derive(Clone, Copy)]
struct Edge {
    to: usize,
    id: usize,
}

fn main() {
    input! {
        n: usize,
        ab: [(Usize1, Usize1); n - 1],
    }

    let mut graph = vec![vec![]; n];
    for (i, (a, b)) in ab.into_iter().enumerate() {
        graph[a].push(Edge { to: b, id: i });
        graph[b].push(Edge { to: a, id: b });
    }

    let mut ans = vec![0; n - 1];
    dfs(0, 0, 0, &graph, &mut ans);

    let max = ans.iter().max().unwrap();
    println!("{}", max);
    for v in ans {
        println!("{}", v);
    }
}

fn dfs(v: usize, p: usize, pc: usize, graph: &Vec<Vec<Edge>>, ans: &mut Vec<usize>) {
    let mut color = 1;
    for &c in graph[v].iter() {
        if c.to == p {
            continue;
        }
        if color == pc {
            color += 1;
        }
        ans[c.id] = color;
        dfs(c.to, v, color, graph, ans);
        color += 1;
    }
}
