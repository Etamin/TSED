# Tree Similarity of Edit Distance (TSED) Calculator

## Overview

This Python script calculates the Tree Similarity of Edit Distance (TSED) between two trees, utilizing the APTED (A Framework for Tree Edit Distance) library. TSED is commonly employed in tasks such as code review and evaluation, offering a metric for assessing the structural similarity between two tree structures.


## Requirements

 - [Python `<=` 3.13](https://www.python.org/doc/versions/)

## Dependencies

- [tree_sitter `>=` 0.23.3](https://pypi.org/project/tree-sitter/)
- [tree_sitter_language_pack `>=` 0.6.1](https://pypi.org/project/tree-sitter-languages/)
- [apted](https://pypi.org/project/apted/)

## Usage

Using a virtual environment is a useful way to manage dependencies,
particularly with multiple versions of Python.

```sh
% python -m venv .venv
% source .venv/bin/activate
```

Follow the rest of the steps in the virtual environment

1. Ensure that the necessary dependencies are installed:

    ```sh
    % pip install -r requirements.txt
    ```

2. Modify the script as needed, providing the language, origin tree, and target tree information.

3. Use in your code:

    ```
    import TSED
    line1 = "Code1"
    line2 = "Code2"
    ts_score = TSED.Calculate("python", line1, line2, 1.0, 0.8, 1.0)
    ```

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
