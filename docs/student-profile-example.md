# Synthetic student profile: field guide

**Demonstration only.** This is invented data for showing a reviewable specification change. It is not a real student, an agreed production schema or an implemented feature.

| Field | Plain-language meaning | Example |
| --- | --- | --- |
| `example_only` | Explicitly flags demonstration data | `true` |
| `profile_id` | A synthetic reference, not a student identity | `demo-student-001` |
| `desired_degree` | Type of course the student is exploring | `bachelor` |
| `study_interests` | Subjects the student wants to explore | Computer science, business |
| `preferred_study_countries` | Countries where the student would consider studying | Italy, Denmark |
| `teaching_languages` | Preferred teaching languages | English |
| `annual_tuition_budget_eur` | Illustrative tuition preference, excluding living costs | €8,000 |
| `intended_start_year` | Illustrative intended enrolment year | 2027 |

There are no names, email addresses, phone numbers, documents or real student records in this fixture.

## Questions for actual specification review

- Which preferences are mandatory eligibility rules, and which only affect ranking?
- Should tuition and living-cost preferences be separate fields?
- Which country/language identifiers will the source university data use?
- How should missing or uncertain preferences appear in the user journey?

These questions remain open for alignment with Davide; no client answers are invented here.
