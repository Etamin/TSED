# Tree Similarity of Edit Distance (TSED) Calculator

## Overview

This Python script calculates the Tree Similarity of Edit Distance (TSED) between two trees, utilizing the APTED (A Framework for Tree Edit Distance) library. TSED is commonly employed in tasks such as code review and evaluation, offering a metric for assessing the structural similarity between two tree structures.


## Requirements

 - [Python `<=` 3.13](https://www.python.org/doc/versions/)

## Dependencies

- [tree_sitter `>=` 0.23.3](https://pypi.org/project/tree-sitter/)
- [tree_sitter_language_pack `>=` 0.6.1](https://pypi.org/project/tree-sitter-languages/)
- [apted](https://pypi.org/project/apted/)

## Installation

TSED is available on [PyPI](https://pypi.org/project/tsed/):

```sh
pip install tsed
```

## Usage

### Python package

```python
import TSED

code1 = "def add(a, b):\n    return a + b"
code2 = "def add(a, b):\n    if a > b:\n        return a - b\n    return a + b"
score = TSED.Calculate("python", code1, code2, 1.0, 0.8, 1.0)
print(score)  # 0.64
```

### Hugging Face `evaluate`

TSED is also available as a metric on the Hugging Face Hub:
[Etamin/tsed](https://huggingface.co/spaces/Etamin/tsed).

```sh
pip install evaluate tsed
```

```python
import evaluate

tsed = evaluate.load("Etamin/tsed")
results = tsed.compute(
    predictions=["def add(a, b):\n    return a + b", "for i in range(10):\n    print(i)"],
    references=["def add(x, y):\n    return x + y", "i = 0\nwhile i < 10:\n    print(i)\n    i += 1"],
    language="python",
)
print(results)  # {'tsed': 0.75625, 'tsed_scores': [1.0, 0.5125]}

# Several references per prediction (the best score is kept), another language
results = tsed.compute(
    predictions=["SELECT name FROM users WHERE age > 30"],
    references=[["SELECT name FROM users", "SELECT id FROM users WHERE age > 18"]],
    language="sql",
)
print(results)  # {'tsed': 1.0, 'tsed_scores': [1.0]}
```

`compute` also accepts `deletion_weight` (default `1.0`), `insertion_weight`
(default `0.8`) and `rename_weight` (default `1.0`).

### From source

Using a virtual environment is a useful way to manage dependencies,
particularly with multiple versions of Python.

```sh
% python -m venv .venv
% source .venv/bin/activate
% pip install -r requirements.txt
```

Then `import TSED` from the repository root, as above.

## Script Explanation

- `Node`: A class representing a node in the tree structure.
- `parse_tree_string(tree_string)`: Parses the tree string and constructs a tree
    structure using the `Node` class.
- `_parse(language, program_str, encoding)`: Parses the given program string
    into a tree format used by `tree_sitter`.
- `_get_tree(language, program_str)`: Parses the given program string into a
    tree format (i.e., `Node`) used by the script.
- `Calculate(programming_language, origin, target, deletion_weight, insertion_weight, rename_weight)`:
    Calculates the TSED using the APTED library with custom edit operation configurations.

## Parameters

- `programming_language`: A programming language for parsing, that is suppored by
    `tree_sitter_language_pack`. A [list of supported languages](https://github.com/Goldziher/tree-sitter-language-pack/tree/main?tab=readme-ov-file#available-languages) is available.
- `origin` and `target`: Strings representing the origin and target trees.
- `deletion_weight`, `insertion_weight`, `rename_weight`: Custom edit operation weights for deletion, insertion, and renaming.

## Output

The script outputs a similarity score between 0 and 1, representing the
structural similarity between two strings representing the origin and target
trees of some source code.

## Citation

If you use TSED, please cite:

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
