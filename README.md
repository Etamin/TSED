# Tree Similarity of Edit Distance (TSED) Calculator

## Overview

This Python script calculates the Tree Similarity of Edit Distance (TSED) between two trees, utilizing the APTED (A Framework for Tree Edit Distance) library. TSED is commonly employed in tasks such as code review and evaluation, offering a metric for assessing the structural similarity between two tree structures.


## Requirements

 - [Python `<=` 3.9](https://www.python.org/doc/versions/)

The dependencies required to run `TSED` are validated to work up to Python
major version 3.9.
There are a number of ways to manage multiple Python versions,
such as [pyenv](https://github.com/pyenv/pyenv).
Manually installing and managing Python versions is also an option.

## Dependencies

- [apted](https://pypi.org/project/apted/)
- [tree_sitter_languages](https://pypi.org/project/tree-sitter-languages/)

## Usage

Using a virtual environment is a useful way to manage dependencies,
particularly with multiple versions of Python.

Confirm you are using Python 3.9:

```sh
% python -V $ # Should print out Python 3.9.21
```

Set up a virtual environment and activate it:

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
    ts_score = TSED.Calculate("python",line1, line2, 1.0, 0.8, 1.0)
    ```

## Script Explanation

- `Node`: A class representing a node in the tree structure.
- `parse_tree_string(tree_string)`: Parses the tree string and constructs a tree structure using the `Node` class.
- `calculate_node_count(node)`: Calculates the number of nodes in the tree.
- `get_Trees(lan,origin,target)`: Retrieves trees for the specified language, origin tree, and target tree.
- `Calculate(lan, str1, str2, d, i, r)`: Calculates the TSED using the APTED library with custom edit operation configurations.

## Parameters

- `lan`: Programming language for parsing (e.g., 'python', 'java').
- `str1` and `str2`: Strings representing the origin and target trees.
- `d`, `i`, `r`: Custom edit operation weights for delete, insert, and rename.

## Output

The script outputs a similarity score between 0 and 1, representing the
structural similarity between two strings representing the origin and target
trees of some source code.
