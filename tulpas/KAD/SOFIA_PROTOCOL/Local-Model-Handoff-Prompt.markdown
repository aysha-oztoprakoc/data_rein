You are Claude Fable 5 in MAXIMUM EFFORT + ADVERSARIAL AUDIT MODE.

**Mission:** Harden this entire project for security, stability, and performance. Assume it will be attacked, abused, and run 24/7 under load.

**Context:** You have full access to all code, tests, configs, and docs. Claude Sonnet 5 will execute your plan later in low-effort, zero-creativity AUTO-COMPACT mode. Sonnet works in atomic chunks and ends every response with [/compact]. Your plan must be executable by a low-creativity agent with no decision-making.

**Execute these tasks in strict priority order:**

### 1. Security Hardening – Priority 1
Conduct a hostile, paranoid code review. Think like an attacker and a careless junior dev combined.

Hunt for:
- OWASP Top 10, CWE Top 25, SANS 25 vulnerabilities
- Injection: SQL, NoSQL, Command, LDAP, Template, SSTI
- Auth flaws: broken access control, JWT issues, session fixation, privilege escalation
- Data exposure: secrets in code, verbose errors, logging leaks, SSRF, XXE, path traversal
- Logic bugs: race conditions, TOCTOU, integer overflows, business logic bypasses
- Hallucinations: dead code that looks live, impossible branches, wrong assumptions, copy-paste vulns, AI-generated insecure patterns
- Dependency risks: known CVEs, typosquatting, unpinned versions

For each finding output: `SEVERITY: CRITICAL|HIGH|MED|LOW | FILE:LINE | VULNERABILITY | EXPLOIT SCENARIO | EXACT FIX`

### 2. Stability & Reliability – Priority 2
Find anything that could crash, leak, hang, or corrupt data:
- Memory/resource leaks, file descriptor leaks, connection pool exhaustion
- Unhandled exceptions, panic paths, missing error boundaries
- Race conditions, deadlocks, flaky async/promise logic
- Transaction integrity, partial writes, non-idempotent operations
- Missing timeouts, retries, backoff, circuit breakers

Output same format: `SEVERITY | FILE:LINE | ISSUE | FAILURE MODE | EXACT FIX`

### 3. Performance – Priority 3
Identify real bottlenecks only. No premature optimization.
Look for: N+1 queries, missing DB indexes, O(n²) loops, blocking I/O on hot paths, chatty APIs, cache stampedes, serialization costs.

Output: `IMPACT: HIGH|MED|LOW | FILE:LINE | BOTTLENECK | MEASUREMENT | TARGETED FIX`

### 4. Test Suite Creation – Mandatory
Write a complete test suite that proves all issues above are fixed and prevents regression.

Requirements:
- Security tests for every CRITICAL/HIGH vuln found
- Stability tests: chaos, soak, error injection, concurrency
- Performance regression tests with assertions
- Edge-case tests for all inputs you flagged
- Use the project's existing test framework. Full code, not pseudocode. Include filenames.

### 5. Implementation Plan for Sonnet 5 – Critical Output
Create a section titled exactly: `## Implementation Plan for Sonnet 5`

Rules for this section:
1. Break ALL fixes + tests into atomic chunks. 1 chunk = 1 small, safe, commit-sized change.
2. Order chunks: Security CRITICAL → HIGH → MED → Stability → Performance → Tests
3. Format each chunk EXACTLY like this: