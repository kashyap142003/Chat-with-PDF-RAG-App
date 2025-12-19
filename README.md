# Chat with PDF - AI-Powered PDF Q&A

A Streamlit web application that allows you to upload PDF documents and ask questions about their content using AI.

## Features

- 📄 Upload any PDF document
- 🤖 Ask questions in natural language
- 💬 Get accurate answers based on PDF content
- 🔍 Uses MMR (Maximum Marginal Relevance) for diverse results
- ⚡ Fast vector-based semantic search
- 🎨 Clean and intuitive UI

## How It Works

1. **Upload PDF**: Upload your PDF document through the web interface
2. **Processing**: The app splits the PDF into chunks and stores them in a vector database
3. **Ask Questions**: Type your question in the chat box
4. **Get Answers**: AI retrieves relevant sections and generates accurate answers

## Technology Stack

- **Streamlit**: Web interface
- **LangChain**: RAG (Retrieval-Augmented Generation) framework
- **ChromaDB**: Vector database for semantic search
- **OpenAI GPT-4o-mini**: Language model (via OpenRouter)
- **OpenAI Embeddings**: Text-to-vector conversion

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up API key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-openrouter-api-key-here
```

Get your API key from [OpenRouter](https://openrouter.ai/)

### 4. Copy config file

```bash
cp config.example.py config.py
```

## Usage

Run the Streamlit app:

```bash
streamlit run chat_pdf.py
```

The app will open in your browser at `http://localhost:8501`

### Steps:
1. Upload a PDF file using the file uploader
2. Wait for processing (you'll see progress messages)
3. Type your question in the text box
4. Get instant answers based on the PDF content!

## Project Structure

```
RAG pdf/
├── chat_pdf.py           # Main Streamlit application
├── config.py             # Configuration (not tracked)
├── config.example.py     # Example configuration
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Features Explained

### MMR Retrieval
Uses Maximum Marginal Relevance to retrieve diverse and relevant document chunks, avoiding redundant information.

### Semantic Search
Converts text to vectors (embeddings) to find content by meaning, not just keywords.

### RAG (Retrieval-Augmented Generation)
Combines document retrieval with AI generation for accurate, context-aware answers.

## Configuration

You can customize the following in `chat_pdf.py`:

- `chunk_size`: Size of text chunks (default: 800)
- `chunk_overlap`: Overlap between chunks (default: 150)
- `k`: Number of chunks to retrieve (default: 3)
- `model`: AI model to use (default: gpt-4o-mini)

## Troubleshooting

**PDF not loading?**
- Ensure the PDF is not password-protected
- Check if the file is a valid PDF

**API errors?**
- Verify your API key in `.env` file
- Check your OpenRouter account has credits

**Slow responses?**
- Large PDFs take longer to process
- First upload is slower (creates vector database)

## Security Note

⚠️ Never commit your `config.py` or `.env` file with real API keys to GitHub!

## License

MIT License - Feel free to use and modify!

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## Author

Your Name - [Your GitHub](https://github.com/YOUR_USERNAME)

## Acknowledgments

- LangChain for the RAG framework
- OpenRouter for API access
- Streamlit for the web framework
