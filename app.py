from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the QR code generator page"""
    return render_template('index.html')

@app.route('/health')
def health_check():
    """Health check endpoint for hosting platforms"""
    return {'status': 'healthy', 'message': 'QR Code Generator is running'}

if __name__ == '__main__':
    # Only for local development
    app.run(debug=True, host='0.0.0.0', port=5000)