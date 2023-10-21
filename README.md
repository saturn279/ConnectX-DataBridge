# DataBridge: Versatile Data Integration Application

## Abstract

This Proof of Concept demonstrates the implementation of DataBridge, a versatile data integration application connecting diverse APIs to databases.

## Contents

- [Application Overview](#application-overview)
- [Pre-requisites](#pre-requisites)
- [Pre-Implementation Checklist](#pre-implementation-checklist)
- [DataBridge Application Deployment](#databridge-application-deployment)
- [Post Deployment Validation of Services](#post-deployment-validation-of-services)
- [Test Cases](#test-cases)
- [Issues and Resolution During Installation](#issues-and-resolution-during-installation)
- [References](#references)

## Application Overview

DataBridge is a versatile data integration application designed to connect any API to any database. It acts as a mediator, fetching data from REST APIs, processing it, and storing it in various databases, including MongoDB. The application architecture consists of a Flask API server, Apache Airflow DAGs (Directed Acyclic Graphs), and MongoDB for seamless data processing and storage. It can work as a pluggable module in numerous data applications solving widely encountered data integration problems.

## Architecture
![Architecture drawio txt-Page-2 (2)](https://github.com/saturn279/ConnectX-DataBridge/assets/45988700/40c1c763-4561-4844-bcfb-01bed8e9a6d3)

### Pre-requisites

- Docker installed on the host machine.
- Python 3.8 or higher installed.
- Proficiency in Docker and Docker Compose usage.
- Access to the required API endpoints for data retrieval.

### Pre-Implementation Checklist

- Confirm the presence of Docker and Docker Compose on the host system.
- Verify accessibility of the API endpoints.
- Validate the MongoDB connection string and ensure the MongoDB server is reachable.
- Review and update configurations in the `.env` file if necessary.
- Ensure that ports 80, 8080, 8081, and 27017 are not in use.

### DataBridge Application Deployment

1. **Clone the Repository:**
git clone <repository_url>
cd <repository_directory>

2. **Configure Environment Variables:**
Update essential environment variables in the `.env` file as needed.

3. **Build and Start the Application:**
docker-compose up --build -d

4. **Accessing Services:**
- Flask API: [http://localhost:8081/api/products](http://localhost:8081/api/products)
- Airflow UI: [http://localhost:8080](http://localhost:8080)
- MongoDB: `mongodb://localhost:27017`

### Post Deployment Validation of Services

- Access the Flask API endpoint to ensure it returns the expected JSON response with product data.
- Log in to the Airflow UI (if credentials are set) and verify that the "DataBridgeDAG" is active and scheduled to run at regular intervals.
- Connect via MongoDB compatible database client to validate data.

### Test Cases

#### Test Case 1: Verify API Endpoint

1. Access the Flask API endpoint: [http://localhost:8081/api/products](http://localhost:8081/api/products)
2. Verify if it returns a JSON response containing product data.

*Expected Result: JSON response with product data.*

#### Test Case 2: Airflow DAG Execution

1. Access the Airflow UI: [http://localhost:8080](http://localhost:8080)
2. Check if the "DataBridgeDAG" is active and scheduled to run periodically.

*Expected Result: Active "DataBridgeDAG" scheduled at regular intervals.*

### Issues and Resolution During Installation

- **Issue 1: Unable to Access API Endpoint**
- *Resolution:* Inspect API server logs for errors and confirm the correct API endpoint URL in `data_ingress.py`.

- **Issue 2: Airflow DAG Fails to Execute**
- *Resolution:* Examine Airflow logs (`docker logs <airflow_container_id>`) for errors and ensure accurate configurations in `DataBridgeDAG.py`.

- **Issue 3: MongoDB Connection Error**
- *Resolution:* Validate the MongoDB connection string in `data_store.py` and confirm the MongoDB server is operational and accessible.

### References

- [Flask Documentation](#) [Link to Flask Documentation]
- [Apache Airflow Documentation](#) [Link to Airflow Documentation]
- [MongoDB Documentation](#) [Link to MongoDB Documentation]
