use std::env;
use std::error::Error;
use std::fs;

pub fn hamming(seq1: &[u8], seq2: &[u8]) -> usize {
    seq1.iter()
        .zip(seq2.iter())
        .filter(|(b1, b2)| b1 != b2)
        .count()
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1g.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let s1 = lines.next().unwrap();
    let s2 = lines.next().unwrap();

    println!("{}", hamming(s1.as_bytes(), s2.as_bytes()));

    Ok(())
}
