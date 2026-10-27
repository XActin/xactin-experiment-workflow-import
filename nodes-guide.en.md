# XActin experiment nodes

Choose a node from what it does, when to use it, and what you get.
Import JSON must use the `code`. Connect nodes according to the usual upstream and downstream lists.

After import, fill each form using [nodes-config-guide.en.md](nodes-config-guide.en.md).

## Assay & Analysis

### BrdU/EdU Incorporation Quantification (`brdu_edu_quantification`)
- **Type:** Result analysis
- **What it does:** Compatible with upstream BrdU/EdU assays; group 24-well plates and output Fold Change and p-values.
- **When to use it:** Use this after the upstream assay, when you need the BrdU/EdU Incorporation Quantification result.
- **What you get:** A quantitative result, such as fold change or a p value, which can be used by conditional routing.
- **Usual upstream:** `brdu`, `edu`
- **Usual downstream:** `conditional_router`

### Dual-Luciferase Reporter Quantification (`luciferase_quantitative_analysis`)
- **Type:** Result analysis
- **What it does:** Group wells from upstream dual-luciferase assays (blank/control/experimental) and configure analysis tasks.
- **When to use it:** Use this after the upstream assay, when you need the Dual-Luciferase Reporter Quantification result.
- **What you get:** A quantitative result, such as fold change or a p value, which can be used by conditional routing.
- **Usual upstream:** `luciferase`
- **Usual downstream:** `conditional_router`

### MTT Viability/Proliferation Quantification (`mtt_quantification`)
- **Type:** Result analysis
- **What it does:** Group MTT 96-well plates and configure analysis tasks to output Fold Change and p-values for routing.
- **When to use it:** Use this after the upstream assay, when you need the MTT Viability/Proliferation Quantification result.
- **What you get:** A quantitative result, such as fold change or a p value, which can be used by conditional routing.
- **Usual upstream:** `mtt`
- **Usual downstream:** `conditional_router`

### Colony Formation Quantification (`plate_cloning_quantification`)
- **Type:** Result analysis
- **What it does:** Group 6-well plate cloning wells and configure analysis tasks to output Fold Change and p-values for routing.
- **When to use it:** Use this after the upstream assay, when you need the Colony Formation Quantification result.
- **What you get:** A quantitative result, such as fold change or a p value, which can be used by conditional routing.
- **Usual upstream:** `plate_cloning`
- **Usual downstream:** `conditional_router`

### qPCR Quantification Analysis (`qpcr_quantification`)
- **Type:** Result analysis
- **What it does:** Quantify upstream qPCR experiments; output Fold Change and p-values per analysis; downstream only Conditional Routing.
- **When to use it:** Use this after the upstream assay, when you need the qPCR Quantification Analysis result.
- **What you get:** A quantitative result, such as fold change or a p value, which can be used by conditional routing.
- **Usual upstream:** `qpcr`
- **Usual downstream:** `conditional_router`

### Transwell Migration/Invasion Quantification (`transwell_quantification`)
- **Type:** Result analysis
- **What it does:** Group Transwell 24-well plates and configure analysis tasks to output Fold Change and p-values for routing.
- **When to use it:** Use this after the upstream assay, when you need the Transwell Migration/Invasion Quantification result.
- **What you get:** A quantitative result, such as fold change or a p value, which can be used by conditional routing.
- **Usual upstream:** `transwell`
- **Usual downstream:** `conditional_router`

### Western Blot Quantification (`western_blot_quantification`)
- **Type:** Result analysis
- **What it does:** Quantify Western Blot results as target protein expression relative to a reference protein.
- **When to use it:** Use this after the upstream assay, when you need the Western Blot Quantification result.
- **What you get:** A quantitative result, such as fold change or a p value, which can be used by conditional routing.
- **Usual upstream:** `western_blot`
- **Usual downstream:** `conditional_branch`

## Cell Biology

