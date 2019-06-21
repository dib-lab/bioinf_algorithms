use std::env;
use std::error::Error;
use std::fs;

pub fn genome_from_path(text: &[&str]) -> String {
    let mut seq: String = text[0].into();
    for kmer in &text[1..] {
        seq.push(kmer.chars().last().unwrap());
    }
    seq
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba3b.txt".into());
    let data = fs::read_to_string(input)?;
    let lines: Vec<&str> = data.lines().collect();

    println!("{}", genome_from_path(&lines));

    Ok(())
}
