# SmartAssistent - Customer Service Chatbot

A modern, AI-powered customer service chatbot built with Flask and NLTK. Features a beautiful, responsive UI with real-time chat functionality.

## 🚀 Features

- **Pattern-Based AI**: Uses intelligent pattern matching for conversation
- **Modern UI**: Beautiful, responsive design with smooth animations
- **Real-time Chat**: Instant messaging with typing indicators
- **Mobile Responsive**: Works perfectly on all devices
- **Interactive Chat Icon**: Enhanced with animations and notifications

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **AI/ML**: NLTK, Pattern Matching
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Phosphor Icons
- **Deployment**: Vercel

## 📁 Project Structure

```
Chatbot/
├── app.py                 # Main Flask application
├── intents.json          # Training data for the chatbot
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
├── runtime.txt          # Python version specification
├── templates/
│   └── index.html       # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css    # Stylesheets
│   └── images/          # Images and logos
└── README.md
```

## 🚀 Deployment on Vercel

### Prerequisites

1. **GitHub Account**: Your code should be in a GitHub repository
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **Required Files**: Ensure all files are in the repository:
   - `app.py`
   - `intents.json`
   - `requirements.txt`
   - `vercel.json`
   - `runtime.txt`

### Deployment Steps

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect it's a Python project

3. **Configure Build Settings**
   - **Framework Preset**: Other
   - **Build Command**: Leave empty (Vercel will auto-detect)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

4. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete (2-3 minutes)

### ✅ Advantages of This Approach

- **Lightweight**: No heavy ML libraries
- **Fast Deployment**: Quick build times
- **Reliable**: No compatibility issues
- **Cost-Effective**: Minimal resource usage
- **Scalable**: Works well with serverless

## 🏃‍♂️ Local Development

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Application**
   - Open `http://localhost:5000` in your browser

## 📱 Usage

1. **Open the Application**: Navigate to your deployed URL
2. **Start Chatting**: Click the chat icon in the bottom-right corner
3. **Type Messages**: Send messages and get AI-powered responses
4. **Explore Features**: Navigate between Home, About, and Contact sections

## 🔧 Customization

### Adding New Intents

1. Edit `intents.json` to add new conversation patterns
2. Add patterns and responses for new intents
3. Deploy the updated version

### Styling Changes

- Modify `static/css/style.css` for visual changes
- Update `templates/index.html` for structural changes

### Chat Icon Customization

The chat icon can be customized in the CSS:
- Change colors in `.chat-icon`
- Modify animations in `@keyframes`
- Update text in the HTML

## 🐛 Troubleshooting

### Common Issues

1. **Build Failures**
   - Check `requirements.txt` for correct versions
   - Ensure Python 3.11 compatibility

2. **NLTK Download Issues**
   - NLTK data will be downloaded automatically on Vercel
   - First request may take longer

3. **Pattern Matching Issues**
   - Check `intents.json` format
   - Ensure patterns are properly formatted

### Vercel-Specific Issues

1. **Function Timeout**
   - Pattern matching is fast, should not timeout
   - Check function logs in Vercel dashboard

2. **Memory Issues**
   - Lightweight approach uses minimal memory
   - Monitor usage in Vercel dashboard

## 📞 Support

For issues or questions:
- Check Vercel deployment logs
- Review function logs in Vercel dashboard
- Ensure all files are properly included

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Chatting! 🤖💬** 