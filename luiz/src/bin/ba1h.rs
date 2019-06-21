use std::env;
use std::error::Error;
use std::fs;
use std::str;

use bioinformatics_algorithms::hamming;

pub fn approximate_pattern_matches(text: &[u8], pattern: &str, distance: usize) -> Vec<usize> {
    text.windows(pattern.len())
        .enumerate()
        .filter_map(|(i, x)| {
            if hamming(str::from_utf8(x).unwrap(), pattern) <= distance {
                Some(i)
            } else {
                None
            }
        })
        .collect()
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1h.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let pattern = lines.next().unwrap();
    let text = lines.next().unwrap();
    let d = lines.next().unwrap().parse().unwrap();

    for word in approximate_pattern_matches(text.as_bytes(), pattern, d) {
        print!("{} ", word);
    }
    println!();

    Ok(())
}
