use proconio::input;

fn main() {
    input! {
        n: usize,
        wx: [(usize, usize); n],
    }

    let mut max_people = 0;
    for h in 0..24 {
        let mut total = 0;
        for (people, time) in wx.iter() {
            let utc_time = (h + time) % 24;
            if 9 <= utc_time && utc_time < 18 { total += people; }
        }
        max_people = max_people.max(total);
    }

    println!{"{}", max_people};
}
