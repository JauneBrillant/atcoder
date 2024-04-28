use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        x: [Chars; n],
    }

    let mut arr = vec![];
    for (i, str) in x.iter().enumerate() {
        let win_cnt = str.iter().filter(|&&c| c == 'o').count();
        arr.push((i + 1, win_cnt));
    }

    arr.sort_by_key(|&(_, win_cnt)| std::cmp::Reverse(win_cnt));

    for (people, _) in arr {
        print!("{} ", people);
    }
}
