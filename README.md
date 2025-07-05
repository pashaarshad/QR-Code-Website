# 🚀 QR Code Generator

<div align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</div>

<div align="center">
  <h3>✨ A modern, beautiful, and lightning-fast QR code generator</h3>
  <p>Transform any URL or text into a professional QR code with our sleek web interface</p>
</div>

---

## 🌟 Features

- **⚡ Instant Generation**: Create QR codes in milliseconds
- **🎨 Modern UI/UX**: Beautiful, responsive design with smooth animations
- **📱 Mobile-First**: Optimized for all devices and screen sizes
- **💾 Easy Download**: One-click PNG download functionality
- **📋 Copy to Clipboard**: Quick link copying with visual feedback
- **🔒 Privacy-First**: No data stored or tracked
- **🎭 Interactive**: Hover effects and loading animations
- **📊 High Quality**: Crisp, scalable QR codes

## 🚀 Quick Start

### Prerequisites

- Python 3.7+ installed on your system
- pip (Python package manager)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 🎯 Usage

1. **Enter your content**: Type or paste any URL or text into the input field
2. **Generate**: Click the "Generate QR Code" button
3. **Preview**: View your QR code instantly with a beautiful preview
4. **Download**: Click "Download PNG" to save the QR code to your device
5. **Copy**: Use the "Copy Link" button to copy the original URL to clipboard

## 🏗️ Project Structure

```
qr-code-generator/
├── app.py                 # Lightweight Flask application
├── requirements.txt       # Python dependencies (Flask + Gunicorn only)
├── runtime.txt           # Python version for hosting platforms
├── Procfile              # Heroku deployment configuration
├── render-build.sh       # Render.com build script
├── README.md             # Project documentation
├── templates/
│   └── index.html        # Main HTML template with client-side QR generation
└── venv/                 # Virtual environment (created after setup)
```

## 🛠️ Technical Details

### Backend
- **Flask**: Lightweight Python web framework for serving the application
- **Gunicorn**: Production WSGI server for hosting
- **Client-Side QR Generation**: No server-side image processing dependencies

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript**: Interactive features and QR code generation
- **QRCode.js**: Client-side QR code generation library
- **Font Awesome**: Beautiful icons
- **Google Fonts**: Inter font family for modern typography

### Architecture Benefits

| Feature | Technology | Benefit |
|---------|------------|---------|
| Client-Side QR Generation | QRCode.js | No server load, works on any hosting platform |
| No File I/O | Browser Canvas API | No file system permissions needed |
| Lightweight Backend | Flask only | Minimal server requirements |
| CDN Resources | External JS/CSS | Fast loading, cached resources |
| Progressive Enhancement | Fallback support | Works on all browsers |

## 🚀 Deployment

### Render.com
1. Connect your GitHub repository to Render
2. Use these settings:
   - **Environment**: Python 3.11
   - **Build Command**: `chmod +x render-build.sh && ./render-build.sh`
   - **Start Command**: `gunicorn app:app`

### Heroku
1. Create a Heroku app
2. Connect your GitHub repository
3. The `Procfile` is already configured
4. Deploy automatically

### Vercel
1. Connect your GitHub repository
2. Set Framework Preset to "Other"
3. Build Command: `pip install -r requirements.txt`
4. Output Directory: `.`

### Railway
1. Connect your GitHub repository  
2. Railway will auto-detect the Python app
3. Uses `requirements.txt` and `Procfile` automatically

### Local Development
```bash
python app.py
```

### Production with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework
- [qrcode](https://github.com/lincolnloop/python-qrcode) - QR code generation library
- [Font Awesome](https://fontawesome.com/) - Icons
- [Google Fonts](https://fonts.google.com/) - Typography

## 📊 Stats

- **Lines of Code**: ~500
- **File Size**: ~50KB total
- **Dependencies**: 3 main packages
- **Browser Support**: All modern browsers
- **Mobile Support**: iOS 10+, Android 6+

## 🔮 Future Enhancements

- [ ] Custom QR code colors
- [ ] Batch QR code generation
- [ ] QR code analytics
- [ ] SVG export option
- [ ] Dark mode toggle
- [ ] Multiple format support (JPEG, WebP)
- [ ] QR code scanner functionality
- [ ] API endpoints for integration

---

<div align="center">
  <p>Made with ❤️ by <strong>Arshad</strong></p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>
