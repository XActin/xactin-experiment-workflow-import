# XActin 实验节点一览

根据你想做的实验，对照「做什么 / 何时用 / 能得到什么」选择节点。
生成导入 JSON 时使用对应的 `code`，并尽量按「常见上游 / 常见下游」来连接。

导入画布之后，各节点表单怎么填，请看 [nodes-config-guide.md](nodes-config-guide.md)。

## 分子生物学

### 二代测序（`next_generation_sequencing`）
- **类型**：实验步骤
- **做什么**：承接上游 RT-PCR 或 RIP-seq 的核酸产出，选择测序目的；流程终点，无下游节点。
- **何时选用**：实验方案里需要包含「二代测序」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出；在当前目录中多为流程终点，或需另接「检测分析」类节点
- **常见上游**：`rt_pcr`, `rip_seq`

### 核酸冻存（`nucleic_acid_cryopreservation`）
- **类型**：实验步骤
- **做什么**：对核酸提取得到的核酸样品进行冻存。
- **何时选用**：实验方案里需要包含「核酸冻存」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出；在当前目录中多为流程终点，或需另接「检测分析」类节点
- **常见上游**：`nucleic_acid_extraction`

### 核酸提取（`nucleic_acid_extraction`）
- **类型**：实验步骤
- **做什么**：从上游细胞样本中提取核酸。
- **何时选用**：实验方案里需要包含「核酸提取」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`nucleic_acid_cryopreservation`、`rt_pcr`
- **常见上游**：`cell_revival`, `cell_culture`
- **常见下游**：`nucleic_acid_cryopreservation`, `rt_pcr`

### 核苷酸序列合成（`nucleotide_synthesis`）
- **类型**：实验步骤
- **做什么**：核苷酸序列合成节点用于设计和合成各类引物/序列。合成后的序列可以直接使用剩余自动存入库存。
若该节点未连接任何下游节点则合成后全部冻存，浓度统一为：500ng/μL
注意：若勾选含有Flag标签，请在设计序列时添加上相应序列。
- **何时选用**：实验方案里需要包含「核苷酸序列合成」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`plasmid_construction`、`conditional_router`、`qpcr`
- **常见下游**：`plasmid_construction`, `conditional_router`, `qpcr`

### 重组质粒构建（`plasmid_construction`）
- **类型**：实验步骤
- **做什么**：通过分子克隆技术构建重组质粒
- **何时选用**：实验方案里需要包含「重组质粒构建」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`protein_extraction`、`transformation`
- **常见上游**：`nucleotide_synthesis`, `conditional_router`, `loop_control`
- **常见下游**：`protein_extraction`, `transformation`

### 质粒冻存（`plasmid_cryopreservation`）
- **类型**：实验步骤
- **做什么**：将提取的质粒DNA进行冻存保存
- **何时选用**：实验方案里需要包含「质粒冻存」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出；在当前目录中多为流程终点，或需另接「检测分析」类节点
- **常见上游**：`plasmid_extraction`

### 质粒提取（`plasmid_extraction`）
- **类型**：实验步骤
- **做什么**：从扩增培养的菌液中提取质粒DNA
- **何时选用**：实验方案里需要包含「质粒提取」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`plasmid_cryopreservation`、`lentiviral_transduction`、`lentiviral_transduction_two_plasmid`、`transient_transfection`、`luciferase`、`co_ip` 等
- **常见上游**：`plasmid_amplification`
- **常见下游**：`plasmid_cryopreservation`, `lentiviral_transduction`, `lentiviral_transduction_two_plasmid`, `transient_transfection`, `luciferase`, `co_ip`, `rip_seq`

### 蛋白冻存（`protein_cryopreservation`）
- **类型**：实验步骤
- **做什么**：该实验用于将提取的蛋白冷冻储存
- **何时选用**：实验方案里需要包含「蛋白冻存」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出；在当前目录中多为流程终点，或需另接「检测分析」类节点
- **常见上游**：`protein_extraction`

### 蛋白提取（`protein_extraction`）
- **类型**：实验步骤
- **做什么**：该实验适用于动物蛋白提取
- **何时选用**：实验方案里需要包含「蛋白提取」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`protein_denaturation`、`protein_cryopreservation`
- **常见上游**：`cell_revival`, `cell_culture`
- **常见下游**：`protein_denaturation`, `protein_cryopreservation`

