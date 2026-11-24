# Knowledge-Aligned Architecture for LLM Coding Agents

**Knowledge-Aligned Architecture for LLM Coding Agents: An Industrial Experience Report**

Mo Zhou, Kuaishou Technology

[Read the paper (PDF)](KAAP-paper-v3.21.pdf) | [Replication package on Zenodo](https://doi.org/10.5281/zenodo.24157719) | [Browse the replication files](replication/README.md)

## Paper and status

This repository publishes the author's submitted manuscript, **v3.21 (12 November 2026)**, and the public replication package. The paper has been submitted to *Science of Computer Programming*. This is an author preprint, not a journal-accepted or publisher-formatted article.

The paper proposes the Knowledge-Aligned Architecture Principle (KAAP): design abstractions, representations, interfaces, and workflows to reuse applicable agent knowledge while making residual obligations explicit. A Knowledge-Aligned Interface Layer (KAIL) exposing a WebGL-shaped programming model over a proprietary graphics runtime is the industrial case examined in the report. The report distinguishes explicit knowledge assets, runtime knowledge use, worker consumption, and assessment of delivered outputs.

The eleven task pairs with original-delivery recordings have an observed successor worker-token total 21.62% below the incumbent total. Their visual-rating means are 4.841 and 4.886, respectively. These are descriptive observations from this case; they do not establish a causal effect of pretraining familiarity, equivalent quality, or complete functional acceptance. Task 07's assessed successor recording belongs to a separate rerun and is excluded from that eleven-pair comparison.

## Recompute the public summaries

Python 3 is required; both scripts use only the standard library.

```sh
cd replication
python recompute_delivery_totals.py
python recompute_visual_summary.py
```

The [replication README](replication/README.md) explains the data, expected results, and scope. The ZIP is byte-for-byte identical to the version archived on Zenodo:

- Version DOI: [10.5281/zenodo.24157719](https://doi.org/10.5281/zenodo.24157719)
- Archive: [KAAP-replication-package-v1.0.0.zip](KAAP-replication-package-v1.0.0.zip)
- Checksums: [SHA256SUMS](SHA256SUMS)

The public package supports recomputation of the reported aggregate token and anonymous visual-rating summaries. Videos, execution logs, raw assessment comments, rater mappings, proprietary SDK code, and project source are excluded. Consequently, it does not support independent video re-rating or full replay of the industrial development pipeline.

## Citation and reuse

Use [CITATION.cff](CITATION.cff) to cite the author preprint. The Zenodo DOI identifies the **replication package**, not the paper.

Replication data and documentation are licensed under **CC BY 4.0**; the two replication Python scripts are licensed under **MIT**. These licenses do not apply to the manuscript PDF. See [RIGHTS.md](RIGHTS.md) and the package's [license notice](replication/README.md#licenses).
