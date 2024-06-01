use proconio::input;
use proconio::marker::Usize1;

fn main() {
    input! {
        n: usize,
        m: usize,
        ab: [(Usize1, Usize1); m],
    }

    let mut graph = vec![vec![]; n];
    for (a, b) in ab.into_iter() {
        graph[a].push(b);
        graph[b].push(a);
    }

    let mut ans = 0;
    for (i, vec) in graph.iter().enumerate() {
        let cnt = vec.iter().filter(|&&e| e < i).count();
        if cnt == 1 {
            ans += 1;
        }
    }

    println!("{}", ans);
}
