use std::env;
use std::error::Error;
use std::fs;

pub fn pattern_count(text: &str, pattern: &str) -> u64 {
    let overlap = text.len() - pattern.len() + 1;

    let mut count = 0;

    for i in 0..overlap {
        let start = i;
        let end = i + pattern.len();
        if &text[start..end] == pattern {
            count += 1;
        }
    }

    count
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1a.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text = lines.next().unwrap();
    let pattern = lines.next().unwrap();

    println!("{}", pattern_count(text, pattern));

    Ok(())
}
