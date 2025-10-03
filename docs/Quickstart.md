# Quickstart (Directive 4.1.13 + DISARM)

1) **Create your copy**  
   - Fork this repo or use "Use this template".

2) **Fill your department details**  
   - Copy `configs/department.yaml.template` → `configs/department.yaml`.
   - Edit names, roles, contacts, and routing.

3) **Set up intake**  
   - Option A: Enable GitHub Issues using `.github/ISSUE_TEMPLATE/incident_intake.yml`.  
   - Option B: Use your existing mailbox/form; route into `/intake/`.

4) **Tag with DISARM**  
   - Start with *observables* (what you can see), then add *inferences* (analyst assessment).  
   - Use the examples in `configs/examples/`.

5) **Run playbooks**  
   - Intake → `playbooks/00_Intake.md`  
   - Tagging → `playbooks/01_Tagging.md`  
   - Response → `playbooks/10_Response_Low.md`, `11_Response_Medium.md`, `12_Response_High.md`  
   - Comms → `playbooks/20_Communications.md`  
   - After-Action → `playbooks/30_After_Action.md`

6) **Validate config**  
   - `make validate` (requires Python 3; installs `jsonschema` in a venv on first run)

7) **Continuous learning**  
   - Log decisions + outcomes. Review weekly. Update playbooks monthly.

See also: `docs/Glossary.md` and `docs/Flow_Diagram.md`.
