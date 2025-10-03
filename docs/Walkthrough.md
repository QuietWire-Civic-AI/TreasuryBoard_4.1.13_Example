# Hands-On Walkthrough

## 1) Copy & validate config
- Copy: `cp configs/department.yaml.template configs/department.yaml`
- Edit: names, emails, routing thresholds.
- Validate: `make validate`  → ✅ if valid.

## 2) Intake an incident
- If using GitHub Issues, click **New issue → Incident intake (4.1.13)** and fill the form.
- Or create a folder under `incidents/EX-YYYY-####/` and add `observable.yaml` + evidence links.

## 3) Tag with DISARM
- Start with observables (`configs/examples/disarm_observable.yaml` as a guide).
- Peer review observables; then create `inference.yaml` (confidence + rationale).
- Keep observables and inferences **separate files**.

## 4) Decide severity & run response playbook
- Use local thresholds in `configs/department.yaml` (low/med/high).
- Run the matching playbook: `playbooks/10_*, 11_*, or 12_*`.

## 5) Communicate & close
- `playbooks/20_Communications.md` → internal brief + external lines.
- `playbooks/30_After_Action.md` → metrics + lessons; update docs monthly.

## 6) Report metrics
- Track: `time_to_tag`, `time_to_decision`, `resolution_category`.
- Send routine summaries to your Treasury Board liaison.
