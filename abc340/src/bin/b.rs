use proconio::input;

fn main() {
    input! {
        q: usize,
        query: [(i32, i32); q],
    }

    let mut res: Vec<i32> = Vec::new();
    for (first, second) in query {
        if first == 1 {
            res.push(second);
        } else {
            println!("{}", res[res.len() - second as usize])
        }
    }
}
