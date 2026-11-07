# Canvas layout

How nodes sit on the canvas after import. Numbers follow `layout_defaults` in `nodes-catalog.json`.

## Constants

| Item | Default |
|------|---------|
| Node width | 220 |
| Grid | 15 (`x` and `y` snap to multiples of 15) |
| Horizontal gap | 30, so the column step is about 250 |
| Row height short / medium / medium_tall / tall | 100 / 140 / 200 / 280 |

Use the larger `layout_height_tier` of neighboring nodes for the vertical step. Nodes grow after parameters are filled. Tall nodes (plates, analysis settings) need the larger row spacing.

## Patterns

### Straight chain

Start at `(100, 100)`. Each step adds about 250 to `x`. Keep `y` the same.

### Branches

- Keep the main chain on the middle `y`.
- Upper branch: subtract the row height from `y`.
- Lower branch: add the row height to `y`.
- Shift a column when edges would cross.

### Conditional routing

- Put the router in its own column.
- Each outgoing edge uses a different `sourceHandle` (for example `branch_success` and `branch_fail`).
- Place the success and failure paths on different rows.

### Looping back

- Set `"ports_swapped": true` on `loop_control` (or the other node that connects backward).
- Put the target to the left or above, so the return edge leaves from the left and meets the target's input side.

### Ligand mount

- Place `ligand_stimulus` directly above or below the host (same `x`, offset by about one row height).
- Edge: `source` is the stimulus, `target` is the host; `sourceHandle: "mount"`, `targetHandle: "stimulus"`.
- Not part of the left/right material chain. One host may have several stimulus nodes (nudge them left/right if needed).

## ports_swapped

- Default: left is input, right is output.
- `ports_swapped: true`: right is input, left is output.
- This only changes handle direction. It is not an experiment parameter.
- Typical use: loop control connects from a later step back to an earlier step.

## Example coordinates

```text
n1 (90,180) -> n2 (345,180) -> n3 (600,195)
                     \-> n4 (600,75)
n3 -> n6 router (855,195) -> n5 (1110,135) [branch_success]
                          -> n7 loop (720,345) ports_swapped [branch_fail]
n7 -> n1
```

Full JSON is in `examples/loop-router.json`.
