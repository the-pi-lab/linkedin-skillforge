# Evolution Audit Log

Append-only. Every `record` / `propose` / `validate` / `apply` / rollback event lands here.
History is never rewritten — rollback is a new entry, not an edit.
