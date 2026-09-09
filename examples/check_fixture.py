"""Check this documentation fixture only; this is not a production validator."""

import json
from pathlib import Path

profile = json.loads(Path(__file__).with_name("student-profile.synthetic.json").read_text())
expected_fields = {
    "example_only", "profile_id", "desired_degree", "study_interests",
    "preferred_study_countries", "teaching_languages",
    "annual_tuition_budget_eur", "intended_start_year",
}
if set(profile) != expected_fields:
    raise ValueError("Fixture fields differ from the documented field guide")
if profile["example_only"] is not True or not profile["profile_id"].startswith("demo-"):
    raise ValueError("Fixture must be explicitly marked as synthetic")
for field in ("study_interests", "preferred_study_countries", "teaching_languages"):
    if not isinstance(profile[field], list) or not profile[field]:
        raise ValueError(f"{field} must be a non-empty list")
if not isinstance(profile["annual_tuition_budget_eur"], int) or profile["annual_tuition_budget_eur"] < 0:
    raise ValueError("Illustrative tuition budget must be a non-negative integer")
print("PASS: synthetic fixture parses and matches the documented basic structure.")