### BrdU Incorporation Assay (`brdu`)
- **Type:** Experiment step
- **What it does:** Run BrdU incorporation on a 24-well plate; set cells/well and configure well cell materials.
- **When to use it:** Use this when the experiment includes BrdU Incorporation Assay.
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `brdu_edu_quantification`.
- **Usual upstream:** `cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **Usual downstream:** `cell_culture`, `brdu_edu_quantification`

### Cell Co-culture (`cell_co_culture`)
- **Type:** Experiment step
- **What it does:** Multi-cell co-culture with per-well cell types/quantities, duration and medium.
- **When to use it:** Use this when the experiment includes Cell Co-culture.
- **What you get:** The product of this step. It can usually continue to: `elisa_detection`, `plate_reader_luminescence`.
- **Usual upstream:** `cell_revival`, `cell_culture`, `transient_transfection`, `lentivirus_transduction_gene`
- **Usual downstream:** `elisa_detection`, `plate_reader_luminescence`

### Cell Cryopreservation (`cell_cryopreservation`)
- **Type:** Experiment step
- **What it does:** Cryopreserve cells.
- **When to use it:** Use this when the experiment includes Cell Cryopreservation.
- **What you get:** The product of this step. In the current list this is often an end step, or it continues to a result-analysis node.
- **Usual upstream:** `cell_revival`, `cell_culture`

### Cell Culture (`cell_culture`)
- **Type:** Experiment step
- **What it does:** Cell culture and passaging.
- **When to use it:** Use this when the experiment includes Cell Culture.
- **What you get:** The product of this step. It can usually continue to: `protein_extraction`, `cell_cryopreservation`, `lentiviral_transduction`, `lentivirus_transduction_gene`, `plate_cloning`, `mtt` and others.
- **Usual upstream:** `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`, `luciferase`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`
- **Usual downstream:** `protein_extraction`, `cell_cryopreservation`, `lentiviral_transduction`, `lentivirus_transduction_gene`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`

### Cell Revival (`cell_revival`)
- **Type:** Experiment step
- **What it does:** Revive cryopreserved cells.
- **When to use it:** Use this when the experiment includes Cell Revival.
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `cell_cryopreservation`, `protein_extraction`, `lentiviral_transduction`, `lentivirus_transduction_gene`, `plate_cloning` and others.
- **Usual downstream:** `cell_culture`, `cell_cryopreservation`, `protein_extraction`, `lentiviral_transduction`, `lentivirus_transduction_gene`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`

### EdU Incorporation Assay (`edu`)
- **Type:** Experiment step
- **What it does:** Run EdU incorporation on a 24-well plate; set cells/well and configure well cell materials.
- **When to use it:** Use this when the experiment includes EdU Incorporation Assay.
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `brdu_edu_quantification`.
- **Usual upstream:** `cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **Usual downstream:** `cell_culture`, `brdu_edu_quantification`

### Lentiviral Packaging (Three-Plasmid) (`lentiviral_transduction`)
- **Type:** Experiment step
- **What it does:** Package lentiviral vectors (three-plasmid); cells from revival/culture; plasmids from extraction or inventory.
- **When to use it:** Use this when the experiment includes Lentiviral Packaging (Three-Plasmid).
- **What you get:** The product of this step. It can usually continue to: `lentivirus_cryopreservation`, `lentivirus_transduction_gene`.
- **Usual upstream:** `cell_revival`, `cell_culture`, `plasmid_extraction`
- **Usual downstream:** `lentivirus_cryopreservation`, `lentivirus_transduction_gene`

### Lentiviral Packaging (Two-Plasmid) (`lentiviral_transduction_two_plasmid`)
- **Type:** Experiment step
- **What it does:** Package lentiviral vectors (two-plasmid); cells from revival/culture; plasmids from extraction or inventory.
- **When to use it:** Use this when the experiment includes Lentiviral Packaging (Two-Plasmid).
- **What you get:** The product of this step. It can usually continue to: `lentivirus_cryopreservation`, `lentivirus_transduction_gene`.
- **Usual upstream:** `cell_revival`, `cell_culture`, `plasmid_extraction`
- **Usual downstream:** `lentivirus_cryopreservation`, `lentivirus_transduction_gene`

### Recombinant Lentivirus Cryopreservation (`lentivirus_cryopreservation`)
- **Type:** Experiment step
- **What it does:** Cryopreserve viral supernatant from upstream lentiviral packaging.
- **When to use it:** Use this when the experiment includes Recombinant Lentivirus Cryopreservation.
- **What you get:** The product of this step. In the current list this is often an end step, or it continues to a result-analysis node.
- **Usual upstream:** `lentiviral_transduction`, `lentiviral_transduction_two_plasmid`

### Gene Transduction (Lentivirus) (`lentivirus_transduction_gene`)
- **Type:** Experiment step
- **What it does:** Transduce cells with recombinant lentivirus; cells from revival/culture; virus from upstream or inventory.
- **When to use it:** Use this when the experiment includes Gene Transduction (Lentivirus).
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `cell_cryopreservation`, `protein_extraction`, `plate_cloning`, `mtt`, `transwell` and others.
- **Usual upstream:** `cell_revival`, `cell_culture`, `lentiviral_transduction`, `lentiviral_transduction_two_plasmid`, `transient_transfection`, `lentivirus_transduction_gene`
- **Usual downstream:** `cell_culture`, `cell_cryopreservation`, `protein_extraction`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`, `lentivirus_transduction_gene`

