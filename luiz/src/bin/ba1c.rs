use std::env;
use std::error::Error;
use std::fs;

use bioinformatics_algorithms::revc;

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba1c.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text = lines.next().unwrap();

    println!("{}", revc(text));

    Ok(())
}
