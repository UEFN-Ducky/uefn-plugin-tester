---
description: "Live session probes — PIE status, log streaming, actor before/after diffs"
metadata:
  label: Session probes
  default_enabled: true
  load_condition: "Checking play session state, streaming logs, or verifying movement/teleport after a live action"
  order: 30
---

# Session probes

Use only after offline sim + harness cannot answer the question.

## Tools

- `session_status` — is a play/PIE session active?
- `play_in_editor` / `stop_pie` — start/stop (best-effort on UEFN builds).
- `get_editor_log(last_n, since_offset, regex)` — stream new log bytes; use `regex` for `[DUCKY-TEST]` or custom markers.
- `actor_state_snapshot(labels|label_filter)` — capture transforms.
- `actor_state_diff(before_json, after_json, epsilon)` — movement/teleport deltas in uu.

## Pattern for movement checks

1. `before = actor_state_snapshot(labels=["PlayerStart", …])`
2. Trigger the path (sim if possible; otherwise play session + user/action).
3. `after = actor_state_snapshot(...)`
4. `actor_state_diff(before, after)` — report delta location.
