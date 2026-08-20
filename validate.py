"""Validate the example TES task document against the official tesTask schema."""

import json
import sys

import jsonschema

TASK = "tes_task_16s_denoising.json"
SCHEMA = "tesTask.schema.json"


def main() -> int:
    with open(TASK, encoding="utf-8") as f:
        task = json.load(f)
    with open(SCHEMA, encoding="utf-8") as f:
        schema = json.load(f)

    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(task), key=lambda e: list(e.path))

    if not errors:
        print(f"{TASK} is VALID against {SCHEMA}")
        return 0

    print(f"{TASK} is INVALID against {SCHEMA}\n")
    for err in errors:
        location = "/".join(str(p) for p in err.path) or "(root)"
        print(f"  {location}: {err.message}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