### 实时荧光定量 PCR（qPCR）（`qpcr`）
- **类型**：实验步骤
- **做什么**：实时荧光定量 PCR（qPCR）：基于 cDNA 模板与上下游引物，按用户设定的扩增程序在 96 孔板中开展定量扩增。
- **何时选用**：实验方案里需要包含「实时荧光定量 PCR（qPCR）」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`qpcr_quantification`
- **常见上游**：`rt_pcr`, `nucleotide_synthesis`
- **常见下游**：`qpcr_quantification`

### RNA 免疫沉淀测序（RIP-seq）（`rip_seq`）
- **类型**：实验步骤
- **做什么**：RNA 免疫沉淀测序（RIP-seq）：支持内源/外源两种方式；输出富集核酸，可衔接二代测序流程。
- **何时选用**：实验方案里需要包含「RNA 免疫沉淀测序（RIP-seq）」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`next_generation_sequencing`
- **常见上游**：`cell_revival`, `cell_culture`, `plasmid_extraction`
- **常见下游**：`next_generation_sequencing`

### 逆转录PCR（RT-PCR）（`rt_pcr`）
- **类型**：实验步骤
- **做什么**：对核酸样品进行逆转录PCR处理，输出反转录核酸产物。
- **何时选用**：实验方案里需要包含「逆转录PCR（RT-PCR）」这一步时（分类：分子生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`qpcr`、`next_generation_sequencing`
- **常见上游**：`nucleic_acid_extraction`
- **常见下游**：`qpcr`, `next_generation_sequencing`

## 控制流

### 条件路由（`conditional_router`）
- **类型**：控制流
- **做什么**：根据上游输出参数配置条件，路由到不同分支。默认一个输出，可配置多个命名输出。
- **何时选用**：当你要按产量、检测指标等条件走不同后续路径（成功/失败分支等）时
- **能得到什么**：按条件把流程分到不同下游分支（导入后还需在节点表单配置分支规则）
- **常见上游**：`*`
- **常见下游**：`*`

### 循环控制（`loop_control`）
- **类型**：控制流
- **做什么**：标记需要重复执行的流程段，循环次数仅用于显示和计算，不影响实际执行。
- **何时选用**：当你希望某段实验自动重复多轮，而不是在画布上复制一长串相同节点时
- **能得到什么**：把一段上游步骤纳入可重复循环（导入后还需配置循环次数与范围）
- **常见上游**：`*`
- **常见下游**：`*`

## 检测分析

### BrdU/EdU掺入实验量化分析（`brdu_edu_quantification`）
- **类型**：结果分析
- **做什么**：兼容上游 BrdU 与 EdU 掺入实验，进行24孔板分组量化分析并输出 Fold Change 与 p值。
- **何时选用**：上游实验孔板/产物已经跑完，需要做「BrdU/EdU掺入实验量化分析」出统计结论，或把指标交给条件路由时
- **能得到什么**：统计分析结果（如 Fold Change、p 值等），可供条件路由判断使用
- **常见上游**：`brdu`, `edu`
- **常见下游**：`conditional_router`

### ELISA检测量化分析（`elisa_quantification`）
- **类型**：结果分析
- **做什么**：对 ELISA 检测结果进行分组与 OD 量化分析。
- **何时选用**：上游实验孔板/产物已经跑完，需要做「ELISA检测量化分析」出统计结论，或把指标交给条件路由时
- **能得到什么**：统计分析结果（如 Fold Change、p 值等），可供条件路由判断使用
- **常见上游**：`elisa_detection`
- **常见下游**：`conditional_router`

### 双荧光素酶报告量化分析（`luciferase_quantitative_analysis`）
- **类型**：结果分析
- **做什么**：对上游双荧光素酶报告实验的孔位进行分组（空白组/对照组/实验组），并配置量化分析任务。
- **何时选用**：上游实验孔板/产物已经跑完，需要做「双荧光素酶报告量化分析」出统计结论，或把指标交给条件路由时
- **能得到什么**：统计分析结果（如 Fold Change、p 值等），可供条件路由判断使用
- **常见上游**：`luciferase`
- **常见下游**：`conditional_router`

### 细胞活力/增殖检测（MTT）量化分析（`mtt_quantification`）
- **类型**：结果分析
- **做什么**：对上游MTT实验96孔板孔位进行分组（空白组 / 对照组 / 实验组），并配置量化分析任务，输出 Fold Change 与 p 值，供条件路由使用。
- **何时选用**：上游实验孔板/产物已经跑完，需要做「细胞活力/增殖检测（MTT）量化分析」出统计结论，或把指标交给条件路由时
- **能得到什么**：统计分析结果（如 Fold Change、p 值等），可供条件路由判断使用
- **常见上游**：`mtt`
- **常见下游**：`conditional_router`

