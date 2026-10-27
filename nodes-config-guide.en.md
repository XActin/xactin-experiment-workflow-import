# How to fill each XActin experiment node

After you import the nodes, open them from upstream to downstream and fill the form.
The assistant should turn these fields into instructions for this specific experiment.

## Assay & Analysis

### BrdU/EdU Incorporation Quantification (`brdu_edu_quantification`)

**Suggested order**
1. On the canvas, click BrdU/EdU Incorporation Quantification and open its form.
2. Fill the required items first: Quantification analysis configuration.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; Cell material from upstream BrdU/EdU incorporation experiment (auto-fetched) | No | — | — |
| 24-well plate configuration | Choose an output from the upstream node; 24-well plate configuration from upstream experiment (auto-fetched) | No | — | — |
| Cells per well | Choose an output from the upstream node; Cells per well set by upstream experiment (auto-fetched) | No | — | — |
| Quantification analysis configuration | Fill in as the form indicates; Group and analysis task configuration | Yes | Default: {'groups': [], 'analyses': []} | — |

### Dual-Luciferase Reporter Quantification (`luciferase_quantitative_analysis`)

**Suggested order**
1. On the canvas, click Dual-Luciferase Reporter Quantification and open its form.
2. Fill the required items first: Quantification analysis configuration.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; Select cell material from dual-luciferase reporter assay output | No | — | — |
| Well configuration | Choose an output from the upstream node; 96-well plate configuration from upstream experiment (auto-fetched) | No | — | — |
| Cells per well | Choose an output from the upstream node; Cells per well set by upstream experiment (auto-fetched) | No | — | — |
| Analysis notes | Enter text | No | — | — |
| Quantification analysis configuration | Set the luciferase analysis; Group and analysis task configuration | Yes | Default: {'groups': [], 'analyses': []} | — |

### MTT Viability/Proliferation Quantification (`mtt_quantification`)

**Suggested order**
1. On the canvas, click MTT Viability/Proliferation Quantification and open its form.
2. Fill the required items first: Quantification analysis configuration.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; Cell material from MTT experiment (auto-fetched) | No | — | — |
| 96-well plate configuration | Choose an output from the upstream node; 96-well plate configuration from upstream experiment (auto-fetched) | No | — | — |
| Cells per well | Choose an output from the upstream node; Cells per well set by upstream experiment (auto-fetched) | No | — | — |
| Assay days | Choose an output from the upstream node; Assay days set by upstream experiment (auto-fetched) | No | — | — |
| Quantification analysis configuration | Fill in as the form indicates; Group and analysis task configuration | Yes | Default: {'groups': [], 'analyses': []} | — |

### Colony Formation Quantification (`plate_cloning_quantification`)

**Suggested order**
1. On the canvas, click Colony Formation Quantification and open its form.
2. Fill the required items first: Quantification analysis configuration.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; Cell material from colony formation experiment (auto-fetched) | No | — | — |
| 6-well plate configuration | Choose an output from the upstream node; 6-well plate configuration from upstream experiment (auto-fetched) | No | — | — |
| Cells per well | Choose an output from the upstream node; Cells per well set by upstream experiment (auto-fetched) | No | — | — |
| Culture days | Choose an output from the upstream node; Culture days set by upstream experiment (auto-fetched) | No | — | — |
| Quantification analysis configuration | Fill in as the form indicates; Group and analysis task configuration | Yes | Default: {'groups': [], 'analyses': []} | — |

### qPCR Quantification Analysis (`qpcr_quantification`)