### Dual-Luciferase Reporter Assay (`luciferase`)
- **Type:** Experiment step
- **What it does:** 96-well dual-luciferase reporter assay with per-well plasmid configuration.
- **When to use it:** Use this when the experiment includes Dual-Luciferase Reporter Assay.
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `luciferase_quantitative_analysis`.
- **Usual upstream:** `cell_revival`, `cell_culture`, `plasmid_extraction`
- **Usual downstream:** `cell_culture`, `luciferase_quantitative_analysis`

### Cell Viability/Proliferation Assay (MTT) (`mtt`)
- **Type:** Experiment step
- **What it does:** MTT assay on a 96-well plate: cells/well, assay days, and well cell materials.
- **When to use it:** Use this when the experiment includes Cell Viability/Proliferation Assay (MTT).
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `mtt_quantification`.
- **Usual upstream:** `cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **Usual downstream:** `cell_culture`, `mtt_quantification`

### Plasmid Amplification Culture (`plasmid_amplification`)
- **Type:** Experiment step
- **What it does:** Amplify plasmids in transformed bacterial cultures.
- **When to use it:** Use this when the experiment includes Plasmid Amplification Culture.
- **What you get:** The product of this step. It can usually continue to: `plasmid_extraction`, `transformation`, `strain_cryopreservation`.
- **Usual upstream:** `transformation`
- **Usual downstream:** `plasmid_extraction`, `transformation`, `strain_cryopreservation`

### Colony Formation Assay (`plate_cloning`)
- **Type:** Experiment step
- **What it does:** Colony formation on a 6-well plate: set cells/well, culture days, and upstream cell material per well.
- **When to use it:** Use this when the experiment includes Colony Formation Assay.
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `plate_cloning_quantification`.
- **Usual upstream:** `cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **Usual downstream:** `cell_culture`, `plate_cloning_quantification`

### Strain Cryopreservation (`strain_cryopreservation`)
- **Type:** Experiment step
- **What it does:** Cryopreserve transformed or amplified bacterial strains.
- **When to use it:** Use this when the experiment includes Strain Cryopreservation.
- **What you get:** The product of this step. In the current list this is often an end step, or it continues to a result-analysis node.
- **Usual upstream:** `plasmid_amplification`

### Transformation (`transformation`)
- **Type:** Experiment step
- **What it does:** Transform recombinant plasmids into competent cells.
- **When to use it:** Use this when the experiment includes Transformation.
- **What you get:** The product of this step. It can usually continue to: `plasmid_amplification`.
- **Usual upstream:** `plasmid_construction`
- **Usual downstream:** `plasmid_amplification`

### Transient Transfection (`transient_transfection`)
- **Type:** Experiment step
- **What it does:** Transient transfection in culture dishes; plasmids from extraction or inventory; volumes in μL (validation ×6).
- **When to use it:** Use this when the experiment includes Transient Transfection.
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `cell_cryopreservation`, `protein_extraction`, `plate_cloning`, `mtt`, `transwell` and others.
- **Usual upstream:** `cell_revival`, `cell_culture`, `plasmid_extraction`
- **Usual downstream:** `cell_culture`, `cell_cryopreservation`, `protein_extraction`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`

### Migration/Invasion Assay (Transwell) (`transwell`)
- **Type:** Experiment step
- **What it does:** Transwell assay on a 24-well plate: optional Matrigel, cells/well, and upstream cell materials.
- **When to use it:** Use this when the experiment includes Migration/Invasion Assay (Transwell).
- **What you get:** The product of this step. It can usually continue to: `cell_culture`, `transwell_quantification`.
- **Usual upstream:** `cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **Usual downstream:** `cell_culture`, `transwell_quantification`

## Control Flow

### Conditional Routing (`conditional_router`)
- **Type:** Flow control
- **What it does:** Route to different branches based on upstream outputs. One default output; multiple named outputs can be configured.
- **When to use it:** Use this when the workflow should follow different paths based on a result or threshold.
- **What you get:** Sends the workflow down different branches. Set each branch rule after import.
- **Usual upstream:** `*`
- **Usual downstream:** `*`