### 平板克隆量化分析（`plate_cloning_quantification`）
- **类型**：结果分析
- **做什么**：对上游平板克隆实验的六孔板孔位进行分组（空白组 / 对照组 / 实验组），并配置量化分析任务，输出 Fold Change 与 p 值，供条件路由使用。
- **何时选用**：上游实验孔板/产物已经跑完，需要做「平板克隆量化分析」出统计结论，或把指标交给条件路由时
- **能得到什么**：统计分析结果（如 Fold Change、p 值等），可供条件路由判断使用
- **常见上游**：`plate_cloning`
- **常见下游**：`conditional_router`

### 实时荧光定量 PCR（qPCR）量化分析（`qpcr_quantification`）
- **类型**：结果分析
- **做什么**：对上游实时荧光定量 PCR（qPCR）实验进行分组量化分析，输出每个分析任务的 Fold Change 与 p 值，下游仅兼容条件路由节点。
- **何时选用**：上游实验孔板/产物已经跑完，需要做「实时荧光定量 PCR（qPCR）量化分析」出统计结论，或把指标交给条件路由时
- **能得到什么**：统计分析结果（如 Fold Change、p 值等），可供条件路由判断使用
- **常见上游**：`qpcr`
- **常见下游**：`conditional_router`

### 迁移/侵袭检测（Transwell）量化分析（`transwell_quantification`）
- **类型**：结果分析
- **做什么**：对上游 Transwell 实验 24 孔板孔位进行分组（空白组 / 对照组 / 实验组），并配置量化分析任务，输出 Fold Change 与 p 值，供条件路由使用。
- **何时选用**：上游实验孔板/产物已经跑完，需要做「迁移/侵袭检测（Transwell）量化分析」出统计结论，或把指标交给条件路由时
- **能得到什么**：统计分析结果（如 Fold Change、p 值等），可供条件路由判断使用
- **常见上游**：`transwell`
- **常见下游**：`conditional_router`

### 蛋白免疫印迹结果量化分析（`western_blot_quantification`）
- **类型**：结果分析
- **做什么**：对Western Blot实验结果进行量化分析，计算目标蛋白相对于内参蛋白的表达水平
- **何时选用**：上游实验孔板/产物已经跑完，需要做「蛋白免疫印迹结果量化分析」出统计结论，或把指标交给条件路由时
- **能得到什么**：统计分析结果（如 Fold Change、p 值等），可供条件路由判断使用
- **常见上游**：`western_blot`
- **常见下游**：`conditional_branch`

## 细胞生物学

### BrdU掺入实验（`brdu`）
- **类型**：实验步骤
- **做什么**：在24孔板中进行 BrdU 掺入实验，设置每孔细胞数量并配置孔位细胞材料。
- **何时选用**：实验方案里需要包含「BrdU掺入实验」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`brdu_edu_quantification`
- **常见上游**：`cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **常见下游**：`cell_culture`, `brdu_edu_quantification`

### 细胞共培养（`cell_co_culture`）
- **类型**：实验步骤
- **做什么**：多细胞共培养：按孔板配置各孔细胞种类与数量，设定共培养时间与培养基。
- **何时选用**：实验方案里需要包含「细胞共培养」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`elisa_detection`、`plate_reader_luminescence`
- **常见上游**：`cell_revival`, `cell_culture`, `transient_transfection`, `lentivirus_transduction_gene`
- **常见下游**：`elisa_detection`, `plate_reader_luminescence`

### 细胞冻存（`cell_cryopreservation`）
- **类型**：实验步骤
- **做什么**：该实验用于冻存细胞。
- **何时选用**：实验方案里需要包含「细胞冻存」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出；在当前目录中多为流程终点，或需另接「检测分析」类节点
- **常见上游**：`cell_revival`, `cell_culture`

### 细胞培养（`cell_culture`）
- **类型**：实验步骤
- **做什么**：细胞培养和传代
- **何时选用**：实验方案里需要包含「细胞培养」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`protein_extraction`、`cell_cryopreservation`、`lentiviral_transduction`、`lentivirus_transduction_gene`、`plate_cloning`、`mtt` 等
- **常见上游**：`cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`, `luciferase`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`
- **常见下游**：`protein_extraction`, `cell_cryopreservation`, `lentiviral_transduction`, `lentivirus_transduction_gene`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`

### 细胞复苏（`cell_revival`）
- **类型**：实验步骤
- **做什么**：该实验用于将冻存细胞复苏
- **何时选用**：实验方案里需要包含「细胞复苏」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`cell_cryopreservation`、`protein_extraction`、`lentiviral_transduction`、`lentivirus_transduction_gene`、`plate_cloning` 等
- **常见下游**：`cell_culture`, `cell_cryopreservation`, `protein_extraction`, `lentiviral_transduction`, `lentivirus_transduction_gene`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`

