# Security Testing: Attack Vectors Summary

This repository contains three independent attack vectors for testing workflow safety against malicious code injection via git patches.

## Attack Vector 1: CI/CD Exfiltration ✅

**File**: [`.github/workflows/exfiltrate.yml`](.github/workflows/exfiltrate.yml)

**How it works**:
- Runs automatically on every push, PR, or workflow dispatch
- Cannot be blocked by `--no-verify` (it's not a git hook)
- Exfiltrates environment variables from GitHub Actions runners
- Also captures `GITHUB_TOKEN` and repository context

**What gets exfiltrated**:
- Full environment variables as JSON
- GitHub Actions secrets (GITHUB_TOKEN)
- Repository metadata

**Trigger**: Automatically runs when code is pushed to GitHub

---

## Attack Vector 2: Malicious Filenames (Command Injection) ✅

**Directory**: [`malicious-filenames/`](malicious-filenames/)

**How it works**:
- Creates files with names containing shell metacharacters
- If a server processes these filenames without proper quoting, commands execute
- Common vulnerable scenarios:
  - `for file in $(ls); do ...` (unquoted expansion)
  - `eval` with filename variables
  - Shell scripts that don't quote `$file`

**Example filenames**:
- `test$(whoami).txt` - Command substitution
- `test;ls;.txt` - Command chaining
- ``test`id`.txt`` - Backtick execution

**Demo**: [`vulnerable-script-example.sh`](malicious-filenames/vulnerable-script-example.sh)

**Trigger**: When filenames are processed by vulnerable shell scripts

---

## Attack Vector 3: Git Config Injection ✅

**Files**:
- [`.gitconfig-malicious`](.gitconfig-malicious)
- [`.gitattributes-malicious`](.gitattributes-malicious)
- [`GIT-CONFIG-ATTACK.md`](GIT-CONFIG-ATTACK.md)

**How it works**:
- Injects malicious git configuration via `[include]` directives
- Poisons common git commands (status, log, diff)
- Uses git filters and diff drivers to exfiltrate file contents

**Attack methods**:
1. **Pager injection**: `git log` triggers exfiltration
2. **Alias poisoning**: `git status` exfiltrates env vars
3. **Content filters**: File contents leaked when staged
4. **Diff drivers**: File contents leaked when diffed

**Activation required**:
- Victim must run `git config include.path` with malicious path
- Or attacker injects into `.git/config` (requires write access)

**Trigger**: When git commands are run after malicious config is included

---

## Testing Methodology

### For CI/CD Attack
1. Push any code to trigger workflow
2. Check webhook.site for exfiltrated data
3. No user interaction needed ✓

### For Filename Attack
1. Clone repo with malicious filenames
2. Run any shell script that processes filenames unsafely
3. Example: `cd malicious-filenames && ./vulnerable-script-example.sh`

### For Git Config Attack
1. Requires victim to include malicious config:
   ```bash
   git config --local include.path ../.gitconfig-malicious
   ```
2. Then any git command triggers exfiltration
3. Example: `git status`, `git log`, `git diff`

---

## Defense Recommendations

### Against CI/CD Attacks
- Review all workflow files in `.github/workflows/`
- Use branch protection rules
- Require approval for workflow changes
- Audit actions for unexpected network calls

### Against Filename Attacks
- Always quote shell variables: `"$file"` not `$file`
- Use `find ... -print0 | xargs -0` instead of `$(ls)`
- Avoid `eval` with user-controlled data
- Use safe file processing: `while IFS= read -r -d '' ...`

### Against Git Config Attacks
- Never run `git config include.path` with untrusted paths
- Audit `.git/config` for `[include]` sections
- Use `git config --show-origin --list` to verify config sources
- Disable automatic filters in sensitive environments

---

## Webhook Endpoint

All attacks send data to: `https://webhook.site/1793fdf7-26c0-494b-b8b0-5a38218c100a`

Check this URL to see exfiltrated data during testing.
