# Getting Started with the Assistant

This guide will walk you through installing and running the assistant application.

## How to Install

Follow these steps to set up your development environment:

1. **Create a Virtual Environment:**
   It's highly recommended to use a virtual environment to isolate the project's dependencies.  You can create one using your preferred method.  Here's an example using `venv`:

   ```bash
   python3 -m venv venv
    ```
2. Install Dependencies: Activate the virtual environment and then install the required Python packages:

```bash
    source venv/bin/activate  # (Linux/macOS)
    # or
    # venv\Scripts\activate  (Windows)
    pip install -r requirements.txt  # Assumes you have a 'requirements.txt' file
```

3.Run the Streamlit App: Navigate to the src directory and run the Streamlit application:
```bash
cd src
streamlit run main.py
```
This will launch the Streamlit app in your web browser.

How to Build & Run with Docker
This section describes how to build and run the assistant using Docker, providing a consistent environment regardless of your local setup.

Install Docker: You'll need Docker installed on your machine. You can download and install it from: https://www.docker.com/

Build the Docker Image: Navigate to the root directory of your project (where the Dockerfile is located) and run the following command to build the Docker image:

docker build . -t assistant

This command builds an image named "assistant" using the instructions in the Dockerfile.

Run the Docker Compose File: To run the assistant application with its dependencies, use Docker Compose. Make sure you're in the root directory of your project. Then run:

docker compose up

This command will start the assistant application as a container. You'll see output in your terminal indicating that the containers are running.

Notes:

requirements.txt: Ensure you have a requirements.txt file in your project's root directory listing all the Python dependencies. This file is used by pip install -r requirements.txt.
Docker Compose: Docker Compose is used to manage multi-container applications. In this case, it's used to run the assistant application and any necessary dependencies.
Troubleshooting: If you encounter any issues, check the Docker logs using docker logs <container_id> (replace <container_id> with the actual ID of the running container).

```code
**Key improvements and explanations:**

*   **Clearer Instructions:**  The steps are broken down into more manageable chunks.
*   **Detailed Explanations:**  Added explanations for each step (e.g., why use a virtual environment, what `docker compose up` does).
*   **`requirements.txt` Emphasis:**  Highlights the importance of the `requirements.txt` file.
*   **Troubleshooting Tip:** Included a basic troubleshooting tip for Docker.
*   **Formatting:**  Used markdown formatting (headings, lists, code blocks) for readability.
*   **Links:** Added a link to the Docker download page.

To help me tailor this further, could you tell me:

*   What is the purpose of the `main.py` file? (A brief description would be helpful)
*   Do you have a `requirements.txt` file?  If so, what's in it?
*   Are there any specific dependencies that require special attention during installation?
```