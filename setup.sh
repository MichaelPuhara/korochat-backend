#!/bin/bash

echo "🚀 Setting up KoroChat Backend..."

# Navigate to backend directory
cd "$(dirname "$0")"

# Remove old virtual environments
echo "🧹 Cleaning up old virtual environments..."
rm -rf .venv venv env

# Create new virtual environment
echo "📦 Creating new virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Backend setup complete!"
echo ""
echo "To start the backend server:"
echo "  1. cd backend"
echo "  2. source .venv/bin/activate"
echo "  3. uvicorn main:app --reload"
echo ""
