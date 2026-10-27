# 001 · Health check

| | |
|---|---|
| **Status** | Implemented |
| **Issue** | — (example spec shipped with the template) |
| **Area** | backend |

## Problem

Hosting platforms and uptime monitors need a cheap endpoint to know the API is alive.

## Scope

**In:** a `GET /health` endpoint that answers without touching the database.
**Out:** readiness checks for the database or third-party services.

## Acceptance criteria

- **AC1** — Given the API is running, when `GET /health` is called, then the status is `200`.
- **AC2** — Given the API is running, when `GET /health` is called, then the body is `{"status": "ok"}`.
- **AC3** — Given the API is running, when any other method is used on `/health`, then the status is `405`.

## Design notes

No authentication. Response is a constant, so it is safe to call every few minutes (see the keep-alive action).

## Test plan

| Criterion | Test |
|---|---|
| AC1, AC2 | `backend/tests/test_health.py::test_health_returns_200_and_ok_status` |
| AC3 | `backend/tests/test_health.py::test_health_rejects_non_get_methods` |
