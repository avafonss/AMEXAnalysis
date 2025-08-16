# Microsoft Teams App Store Analysis

A Streamlit application for analyzing Microsoft Teams app store reviews using OpenAI and SerpAPI.

## Local Development

1. Create a virtual environment:
   ```bash
   python3.13 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SERPAPI_KEY=your_serpapi_key_here
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Streamlit Cloud Deployment

1. Push your code to GitHub
2. Connect your repository to Streamlit Cloud
3. Set the following environment variables in Streamlit Cloud:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `SERPAPI_KEY`: Your SerpAPI key
4. Deploy!

## Requirements

- Python 3.13+
- OpenAI API key
- SerpAPI key