### EdU掺入实验（`edu`）
- **类型**：实验步骤
- **做什么**：在24孔板中进行 EdU 掺入实验，设置每孔细胞数量并配置孔位细胞材料。
- **何时选用**：实验方案里需要包含「EdU掺入实验」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`brdu_edu_quantification`
- **常见上游**：`cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **常见下游**：`cell_culture`, `brdu_edu_quantification`

### 慢病毒包装（三质粒系统）（`lentiviral_transduction`）
- **类型**：实验步骤
- **做什么**：使用慢病毒载体包装；细胞来自上游细胞复苏/培养，质粒可来自上游质粒提取或库存（PLASMID 质粒材料）
- **何时选用**：实验方案里需要包含「慢病毒包装（三质粒系统）」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`lentivirus_cryopreservation`、`lentivirus_transduction_gene`
- **常见上游**：`cell_revival`, `cell_culture`, `plasmid_extraction`
- **常见下游**：`lentivirus_cryopreservation`, `lentivirus_transduction_gene`

### 慢病毒包装（二质粒系统）（`lentiviral_transduction_two_plasmid`）
- **类型**：实验步骤
- **做什么**：使用慢病毒载体包装；细胞来自上游细胞复苏/培养，质粒可来自上游质粒提取或库存（PLASMID 质粒材料）
- **何时选用**：实验方案里需要包含「慢病毒包装（二质粒系统）」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`lentivirus_cryopreservation`、`lentivirus_transduction_gene`
- **常见上游**：`cell_revival`, `cell_culture`, `plasmid_extraction`
- **常见下游**：`lentivirus_cryopreservation`, `lentivirus_transduction_gene`

### 重组慢病毒冻存（`lentivirus_cryopreservation`）
- **类型**：实验步骤
- **做什么**：冻存上游慢病毒包装节点产生的病毒上清液
- **何时选用**：实验方案里需要包含「重组慢病毒冻存」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出；在当前目录中多为流程终点，或需另接「检测分析」类节点
- **常见上游**：`lentiviral_transduction`, `lentiviral_transduction_two_plasmid`

### 基因转导（慢病毒）（`lentivirus_transduction_gene`）
- **类型**：实验步骤
- **做什么**：使用重组慢病毒对细胞进行基因转导；细胞来自上游细胞复苏/培养，慢病毒可来自上游或库存
- **何时选用**：实验方案里需要包含「基因转导（慢病毒）」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`cell_cryopreservation`、`protein_extraction`、`plate_cloning`、`mtt`、`transwell` 等
- **常见上游**：`cell_revival`, `cell_culture`, `lentiviral_transduction`, `lentiviral_transduction_two_plasmid`, `transient_transfection`, `lentivirus_transduction_gene`
- **常见下游**：`cell_culture`, `cell_cryopreservation`, `protein_extraction`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`, `lentivirus_transduction_gene`

### 双荧光素酶报告实验（`luciferase`）
- **类型**：实验步骤
- **做什么**：基于96孔板的双荧光素酶报告实验，支持逐孔配置质粒方案。
- **何时选用**：实验方案里需要包含「双荧光素酶报告实验」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`luciferase_quantitative_analysis`
- **常见上游**：`cell_revival`, `cell_culture`, `plasmid_extraction`
- **常见下游**：`cell_culture`, `luciferase_quantitative_analysis`

### 细胞活力/增殖检测（MTT）（`mtt`）
- **类型**：实验步骤
- **做什么**：在96孔板进行MTT实验，配置每孔细胞数量、检测天数及孔位细胞材料。
- **何时选用**：实验方案里需要包含「细胞活力/增殖检测（MTT）」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`mtt_quantification`
- **常见上游**：`cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **常见下游**：`cell_culture`, `mtt_quantification`

### 质粒扩增培养（`plasmid_amplification`）
- **类型**：实验步骤
- **做什么**：将转化后的菌种进行质粒扩增培养
- **何时选用**：实验方案里需要包含「质粒扩增培养」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`plasmid_extraction`、`transformation`、`strain_cryopreservation`
- **常见上游**：`transformation`
- **常见下游**：`plasmid_extraction`, `transformation`, `strain_cryopreservation`

### 平板克隆实验（`plate_cloning`）
- **类型**：实验步骤
- **做什么**：在六孔板上进行平板克隆实验：设置每孔细胞数量、培养天数，并为每孔选择使用的上游细胞材料。
- **何时选用**：实验方案里需要包含「平板克隆实验」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`plate_cloning_quantification`
- **常见上游**：`cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **常见下游**：`cell_culture`, `plate_cloning_quantification`

