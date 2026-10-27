---
name: xactin-experiment-workflow-import
description: >-
  Helps XActin users quickly place experiment nodes and configure them.
  The user installs this skill in their own agent. The agent turns an
  experiment description into JSON for「导入实验节点」, then explains how to
  fill each node's parameters on the canvas. Use when the user wants to
  build a workflow, import nodes, or asks how to configure a node.
---

# Place experiment nodes on XActin and explain how to fill them

Reply in the language the user is using. For English, read `nodes-guide.en.md` and `nodes-config-guide.en.md`, and name nodes in English. For Chinese, read `nodes-guide.md` and `nodes-config-guide.md`, and name nodes in Chinese. The `code` values in JSON are the same in both languages. The Chinese procedure is in the second half of this file.

XActin is an online experiment platform. After this skill is installed in the user's own assistant, the user describes the experiment in everyday language.

Do two things:

1. Pick the nodes for the experiment and produce JSON the user can paste into **Import experiment nodes**, so the whole flow appears at once.
2. After import, explain how to fill each node's form, from upstream to downstream.

## What the user does on the website

1. Open the experiment workflow page, click **Import experiment nodes**, and paste the JSON.
2. Open each node from upstream to downstream and save, following your instructions.
3. Submit the experiment only after every node is filled in.

The JSON carries node type, position, and connections. Materials, amounts, plates, and times are filled in the web form. Use [nodes-config-guide.en.md](nodes-config-guide.en.md) and tailor the advice to this experiment.

## Which files to read

Prefer the files in this skill folder. If the addresses in `version.json` open and the remote `catalog_version` is newer, use the remote files of the same name, including the `.en.md` guides.

| File | Use it for |
|------|------------|
| [nodes-guide.en.md](nodes-guide.en.md) | What each node does, when to use it, and what you get |
| [nodes-config-guide.en.md](nodes-config-guide.en.md) | How to fill the form after import |
| [nodes-catalog.json](nodes-catalog.json) | Node codes, allowed connections, and form fields |

If an address does not open, keep using the files in this folder and tell the user that the node descriptions match the copy they have.

## How to choose nodes and write JSON

1. Clarify the experiment goal, the cells or materials, and whether there is a branch or a repeat.
2. Choose nodes from `nodes-guide.en.md`. In the reply, name nodes in English.
3. Every `code` must exist in the catalog. Connect only compatible upstream and downstream nodes.
4. When there is a branch or a loop, set coordinates on a 15-pixel grid. For a connection that loops back, set `"ports_swapped": true` on the loop node so the input and output handles swap sides.

Use this shape when there is a branch or a loop:

```json
{
  "nodes": [
    { "id": "n1", "code": "cell_culture", "position": { "x": 100, "y": 100 } },
    { "id": "n2", "code": "loop_control", "position": { "x": 400, "y": 280 }, "ports_swapped": true }
  ],
  "edges": [
    { "source": "n1", "target": "n2" },
    { "source": "n2", "target": "n1" }
  ]
}
```

A single straight chain with no branches may use `steps` plus `step_positions`.
Do not put materials or volumes into the JSON of an ordinary node. The website does not import those values. Write rules into the JSON only for conditional routing and loop control, and only when the user asks for those rules.

Layout details are in [reference-layout.en.md](reference-layout.en.md). Examples are in [examples/](examples/).

## Always explain how to fill the forms

When you give JSON, or when the user asks how to fill a node:

1. Walk the flow from upstream to downstream.
2. Open that node's section in `nodes-config-guide.en.md`.
3. For this experiment, say what each required field should contain: which cells, which medium, which plasmid, how long to culture, and what to measure. Do not only repeat the field names.
4. For each node, say where to click on the canvas, what the required fields should say, and which upstream node supplies the sample.
5. For conditional routing, explain how each branch is decided. For a loop, explain the repeat count and range.
6. When there are many nodes, explain the whole flow first, then the first few nodes in detail, and ask whether to continue.

The reply includes both the JSON and how to fill each relevant node.

## Suggested reply order

1. Explain the experiment flow in English and why these nodes were chosen.
2. Give one JSON block.
3. Explain how to fill each node after import.
4. Remind the user to save every node, then submit the experiment.

If the user only asks how to fill one node, answer that section only. Do not resend the whole JSON.

# 帮用户在 XActin 上快速放好实验节点并配好参数

