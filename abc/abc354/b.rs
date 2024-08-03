use proconio::input;

fn main() {
    input! {
        n: usize,
        mut sc: [(String, usize); n],
    }

    let sum = sc.iter().map(|(_, v)| v).sum::<usize>();
    let t = sum % n;

    sc.sort_by(|(n1, _), (n2, _)| n1.cmp(n2));
    let res = &sc.iter().nth(t).unwrap().0;

    println!("{}", res);
}
