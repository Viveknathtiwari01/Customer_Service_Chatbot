#!/bin/bash

echo "🚀 Preparing SmartAssistent Chatbot for Vercel Deployment..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    exit 1
fi

# Check if all required files exist
echo "📋 Checking required files..."

required_files=(
    "app.py"
    "intents.json"
    "words.pkl"
    "classes.pkl"
    "vivek_customer_service_chatbot.h5"
    "requirements.txt"
    "vercel.json"
    "templates/index.html"
    "static/css/style.css"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Missing required file: $file"
        exit 1
    else
        echo "✅ Found: $file"
    fi
done

# Check file sizes
echo ""
echo "📊 Checking file sizes..."

model_size=$(du -h "vivek_customer_service_chatbot.h5" | cut -f1)
echo "🤖 Model size: $model_size"

# Warning for large models
if [ $(du -m "vivek_customer_service_chatbot.h5" | cut -f1) -gt 45 ]; then
    echo "⚠️  WARNING: Model file is large (>45MB). Vercel has a 50MB limit for serverless functions."
    echo "   Consider optimizing your model or using a smaller variant."
fi

echo ""
echo "🔧 Preparing for deployment..."

# Add all files to git
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "📝 Committing changes..."
    git commit -m "Prepare for Vercel deployment - $(date)"
fi

echo ""
echo "✅ Ready for deployment!"
echo ""
echo "📋 Next steps:"
echo "1. Push to GitHub:"
echo "   git push origin main"
echo ""
echo "2. Deploy on Vercel:"
echo "   - Go to https://vercel.com"
echo "   - Click 'New Project'"
echo "   - Import your GitHub repository"
echo "   - Click 'Deploy'"
echo ""
echo "3. Wait for deployment (5-10 minutes for first deployment)"
echo ""
echo "🔗 Your chatbot will be available at: https://your-project-name.vercel.app"
echo ""
echo "📚 For detailed instructions, see README.md" 