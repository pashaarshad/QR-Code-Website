from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

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
        return 'No link provided', 400
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
    return send_file(buf, mimetype='image/png', as_attachment=True, download_name='qrcodeap.png')

if __name__ == '__main__':
    app.run(debug=True)