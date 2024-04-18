use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        arr: [usize; n],
    }

    let result: Vec<_> = arr.iter()
        .filter(|num| *num % k == 0)
        .map(|num| num / k)
        .collect();

    for num in result.iter() {
        print!("{} ", num);
    }
}
