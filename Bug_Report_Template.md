# Bug Report Template

## Bug ID: BR-001
## Title: [Brief description of the issue]

## Severity:
- [ ] Critical (System crash, data loss)
- [ ] High (Major functionality broken)
- [ ] Medium (Feature partially broken)
- [ ] Low (Minor UI issue, cosmetic)

## Priority:
- [ ] P1 (Fix immediately)
- [ ] P2 (Fix in next sprint)
- [ ] P3 (Fix when possible)
- [ ] P4 (Nice to have)

## Environment:
- Browser: [Chrome/Firefox/Edge]
- OS: [Windows/Mac/Linux]
- URL: [test_app.html]
- Test Data: [username/password used]

## Steps to Reproduce:
1. Open `test_app.html` in browser
2. Enter [specific username]
3. Enter [specific password]
4. Click Login button
5. Observe [what happens]

## Expected Result:
[What should happen according to requirements]

## Actual Result:
[What actually happened]

## Screenshots:
[Attach screenshots if applicable]
- Before login
- After login attempt
- Error message

## Additional Notes:
- Browser console errors
- Network requests
- Any other observations

## Root Cause:
[If known]

## Fix Suggestion:
[QA's recommendation for fix]

## Status:
- [ ] Open
- [ ] In Progress
- [ ] Fixed
- [ ] Closed
- [ ] Won't Fix

## Assigned To:
[Developer name]

## Reported By:
[QA Engineer name]

## Date Reported:
[Date]

## Date Fixed:
[Date]

---

## Example Bug Report

### Bug ID: BR-001
### Title: Login fails with valid credentials on Firefox

### Severity: High
### Priority: P1

### Environment:
- Browser: Firefox 125.0
- OS: Windows 11
- URL: file:///C:/Users/dhruv/OneDrive/Desktop/login_automation/test_app.html
- Test Data: username="admin", password="admin123"

### Steps to Reproduce:
1. Open test_app.html in Firefox
2. Enter username: admin
3. Enter password: admin123
4. Click Login button

### Expected Result:
Dashboard should appear with success message

### Actual Result:
Page shows "Invalid credentials - error in login"

### Screenshots:
[Attach screenshot of error message]

### Additional Notes:
- Works fine in Chrome
- Console shows no JavaScript errors
- Network tab shows no failed requests

### Root Cause:
Browser compatibility issue with JavaScript execution

### Fix Suggestion:
Test JavaScript code across different browsers, add browser-specific handling if needed

### Status: Open
### Assigned To: Developer Team
### Reported By: QA Engineer
### Date Reported: April 10, 2026