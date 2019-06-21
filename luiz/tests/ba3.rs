use std::io::Write;
use std::process::Command;

use assert_cmd::prelude::*;
use predicates::prelude::*;
use predicates::str::contains;
use tempfile::NamedTempFile;

#[test]
fn ba3a_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "5\nCAATCCAAC")?;

    let mut cmd = Command::cargo_bin("ba3a")?;
    cmd.arg(file.path());

    for kmer in &["AATCC", "ATCCA", "CAATC", "CCAAC", "TCCAA"] {
        cmd.assert().stdout(contains(*kmer));
    }

    Ok(())
}

#[test]
fn ba3b_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(
        file,
        "ACCGA
CCGAA
CGAAG
GAAGC
AAGCT"
    )?;

    let mut cmd = Command::cargo_bin("ba3b")?;
    cmd.arg(file.path());
    cmd.assert().success().stdout("ACCGAAGCT\n");

    Ok(())
}

#[test]
fn ba3c_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(
        file,
        "ATGCG
GCATG
CATGC
AGGCA
GGCAT"
    )?;

    let mut cmd = Command::cargo_bin("ba3c")?;
    cmd.arg(file.path());
    cmd.assert().success();

    let edges = [
        "AGGCA -> GGCAT",
        "CATGC -> ATGCG",
        "GCATG -> CATGC",
        "GGCAT -> GCATG",
    ];

    for edge in &edges {
        cmd.assert().stdout(contains(*edge));
    }

    Ok(())
}

#[test]
fn ba3d_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "4\nAAGATTCTCTAC")?;

    let mut cmd = Command::cargo_bin("ba3d")?;
    cmd.arg(file.path());
    cmd.assert().success();

    let edges = [
        "AAG -> AGA",
        "AGA -> GAT",
        "ATT -> TTC",
        "CTA -> TAC",
        "CTC -> TCT",
        "GAT -> ATT",
        "TTC -> TCT",
    ];

    for edge in &edges {
        cmd.assert().stdout(contains(*edge));
    }

    cmd.assert()
        .stdout(contains("TCT -> CTA,CTC").or(contains("TCT -> CTC,CTA")));

    Ok(())
}
