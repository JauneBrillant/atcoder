use proconio::input;
use std::collections::BTreeMap;

fn main() {
    input! {
        _n: usize,
        m: usize,
        votes: [usize; m],
    }

    let mut tree_map = BTreeMap::new();
    let mut winner = (0, 0);
    for vote in votes.iter() {
        *tree_map.entry(vote).or_insert(0) += 1;
        if let Some(count) = tree_map.get(&vote) {
            if *count == winner.1 && *vote < winner.0 {
                winner = (*vote, *count);
            }

            if *count > winner.1 {
                winner = (*vote, *count);
            }
        }
        println!("{}", winner.0);
    }
}
