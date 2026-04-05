# Reference Data

This folder contains static grounding data that the AI must look up — never invent.

## Contents

| File | Purpose | Update Frequency |
|---|---|---|
| [filename_1] | [What it provides] | [How often it changes] |
| [filename_2] | [What it provides] | [How often it changes] |

## Rules

1. If a reference file is missing, the AI must flag or hard-stop — never fabricate the data.
2. If a reference file is outdated, the AI must flag the currency concern in the run log.
3. New reference data discovered during real runs should be added here and documented in this README.

## Load-Bearing References

These files are load-bearing — if they are missing or wrong, the output fails silently:

- [filename]: [Why it's critical]
- [filename]: [Why it's critical]

Each of these has a corresponding validation check in `Instructions/Validation_and_Failure_Modes.md`.
