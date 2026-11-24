# KAAP industrial experience report: replication package

Companion to *Knowledge-Aligned Architecture for LLM Coding Agents: An Industrial Experience Report*, by Mo Zhou (Kuaishou Technology).

## Recompute the reported summaries

Extract the archive and run the following commands from the directory containing this README. Use Python 3. The scripts use the standard library and the included CSV files.

```sh
python recompute_delivery_totals.py
python recompute_visual_summary.py
```

| File | Contents |
| --- | --- |
| `tables/delivery-consumption.csv` | Original worker token counts and provenance of the visual assessment for 12 task pairs |
| `anonymous-ratings.csv` | 96 scalar ratings from four raters across 12 tasks and two systems |
| `recompute_delivery_totals.py` | Descriptive worker token totals for 12 original sessions per system and the 11 pairs with original successor recordings |
| `recompute_visual_summary.py` | Full panel summary and visual means for the 11 original-delivery pairs |
| `KAAP-architecture-decision-record.md` | Blank template accompanying the proposed decision procedure in Section 3.6 |
| `engineering-obligations.md` | Sanitized summary of the maintenance records discussed in Section 4.6 |
| `manifest.json` | SHA-256 checksums for the package files |

For the 12 original task pairs the expected successor and incumbent worker totals are 56,219,271 and 72,505,357 tokens. For the 11 original-delivery pairs the expected totals are 49,969,436 and 63,756,348 tokens, a 21.62% lower observed successor total. Their expected visual means are 4.841 and 4.886. The full visual panel has 48 scores per system and sums of 233 and 235, respectively.

The original task 07 worker cost remains in the 12-pair totals. The assessed successor recording for task 07 comes from a separate rerun and stays out of the 11-pair original-delivery comparison. The scripts print the separately documented rerun token count as a retained value.

## Scope

The data support recomputation of the descriptive worker-token and visual-rating summaries in Section 7.2. The engineering digest and decision-record template accompany the paper's worked examples and design guidance. Participant consent covered release of their anonymous scores. The scope excludes raw comments, videos, execution logs, rater identities and mappings, and proprietary SDK and project source. Those restrictions limit independent video re-rating, full replay, and validation of the complete development pipeline. The naming and historical budget studies are documented in the paper's appendices and are outside this package's recomputation scope.

## Licenses

The data and documentation, including the data manifest, are licensed under
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
Attribute the replication package to Mo Zhou (Kuaishou Technology).

The scripts `recompute_delivery_totals.py` and `recompute_visual_summary.py`
are licensed under the MIT License. See [LICENSE-MIT.txt](LICENSE-MIT.txt).
