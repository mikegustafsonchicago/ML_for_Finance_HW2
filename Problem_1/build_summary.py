#!/usr/bin/env python3
import re
import csv

def parse_results(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    # split into blocks marked by --- var ---
    pattern = re.compile(r"---\s*(?P<var>\w+)\s*---")
    matches = list(pattern.finditer(text))
    records = []
    for idx, match in enumerate(matches):
        var = match.group('var')
        start = match.end()
        end = matches[idx+1].start() if idx+1 < len(matches) else len(text)
        rest = text[start:end]
        rec = {'var': var}

        # alpha
        m = re.search(r"Selected alpha.*?:\s*([0-9\.eE\+-]+)", rest)
        if m is None:
            continue
        rec['alpha'] = m.group(1)

        # count terms
        m = re.search(r"Selected count terms:\s*\[([^\]]+)\]", rest)
        topics = [t.strip().strip("'\"") for t in m.group(1).split(',')] if m else []
        rec['topics'] = topics

        # overall R2
        m = re.search(r"R-squared:\s*([0-9\.eE\+-]+)", rest)
        rec['r2'] = m.group(1) if m else ''

        # F-statistic and Prob
        m = re.search(r"F-statistic:\s*([0-9\.eE\+-]+).*?Prob \(F-statistic\):\s*([0-9\.eE\+-]+)", rest, re.S)
        if m:
            rec['F'] = m.group(1)
            rec['Prob'] = m.group(2)

        # extract significant topics based on p-values in the OLS table
        sig = []
        table = re.search(r"coef\s+std err.*?\n(-+\n)?(.*?)\nOmnibus", rest, re.S)
        if table:
            rows = table.group(2).strip().split('\n')
            for row in rows:
                parts = re.split(r"\s{2,}", row.strip())
                if len(parts) >= 5:
                    name, pval = parts[0], parts[3]
                    try:
                        if name in topics and float(pval) < 0.05:
                            sig.append(name)
                    except:
                        pass
        rec['sig_topics'] = sig

        records.append(rec)
    return records

def write_csv(records, out_csv):
    with open(out_csv, 'w', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(['var','alpha','r2','5 Topics','Significant Topics (p<0.05)','F-statistic','Prob'])
        for r in records:
            w.writerow([
                r['var'],
                r['alpha'],
                r['r2'],
                ";".join(r['topics']),
                ";".join(r['sig_topics']),
                r['F'],
                r['Prob']
            ])

def write_md(records, out_md):
    with open(out_md, 'w') as md:
        md.write('| var | alpha | r2 | 5 Topics | Significant Topics (p<0.05) | F-statistic | Prob |\n')
        md.write('|-----|-------|----|----------|-----------------------------|-------------|------|\n')
        for r in records:
            md.write(
                f"| {r['var']} | {r['alpha']} | {r['r2']} | "
                f"{', '.join(r['topics'])} | {', '.join(r['sig_topics']) or '-'} | "
                f"{r['F']} | {r['Prob']} |\n"
            )

if __name__ == "__main__":
    recs = parse_results('transformers_results.md')
    write_csv(recs, 't_results.csv')
    write_md(recs, 't_results.md')