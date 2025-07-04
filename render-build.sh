#!/usr/bin/env bash
# Render build script

# Update pip to latest version
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import flask, qrcode, gunicorn; print('All dependencies installed successfully!')"

echo "Build completed successfully!"
