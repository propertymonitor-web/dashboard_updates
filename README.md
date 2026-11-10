# dashboard_updates

The newest dashboard pages for LODESTAR NOVA / ORION and OTR, and the list the dashboard's **Updates** screen reads.

- `dashboards/matrix-range.html` - the OPTIONAL Matrix dashboard with the range-estimate tile (its own entry, `matrix-range`, in `latest.json`; it never replaces `matrix.html`).
- `latest.json` - newest version of each dashboard, with file name, size and SHA-256.
- `dashboards/otr.html` (OTR), `dashboards/tactical.html` (ORION tactical), `dashboards/nova.html` (NOVA / ORION, saved as `index.html`), `dashboards/cairn.html` (CAIRN, saved as `index.html`), `dashboards/matrix.html` (PROJECT MATRIX).
- `tools/add_updates_tab.py` + `tools/updates_tab.html` - the source of the Updates button and screen. Run `python3 tools/add_updates_tab.py <page.html> --id otr --version 1.2.0` to put it into a dashboard page.

Publishing a new dashboard: add the Updates tab with the new version number, copy the page to `dashboards/`, update `version`, `size` and `sha256` in `latest.json`, commit to `main`.
