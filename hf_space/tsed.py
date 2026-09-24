"""TSED: Tree Similarity of Edit Distance metric for Hugging Face `evaluate`."""

import datasets
import evaluate
import TSED

_CITATION = """\
@inproceedings{song-etal-2024-revisiting,
    title = "Revisiting Code Similarity Evaluation with Abstract Syntax Tree Edit Distance",
    author = "Song, Yewei  and
      Lothritz, Cedric  and
      Tang, Daniel  and
      Bissyand{\\'e}, Tegawend{\\'e}  and
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
"""

_DESCRIPTION = """\
TSED (Tree Similarity of Edit Distance) measures the structural similarity of two
pieces of source code. Both programs are parsed into abstract syntax trees with
tree-sitter, the APTED tree edit distance between them is computed with
configurable deletion / insertion / rename weights, and the distance is normalised
by the size of the larger tree: TSED = max(0, 1 - distance / max_nodes).
Scores range from 0 (completely different) to 1 (structurally identical).
"""

_KWARGS_DESCRIPTION = """
Args:
    predictions (list of str): generated code snippets.
    references (list of str, or list of list of str): reference code snippet(s).
        With several references per prediction, the best (maximum) score is used.
    language (str): a tree-sitter-language-pack language name. Defaults to "python".
    deletion_weight (float): weight of a node deletion. Defaults to 1.0.
    insertion_weight (float): weight of a node insertion. Defaults to 0.8.
    rename_weight (float): weight of a node rename. Defaults to 1.0.
Returns:
    tsed (float): mean TSED score over all pairs.
    tsed_scores (list of float): per-example TSED scores.
Examples:
    >>> tsed = evaluate.load("Etamin/tsed")
    >>> results = tsed.compute(
    ...     predictions=["def add(a, b):\\n    return a + b"],
    ...     references=["def add(x, y):\\n    return x + y"],
    ...     language="python",
    ... )
    >>> print(results["tsed"])
    1.0
"""


@evaluate.utils.file_utils.add_start_docstrings(_DESCRIPTION, _KWARGS_DESCRIPTION)
class Tsed(evaluate.Metric):
    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=[
                datasets.Features(
                    {
                        "predictions": datasets.Value("string"),
                        "references": datasets.Sequence(datasets.Value("string")),
                    }
                ),
                datasets.Features(
                    {
                        "predictions": datasets.Value("string"),
                        "references": datasets.Value("string"),
                    }
                ),
            ],
            homepage="https://github.com/Etamin/TSED",
            codebase_urls=["https://github.com/Etamin/TSED"],
            reference_urls=["https://aclanthology.org/2024.acl-short.3/"],
        )

    def _compute(
        self,
        predictions,
        references,
        language="python",
        deletion_weight=1.0,
        insertion_weight=0.8,
        rename_weight=1.0,
    ):
        scores = []
        for pred, refs in zip(predictions, references):
            if isinstance(refs, str):
                refs = [refs]
            scores.append(
                max(
                    TSED.Calculate(
                        language, pred, ref, deletion_weight, insertion_weight, rename_weight
                    )
                    for ref in refs
                )
            )
        return {
            "tsed": sum(scores) / len(scores) if scores else 0.0,
            "tsed_scores": scores,
        }
