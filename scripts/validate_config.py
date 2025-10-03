#!/usr/bin/env python3
import json, sys, yaml, os
try:
    import jsonschema
except ImportError:
    print("Installing jsonschema...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "jsonschema"])
    import jsonschema

schema_path = "configs/department.schema.json"
config_path = "configs/department.yaml"

with open(schema_path) as f:
    schema = json.load(f)

if not os.path.exists(config_path):
    print("No configs/department.yaml found. Copy from department.yaml.template and edit.")
    sys.exit(1)

with open(config_path) as f:
    data = yaml.safe_load(f)

jsonschema.validate(instance=data, schema=schema)
print("✅ configs/department.yaml is valid against department.schema.json")
