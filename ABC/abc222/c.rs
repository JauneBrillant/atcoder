use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [Chars; n * 2],
    }

    let mut rank = (0..n + n).map(|i| (i, 0)).collect::<Vec<_>>();
    for i in 0..m {
        for j in (0..n + n).step_by(2) {
            let l = a[rank[j].0][i];
            let r = a[rank[j + 1].0][i];
            if let Some(winner) = get_winner(l, r, j, j + 1) {
                rank[winner].1 += 1;
            }
        }

        rank.sort_by(
            |(a1, b1), (a2, b2)| {
                if b1 == b2 {
                    a1.cmp(a2)
                } else {
                    b2.cmp(b1)
                }
            },
        );
    }

    for (i, _) in rank {
        println!("{}", i + 1);
    }
}

fn get_winner(p1: char, p2: char, p1_idx: usize, p2_idx: usize) -> Option<usize> {
    match (p1, p2) {
        ('G', 'C') | ('C', 'P') | ('P', 'G') => Some(p1_idx),
        ('G', 'P') | ('C', 'G') | ('P', 'C') => Some(p2_idx),
        _ => None,
    }
}
