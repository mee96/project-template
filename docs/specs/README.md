# Specs

One short spec per feature, written **before** the code (Spec-Driven Development, light version).

1. Copy `_TEMPLATE.md` to `NNN-feature-name.md` (next free number).
2. Fill in problem, scope and numbered acceptance criteria.
3. Open the issue (feature template) and link the spec.
4. Implement on `feature/<issue>-…`. Every acceptance criterion gets a test.
5. When the PR merges, set the spec **Status** to `Implemented`.

Bug fixes don't need a spec; they need a test that fails without the fix.
