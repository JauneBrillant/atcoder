use proconio::input;

fn main() {
    let mut list = Vec::new();
    loop {
      input! {
          num: i32,
      }
      list.push(num);
      if num == 0 {
          break;
      }
    }

    list.reverse();
    for num in list {
        println!("{}", num);
    }
}
