# Face-Detection Task with FAST-API.

## Setup and Installation

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/A-Rafay-Siddiqui/Face-Detection-Task-with-FAST-API..git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI Application**: Start the FastAPI application by running the following command:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints and Usage

### 1. Create User
- **Endpoint**: `/users/`
- **Method**: POST
- **Description**: Creates a new user.
- **Request Body**: 
  - `name`: Name of the user.
- **Authorization**: API Key required in the header (e.g., `Authorization: BLEEDAI-Rafay-KEY`).

### 2. Retrieve User by ID
- **Endpoint**: `/users/{user_id}/name/`
- **Method**: GET
- **Description**: Retrieves the name of a user by their ID.
- **Path Parameters**: 
  - `user_id`: ID of the user.
- **Authorization**: API Key required in the header (e.g., `Authorization: BLEEDAI-Rafay-KEY`).

### 3. Update User Name by ID
- **Endpoint**: `/users/{user_id}/name/`
- **Method**: PUT
- **Description**: Updates the name of a user by their ID.
- **Path Parameters**: 
  - `user_id`: ID of the user.
- **Request Body**: 
  - `new_name`: New name of the user.
- **Authorization**: API Key required in the header (e.g., `Authorization: BLEEDAI-Rafay-KEY`).

### 4. Search Users by Name
- **Endpoint**: `/users/search/`
- **Method**: GET
- **Description**: Searches for users by name using string matching techniques.
- **Query Parameters**: 
  - `name`: Name to search for.
- **Authorization**: API Key required in the header (e.g., `Authorization: BLEEDAI-Rafay-KEY`).

### 5. Process Image for Face Detection
- **Endpoint**: `/process-image/`
- **Method**: POST
- **Description**: Processes an uploaded image for face detection.
- **Request Body**: 
  - `file`: Image file to be processed.
- **Authorization**: API Key required in the header (e.g., `Authorization: BLEEDAI-Rafay-KEY`).

## Guidelines for Contributing

1. Fork the repository.
2. Make your changes in a feature branch.
3. Ensure all tests pass.
4. Create a pull request with a descriptive title and detailed description.

---
