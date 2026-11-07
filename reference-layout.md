# 画布布局参考

导入后节点在画布上怎么摆更清楚。数值以 `nodes-catalog.json` 里的 `layout_defaults` 为准。

## 常量

| 项 | 默认值 |
|----|--------|
| 节点宽 | 220 |
| 网格 | 15（`x/y` 取整到 15 的倍数） |
| 水平间距 | 30 → 列步长约 250 |
| 行高 short / medium / medium_tall / tall | 100 / 140 / 200 / 280 |

取相邻节点较大的 `layout_height_tier` 决定纵向步长。填参后节点变高，tall（孔板、分析配置等）务必用更大行距。

## 拓扑模式

### 线性主链

从 `(100, 100)` 起，每步 `x += 250`（已含宽与间距近似），`y` 不变。

### 分支

- 主链保持中间 `y`。
- 上分支：`y -= tier_row_height`。
- 下分支：`y += tier_row_height`。
- 避免边交叉：必要时再错开一列。

### 条件路由

- 路由节点单独一列。
- 每条出线不同 `sourceHandle`（如 `branch_success` / `branch_fail`）。
- 成功/失败下游在纵向错开。

### 循环回连

- `loop_control`（或其它回连节点）设 `"ports_swapped": true`。
- 回连目标放在左侧或上方，回边从左出（交换后）连到目标输入侧，减少绕线。

### 配体挂载

- `ligand_stimulus` 放在宿主节点正上方或正下方（同一列 `x`，上下错开约一个行高）。
- 边：`source` = 配体刺激，`target` = 宿主；`sourceHandle: "mount"`，`targetHandle: "stimulus"`。
- 不参与左右物料主链；一个宿主可挂多个配体刺激节点（可左右略微错开）。

## ports_swapped

- 默认：左 = 输入，右 = 输出。
- `ports_swapped: true`：右 = 输入，左 = 输出。
- 仅影响连线柄方向，不是业务参数。
- 典型：循环控制从下游回连到上游入口。

## 坐标示例

```text
n1 (90,180) -> n2 (345,180) -> n3 (600,195)
                     \-> n4 (600,75)
n3 -> n6 router (855,195) -> n5 (1110,135) [branch_success]
                          -> n7 loop (720,345) ports_swapped [branch_fail]
n7 -> n1
```

完整 JSON 见 `examples/loop-router.json`。