用用户正在使用的语言回复。用户用英文时，读 `nodes-guide.en.md` 和 `nodes-config-guide.en.md`，回复用英文节点名。用户用中文时，读 `nodes-guide.md` 和 `nodes-config-guide.md`，回复用中文节点名。JSON 里的 `code` 两种语言相同。

XActin 是在线实验平台。用户在自己的助手里安装本技能后，用日常语言描述实验即可。

你做两件事：

1. 按实验目的选出节点，生成可粘贴到「导入实验节点」的 JSON，让用户一次放上整条流程  
2. 导入之后，按顺序说明每个节点打开后参数怎么填

## 用户在网站上怎么做

1. 打开实验工作流页面，点 **「导入实验节点」**，粘贴你给的 JSON  
2. 按你的说明，从上游到下游点开每个节点并保存  
3. 全部填完后再提交实验  

JSON 只带上节点种类、位置和连线。材料、用量、孔板、时间等，要在网页表单里填。填写方法以本文件夹里的 [nodes-config-guide.md](nodes-config-guide.md) 为准，并结合用户这次实验来讲。

## 先读哪几份说明

优先使用本技能文件夹里的文件。若 `version.json` 里的地址可以打开，且其中的 `catalog_version` 比本地新，再改用网上的同名文件（含 `.en.md`）。

| 文件 | 用来做什么 |
|------|------------|
| [nodes-guide.en.md](nodes-guide.en.md) | 英文：判断该用哪个节点 |
| [nodes-guide.md](nodes-guide.md) | 中文：判断该用哪个节点 |
| [nodes-config-guide.en.md](nodes-config-guide.en.md) | 英文：导入后表单怎么填 |
| [nodes-config-guide.md](nodes-config-guide.md) | 中文：导入后表单怎么填 |
| [nodes-catalog.json](nodes-catalog.json) | 节点代码、谁可以接谁、表单字段 |

地址打不开时，继续用文件夹里的文件，并告诉用户：节点说明以当前这份为准。

## 怎么选节点、怎么写 JSON

1. 问清实验目的、用什么细胞或材料、要不要分支或重复。  
2. 对照 `nodes-guide.md` 选型。回复里用**中文节点名**把流程讲清楚。  
3. JSON 里的 `code` 必须是目录里有的代码；能接上的上下游才连。  
4. 有分支或回头连线时写上坐标（15 的倍数）。循环往回连时，循环节点写 `"ports_swapped": true`，输入输出圆点对调后更好认。

有分支或循环时用这种写法：

```json
{
  "nodes": [
    { "id": "n1", "code": "cell_culture", "position": { "x": 100, "y": 100 } },
    { "id": "n2", "code": "loop_control", "position": { "x": 400, "y": 280 }, "ports_swapped": true }
  ],
  "edges": [
    { "source": "n1", "target": "n2" },
    { "source": "n2", "target": "n1" }
  ]
}
```

只有一条直线、没有分支时，可以写成 `steps` 加 `step_positions`。  
不要把材料、体积写进普通节点的 JSON（网站导入时不会带上）。只有条件路由、循环控制，用户明确要求时才写入规则。

摆放方式见 [reference-layout.md](reference-layout.md)，例子见 [examples/](examples/)。

## 导入之后一定要讲怎么填

给出 JSON，或用户问「这个节点怎么填」时：

1. 按流程从上游讲到下游。  
2. 打开该节点在 `nodes-config-guide.md` 里的一节。  
3. 按**这次实验**说明每个必填项填什么，例如用哪种细胞、哪种培养基、哪份质粒、共培养多久、检测哪一项。不要只念字段名称。  
4. 每个节点至少说明：在画布上点哪里打开、必填项写什么、样本从哪一个上游节点里选。  
5. 条件路由要讲清每条分支怎么判断；循环要讲清重复次数和范围。  
6. 节点很多时，先讲清整条流程，再细讲前几步，并问用户要不要继续讲后面的节点。

回复里同时给出 JSON，以及每个相关节点的参数怎么填。

## 回复时建议的顺序

1. 用中文说明整条实验怎么走、为什么选这些节点  
2. 给出一份 JSON  
3. 按节点顺序写导入后的填写说明  
4. 提醒：每个节点保存后，再提交实验  

用户如果只问某一个节点怎么填，只回答那一节，不必重发整份 JSON。
