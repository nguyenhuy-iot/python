#!/bin/bash

set -e

echo "🚀 Starting script..."

# Create virtual environment if it does not exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run main Python script
echo "▶️ Running srt_to_mp3.py..."
python srt_to_mp3.py

# Deactivate virtual environment
echo "🧹 Deactivating virtual environment..."
deactivate

echo "🎉 Done!"