### Loop Control (`loop_control`)
- **Type:** Flow control
- **What it does:** Mark a workflow segment to repeat; loop count is for display/estimate and does not change execution itself.
- **When to use it:** Use this when a stretch of steps should repeat instead of being copied many times on the canvas.
- **What you get:** Marks a repeatable section. Set the repeat count and range after import.
- **Usual upstream:** `*`
- **Usual downstream:** `*`

## Detection Analysis

### ELISA Quantification (`elisa_quantification`)
- **Type:** Result analysis
- **What it does:** Group wells and quantify ELISA OD results.
- **When to use it:** Use this after the upstream assay, when you need the ELISA Quantification result.
- **What you get:** A quantitative result, such as fold change or a p value, which can be used by conditional routing.
- **Usual upstream:** `elisa_detection`
- **Usual downstream:** `conditional_router`

## Molecular Biology

### Next-Generation Sequencing (`next_generation_sequencing`)
- **Type:** Experiment step
- **What it does:** Takes nucleic acid outputs from upstream RT-PCR or RIP-seq and selects sequencing purpose; terminal step with no downstream.
- **When to use it:** Use this when the experiment includes Next-Generation Sequencing.
- **What you get:** The product of this step. In the current list this is often an end step, or it continues to a result-analysis node.
- **Usual upstream:** `rt_pcr`, `rip_seq`

### Nucleic Acid Cryopreservation (`nucleic_acid_cryopreservation`)
- **Type:** Experiment step
- **What it does:** Cryopreserve nucleic acid samples from extraction.
- **When to use it:** Use this when the experiment includes Nucleic Acid Cryopreservation.
- **What you get:** The product of this step. In the current list this is often an end step, or it continues to a result-analysis node.
- **Usual upstream:** `nucleic_acid_extraction`

### Nucleic Acid Extraction (`nucleic_acid_extraction`)
- **Type:** Experiment step
- **What it does:** Extract nucleic acids from upstream cell samples.
- **When to use it:** Use this when the experiment includes Nucleic Acid Extraction.
- **What you get:** The product of this step. It can usually continue to: `nucleic_acid_cryopreservation`, `rt_pcr`.
- **Usual upstream:** `cell_revival`, `cell_culture`
- **Usual downstream:** `nucleic_acid_cryopreservation`, `rt_pcr`

### Nucleotide Sequence Synthesis (`nucleotide_synthesis`)
- **Type:** Experiment step
- **What it does:** Design and synthesize primers/sequences. Unused products can be auto-saved to inventory.
If this node has no downstream, all products are cryopreserved at 500 ng/μL.
Note: if Flag-tagged, include the tag sequence when designing.
- **When to use it:** Use this when the experiment includes Nucleotide Sequence Synthesis.
- **What you get:** The product of this step. It can usually continue to: `plasmid_construction`, `conditional_router`, `qpcr`.
- **Usual downstream:** `plasmid_construction`, `conditional_router`, `qpcr`

### Recombinant Plasmid Construction (`plasmid_construction`)
- **Type:** Experiment step
- **What it does:** Build recombinant plasmids by molecular cloning.
- **When to use it:** Use this when the experiment includes Recombinant Plasmid Construction.
- **What you get:** The product of this step. It can usually continue to: `protein_extraction`, `transformation`.
- **Usual upstream:** `nucleotide_synthesis`, `conditional_router`, `loop_control`
- **Usual downstream:** `protein_extraction`, `transformation`

### Plasmid Cryopreservation (`plasmid_cryopreservation`)
- **Type:** Experiment step
- **What it does:** Cryopreserve extracted plasmid DNA.
- **When to use it:** Use this when the experiment includes Plasmid Cryopreservation.
- **What you get:** The product of this step. In the current list this is often an end step, or it continues to a result-analysis node.
- **Usual upstream:** `plasmid_extraction`

### Plasmid Extraction (`plasmid_extraction`)
- **Type:** Experiment step
- **What it does:** Extract plasmid DNA from amplified culture.
- **When to use it:** Use this when the experiment includes Plasmid Extraction.
- **What you get:** The product of this step. It can usually continue to: `plasmid_cryopreservation`, `lentiviral_transduction`, `lentiviral_transduction_two_plasmid`, `transient_transfection`, `luciferase`, `co_ip` and others.
- **Usual upstream:** `plasmid_amplification`
- **Usual downstream:** `plasmid_cryopreservation`, `lentiviral_transduction`, `lentiviral_transduction_two_plasmid`, `transient_transfection`, `luciferase`, `co_ip`, `rip_seq`

