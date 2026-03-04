# Step 1: Use an official lightweight Python image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy our local files into the container
COPY . /app

# Step 4: Install the required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port GCP uses
EXPOSE 8080

# Step 6: Command to start the web server
CMD ["python", "app.py"]
