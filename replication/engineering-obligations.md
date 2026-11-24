# Engineering obligations: sanitized retained-record digest

Accompanies the KAAP industrial experience report, SCP submission version v3.20.
This document paraphrases selected design and maintenance notes. It is not SDK source, an execution log, a new experiment, or an independently reproduced root-cause analysis. The episodes are not additional members of the paired-task cohorts. No maintenance hours or episode-specific worker consumption are available. Private product names, paths, and source-code identifiers are omitted.

## Uniform binding

The retained design record reports that public shader locations differ from private runtime uniform slots. A wrong mapping can leave shader inputs at defaults. The recorded design uses uniform-name and shader-stage reflection to establish the mapping. This supports an implementation responsibility assignment; it does not independently establish complete standard conformance or a causal consumption benefit.

## Framebuffer-texture lifetime

The maintenance record reports a native framebuffer-texture remapping cleared each frame. A capture performed only on one frame could therefore lose its mapping when sampled later, producing black output. The recorded repair persists the remapping, registers it on framebuffer binding, and removes it on deletion or destruction. The paper has not newly rerun this episode. A sequence that captures on one frame and samples on later frames is a proposed regression check, not a reported new pass.

## Texture-unit constants

The notes report that a missing supported constant allowed invalid values to propagate into native texture-unit selection. The recorded response completes the constant table and rejects invalid inputs explicitly. The notes describe repair and regression evidence; this digest does not independently repeat it or assign its episode to a paired-task identifier.

## Revision of a packaging assumption

An earlier design note treated a runtime directory as required for loading. A later annotation reports that the requirement did not hold for another package form and revises the packaging rule, while environment-specific checks remain relevant. This is a correction to retained engineering knowledge, not a universal loading rule or a new experiment.

## Scope of reuse

These accounts ground the worked trace in Section 4.6 and Appendix G.5. They illustrate private knowledge encoded in software, explicit deviations, and continuing validation responsibilities. They do not measure avoided discovery time, maintenance savings, complete task acceptance, or pretrained knowledge's causal contribution. Original source identity and line locators remain in the confidential audit record, rather than being supplied here as publicly accessible primary artifacts.
