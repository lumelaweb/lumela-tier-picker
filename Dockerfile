# Use the official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install required Python packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code into the container
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
