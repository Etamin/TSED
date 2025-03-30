from apted import APTED, PerEditOperationConfig
from tree_sitter import Tree
from tree_sitter_language_pack import get_parser, SupportedLanguage


class Node:
    def __init__(self, name, path):
        self.id = path
        self.name = name
        self.children = []
        self.len_sexp = 0

    def add_child(self, node):
        self.children.append(node)


def parse_tree_string(tree_string):
    stack = []
    current_node = None
    tokens = tree_string.replace("(", " ( ").replace(")", " ) ").split()

    for token in tokens:
        if token == "(":
            if current_node is not None:
                stack.append(current_node)
            current_node = Node("", "")
        elif token == ")":
            if stack:
                parent_node = stack.pop()
                parent_node.add_child(current_node)
                current_node = parent_node
            else:
                # Extra closing parenthesis, ignore it
                continue
        else:
            # Use the content between brackets as the node name
            name = token.strip("()")
            if current_node is None:
                current_node = Node("", "")
            if name != "":
                # if ":" in name:
                #     name=name.split(":")[0]
                current_node.name = name
            else:
                current_node.name = " "

    return current_node


def _parse(language: SupportedLanguage, program_str: str, encoding="utf-8") -> Tree:
    """Returns a tree-sitter representation of a program string.

    Args:
        language (str): A programming language supported by
            tree_sitter_language_pack.
        program_str (str): A string representation of a program.
        encoding (str, optional): The encoding of program_str. Defaults to
            "utf-8".

    Returns:
        Tree: A tree-sitter representation of the given program string.
    """
    parser = get_parser(language)
    return parser.parse(bytes(program_str, encoding=encoding))


def _get_tree(language: SupportedLanguage, tree_str: str) -> Node:
    """Returns a Node (i.e., an AST) representation of the given string, which
    represents a program.

    Args:
        language (SupportedLanguage): A programming language supported by
            tree_sitter_language_pack.
        tree_str (str): A string representation of a program.

    Returns:
        Node: A Node representation of the given string.
    """
    tree_sitter_representation = _parse(language, tree_str)
    tree_sexp = str(tree_sitter_representation.root_node)
    tree_node = parse_tree_string(tree_sexp)
    tree_node.len_sexp = tree_sexp.count(")")
    return tree_node


def Calculate(
    programming_language: SupportedLanguage,
    origin: str,
    target: str,
    deletion_weight: float,
    insertion_weight: float,
    rename_weight: float,
) -> float:
    """Calculates the TSED (Tree Similarity of Edit Distance) score between two
    trees using the APTED algorithm
    (http://tree-edit-distance.dbresearch.uni-salzburg.at.

    Args:
        programming_language (SupportedLanguage): A programming language
            supported by tree_sitter_language_pack.
        origin (str): The origin string comprising a program.
        target (str): The destination string (i.e., the end-result after edit
            operations are applied) comprising a program.
        deletion_weight (float): The weight for deletion operations.
        insertion_weight (float): The weight for insertion operations.
        rename_weight (float): The weight for re-name operations.

    Returns:
        float: The TSED score computed for the two input trees.
    """
    tree1, tree2 = (
        _get_tree(programming_language, origin),
        _get_tree(programming_language, target),
    )
    max_len = max(tree1.len_sexp, tree2.len_sexp)
    apted = APTED(
        tree1,
        tree2,
        PerEditOperationConfig(deletion_weight, insertion_weight, rename_weight),
    )
    res = apted.compute_edit_distance()
    if max_len > 0:
        if res > max_len:
            return 0.0
        else:
            return (max_len - res) / max_len
    else:
        return 1.0
