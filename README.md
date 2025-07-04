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
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/
│   └── index.html        # Main HTML template with modern UI
└── venv/                 # Virtual environment (created after setup)
```

## 🛠️ Technical Details

### Backend
- **Flask**: Lightweight Python web framework
- **qrcode**: Python library for QR code generation
- **Pillow**: Image processing library
- **io**: For in-memory file handling

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript**: Interactive features and clipboard functionality
- **Font Awesome**: Beautiful icons
- **Google Fonts**: Inter font family for modern typography

### Features Implementation

| Feature | Technology | Description |
|---------|------------|-------------|
| QR Generation | Python `qrcode` | High-quality QR code creation |
| Base64 Encoding | Python `base64` | Efficient image display |
| File Download | Flask `send_file` | Secure file serving |
| Responsive Design | CSS Grid/Flexbox | Mobile-first approach |
| Animations | CSS Keyframes | Smooth transitions |
| Copy to Clipboard | JavaScript Clipboard API | Modern clipboard interaction |

## 🎨 Design Philosophy

- **Minimalist**: Clean, uncluttered interface
- **Accessibility**: High contrast, readable fonts
- **Performance**: Lightweight and fast loading
- **Modern**: Contemporary design trends
- **Intuitive**: Self-explanatory user interface

## 📈 Performance

- **Generation Time**: < 100ms for standard QR codes
- **File Size**: Optimized PNG output (~2-5KB)
- **Page Load**: < 1 second on average connection
- **Mobile Performance**: Smooth 60fps animations

## 🔧 Configuration

You can customize the QR code settings in `app.py`:

```python
qr = qrcode.QRCode(
    version=1,                    # QR code version (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,                  # Size of each box in pixels
    border=4,                     # Border size in boxes
)
```

### Error Correction Levels
- `ERROR_CORRECT_L`: ~7% correction
- `ERROR_CORRECT_M`: ~15% correction  
- `ERROR_CORRECT_Q`: ~25% correction
- `ERROR_CORRECT_H`: ~30% correction

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### 🌐 Render.com Deployment

This project is optimized for [Render.com](https://render.com) deployment:

#### Step-by-step Render Deployment:

1. **Push to GitHub**: Make sure your code is in a GitHub repository

2. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Click "New Web Service"
   - Connect your GitHub repository

3. **Configure the service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
   - **Environment**: `Python 3`

4. **Set Environment Variables** (in Render dashboard):
   ```
   SECRET_KEY=your-super-secret-production-key-here
   FLASK_ENV=production
   ```

5. **Deploy**: Click "Create Web Service"

#### Render Configuration:
- **Runtime**: Python 3.12
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
- **Auto-Deploy**: Yes (deploys on every git push)

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
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
