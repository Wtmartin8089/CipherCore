#!/bin/bash
echo "🔧 Activating virtual environment..."
source venv/bin/activate || { echo '❌ Failed to activate venv'; exit 1; }

echo "🚀 Launching Kivy GUI..."
python ui/gui.py || { echo '❌ GUI crashed'; exit 1; }

