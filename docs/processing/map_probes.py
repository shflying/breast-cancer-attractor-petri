""" Map probe  IDs to gene symbols using platform annotation."""


import gzip
import pandas as pd
import argparse
from io import StringIO

def load_annotation(path: str) -> pd.DataFrame:
    """Load platform annotation file and extract probe-to-gene mapping."""
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    
    # Find platform table
    table_start = None
    for i, line in enumerate(lines):
        if "!platform_table_begin" in line:
            table_start = i + 1
            break
    
    if table_start is None:
        raise ValueError("No platform table found")
    
    table_lines = []
    for line in lines[table_start:]:
        if "!platform_table_end" in line:
            break
        table_lines.append(line)
    
    annot = pd.read_csv(StringIO("".join(table_lines)), sep="\t")
    return annot

def map_probes(expr: pd.DataFrame, annot: pd.DataFrame, 
               probe_col: str = "ID", gene_col: str = "GENE SYMBOL") -> pd.DataFrame:
    """Map probe IDs to gene symbols and aggregate by gene."""
    if gene_col not in annot.columns:
        # Try alternative column names
        for col in ["Gene symbol", "Gene Symbol", "gene_symbol"]:
            if col in annot.columns:
                gene_col = col
                break
    
    mapping = annot[[probe_col, gene_col]].dropna()
    mapping = mapping[mapping[gene_col] != ""]
    
    # Filter expression to mapped probes
    common = expr.index.intersection(mapping[probe_col])
    expr_mapped = expr.loc[common]
    
    # Add gene symbols and aggregate
    gene_map = dict(zip(mapping[probe_col], mapping[gene_col]))
    expr_mapped.index = expr_mapped.index.map(gene_map)
    expr_gene = expr_mapped.groupby(expr_mapped.index).mean()
    
    return expr_gene

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--expr", required=True, help="Expression matrix CSV")
    parser.add_argument("--annot", required=True, help="Platform annotation file")
    parser.add_argument("--output", default="mapped.csv", help="Output mapped expression")
    args = parser.parse_args()
    
    expr = pd.read_csv(args.expr, index_col=0)
    annot = load_annotation(args.annot)
    mapped = map_probes(expr, annot)
    mapped.to_csv(args.output)
    print(f"Mapped expression: {mapped.shape}")
