use std::env;
use std::error::Error;
use std::fs;

pub fn minimum_skew(text: &[u8]) -> Vec<usize> {
    let mut g_count = 0;
    let mut c_count = 0;
    let mut min_skew = 0;
    let mut mins = Vec::default();

    text.iter()
        .enumerate()
        .map(|(i, base)| {
            let skew = g_count - c_count;

            if skew < min_skew {
                min_skew = skew;
                mins.clear();
                mins.push(i);
            } else if skew == min_skew {
                mins.push(i);
            };

            match *base as char {
                'C' => c_count += 1,
                'G' => g_count += 1,
                _ => (),
            }
        })
        .count();

    mins
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1f.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text = lines.next().unwrap();

    for pos in minimum_skew(text.as_bytes()) {
        print!("{} ", pos);
    }
    println!();

    Ok(())
}
