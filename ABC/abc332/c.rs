use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        _n: usize,
        m: usize,
        schedule: Chars,
    }

    // true -> 使用可能, false -> 使用済み
    let mut logo_t_shirts: Vec<bool> = vec![];
    let mut t_shirts: Vec<bool> = vec![true; m];

    for day in schedule {
        // なんの予定もない時
        // 全てのtシャツを洗濯
        if day == '0' {
            set_all_true(&mut logo_t_shirts);
            set_all_true(&mut t_shirts);
        }

        // 食事に行く
        // 無地Tを着る・なければロゴTを着る
        else if day == '1' {
            if has_t_shirts(&mut t_shirts) {
                //
            } else {
                if has_t_shirts(&mut logo_t_shirts) {
                    //
                } else {
                    logo_t_shirts.push(false);
                }
            }
        }

        else if day == '2' {
            if has_t_shirts(&mut logo_t_shirts) {
                //
            } else {
                logo_t_shirts.push(false);
            }
        }
    }
    println!("{}", logo_t_shirts.len());
}

fn set_all_true(v: &mut Vec<bool>) {
    v.iter_mut().for_each(|x| *x = true);
}

fn has_t_shirts(shirts: &mut Vec<bool>) -> bool {
    for e in shirts.iter_mut() {
        if *e {
            *e = false;
            return true;
        }
    }
    false
}