### 菌种冻存（`strain_cryopreservation`）
- **类型**：实验步骤
- **做什么**：将转化或扩增后的菌种进行冻存保存
- **何时选用**：实验方案里需要包含「菌种冻存」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出；在当前目录中多为流程终点，或需另接「检测分析」类节点
- **常见上游**：`plasmid_amplification`

### 转化（`transformation`）
- **类型**：实验步骤
- **做什么**：将重组质粒转化到感受态细胞中
- **何时选用**：实验方案里需要包含「转化」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`plasmid_amplification`
- **常见上游**：`plasmid_construction`
- **常见下游**：`plasmid_amplification`

### 瞬时转染（`transient_transfection`）
- **类型**：实验步骤
- **做什么**：细胞培养皿上进行瞬时转染；质粒可来自上游质粒提取或库存，用量由用户按 μL 填写（材料验证按×6累计）。
- **何时选用**：实验方案里需要包含「瞬时转染」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`cell_cryopreservation`、`protein_extraction`、`plate_cloning`、`mtt`、`transwell` 等
- **常见上游**：`cell_revival`, `cell_culture`, `plasmid_extraction`
- **常见下游**：`cell_culture`, `cell_cryopreservation`, `protein_extraction`, `plate_cloning`, `mtt`, `transwell`, `brdu`, `edu`

### 迁移/侵袭检测（Transwell）（`transwell`）
- **类型**：实验步骤
- **做什么**：在 24 孔板上进行 Transwell 迁移/侵袭检测：可选添加基质胶、设置每孔细胞数量、配置每孔使用的上游细胞材料。
- **何时选用**：实验方案里需要包含「迁移/侵袭检测（Transwell）」这一步时（分类：细胞生物学）
- **能得到什么**：本步实验产出，常见可继续接到：`cell_culture`、`transwell_quantification`
- **常见上游**：`cell_culture`, `cell_revival`, `transient_transfection`, `lentivirus_transduction_gene`
- **常见下游**：`cell_culture`, `transwell_quantification`

## 蛋白质学

### 免疫共沉淀（Co-IP）（`co_ip`）
- **类型**：实验步骤
- **做什么**：免疫共沉淀（Co-IP）：研究蛋白互作；可选择内源或外源（标签过表达）方式。
- **何时选用**：实验方案里需要包含「免疫共沉淀（Co-IP）」这一步时（分类：蛋白质学）
- **能得到什么**：本步实验产出，常见可继续接到：`protein_denaturation`
- **常见上游**：`cell_revival`, `cell_culture`, `plasmid_extraction`
- **常见下游**：`protein_denaturation`

### ELISA检测（`elisa_detection`）
- **类型**：实验步骤
- **做什么**：在 96 孔板上配置 ELISA：点选上游共培养孔位作为样本，并设置靶标与检测参数。
- **何时选用**：实验方案里需要包含「ELISA检测」这一步时（分类：蛋白质学）
- **能得到什么**：本步实验产出，常见可继续接到：`elisa_quantification`
- **常见上游**：`cell_co_culture`
- **常见下游**：`elisa_quantification`

### 酶标仪发光检测（`plate_reader_luminescence`）
- **类型**：实验步骤
- **做什么**：基于上游共培养 96 孔板进行酶标仪发光读数；可逐孔选择是否添加发光底物及底物种类。
- **何时选用**：实验方案里需要包含「酶标仪发光检测」这一步时（分类：蛋白质学）
- **能得到什么**：本步实验产出；在当前目录中多为流程终点，或需另接「检测分析」类节点
- **常见上游**：`cell_co_culture`

### 蛋白变性（`protein_denaturation`）
- **类型**：实验步骤
- **做什么**：该实验用于将提取的蛋白进行变性处理
- **何时选用**：实验方案里需要包含「蛋白变性」这一步时（分类：蛋白质学）
- **能得到什么**：本步实验产出，常见可继续接到：`western_blot`
- **常见上游**：`protein_extraction`
- **常见下游**：`western_blot`

### 蛋白免疫印迹实验（`western_blot`）
- **类型**：实验步骤
- **做什么**：蛋白免疫印迹实验，支持自定义目标蛋白范围和10个孔位独立配置
- **何时选用**：实验方案里需要包含「蛋白免疫印迹实验」这一步时（分类：蛋白质学）
- **能得到什么**：本步实验产出，常见可继续接到：`western_blot_quantification`
- **常见下游**：`western_blot_quantification`
