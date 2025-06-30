@echo off
echo 🚀 Preparing SmartAssistent Chatbot for Vercel Deployment...
echo.

REM Check if git is initialized
if not exist ".git" (
    echo ❌ Git repository not found. Please initialize git first:
    echo    git init
    echo    git add .
    echo    git commit -m "Initial commit"
    pause
    exit /b 1
)

echo 📋 Checking required files...
echo.

REM Check required files
set "required_files=app.py intents.json words.pkl classes.pkl vivek_customer_service_chatbot.h5 requirements.txt vercel.json templates\index.html static\css\style.css"

for %%f in (%required_files%) do (
    if exist "%%f" (
        echo ✅ Found: %%f
    ) else (
        echo ❌ Missing required file: %%f
        pause
        exit /b 1
    )
)

echo.
echo 🔧 Preparing for deployment...

REM Add all files to git
git add .

REM Check if there are changes to commit
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo ℹ️  No changes to commit
) else (
    echo 📝 Committing changes...
    git commit -m "Prepare for Vercel deployment"
)

echo.
echo ✅ Ready for deployment!
echo.
echo 📋 Next steps:
echo 1. Push to GitHub:
echo    git push origin main
echo.
echo 2. Deploy on Vercel:
echo    - Go to https://vercel.com
echo    - Click "New Project"
echo    - Import your GitHub repository
echo    - Click "Deploy"
echo.
echo 3. Wait for deployment (5-10 minutes for first deployment)
echo.
echo 🔗 Your chatbot will be available at: https://your-project-name.vercel.app
echo.
echo 📚 For detailed instructions, see README.md
echo.
pause 