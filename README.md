# SmartAssistent - Customer Service Chatbot

A modern, AI-powered customer service chatbot built with Flask, TensorFlow, and NLTK. Features a beautiful, responsive UI with real-time chat functionality.

## 🚀 Features

- **AI-Powered Responses**: Uses TensorFlow and NLTK for intelligent conversation
- **Modern UI**: Beautiful, responsive design with smooth animations
- **Real-time Chat**: Instant messaging with typing indicators
- **Mobile Responsive**: Works perfectly on all devices
- **Interactive Chat Icon**: Enhanced with animations and notifications

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **AI/ML**: TensorFlow, NLTK, scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Phosphor Icons
- **Deployment**: Vercel

## 📁 Project Structure

```
Chatbot/
├── app.py                 # Main Flask application
├── intents.json          # Training data for the chatbot
├── words.pkl             # Preprocessed words
├── classes.pkl           # Intent classes
├── vivek_customer_service_chatbot.h5  # Trained model
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
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
3. **Model Files**: Ensure all model files are in the repository:
   - `vivek_customer_service_chatbot.h5`
   - `words.pkl`
   - `classes.pkl`
   - `intents.json`

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

4. **Environment Variables** (if needed)
   - Add any environment variables in the Vercel dashboard

5. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete (may take 5-10 minutes for first deployment)

### ⚠️ Important Notes

- **Model Size**: TensorFlow models can be large. Vercel has a 50MB limit for serverless functions
- **Cold Starts**: First request may be slower due to model loading
- **NLTK Downloads**: Will be downloaded automatically on first request
- **Memory Usage**: Monitor memory usage in Vercel dashboard

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
2. Retrain the model (requires local development setup)
3. Update the model file

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

1. **Model Loading Errors**
   - Ensure all model files are in the repository
   - Check file paths in `app.py`

2. **NLTK Download Issues**
   - NLTK data will be downloaded automatically on Vercel
   - First request may take longer

3. **Memory Issues**
   - Monitor Vercel function logs
   - Consider optimizing model size

4. **Build Failures**
   - Check `requirements.txt` for correct versions
   - Ensure all dependencies are compatible

### Vercel-Specific Issues

1. **Function Timeout**
   - Increase `maxDuration` in `vercel.json`
   - Optimize model loading

2. **Large Bundle Size**
   - Consider using smaller model variants
   - Optimize dependencies

## 📞 Support

For issues or questions:
- Check Vercel deployment logs
- Review function logs in Vercel dashboard
- Ensure all model files are properly included

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Chatting! 🤖💬** 