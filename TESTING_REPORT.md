# Student Handbook AI Assistant – Testing Report

## 1. Introduction

The Student Handbook AI Assistant was tested using its FastAPI POST `/ask` endpoint. The tests checked information retrieval, answer generation and fallback responses.

## 2. Manual API Tests

### Test 1: Live Class Times

**Question:** What are the live class times?

**Answer:**
- Monday Morning Sessions: 9 am – 11 am.
- Wednesday Evening Sessions: 6 pm – 8 pm.

**Source:** Page 7, Page 11, Page 12.

**Result:** PASSED

### Test 2: Attendance Requirement

**Question:** What is the attendance requirement?

**Answer:** I don't know. The handbook does not provide this information.

**Source:** No source returned.

**Result:** PASSED

### Test 3: Student Accommodation

**Question:** Does Zaio provide free accommodation to students?

**Answer:** I don't know. The handbook does not provide this information.

**Source:** No source returned.

**Result:** PASSED

## 3. Automated Unit Tests

Automated tests were executed using:

`python -m pytest tests/ -v`

The following tests were completed:

| Test | Result |
|---|---|
| Home endpoint | PASSED |
| Empty question | PASSED |
| Invalid request | PASSED |
| Accommodation fallback | PASSED |
| Attendance fallback | PASSED |

**Total tests:** 5

**Passed:** 5

**Failed:** 0

## 4. Conclusion

The Student Handbook AI Assistant successfully processes student questions through its API, retrieves relevant handbook information and returns the required fallback response when information is unavailable.

All five automated tests passed successfully.