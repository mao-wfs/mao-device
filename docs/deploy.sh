#!/bin/bash
# Check current branch is "master"
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [[ $current_branch != master ]]; then
  echo "execution on non-master branch is not allowed"
  exit 1
fi

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project
make html

# Go to html folder
cd build/html
# Add changes to git
git add .

# Commit changes
msg="Rebulding site date"
if [ $# -eq 1 ]; then
  msg="$1"
fi
git commit -m "$msg"

# Push source and build repos
git push origin gh-pages

# Come back up to the project root
cd ../../