### Protein Cryopreservation (`protein_cryopreservation`)
- **Type:** Experiment step
- **What it does:** Cryopreserve extracted proteins.
- **When to use it:** Use this when the experiment includes Protein Cryopreservation.
- **What you get:** The product of this step. In the current list this is often an end step, or it continues to a result-analysis node.
- **Usual upstream:** `protein_extraction`

### Protein Extraction (`protein_extraction`)
- **Type:** Experiment step
- **What it does:** Extract proteins (animal protein workflows).
- **When to use it:** Use this when the experiment includes Protein Extraction.
- **What you get:** The product of this step. It can usually continue to: `protein_denaturation`, `protein_cryopreservation`.
- **Usual upstream:** `cell_revival`, `cell_culture`
- **Usual downstream:** `protein_denaturation`, `protein_cryopreservation`

### Quantitative Real-Time PCR (qPCR) (`qpcr`)
- **Type:** Experiment step
- **What it does:** qPCR using cDNA templates and primers with a user-defined amplification program on a 96-well plate.
- **When to use it:** Use this when the experiment includes Quantitative Real-Time PCR (qPCR).
- **What you get:** The product of this step. It can usually continue to: `qpcr_quantification`.
- **Usual upstream:** `rt_pcr`, `nucleotide_synthesis`
- **Usual downstream:** `qpcr_quantification`

### RNA Immunoprecipitation Sequencing (RIP-seq) (`rip_seq`)
- **Type:** Experiment step
- **What it does:** RNA immunoprecipitation sequencing (RIP-seq): supports endogenous/exogenous modes; outputs enriched nucleic acids for NGS.
- **When to use it:** Use this when the experiment includes RNA Immunoprecipitation Sequencing (RIP-seq).
- **What you get:** The product of this step. It can usually continue to: `next_generation_sequencing`.
- **Usual upstream:** `cell_revival`, `cell_culture`, `plasmid_extraction`
- **Usual downstream:** `next_generation_sequencing`

### Reverse Transcription PCR (RT-PCR) (`rt_pcr`)
- **Type:** Experiment step
- **What it does:** Perform RT-PCR on nucleic acid samples and output reverse-transcribed products.
- **When to use it:** Use this when the experiment includes Reverse Transcription PCR (RT-PCR).
- **What you get:** The product of this step. It can usually continue to: `qpcr`, `next_generation_sequencing`.
- **Usual upstream:** `nucleic_acid_extraction`
- **Usual downstream:** `qpcr`, `next_generation_sequencing`

## Proteomics

### Co-Immunoprecipitation (Co-IP) (`co_ip`)
- **Type:** Experiment step
- **What it does:** Study protein–protein interactions via Co-IP (endogenous or tagged overexpression).
- **When to use it:** Use this when the experiment includes Co-Immunoprecipitation (Co-IP).
- **What you get:** The product of this step. It can usually continue to: `protein_denaturation`.
- **Usual upstream:** `cell_revival`, `cell_culture`, `plasmid_extraction`
- **Usual downstream:** `protein_denaturation`

### ELISA Assay (`elisa_detection`)
- **Type:** Experiment step
- **What it does:** Configure ELISA on a 96-well plate: pick upstream co-culture wells as samples and set analyte/detection parameters.
- **When to use it:** Use this when the experiment includes ELISA Assay.
- **What you get:** The product of this step. It can usually continue to: `elisa_quantification`.
- **Usual upstream:** `cell_co_culture`
- **Usual downstream:** `elisa_quantification`

### Plate Reader Luminescence (`plate_reader_luminescence`)
- **Type:** Experiment step
- **What it does:** Luminescence readout on upstream co-culture 96-well plate; optional per-well luminescence substrate.
- **When to use it:** Use this when the experiment includes Plate Reader Luminescence.
- **What you get:** The product of this step. In the current list this is often an end step, or it continues to a result-analysis node.
- **Usual upstream:** `cell_co_culture`

### Protein Denaturation (`protein_denaturation`)
- **Type:** Experiment step
- **What it does:** Denature extracted proteins.
- **When to use it:** Use this when the experiment includes Protein Denaturation.
- **What you get:** The product of this step. It can usually continue to: `western_blot`.
- **Usual upstream:** `protein_extraction`
- **Usual downstream:** `western_blot`

### Western Blot (`western_blot`)
- **Type:** Experiment step
- **What it does:** Western blot with customizable target protein range and independent well configuration (up to 10 wells).
- **When to use it:** Use this when the experiment includes Western Blot.
- **What you get:** The product of this step. It can usually continue to: `western_blot_quantification`.
- **Usual downstream:** `western_blot_quantification`
