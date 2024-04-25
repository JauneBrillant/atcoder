use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    println!("{}", find_second_max(&a).unwrap());
}

fn find_second_max(a: &[usize]) -> Option<usize> {
    let max = *a.iter().max().unwrap();
    let filter_arr = a.iter().filter(|&v| *v != max);
    filter_arr.max().copied()
}
