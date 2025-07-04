from flask import Flask, render_template, request, send_file, jsonify, flash, redirect
import qrcode
import io
import re
from urllib.parse import urlparse
import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

def is_valid_url(url):
    """Check if the provided string is a valid URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def generate_filename(link):
    """Generate a meaningful filename for the QR code"""
    if is_valid_url(link):
        domain = urlparse(link).netloc
        # Clean domain name for filename
        domain = re.sub(r'[^\w\-_.]', '_', domain)
        return f"qrcode_{domain}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    else:
        # For text, use first few characters
        text_part = re.sub(r'[^\w\-_.]', '_', link[:20])
        return f"qrcode_{text_part}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

@app.route('/', methods=['GET', 'POST'])
def index():
    import base64
    qr_img = None
    link_val = ''
    if request.method == 'POST':
        link = request.form.get('link')
        link_val = link
        if link:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            buf.seek(0)
            qr_img = base64.b64encode(buf.getvalue()).decode('utf-8')
    return render_template('index.html', qr_img=qr_img, link_val=link_val)

@app.route('/download', methods=['POST'])
def download():
    link = request.form.get('link')
    if not link:
        flash('No link provided', 'error')
        return redirect('/')
    
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        
        # Generate a meaningful filename
        filename = generate_filename(link)
        
        return send_file(buf, mimetype='image/png', as_attachment=True, download_name=filename)
    except Exception as e:
        flash(f'Error generating QR code: {str(e)}', 'error')
        return redirect('/')

if __name__ == '__main__':
    # Only for local development; Gunicorn will run the app in production
    app.run(debug=True)