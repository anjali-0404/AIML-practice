# GitHub Push Instructions

## Quick Commands to Push

```powershell
cd "d:\Elevate labs\EDA_Project"

# Add remote origin
git remote add origin https://github.com/anjali-0404/AIML-practice.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## If You Need to Authenticate:

### Option 1: Personal Access Token (Recommended)

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token"
3. Select scopes: `repo` (all), `gist`, `write:packages`
4. Copy the token
5. When prompted by Git:
   - Username: `your-github-username`
   - Password: `your-personal-access-token`

### Option 2: GitHub CLI

```powershell
# Install GitHub CLI first
winget install GitHub.cli

# Authenticate
gh auth login

# Then push
git push -u origin main
```

## Verify Push was Successful

```powershell
# Check remote
git remote -v

# Check status
git status

# View commit history
git log
```

## Files Included in Push:

✅ eda.py - Python script
✅ eda.ipynb - Jupyter notebook  
✅ README.md - Documentation
✅ QUICKSTART.md - Quick start guide
✅ PROJECT_COMPLETION_REPORT.txt - Project report
✅ Titanic-Dataset.csv - Dataset
✅ .gitignore - Git ignore rules

## After Successful Push:

Your repository will be visible at:
https://github.com/anjali-0404/AIML-practice

Total files: 7
Commits: 1
Branch: main
