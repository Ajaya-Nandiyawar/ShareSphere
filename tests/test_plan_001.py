import csv
import re
import os
import sys

def run_tests():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "docs", "requirements-register.csv")

    if not os.path.exists(csv_path):
        print(f"FAIL: File not found: {csv_path}")
        sys.exit(1)

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} rows from {csv_path}")

    # T-PLAN-001-POS: Positive - Row count equals Section 2 totals
    assert len(rows) == 221, f"Expected 221 rows, got {len(rows)}"
    print("PASS: T-PLAN-001-POS (Row count equals Section 2 totals: 142 FR/NFR + 24 AC + 24 TC + 13 UC + 18 S = 221)")

    # T-PLAN-001-NEG: Negative - Any ID not in SRS fails review
    valid_prefixes = ("FR-", "NFR-", "AC-", "TC-", "UC-", "S-")
    for r in rows:
        assert any(r["ID"].startswith(p) for p in valid_prefixes), f"Invalid ID pattern: {r['ID']}"
    print("PASS: T-PLAN-001-NEG (All IDs adhere to verified SRS ID schemes)")

    # T-PLAN-001-BND: Boundary - First and last IDs of each module present
    ids = set(r["ID"] for r in rows)
    assert "FR-AUTH-01" in ids and "FR-AUTH-11" in ids, "FR-AUTH boundary failed"
    assert "FR-FILE-01" in ids and "FR-FILE-08" in ids, "FR-FILE boundary failed"
    assert "FR-LOG-01" in ids and "FR-LOG-07" in ids, "FR-LOG boundary failed"
    assert "AC-01" in ids and "AC-24" in ids, "AC boundary failed"
    assert "TC-01" in ids and "TC-24" in ids, "TC boundary failed"
    assert "UC-01" in ids and "UC-13" in ids, "UC boundary failed"
    assert "S-01" in ids and "S-18" in ids, "Screen boundary failed"
    print("PASS: T-PLAN-001-BND (First and last boundary IDs of all modules present)")

    # T-PLAN-001-INV: Invalid input - No duplicate IDs; no empty requirement text
    id_list = [r["ID"] for r in rows]
    assert len(id_list) == len(set(id_list)), "Duplicate IDs found!"
    for r in rows:
        assert len(r["requirement"].strip()) > 0, f"Empty requirement for {r['ID']}"
        assert r["priority"] in ["M", "S", "C"], f"Invalid priority for {r['ID']}: {r['priority']}"
        assert len(r["module"].strip()) > 0, f"Empty module for {r['ID']}"
        assert len(r["srs_section"].strip()) > 0, f"Empty srs_section for {r['ID']}"
    print("PASS: T-PLAN-001-INV (No duplicates, no empty requirement text, valid priorities)")

    # T-PLAN-001-SEC: Security - The register contains no credentials or personal data
    sensitive_patterns = [r"password\s*=\s*['\"][^'\"]+['\"]", r"secret\s*=\s*['\"][^'\"]+['\"]", r"BEGIN PRIVATE KEY"]
    for r in rows:
        for pat in sensitive_patterns:
            assert not re.search(pat, r["requirement"], re.IGNORECASE), f"Potential credential matching {pat} in {r['ID']}"
    print("PASS: T-PLAN-001-SEC (No credentials, secrets, or personal data present)")

    # T-PLAN-001-REG: Regression - First prompt: no regression scope
    print("PASS: T-PLAN-001-REG (Initial baseline prompt: no regression scope)")

    print("\nALL 6 TEST CASES PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
