# Complete GitHub Large File Error Documentation (Beginner → Advanced)

You got this error because GitHub does **NOT allow files larger than 100 MB** in normal Git repositories.

Your file:

```bash id="c0z8my"
month-2/ml/practice/DOHMH_New_York_City_Restaurant_Inspection_Results.csv
```

Size:

```bash id="z0w8p8"
139.37 MB
```

GitHub Limit:

```bash id="2vl7t3"
100 MB
```

---

# Why This Error Happens Internally

When you run:

```bash id="v9ikz4"
git add .
git commit -m "message"
```

Git stores snapshots of files inside `.git/objects`.

Even if you later delete the file:

```bash id="g10s4h"
git rm --cached file.csv
```

the old commit still contains the file history.

So GitHub still sees:

```bash id="h3m4l7"
139 MB file exists in commit history
```

and blocks the push.

---

# REAL SOLUTION (Your Case)

You already made:

1. First commit with large file
2. Second commit deleting large file

But the first commit still exists locally.

So we must remove those commits and create clean commits.

---

# STEP-BY-STEP FIX (SAFE METHOD)

---

# STEP 1 — Check Current Status

Run:

```bash id="4vf2z1"
git log --oneline
```

Example output:

```bash id="sh6gn5"
6ec67ea Remove large dataset file from tracking
a1b2c3d update cms and loading in frontend
```

You have 2 local commits not pushed.

---

# STEP 2 — Remove Last 2 Commits (SAFE)

Run:

```bash id="l1x0k9"
git reset --soft HEAD~2
```

## What This Does

| Option   | Meaning                |
| -------- | ---------------------- |
| `--soft` | keeps your files       |
| `HEAD~2` | removes last 2 commits |

Now:

* commits removed
* files still exist locally
* nothing deleted from computer

---

# STEP 3 — Remove Large File From Git Tracking

Run:

```bash id="sz4wjm"
git rm --cached "month-2/ml/practice/DOHMH_New_York_City_Restaurant_Inspection_Results.csv"
```

## Important

| Command    | Meaning              |
| ---------- | -------------------- |
| `rm`       | remove               |
| `--cached` | remove only from git |
| local file | stays on your PC     |

So your CSV still exists on your computer.

---

# STEP 4 — Prevent Future Uploads

Add to `.gitignore`

Run:

```bash id="q0a6q4"
echo "month-2/ml/practice/DOHMH_New_York_City_Restaurant_Inspection_Results.csv" >> .gitignore
```

Now Git will ignore this file forever.

---

# STEP 5 — Add Files Again

Run:

```bash id="p1q6a5"
git add .
```

---

# STEP 6 — Create New Clean Commit

Run:

```bash id="ms3r0g"
git commit -m "Add ML files without large dataset"
```

---

# STEP 7 — Push to GitHub

Run:

```bash id="m4j3e5"
git push origin main
```

Now it should work.

---

# VISUAL FLOW

```text
OLD HISTORY
────────────
Commit 1 → contains 139MB file ❌
Commit 2 → deletes file

GitHub still sees Commit 1

──────────────────────────────

AFTER RESET
────────────
No bad commits

New Commit → clean project ✅

Push works
```

---

# BEGINNER GIT CONCEPTS

---

# What is HEAD?

```text
HEAD = current latest commit
```

Example:

```text
Commit A
Commit B
Commit C ← HEAD
```

---

# What is HEAD~1 ?

```text
HEAD~1 = one commit before HEAD
```

Example:

```text
Commit A
Commit B ← HEAD~1
Commit C ← HEAD
```

---

# What is HEAD~2 ?

```text
HEAD~2 = two commits before HEAD
```

---

# Difference Between Reset Types

| Command   | Removes Commit | Keeps Files | Keeps Staging |
| --------- | -------------- | ----------- | ------------- |
| `--soft`  | ✅              | ✅           | ✅             |
| `--mixed` | ✅              | ✅           | ❌             |
| `--hard`  | ✅              | ❌           | ❌             |

---

# SPECIAL CASES

---

# CASE 1 — File Already Pushed to GitHub

If large file already pushed:

Use:

```bash id="xixg62"
git filter-branch
```

or

```bash id="5dcf6u"
git filter-repo
```

to rewrite history.

Then:

```bash id="mbf9q3"
git push --force
```

---

# CASE 2 — Team Project

Never use force push without permission.

Because:

```text
Force push rewrites history
```

and may break teammates' branches.

---

# CASE 3 — ML/Dataset Projects

Best practice:

| File Type | Recommended  |
| --------- | ------------ |
| datasets  | Kaggle/Drive |
| models    | Git LFS      |
| notebooks | GitHub       |
| small CSV | GitHub       |

---

# CASE 4 — Use Git LFS

For huge ML files:

Install:

```bash id="4bqz6g"
sudo apt install git-lfs
```

Setup:

```bash id="brkgqv"
git lfs install
```

Track CSV:

```bash id="v7kxyf"
git lfs track "*.csv"
```

Commit:

```bash id="3pk3c5"
git add .gitattributes
git commit -m "Configure Git LFS"
```

---

# CASE 5 — Accidentally Added node_modules

Fix:

```bash id="3a6gg2"
git rm -r --cached node_modules
echo "node_modules/" >> .gitignore
```

---

# CASE 6 — Remove All Large Files

Find large files:

Linux:

```bash id="08z9es"
find . -type f -size +100M
```

---

# PROFESSIONAL .gitignore FOR MERN + ML

Example:

```gitignore id="p4skyl"
node_modules/
.env
dist/
build/

*.csv
*.zip
*.tar.gz
*.h5
*.pt
*.pth
*.pkl
*.joblib

.DS_Store
```

---

# PROFESSIONAL GIT WORKFLOW

```text
1. git pull
2. code changes
3. git status
4. git add .
5. git commit -m "message"
6. git push
```

---

# BEST PRACTICES

| Good Practice          | Why                  |
| ---------------------- | -------------------- |
| Use `.gitignore` early | avoid mistakes       |
| Keep repo small        | faster clone         |
| Use Git LFS for ML     | supports large files |
| Never commit secrets   | security             |
| Use meaningful commits | maintainability      |

---

# YOUR FINAL FIX COMMANDS

Run EXACTLY:

```bash id="2w5e5x"
git reset --soft HEAD~2

git rm --cached "month-2/ml/practice/DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

echo "month-2/ml/practice/DOHMH_New_York_City_Restaurant_Inspection_Results.csv" >> .gitignore

git add .

git commit -m "Add ML practice files without dataset"

git push origin main
```

---

# Expected Success Output

```text
Enumerating objects...
Writing objects...
To github.com:user/repo.git
   abc123..def456 main -> main
```

No more GH001 error.
