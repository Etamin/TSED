---
title: TSED
emoji: 🌳
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 3.19.1
app_file: app.py
pinned: false
tags:
- evaluate
- metric
- code
description: >-
  Tree Similarity of Edit Distance (TSED): AST-based structural similarity
  between generated and reference source code.
---

# Metric Card for TSED

## Metric Description

TSED (Tree Similarity of Edit Distance) measures how structurally similar two
pieces of source code are. Both snippets are parsed into abstract syntax trees
with [tree-sitter](https://tree-sitter.github.io/), the
[APTED](https://github.com/JoaoFelipe/apted) tree edit distance between them is
computed with configurable operation weights, and the result is normalised by the
size of the larger tree:

```
TSED = max(0, 1 - TreeEditDistance(T_pred, T_ref) / max(|T_pred|, |T_ref|))
```

It supports every language in
[tree-sitter-language-pack](https://github.com/Goldziher/tree-sitter-language-pack).

## How to Use

```python
import evaluate

tsed = evaluate.load("Etamin/tsed")
results = tsed.compute(
    predictions=["def add(a, b):\n    return a + b"],
    references=["def add(x, y):\n    return x + y"],
    language="python",
)
print(results)  # {'tsed': 1.0, 'tsed_scores': [1.0]}
```

### Inputs

- **predictions** (`list[str]`): generated code.
- **references** (`list[str]` or `list[list[str]]`): reference code. With several
  references per prediction, the maximum score is kept.
- **language** (`str`, default `"python"`): tree-sitter language name, e.g.
  `"java"`, `"javascript"`, `"sql"`, `"cpp"`.
- **deletion_weight** (`float`, default `1.0`)
- **insertion_weight** (`float`, default `0.8`)
- **rename_weight** (`float`, default `1.0`)

### Output Values

- **tsed** (`float`): mean score in `[0, 1]`; higher is more similar.
- **tsed_scores** (`list[float]`): per-example scores.

## Standalone package

```bash
pip install tsed
```

```python
import TSED
TSED.Calculate("python", code1, code2, 1.0, 0.8, 1.0)
```

## Limitations

TSED compares syntax-tree structure only: identifier names and literal values
are not tree nodes, so snippets that differ only in naming score 1.0, and two
programs with different structure but identical behaviour can score low.

## Citation

```bibtex
@inproceedings{song-etal-2024-revisiting,
    title = "Revisiting Code Similarity Evaluation with Abstract Syntax Tree Edit Distance",
    author = "Song, Yewei  and
      Lothritz, Cedric  and
      Tang, Daniel  and
      Bissyand{\'e}, Tegawend{\'e}  and
      Klein, Jacques",
    editor = "Ku, Lun-Wei  and
      Martins, Andre  and
      Srikumar, Vivek",
    booktitle = "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.acl-short.3/",
    doi = "10.18653/v1/2024.acl-short.3",
    pages = "38--46",
}
```

## Further References

- Code: https://github.com/Etamin/TSED
- Paper: https://aclanthology.org/2024.acl-short.3/
