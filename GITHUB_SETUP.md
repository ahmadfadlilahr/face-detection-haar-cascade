# How to Push Your Project to GitHub

Follow these steps to push this project to GitHub:

## 1. Initialize the Git Repository (if not already done)

```
cd "d:\Projek\New folder\Deteksi Wajah dengan Harr Cascade"
git init
```

## 2. Add All Files to the Repository

```
git add -A
```

## 3. Make the Initial Commit

```
git commit -m "Initial commit"
```

## 4. Create a New Repository on GitHub

- Go to https://github.com/new
- Enter a repository name, e.g., "face-detection-haar-cascade"
- Add a description (optional)
- Choose whether the repository should be public or private
- Do NOT initialize with README, .gitignore, or license (as we already have these files)
- Click "Create repository"

## 5. Connect Your Local Repository to GitHub

After creating your repository on GitHub, you'll see instructions. Run these commands:

```
git remote add origin https://github.com/your-username/face-detection-haar-cascade.git
git branch -M main
git push -u origin main
```

Replace `your-username` with your GitHub username.

## 6. Verify Your Repository on GitHub

- Go to https://github.com/your-username/face-detection-haar-cascade
- You should see all your project files there

## 7. Future Updates

After making changes to your code:

```
git add -A
git commit -m "Description of changes"
git push
```
