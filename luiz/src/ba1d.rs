use std::env;
use std::error::Error;
use std::fs;
use std::str;

pub fn pattern_matches(text: &[u8], pattern: &str) -> Vec<usize> {
    text.windows(pattern.len())
        .enumerate()
        .filter_map(|(i, x)| {
            if str::from_utf8(x).unwrap() == pattern {
                Some(i)
            } else {
                None
            }
        })
        .collect()
}

fn main() -> Result<(), Box<dyn Error>> {
    assert_eq!(pattern_matches(b"GATATATGCATATACTT", "ATAT"), vec![1, 3, 9]);

    let input: String = env::args().nth(1).expect("Input data file missing");
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let pattern = lines.next().unwrap();
    let text = lines.next().unwrap();

    for word in pattern_matches(text.as_bytes(), pattern) {
        print!("{} ", word);
    }
    println!("");

    Ok(())
}
