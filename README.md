# auction-store
This project is a backend REST API for an auction store, built using Django Rest Framework (DRF). It uses PostgreSQL as a database and celery and celery beat for task scheduling. JSON Web Token (JWT) is used for authentication.

# How to use
1. **Install required packages:**
    ```bash
     pip install -r requirements.txt
     ```

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/anuj66283/auction-store
   ```
   ``` bash
   cd auction-store
   ```

3. **Database Setup:**
   - Configure your database settings in the ```.env``` file.
   - Run migrations:
     ```bash
     python manage.py makemigrations
     ```
     ``` bash
     python manage.py migrate
     ```

4. **Celery Configuration:**
   - Install and start redis server

5. **Run the Application:**
   ```bash
   python manage.py runserver
   ```
   ```bash
   celery -A auction_store worker -l info
   ```
   ```bash
   celery -A auction_store beat -l info
    ```

# Endpoints
## Authentications
### Buyer Registration

- **Endpoint:** `POST /api/v1/auth/buyer/register/`
- **Request Body:**
    ```json
    {
      "buyer": {
        "username": "newbuyer",
        "first_name": "First",
        "last_name": "Last",
        "email": "buyer@example.com",
        "phone": "1234567890",
        "password1": "password123",
        "password2": "password123"
      },
      "profile": "path/to/profile/image.jpg"
    }
    ```

### Seller Registration

- **Endpoint:** `POST /api/v1/auth/seller/register/`
- **Request Body:**
    ```json
    {
      "seller": {
        "username": "newseller",
        "first_name": "First",
        "last_name": "Last",
        "email": "seller@example.com",
        "phone": "1234567890",
        "password1": "password123",
        "password2": "password123"
      },
      "profile": "path/to/profile/image.jpg",
      "district": "District Name",
      "full_address": "Full Address"
    }
    ```

### Verify Account

- **Endpoint:** `POST /api/v1/auth/verify/`
- **Request Body:**
    ```json
    {
      "code": 123456,
      "username": "username"
    }
    ```
### Login

- **Endpoint:** `POST /api/v1/token/`
- **Request Body:**
    ```json
    {
      "username": "user",
      "password": "password"
    }
    ```

### Token Refresh

- **Endpoint:** `POST /api/v1/token/refresh/`
- **Request Body:**
    ```json
    {
      "refresh": "refresh_token"
    }
    ```
## Store
### add product
- **Endpoint:** `POST /api/v1/store/create/`
- **Permissions:** Authenticated users with seller permission
- **Request Body:**
    ```json
    {
      "title": "Product Title",
      "desc": "Product Description",
      "sub_category": "Subcategory ID",
      "quantity": 1,
      "price": 100,
      "unit": "Unit",
      "uploaded_images": ["image1.jpg", "image2.jpg"]
    }
    ```
### get products
- **Endpoint:** `GET /api/v1/store/products/`

### get single product
- **Endpoint:** `GET /api/v1/store/products/`
- **Query Parameters:**
    - `pid`: Product ID

## Bid
### Place a Bid

- **Endpoint:** `POST /api/v1/bid/`
- **Permissions:** Authenticated users with buyer permission
- **Request Body:**
    ```json
    {
      "price": 150,
      "product": "Product UUID"
    }
    ```

### Get Bids for a Product

- **Endpoint:** `GET /api/v1/bid/get/`
- **Query Parameters:**
    - `pid`: Product ID to get bids for
- **Response:**
    ```json
    [
      {
        "price": 150,
        "product": "Product UUID"
      },
      ...
    ]
    ```

## Review
### Add Review

- **Endpoint:** `POST /api/v1/review/<str:pid>/`
- **Permissions:** Authenticated users with buyer permission
- **Request Body:**
    ```json
    {
      "rating": 4,
      "review": "Review text"
    }
    ```

### Get Reviews

- **Endpoint:** `GET /api/v1/review/get/`
- **Query Parameters:**
    - `bid`: Buyer ID to get reviews given by the buyer
    - `sid`: Seller ID to get reviews received by the seller
- **Response:** Returns a list of reviews
    ```json
    [
      {
        "rating": 4,
        "review": "Review text"
      },
      ...
    ]
    ```
# TODO
* Design Frontend
* Add more features