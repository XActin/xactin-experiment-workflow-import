# XActin experiment node skill

XActin is an online experiment platform. Install this skill in your own assistant (Cursor, Codex, Harness, Doubao, and similar tools). Describe the experiment in everyday language. The assistant will:

1. Produce JSON you paste into **Import experiment nodes** on the experiment workflow page, so the whole flow appears at once.
2. Tell you, in order, how to fill each node's parameters after you open it.

## How to use it

1. Give this folder to your assistant, as described below.
2. Describe the experiment, for example: "Revive cells, culture them, extract protein, then run a western blot."
3. Copy the JSON and paste it into **Import experiment nodes** on the XActin experiment workflow page.
4. Following the assistant, open each node from upstream to downstream, fill in materials, amounts, and times, and save.
5. To see only one step, ask: "How do I configure this node?"

## Install it in an assistant

**Cursor**

Put this folder in either:

- `.cursor/skills/xactin-experiment-workflow-import/` in the current project, or
- the same folder name in your personal skills directory

**Codex, Harness, Doubao, and similar tools**

Add the folder the way that product adds a skill or custom instructions. The assistant needs to read `SKILL.md`, plus `nodes-guide.en.md` and `nodes-config-guide.en.md` for English, or `nodes-guide.md` and `nodes-config-guide.md` for Chinese.

## What is in this folder

| File | Purpose |
|------|---------|
| `SKILL.md` | Steps for the assistant: English first, Chinese second |
| `nodes-guide.en.md` | English: what each node does and when to use it |
| `nodes-guide.md` | 中文：每个节点做什么、什么时候用 |
| `nodes-config-guide.en.md` | English: how to fill each node after import |
| `nodes-config-guide.md` | 中文：导入之后，每个节点的参数怎么填 |
| `nodes-catalog.json` | Node codes and connections, for the assistant |
| `examples/` | Example import JSON |
| `version.json` | Skill version; the assistant can read newer node descriptions from here |

# XActin 实验节点技能

XActin 是在线实验平台。把本技能安装到你自己的助手（Cursor、Codex、Harness、豆包等）后，可以用日常语言描述实验。助手会：

1. 生成一份 JSON，粘贴到实验工作流页的「导入实验节点」，一次放上整条流程  
2. 按顺序告诉你每个节点打开后，参数怎么填

## 使用步骤

1. 按下面的方式，把本文件夹交给助手。  
2. 描述实验，例如：「复苏细胞，培养后提取蛋白，再做蛋白免疫印迹」。  
3. 复制助手给出的 JSON，在 XActin 实验工作流页点击「导入实验节点」并粘贴。  
4. 按助手的说明，从上游到下游点开每个节点，填写材料、用量、时间等参数并保存。  
5. 若只要看某一步怎么填，直接问：「这个节点的参数怎么配置？」

## 安装到助手

**Cursor**

将本文件夹放到：

- 当前项目的 `.cursor/skills/xactin-experiment-workflow-import/`，或  
- 个人技能目录中的同名文件夹

**Codex、Harness、豆包等**

按该软件添加技能或自定义说明的方式挂上本文件夹。助手需要能读到 `SKILL.md`。英文用 `nodes-guide.en.md` 和 `nodes-config-guide.en.md`，中文用 `nodes-guide.md` 和 `nodes-config-guide.md`。

## 文件夹里有什么

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 助手的工作步骤（先英文，后中文） |
| `nodes-guide.en.md` | 英文：每个节点做什么、什么时候用 |
| `nodes-guide.md` | 中文：每个节点做什么、什么时候用 |
| `nodes-config-guide.en.md` | 英文：导入之后，每个节点的参数怎么填 |
| `nodes-config-guide.md` | 中文：导入之后，每个节点的参数怎么填 |
| `nodes-catalog.json` | 节点代码与上下游关系，供助手选用 |
| `examples/` | 可参考的导入示例 |
| `version.json` | 技能版本；助手可据此读取更新后的节点说明 |
