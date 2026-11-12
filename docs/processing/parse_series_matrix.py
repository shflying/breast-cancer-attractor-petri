"""Parse GEO Series Matrix  files to extract sample metadata and expression data."""


import gzip
import pandas as pd
import argparse

def parse_series_matrix(path: str) -> tuple:
    """
    Parse a GEO Series Matrix file.
    
    Returns
    -------
    meta : DataFrame
        Sample characteristics
    expr : DataFrame
        Expression matrix (genes/probes × samples)
    """
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    
    # Extract sample characteristics
    char_lines = [l for l in lines if l.startswith("!Sample_characteristics_ch1")]
    title_lines = [l for l in lines if l.startswith("!Sample_title")]
    
    # Find expression table
    table_start = None
    for i, line in enumerate(lines):
        if line.startswith("!series_matrix_table_begin"):
            table_start = i + 1
            break
    
    if table_start:
        # Read expression table
        table_lines = []
        for line in lines[table_start:]:
            if line.startswith("!series_matrix_table_end"):
                break
            table_lines.append(line)
        
        from io import StringIO
        expr = pd.read_csv(StringIO("".join(table_lines)), sep="\t", index_col=0)
    else:
        expr = pd.DataFrame()
    
    # Build metadata
    meta = pd.DataFrame()
    if title_lines:
        titles = title_lines[0].strip().split("\t")[1:]
        meta["title"] = [t.strip('"') for t in titles]
    
    return meta, expr

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to Series Matrix file")
    parser.add_argument("--output", default="samples.csv", help="Output metadata CSV")
    args = parser.parse_args()
    
    meta, expr = parse_series_matrix(args.input)
    meta.to_csv(args.output, index=False)
    print(f"Parsed {len(meta)} samples")
    if not expr.empty:
        print(f"Expression matrix: {expr.shape}")
