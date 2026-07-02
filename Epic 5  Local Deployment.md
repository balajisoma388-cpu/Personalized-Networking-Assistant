Local Deployment and End-to-End Testing

After successfully passing all unit and integration tests, the application is deployed locally for comprehensive end-to-end testing. The system consists of two independent components that must run simultaneously: the FastAPI backend, which provides the REST API and AI services, and the Streamlit frontend, which delivers the interactive user interface.

Start the FastAPI backend from the project root using:

                                            uvicorn app.main:app --reload

The --reload option enables automatic hot reloading during development. Whenever a Python source file is modified, Uvicorn detects the change and restarts the server automatically, allowing developers to see updates immediately without manually restarting the application. This significantly speeds up the development and debugging process.

Next, start the Streamlit frontend in a separate terminal:

                                             streamlit run frontend/streamlit_app.py

Once both services are running, the application is fully operational. The Streamlit interface is available at:

                                                http://localhost:8501

where users can generate personalized conversation starters, perform fact-checks, view conversation history, and review previous feedback.

The FastAPI backend automatically exposes interactive API documentation through Swagger UI at:

                                                http://127.0.0.1:8000/docs

This documentation allows developers to inspect available endpoints, view request and response schemas, and test API calls directly from the browser without requiring external tools such as Postman. Together, the FastAPI backend and Streamlit frontend provide a complete end-to-end system that supports both user interaction and developer testing during local deployment.