**Suggested order**
1. On the canvas, click qPCR Quantification Analysis and open its form.
2. Fill the required items first: Quantification analysis configuration.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| qPCR experiment results | Choose an output from the upstream node; Ct data from upstream qPCR experiment (auto-fetched) | No | — | — |
| 96-well plate configuration | Choose an output from the upstream node; 96-well plate configuration from upstream qPCR experiment (auto-fetched) | No | — | — |
| Amplification program | Choose an output from the upstream node; Amplification program settings from upstream qPCR node (auto-fetched) | No | — | — |
| Quantification analysis configuration | Set the qPCR analysis; Group upstream qPCR 96-well plate and configure analysis tasks (normalization + statistical method + blank/control… | Yes | Default: {'groups': [], 'analyses': []} | — |

### Transwell Migration/Invasion Quantification (`transwell_quantification`)

**Suggested order**
1. On the canvas, click Transwell Migration/Invasion Quantification and open its form.
2. Fill the required items first: Quantification analysis configuration.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; Cell material from Transwell experiment (auto-fetched) | No | — | — |
| 24-well plate configuration | Choose an output from the upstream node; 24-well plate configuration from upstream experiment (auto-fetched) | No | — | — |
| Cells per well | Choose an output from the upstream node; Cells per well set by upstream experiment (auto-fetched) | No | — | — |
| Add Matrigel | Choose an output from the upstream node; Whether upstream experiment added Matrigel in the upper chamber (auto-fetched) | No | — | — |
| Quantification analysis configuration | Set the Transwell analysis; Group and analysis task configuration | Yes | Default: {'groups': [], 'analyses': []} | — |

### Western Blot Quantification (`western_blot_quantification`)

**Suggested order**
1. On the canvas, click Western Blot Quantification and open its form.
2. Fill the required items first: Analysis task list.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Analysis task list | Set the analysis list; Configure one or more quantification analysis tasks; each task can select different target protein, reference prot… | Yes | — | — |

## Cell Biology

### BrdU Incorporation Assay (`brdu`)

**Suggested order**
1. On the canvas, click BrdU Incorporation Assay and open its form.
2. Fill the required items first: Cells per well.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cells per well | Enter a number; Cells seeded per well (positive integer) | Yes | Unit: pcs; Default: 100000; Min: 1 | — |
| 24-well plate configuration | Set up the 24-well plate; Click to open dialog and select upstream cell material for each well | No | — | — |

### Cell Co-culture (`cell_co_culture`)

**Suggested order**
1. On the canvas, click Cell Co-culture and open its form.
2. Fill the required items first: Culture plate type, Well plate cell configuration, Co-culture duration, Culture medium type, Fetal bovine serum (FBS), L-Glutamine, Penicillin-Streptomycin.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Culture plate type | Choose from the list; Select plate format, then configure co-culture cells per well | Yes | 6-well plate; 12-well plate; 24-well plate; 96-well plate | — |
| Well plate cell configuration | Set up the co-culture plate; Configure at least 1 well; up to 5 cell types per well via Add cell material | Yes | — | — |
| Co-culture duration | Enter a number; Co-culture duration in hours (positive integer) | Yes | Unit: hour(s); Default: 24; Min: 1 | — |
| Culture medium type | Choose from the list | Yes | DMEM; RPMI-1640; F12 | — |
| Advanced medium settings | Tick if it applies; Expand optional FBS, L-glutamine and Penicillin-Streptomycin settings | No | Default: False | — |
| Fetal bovine serum (FBS) | Enter a number | Yes | Unit: %; Default: 10; Min: 0; Max: 100 | Shown when medium_advanced_config is True |
| L-Glutamine | Enter a number | Yes | Unit: mM; Default: 2; Min: 0; Max: 100 | Shown when medium_advanced_config is True |
| Penicillin-Streptomycin | Enter a number | Yes | Unit: %; Default: 1; Min: 0; Max: 100 | Shown when medium_advanced_config is True |

### Cell Cryopreservation (`cell_cryopreservation`)

**Suggested order**
1. On the canvas, click Cell Cryopreservation and open its form.
2. Fill the required items first: Cell sample, Select cryopreservation quantity.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell sample | Choose an output from the upstream node; Select cell samples to cryopreserve | Yes | — | — |
| Select cryopreservation quantity | Enter a number | Yes | Unit: vial(s); Default: 1; Min: 1 | — |

### Cell Culture (`cell_culture`)

**Suggested order**
1. On the canvas, click Cell Culture and open its form.
2. Fill the required items first: Cell sample, Select cell quantity, Culture medium type, Fetal bovine serum (FBS), L-Glutamine, Penicillin-Streptomycin, Passage number, Passage dish count (100 mm cell culture dish).
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell sample | Choose an output from the upstream node; Select revived cell sample | Yes | — | — |
| Select cell quantity | Enter a number | Yes | Unit: dish(es); Default: 1; Min: 1 | — |
| Culture medium type | Choose from the list | Yes | DMEM; RPMI-1640; F12 | — |
| Advanced medium settings | Tick if it applies; Expand optional FBS, L-glutamine and Penicillin-Streptomycin settings | No | Default: False | — |
| Fetal bovine serum (FBS) | Enter a number; Final FBS concentration as integer percent | Yes | Unit: %; Default: 10; Min: 0; Max: 100 | Shown when medium_advanced_config is True |
| L-Glutamine | Enter a number; Final L-glutamine concentration as integer mM | Yes | Unit: mM; Default: 2; Min: 0; Max: 100 | Shown when medium_advanced_config is True |
| Penicillin-Streptomycin | Enter a number; Final penicillin-streptomycin concentration as integer percent | Yes | Unit: %; Default: 1; Min: 0; Max: 100 | Shown when medium_advanced_config is True |
| Passage number | Enter a number | Yes | Unit: passage(s); Default: 1; Min: 1; Max: 5 | — |
| Passage dish count (100 mm cell culture dish) | Enter a number | Yes | Unit: dish(es); Default: 2; Min: 1; Max: 4 | — |

### Cell Revival (`cell_revival`)

**Suggested order**
1. On the canvas, click Cell Revival and open its form.
2. Fill the required items first: Cell sample, Select cell quantity, Culture medium type, Fetal bovine serum (FBS), L-Glutamine, Penicillin-Streptomycin.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell sample | Choose from your material library; Select cell sample from inventory | Yes | — | — |
| Select cell quantity | Enter a number | Yes | Unit: vial(s); Default: 1; Min: 1 | — |
| Culture medium type | Choose from the list | Yes | DMEM; RPMI-1640; F12 | — |
| Advanced medium settings | Tick if it applies; Expand optional FBS, L-glutamine and Penicillin-Streptomycin settings | No | Default: False | — |
| Fetal bovine serum (FBS) | Enter a number; Final FBS concentration as integer percent | Yes | Unit: %; Default: 10; Min: 0; Max: 100 | Shown when medium_advanced_config is True |
| L-Glutamine | Enter a number; Final L-glutamine concentration as integer mM | Yes | Unit: mM; Default: 2; Min: 0; Max: 100 | Shown when medium_advanced_config is True |
| Penicillin-Streptomycin | Enter a number; Final penicillin-streptomycin concentration as integer percent | Yes | Unit: %; Default: 1; Min: 0; Max: 100 | Shown when medium_advanced_config is True |

### EdU Incorporation Assay (`edu`)

**Suggested order**
1. On the canvas, click EdU Incorporation Assay and open its form.
2. Fill the required items first: Cells per well.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cells per well | Enter a number; Cells seeded per well (positive integer) | Yes | Unit: pcs; Default: 100000; Min: 1 | — |
| 24-well plate configuration | Set up the 24-well plate; Click to open dialog and select upstream cell material for each well | No | — | — |

### Lentiviral Packaging (Three-Plasmid) (`lentiviral_transduction`)

**Suggested order**
1. On the canvas, click Lentiviral Packaging (Three-Plasmid) and open its form.
2. Fill the required items first: Cell material, Target plasmid (select and amount; more than one allowed), Packaging plasmid pLP/VSVG, Packaging plasmid pLP1, Packaging plasmid pLP2.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; From upstream cell revival or cell culture node | Yes | — | — |
| Cell material usage quantity | Enter a number; Number of dishes used; when selecting upstream, cannot exceed upstream available quantity. Each plasmid usage = base usag… | No | Unit: dish(es); Default: 1 | — |
| Target plasmid (select and amount; more than one allowed) | Choose from your material library; Choose the transfer or target plasmid from your library | Yes | Add each target plasmid and its amount in the form | — |
| Packaging plasmid pLP/VSVG | Choose from your material library; Select from upstream plasmid extraction node or material inventory (PLASMID plasmid material); availab… | Yes | — | — |
| Packaging plasmid pLP1 | Choose from your material library; Select from upstream plasmid extraction node or material inventory (PLASMID plasmid material); availab… | Yes | — | — |
| Packaging plasmid pLP2 | Choose from your material library; Select from upstream plasmid extraction node or material inventory (PLASMID plasmid material); availab… | Yes | — | — |

### Lentiviral Packaging (Two-Plasmid) (`lentiviral_transduction_two_plasmid`)

**Suggested order**
1. On the canvas, click Lentiviral Packaging (Two-Plasmid) and open its form.
2. Fill the required items first: Cell material, Target plasmid (select and amount; more than one allowed), Packaging plasmid pMD2.G, Packaging plasmid psPAX2.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; From upstream cell revival or cell culture node | Yes | — | — |
| Cell material usage quantity | Enter a number; Number of dishes used; when selecting upstream, cannot exceed upstream available quantity. Each plasmid usage = base usag… | No | Unit: dish(es); Default: 1 | — |
| Target plasmid (select and amount; more than one allowed) | Choose from your material library; Choose the transfer or target plasmid from your library | Yes | Add each target plasmid and its amount in the form | — |
| Packaging plasmid pMD2.G | Choose from your material library; Select from upstream plasmid extraction node or material inventory (PLASMID plasmid material); availab… | Yes | — | — |
| Packaging plasmid psPAX2 | Choose from your material library; Select from upstream plasmid extraction node or material inventory (PLASMID plasmid material); availab… | Yes | — | — |

### Recombinant Lentivirus Cryopreservation (`lentivirus_cryopreservation`)

**Suggested order**
1. On the canvas, click Recombinant Lentivirus Cryopreservation and open its form.
2. Fill the required items first: Viral supernatant material, Cryopreservation quantity of viral supernatant.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Viral supernatant material | Choose an output from the upstream node; From upstream lentiviral packaging node | Yes | — | — |
| Cryopreservation quantity of viral supernatant | Enter a number; Cryopreservation quantity; when selecting upstream material, cannot exceed upstream available quantity | Yes | Unit: vial(s); Default: 1; Min: 1 | — |

### Gene Transduction (Lentivirus) (`lentivirus_transduction_gene`)

**Suggested order**
1. On the canvas, click Gene Transduction (Lentivirus) and open its form.
2. Fill the required items first: Cell material, Cell material usage volume, Recombinant lentivirus material, Virus volume per well.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; From upstream cell revival or cell culture node only | Yes | — | — |
| Cell material usage volume | Enter a number | Yes | Unit: dish(es); Default: 1; Min: 1 | — |
| Recombinant lentivirus material | Choose from your material library; From upstream lentiviral packaging/cryopreservation node or material inventory (virus material) | Yes | — | — |
| Virus volume per well | Enter a number | Yes | Unit: tube(s); Default: 1; Min: 1 | — |
| Selection drug | Choose from the list | No | Puro-Puromycin | — |

### Dual-Luciferase Reporter Assay (`luciferase`)

**Suggested order**
1. On the canvas, click Dual-Luciferase Reporter Assay and open its form.
2. Fill the required items first: Cell material, Cells per well.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; Select cells for dual-luciferase reporter assay (from upstream node) | Yes | — | — |
| Cells per well | Enter a number; Number of cells seeded in each well of a 96-well plate | Yes | Unit: pcs; Default: 10000; Min: 100 | — |
| 96-well plate configuration | Set up the 96-well plate; Configure plasmid scheme per well in 96-well plate; click button below to open configuration dialog | No | — | — |

### Cell Viability/Proliferation Assay (MTT) (`mtt`)

**Suggested order**
1. On the canvas, click Cell Viability/Proliferation Assay (MTT) and open its form.
2. Fill the required items first: Cells per well, Assay days.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cells per well | Enter a number; Cells seeded per well (positive integer) | Yes | Unit: pcs; Default: 1000; Min: 1 | — |
| Assay days | Enter a number; Assay days (5–7 days, positive integer) | Yes | Unit: day(s); Default: 5; Min: 5; Max: 7 | — |
| 96-well plate configuration | Set up the 96-well plate; Configure 96-well plate cell materials; outer ring (rows A/H, columns 1/12) fixed as PBS fill. | No | — | — |

### Plasmid Amplification Culture (`plasmid_amplification`)

**Suggested order**
1. On the canvas, click Plasmid Amplification Culture and open its form.
2. Fill the required items first: Transformed colony, Antibiotic, Number of transformed colonies used, Number of culture flasks used.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Transformed colony | Choose from your material library; With upstream [Transformation] connection, only upstream transformed colonies are shown; without upstr… | Yes | — | — |
| Antibiotic | Choose from the list; Select antibiotic matching plasmid resistance | Yes | Ampicillin; Kanamycin; Chloramphenicol; Tetracycline; Streptomycin | — |
| Number of transformed colonies used | Enter a number; Number of transformed colonies used; validate against upstream output when selecting upstream colonies, or available inve… | Yes | Unit: pcs; Default: 1; Min: 1 | — |
| Number of culture flasks used | Enter a number; Number of culture flasks used (1–10, integers only) | Yes | Unit: pcs; Default: 1; Min: 1; Max: 10 | — |

### Colony Formation Assay (`plate_cloning`)

**Suggested order**
1. On the canvas, click Colony Formation Assay and open its form.
2. Fill the required items first: Cells per well, Culture days.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cells per well | Enter a number; Cells seeded per well; must be a positive integer | Yes | Unit: pcs; Default: 1000; Min: 1 | — |
| Culture days | Enter a number; Colony formation culture days (5–10 days, positive integer) | Yes | Unit: day(s); Default: 7; Min: 5; Max: 10 | — |
| 6-well plate well configuration | Set up the 6-well plate; Click to open dialog and select upstream cell material for each well | No | — | — |

### Strain Cryopreservation (`strain_cryopreservation`)

**Suggested order**
1. On the canvas, click Strain Cryopreservation and open its form.
2. Fill the required items first: Strain sample, Select cryopreservation strain quantity.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Strain sample | Choose an output from the upstream node; Select strain samples to cryopreserve | Yes | — | — |
| Select cryopreservation strain quantity | Enter a number | Yes | Unit: vial(s); Default: 1; Min: 1 | — |
| Auto-cryopreserve remaining unused material | Tick if it applies; When checked, cryopreserve all remaining unused strains; when unchecked, specify cryopreservation quantity manually | No | Default: True | — |

### Transformation (`transformation`)

**Suggested order**
1. On the canvas, click Transformation and open its form.
2. Fill the required items first: Plasmid sample, Competent cells, Colonies picked for sequencing.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Plasmid sample | Choose an output from the upstream node; Select plasmid from upstream recombinant plasmid construction node | Yes | — | — |
| Competent cells | Choose from the list; Select competent cell type | Yes | DH5α | — |
| Colonies picked for sequencing | Enter a number; Number of test colonies picked | Yes | Unit: pcs; Default: 3; Min: 1; Max: 10 | — |

### Transient Transfection (`transient_transfection`)

**Suggested order**
1. On the canvas, click Transient Transfection and open its form.
2. Fill the required items first: Cell material, Target plasmid (select and amount; more than one allowed).
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; From upstream cell revival or cell culture node | Yes | — | — |
| Cell material usage quantity | Enter a number; Cell material dish count; when selecting upstream, cannot exceed available quantity. Cells deducted by selected count; ea… | No | Unit: dish(es); Default: 1 | — |
| Target plasmid (select and amount; more than one allowed) | Choose from your material library; Choose the transfer or target plasmid from your library | Yes | Add each target plasmid and its amount in the form | — |

### Migration/Invasion Assay (Transwell) (`transwell`)

**Suggested order**
1. On the canvas, click Migration/Invasion Assay (Transwell) and open its form.
2. Fill the required items first: Cells per well.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Add Matrigel | Tick if it applies; When checked, add Matrigel in Transwell upper chamber (for invasion assay) | No | Default: False | — |
| Cells per well | Enter a number; Cells seeded per well (positive integer) | Yes | Unit: pcs; Default: 200000; Min: 1 | — |
| 24-well plate configuration | Set up the 24-well plate; Click to open dialog and select upstream cell material for each well | No | — | — |

## Control Flow

### Conditional Routing (`conditional_router`)

**Suggested order**
1. On the canvas, click Conditional Routing and open its form.
3. Save, check the connections, then configure the next node.

This node is configured from the steps above.

### Loop Control (`loop_control`)

**Suggested order**
1. On the canvas, click Loop Control and open its form.
2. Fill the required items first: Maximum loop count.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Maximum loop count | Enter a number; Maximum number of loop iterations (1–5) | Yes | Default: 1; Min: 1; Max: 5 | — |

## Detection Analysis

### ELISA Quantification (`elisa_quantification`)

**Suggested order**
1. On the canvas, click ELISA Quantification and open its form.
2. Fill the required items first: ELISA quantification config.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| ELISA results | Choose an output from the upstream node; Select ELISA result data from upstream | No | — | — |
| Well plate configuration | Choose an output from the upstream node; Upstream 96-well layout for grouping | No | — | — |
| ELISA quantification config | Fill in as the form indicates; Assign blank/control/experimental groups and OD analyses | Yes | — | — |
| Analysis note | Enter text | No | — | — |

## Molecular Biology

### Next-Generation Sequencing (`next_generation_sequencing`)

**Suggested order**
1. On the canvas, click Next-Generation Sequencing and open its form.
2. Fill the required items first: Sequencing nucleic acid material, Sequencing purpose.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Sequencing nucleic acid material | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | Yes | — | — |
| Sequencing nucleic acid material 2 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 3 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 4 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 5 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 6 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 7 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 8 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 9 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 10 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 11 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 12 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 13 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 14 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 15 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing nucleic acid material 16 | Choose from your material library; Select nucleic acid material from upstream "Reverse transcription PCR (RT-PCR)" or "RIP-seq" node outp… | No | — | — |
| Sequencing purpose | Choose from the list; Select sequencing type or analysis purpose for this library (placeholder option; may link to ordering rules later). | Yes | RIP-Seq; RNA-Seq | — |

### Nucleic Acid Cryopreservation (`nucleic_acid_cryopreservation`)

**Suggested order**
1. On the canvas, click Nucleic Acid Cryopreservation and open its form.
2. Fill the required items first: Nucleic acid sample, Select cryopreservation nucleic acid volume.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Nucleic acid sample | Choose an output from the upstream node; Select nucleic acid samples to cryopreserve | Yes | — | — |
| Select cryopreservation nucleic acid volume | Enter a number | Yes | Unit: μL; Default: 0; Min: 1 | — |
| Freeze unused extracted nucleic acid | Tick if it applies; When checked, cryopreserve all remaining extracted nucleic acid; when unchecked, freeze by quantity above. | No | Default: True | — |

### Nucleic Acid Extraction (`nucleic_acid_extraction`)

**Suggested order**
1. On the canvas, click Nucleic Acid Extraction and open its form.
2. Fill the required items first: Cell sample, Select quantity.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell sample | Choose an output from the upstream node; Select cell samples for nucleic acid extraction | Yes | — | — |
| Select quantity | Enter a number | Yes | Unit: dish/plate; Default: 1; Min: 1 | — |

### Nucleotide Sequence Synthesis (`nucleotide_synthesis`)

**Suggested order**
1. On the canvas, click Nucleotide Sequence Synthesis and open its form.
2. Fill the required items first: Synthesis purpose, Target gene, Forward strand 3' UTR sequence, Reverse strand 3' UTR sequence, Type, 5' end restriction enzyme, 3' end restriction enzyme, Type.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Synthesis purpose | Choose from the list; Select purpose of nucleotide sequence | Yes | qPCR primers; Overexpression vector construction; Gene expression (pCDH); Knockdown vector construction (shRNA); Gene knock-out (CRISPR s… | — |
| Target gene | Search and select the target gene; Search and select target gene | Yes | — | — |
| Whether synthesized sequence contains Flag tag | Tick if it applies | No | Default: True | Shown when synthesis_purpose is overexpression_vector or overexpression or gene_expression_pcdh |
| Forward strand 3' UTR sequence | Enter a DNA sequence; Enter forward strand 3' UTR sequence, 5'→3' direction | Yes | — | Shown when synthesis_purpose is mirna_target_pmirglo |
| Reverse strand 3' UTR sequence | Enter a DNA sequence; Enter reverse strand 3' UTR sequence, 5'→3' direction | Yes | — | Shown when synthesis_purpose is mirna_target_pmirglo |
| Type | Choose one option; Select type; only one allowed | Yes | Wild type (WT); Mutant (MUT) | Shown when synthesis_purpose is mirna_target_pmirglo |
| 5' end restriction enzyme | Choose from the list; Select 5' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is mirna_target_pmirglo |
| 3' end restriction enzyme | Choose from the list; Select 3' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is mirna_target_pmirglo |
| Type | Choose one option; Select type; only one allowed | Yes | Wild type (WT); Mutant (MUT) | Shown when synthesis_purpose is lncrna_circrna_regulation_pmirglo |
| Target gene 3' UTR sequence | Enter a DNA sequence; Enter target gene 3' UTR sequence, 5'→3' direction | Yes | — | Shown when synthesis_purpose is lncrna_circrna_regulation_pmirglo |
| Target lncRNA/circRNA full-length sequence | Enter a DNA sequence; Enter target lncRNA/circRNA full-length sequence, 5'→3' direction | Yes | — | Shown when synthesis_purpose is lncrna_circrna_regulation_pmirglo |
| 5' end restriction enzyme | Choose from the list; Select 5' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is lncrna_circrna_regulation_pmirglo |
| 3' end restriction enzyme | Choose from the list; Select 3' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is lncrna_circrna_regulation_pmirglo |
| Target gene promoter full-length/truncation sequence | Enter a DNA sequence; Enter target gene promoter full-length/truncation sequence, 5'→3' direction | Yes | — | Shown when synthesis_purpose is lncrna_circrna_regulation_pgl3 |
| 5' end restriction enzyme | Choose from the list; Select 5' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is lncrna_circrna_regulation_pgl3 |
| 3' end restriction enzyme | Choose from the list; Select 3' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is lncrna_circrna_regulation_pgl3 |
| Tandem pathway response element sequence | Enter a DNA sequence; Enter tandem pathway response element sequence, 5'→3' direction, must include SV40 promoter sequence | Yes | — | Shown when synthesis_purpose is pathway_activity_pgl3 |
| 5' end restriction enzyme | Choose from the list; Select 5' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is pathway_activity_pgl3 |
| 3' end restriction enzyme | Choose from the list; Select 3' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is pathway_activity_pgl3 |
| Category | Choose one option; Select protein type; only one allowed | Yes | Bait protein; Prey protein | Shown when synthesis_purpose is protein_interaction_pgl3_gal4 |
| 5'→3' CDS sequence | Enter a DNA sequence; Enter CDS sequence, 5'→3' direction, without stop codon | Yes | — | Shown when synthesis_purpose is protein_interaction_pgl3_gal4 |
| 5' end restriction enzyme | Choose from the list; Select 5' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ; NdeⅠ | Shown when synthesis_purpose is protein_interaction_pgl3_gal4 |
| 3' end restriction enzyme | Choose from the list; Select 3' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is protein_interaction_pgl3_gal4 |
| Forward primer | Enter a DNA sequence | Yes | — | Shown when synthesis_purpose is pcr or qpcr |
| Reverse primer | Enter a DNA sequence | Yes | — | Shown when synthesis_purpose is pcr or qpcr |
| Forward strand sequence | Enter a DNA sequence | Yes | — | Shown when synthesis_purpose is overexpression_vector or interference_vector or gene_expression_pcdh |
| Reverse strand sequence | Enter a DNA sequence | Yes | — | Shown when synthesis_purpose is overexpression_vector or interference_vector or gene_expression_pcdh |
| Forward strand restriction enzyme | Choose from the list | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is overexpression_vector or interference_vector or gene_expression_pcdh |
| Reverse strand restriction enzyme | Choose from the list | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is overexpression_vector or interference_vector or gene_expression_pcdh |
| sgRNA target sequence (20 nt) | Enter a DNA sequence | Yes | — | Shown when synthesis_purpose is crispr_knockout or crispr_knockin |
| HDR repair template sequence | Enter a DNA sequence | Yes | — | Shown when synthesis_purpose is crispr_knockin |
| Full-length promoter and serial truncation nucleotide sequences | Enter a DNA sequence; Enter full-length promoter and serial truncation nucleotide sequences, 5'→3' direction | Yes | — | Shown when synthesis_purpose is promoter_activity_pgl3 |
| 5' end restriction enzyme | Choose from the list; Select 5' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is promoter_activity_pgl3 |
| 3' end restriction enzyme | Choose from the list; Select 3' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is promoter_activity_pgl3 |
| Forward strand 5'→3' sequence | Enter a DNA sequence; Enter forward strand sequence, 5'→3' direction | Yes | — | Shown when synthesis_purpose is cis_element_pgl3 |
| Reverse strand 5'→3' sequence | Enter a DNA sequence; Enter reverse strand sequence, 5'→3' direction | Yes | — | Shown when synthesis_purpose is cis_element_pgl3 |
| 5' end restriction enzyme | Choose from the list; Select 5' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is cis_element_pgl3 |
| 3' end restriction enzyme | Choose from the list; Select 3' end restriction enzyme | Yes | AgeⅠ; EcoRⅠ; BamHⅠ; XhoⅠ; XbaⅠ; HindⅢ; NotⅠ; SacⅠ; SalⅠ; SmaⅠ; KpnⅠ; BglⅡ; PstⅠ; EcoRⅤ; NheⅠ; ClaⅠ; SphⅠ; XmaⅠ | Shown when synthesis_purpose is cis_element_pgl3 |

### Recombinant Plasmid Construction (`plasmid_construction`)

**Suggested order**
1. On the canvas, click Recombinant Plasmid Construction and open its form.
2. Fill the required items first: Vector category, Vector plasmid, Oligonucleotide sequence.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Vector category | Choose from the list; Select vector plasmid category | Yes | Overexpression vector construction; Gene expression (pCDH); Knockdown vector construction (shRNA); Gene knock-out (CRISPR sgRNA); Gene kn… | — |
| Vector plasmid | Fill in as the form indicates; Select specific vector plasmid by vector category | Yes | — | — |
| Oligonucleotide sequence | Choose from your material library; Prefer upstream [Nucleotide sequence synthesis] node; if no upstream connection, select existing synth… | Yes | — | — |

### Plasmid Cryopreservation (`plasmid_cryopreservation`)

**Suggested order**
1. On the canvas, click Plasmid Cryopreservation and open its form.
2. Fill the required items first: Plasmid sample, Select cryopreservation plasmid volume.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Plasmid sample | Choose an output from the upstream node; Select plasmid samples to cryopreserve | Yes | — | — |
| Select cryopreservation plasmid volume | Enter a number | Yes | Unit: μL; Default: 10; Min: 1 | — |
| Auto-cryopreserve remaining unused material | Tick if it applies; When checked, cryopreserve all remaining unused plasmids; when unchecked, specify cryopreservation quantity manually | No | Default: True | — |

### Plasmid Extraction (`plasmid_extraction`)

**Suggested order**
1. On the canvas, click Plasmid Extraction and open its form.
2. Fill the required items first: Amplified culture, Culture volume to extract.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Amplified culture | Choose an output from the upstream node; Select bacterial culture from upstream plasmid amplification node | Yes | — | — |
| Culture volume to extract | Enter a number; Each unit represents 100 mL culture; positive integers only | Yes | Unit: X 100mL; Default: 1; Min: 1 | — |

### Protein Cryopreservation (`protein_cryopreservation`)

**Suggested order**
1. On the canvas, click Protein Cryopreservation and open its form.
2. Fill the required items first: Protein sample, Select cryopreservation protein volume.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Protein sample | Choose an output from the upstream node; Select protein samples to cryopreserve | Yes | — | — |
| Select cryopreservation protein volume | Enter a number | Yes | Unit: μL; Default: 0; Min: 1 | — |
| Cryopreserve all unused extracted protein | Tick if it applies; When checked, cryopreserve all unused extracted protein; when unchecked, specify cryopreservation volume manually | No | Default: True | — |

### Protein Extraction (`protein_extraction`)

**Suggested order**
1. On the canvas, click Protein Extraction and open its form.
2. Fill the required items first: Cell sample, Select quantity.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell sample | Choose an output from the upstream node; Select samples for protein extraction | Yes | — | — |
| Select quantity | Enter a number | Yes | Unit: dish/plate; Default: 1; Min: 1 | — |

### Quantitative Real-Time PCR (qPCR) (`qpcr`)

**Suggested order**
1. On the canvas, click Quantitative Real-Time PCR (qPCR) and open its form.
2. Fill the required items first: qPCR amplification program settings.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| qPCR amplification program settings | Set the qPCR program; Customize qPCR amplification cycles: add/remove steps, add cycle ranges (select from end backward only); each range… | Yes | Default: {'steps': [{'id': 'step1', 'temperature': 95, 'duration': 30}, {'id': 'step2', 'temperature': 95, 'duration': 5}, {'id': 'step3'… | — |
| 96-well plate configuration | Set up the qPCR 96-well plate; Configure forward/reverse primers and cDNA template per well (supports inventory OLIGO and upstream nucleo… | No | — | — |

### RNA Immunoprecipitation Sequencing (RIP-seq) (`rip_seq`)

**Suggested order**
1. On the canvas, click RNA Immunoprecipitation Sequencing (RIP-seq) and open its form.
2. Fill the required items first: Cell material, Cell material usage volume, Protein source, Target plasmid (select and amount; more than one allowed).
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; Select cell material from upstream cell culture/revival node | Yes | — | — |
| Cell material usage volume | Enter a number; Cell material dish count (positive integer); cannot exceed upstream available quantity. Allocation validation deducts by … | Yes | Unit: dish(es); Default: 1; Min: 1 | — |
| Protein source | Choose from the list; Exogenous: enrich RNA-binding protein by transfecting tagged (FLAG/GFP/HA/MYC, etc.) overexpression vectors; select… | Yes | Exogenous; Endogenous | — |
| Target plasmid (select and amount; more than one allowed) | Choose from your material library; Choose the transfer or target plasmid from your library | Yes | Add each target plasmid and its amount in the form | — |

### Reverse Transcription PCR (RT-PCR) (`rt_pcr`)

**Suggested order**
1. On the canvas, click Reverse Transcription PCR (RT-PCR) and open its form.
2. Fill the required items first: Nucleic acid material selection, Nucleic acid material usage volume.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Nucleic acid material selection | Choose from your material library; From upstream nucleic acid extraction node or user inventory nucleic acid material | Yes | — | — |
| Nucleic acid material usage volume | Enter a number; Enter nucleic acid amount for reaction (material consumption = input × 2) | Yes | Unit: X2 μL; Default: 1; Min: 1 | — |
| Add reverse transcriptase | Tick if it applies; Whether to add reverse transcriptase in RT-PCR reaction | No | Default: True | — |

## Proteomics

### Co-Immunoprecipitation (Co-IP) (`co_ip`)

**Suggested order**
1. On the canvas, click Co-Immunoprecipitation (Co-IP) and open its form.
2. Fill the required items first: Cell material, Cell material usage volume, Protein source, Target plasmid (select and amount; more than one allowed).
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Cell material | Choose an output from the upstream node; Select cell material from upstream cell culture/revival node | Yes | — | — |
| Cell material usage volume | Enter a number; Cell material dish count (positive integer); cannot exceed upstream available quantity. Allocation validation deducts by … | Yes | Unit: dish(es); Default: 1; Min: 1 | — |
| Protein source | Choose from the list; Exogenous: overexpress protein of interest via tagged (FLAG/GFP/HA/MYC, etc.) vectors; select plasmid and enter usa… | Yes | Exogenous; Endogenous | — |
| Target plasmid (select and amount; more than one allowed) | Choose from your material library; Choose the transfer or target plasmid from your library | Yes | Add each target plasmid and its amount in the form | — |

### ELISA Assay (`elisa_detection`)

**Suggested order**
1. On the canvas, click ELISA Assay and open its form.
2. Fill the required items first: ELISA 96-well plate config.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| ELISA 96-well plate config | Set up the ELISA plate; Configure each 96-well: pick upstream well as cell sample source, then set analyte, wavelength and incubation. | Yes | — | — |

### Plate Reader Luminescence (`plate_reader_luminescence`)

**Suggested order**
1. On the canvas, click Plate Reader Luminescence and open its form.
2. Fill the required items first: Luminescence plate config, Measurement mode, Integration time, Gain, Post-substrate incubation.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Luminescence plate config | Fill in as the form indicates; Read upstream co-culture 96-well plate and configure substrate per well. Non-96 upstream plates cannot be … | Yes | — | — |
| Measurement mode | Choose from the list; Endpoint: single read; Kinetic: timed series | Yes | Endpoint; Kinetic | — |
| Integration time | Enter a number; Luminescence integration time | Yes | Unit: ms; Default: 1000; Min: 100; Max: 60000 | — |
| Gain | Enter a number; Detector gain (instrument-dependent) | Yes | Default: 100; Min: 1; Max: 1000 | — |
| Post-substrate incubation | Enter a number; Incubation after substrate before reading | Yes | Unit: min; Default: 10; Min: 0; Max: 120 | — |

### Protein Denaturation (`protein_denaturation`)

**Suggested order**
1. On the canvas, click Protein Denaturation and open its form.
2. Fill the required items first: Protein sample, Select protein volume for denaturation, Denaturation temperature, Denaturation time.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Protein sample | Choose from your material library; Select protein sample from upstream extraction | Yes | — | — |
| Select protein volume for denaturation | Enter a number | Yes | Unit: μL; Default: 1; Min: 1 | — |
| Denaturation temperature | Enter a number; Protein denaturation temperature; positive integers only | Yes | Unit: ℃; Default: 95; Min: 1 | — |
| Denaturation time | Enter a number; Protein denaturation time; positive integers only | Yes | Unit: min; Default: 5; Min: 0 | — |

### Western Blot (`western_blot`)

**Suggested order**
1. On the canvas, click Western Blot and open its form.
2. Fill the required items first: Protein per well (denatured protein normalized to 20 μg/μL), Gel type, Reference protein, Target protein, Well 1 protein sample, Well 2 protein sample.
3. Save, check the connections, then configure the next node.

**Form fields**

| Field | How to fill it | Required | Options or limits | When it appears |
|---|---|---|---|---|
| Protein per well (denatured protein normalized to 20 μg/μL) | Enter a number | Yes | Unit: μg; Default: 20; Min: 1; Max: 100 | — |
| Gel type | Fill in as the form indicates; Select gel type suitable for target protein molecular weight | Yes | — | — |
| Reference protein | Search and select the target gene; Select reference proteins for normalization; multi-select supported | Yes | — | — |
| Target protein | Search and select the target gene; Select target proteins for detection; multi-select supported | Yes | — | — |
| Well 1 protein sample | Choose an output from the upstream node; Required — select sample from upstream protein denaturation node | Yes | — | — |
| Well 2 protein sample | Choose an output from the upstream node; Required — select sample from upstream protein denaturation node | Yes | — | — |
| Well 3 protein sample | Choose an output from the upstream node; Select sample from upstream protein denaturation node | No | — | — |
| Well 4 protein sample | Choose an output from the upstream node; Select sample from upstream protein denaturation node | No | — | — |
| Well 5 protein sample | Choose an output from the upstream node; Select sample from upstream protein denaturation node | No | — | — |
| Well 6 protein sample | Choose an output from the upstream node; Select sample from upstream protein denaturation node | No | — | — |
| Well 7 protein sample | Choose an output from the upstream node; Select sample from upstream protein denaturation node | No | — | — |
| Well 8 protein sample | Choose an output from the upstream node; Select sample from upstream protein denaturation node | No | — | — |
| Well 9 protein sample | Choose an output from the upstream node; Select sample from upstream protein denaturation node | No | — | — |
| Well 10 protein sample | Choose an output from the upstream node; Select sample from upstream protein denaturation node | No | — | — |
