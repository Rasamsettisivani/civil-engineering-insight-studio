# 🏗️ Civil Engineering Insight Studio

An AI-powered web application that analyzes civil engineering structures from images using Google's Gemini AI model. Upload an image of any construction or structure, and get detailed insights about materials, components, and engineering features.

## ✨ Features

- 🔍 Automatic structure type identification
- 🧱 Material composition analysis
- 🏛️ Structural component detection
- 📊 Construction progress assessment
- 💡 Engineering insights and recommendations
- 🎨 Modern, responsive UI with gradient design

## 🛠️ Technologies Used

- **Streamlit** - Web application framework
- **Google Generative AI (Gemini)** - AI model for image analysis
- **Python-dotenv** - Environment variable management
- **Pillow (PIL)** - Image processing

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher installed
- A Google API key for Gemini AI
- pip (Python package manager)

## 🚀 Installation & Setup

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd civil-engineering-insight-studio
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:
- streamlit
- google-generativeai
- python-dotenv
- Pillow

### 3. Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

**To get your Google API key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy and paste it into your `.env` file

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your default web browser at `http://localhost:8501`

## 📖 How to Use

1. **Launch the Application** - Run the command above
2. **Upload an Image** - Click the upload button and select a JPG, JPEG, or PNG image of a civil engineering structure
3. **Add Optional Prompt** - Enter any specific questions or details you want to know (optional)
4. **Analyze** - Click the "🔍 Analyze Structure" button
5. **View Results** - Get a detailed analysis report including:
   - Type of structure
   - Materials used
   - Structural components
   - Construction stage
   - Notable engineering features

## 📁 Project Structure

```
civil-engineering-insight-studio/
│
├── app.py                          # Main application file
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (create this)
├── README.md                      # Project documentation
├── Civil Engineering Insight Studio.docx  # Additional documentation
│
└── inputs/                        # Sample input images
    ├── input1.png
    └── input2.jpg
```

## 🎯 Use Cases

- **Construction Monitoring** - Analyze construction progress
- **Educational Tool** - Learn about different structural types
- **Quality Assessment** - Identify materials and components
- **Documentation** - Generate detailed structure reports
- **Research** - Study various civil engineering structures

## ⚠️ Troubleshooting

### Common Issues:

**"No module named 'streamlit'"**
- Solution: Run `pip install -r requirements.txt`

**"API key not found"**
- Solution: Ensure your `.env` file exists and contains a valid `GOOGLE_API_KEY`

**"File upload error"**
- Solution: Ensure the image is in JPG, JPEG, or PNG format

**Port already in use**
- Solution: Run `streamlit run app.py --server.port 8502` to use a different port

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your Google API key confidential
- The `.env` file is already in `.gitignore` (if using Git)

## 📝 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Support

For questions or support, please open an issue in the repository.

---

**Built with ❤️ using Streamlit and Google Gemini AI**
