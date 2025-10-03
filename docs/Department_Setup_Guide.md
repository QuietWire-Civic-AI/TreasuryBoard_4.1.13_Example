# Department Setup Guide (Directive 4.1.13)

Step-by-step instructions for a department to stand up a 4.1.13 compliance process:

1. **Create your copy**
   - Fork this repository or use it as a template.

2. **Fill in your contacts and escalation points**
   - Edit `configs/department.yaml` with department name, leads, and response roles.

3. **Stand up tagging + intake**
   - Adopt DISARM tagging (observables first, then inferences) for all incidents.
   - Decide your intake channels (shared inbox, portal form, API).

4. **Run the base playbooks**
   - Follow `/playbooks/Misinformation_Playbook.md` for common cases.
   - Add department-specific playbooks for elections, public health, emergencies.

5. **Coordinate**
   - Publish your internal comms routine (daily standup, weekly review).
   - Name cross-dept points of contact and Treasury Board liaison.

6. **Report & learn**
   - Track metrics (time-to-tag, time-to-decision, outcomes).
   - Capture lessons learned; update playbooks monthly.

> Tip: keep “observable” vs “inference” tagging distinct. Start simple, then layer nuance.
