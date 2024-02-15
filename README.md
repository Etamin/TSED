# Tree Similarity of Edit Distance (TSED) Calculator

## Overview

This Python script calculates the Tree Similarity of Edit Distance (TSED) between two trees, utilizing the APTED (A Framework for Tree Edit Distance) library. TSED is commonly employed in tasks such as code review and evaluation, offering a metric for assessing the structural similarity between two tree structures.

## Dependencies

- apted
- tree_sitter_languages

## Usage

1. Ensure that the necessary dependencies are installed:

    ```
    pip install apted tree_sitter_languages
    ```

2. Modify the script as needed, providing the language, origin tree, and target tree information.

3. Use in your code:

    ```
    import TSED
    line1 = "Code1"
    line2 = "Code2"
    ts_score=TSED.Calaulte("python",line1, line2, 1.0, 0.8, 1.0)
    ```

## Script Explanation

- `Node`: A class representing a node in the tree structure.
- `parse_tree_string(tree_string)`: Parses the tree string and constructs a tree structure using the `Node` class.
- `calculate_node_count(node)`: Calculates the number of nodes in the tree.
- `get_Trees(lan,origin,target)`: Retrieves trees for the specified language, origin tree, and target tree.
- `Calaulte(lan, str1, str2, d, i, r)`: Calculates the TSED using the APTED library with custom edit operation configurations.

## Parameters

- `lan`: Programming language for parsing (e.g., 'python', 'java').
- `str1` and `str2`: Strings representing the origin and target trees.
- `d`, `i`, `r`: Custom edit operation weights for delete, insert, and rename.

## Output

The script outputs a similarity score between 0 and 1, representing the structural similarity be
