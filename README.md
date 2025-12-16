# Ecommerce Website - Django

This is a Django e-commerce website that provides a shopping platform for customers and an admin panel for management and includes separate authentication for customers and admins, session-based cart management.

## 🚀 Features

### Customer Features
- **User Authentication**: Customer registration, login, and logout
- **Product Browsing**: Browse all products with pagination, search functionality, and category filtering
- **Product Details**: View detailed product information with images, pricing, and specifications
- **Shopping Cart**: Add products to cart, manage quantities, and remove items
- **Checkout Process**: Secure checkout with order placement
- **Order Management**: View order history and track order status
- **Profile Management**: Customer profile with order history
- **Password Reset**: Email-based password reset functionality
- **Search**: Advanced product search across titles, descriptions, and policies

### Admin Features
- **Admin Dashboard**: Overview of pending orders and system statistics
- **Product Management**: Create, read, update, and delete products
- **Order Management**: View all orders, update order status, and manage order details
- **Admin Authentication**: Secure admin login system

### Payment Integration
- **Khalti Payment Gateway**: Integrated payment processing via Khalti
- **Cash on Delivery**: Support for COD payment method

## 🛠️ Technology Stack

- **Backend Framework**: Django
- **Database**: SQLite
- **Image Processing**: Pillow
- **Forms**: Django Crispy Forms with Bootstrap
- **Payment Gateway**: Khalti API
- **Email**: SMTP (Gmail) for password reset

### Step 2: Clone the Repository

```bash
git clone https://github.com/UmeshBabu7/Ecommerce-Website.git
cd Ecommerce-Website
```

If you don't have Git installed, download the project as a ZIP file and extract it.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install django pillow requests django-crispy-forms crispy-bootstrap5
```

### Step 4: Database Migration

```bash
cd website
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

To access Django admin panel:
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`


### Email Configuration

For password reset functionality, configure email settings in `website/settings.py`:

```python
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_app_password"
```

**Note**: For Gmail, you'll need to generate an App Password instead of using your regular password.

### Payment Gateway Configuration

Update the Khalti secret key in `website/ecomapp/views.py`:

```python
headers = {
    "Authorization": "your_khalti_secret_key"
}
```

## 📁 Project Structure

```
Ecommerce-Website/
├── website/
│   ├── ecomapp/          # Main application
│   │   ├── models.py     # Database models
│   │   ├── views.py      # View logic
│   │   ├── urls.py       # URL routing
│   │   ├── forms.py      # Form definitions
│   │   └── migrations/   # Database migrations
│   ├── templates/        # HTML templates
│   │   ├── adminpages/   # Admin panel templates
│   │   └── *.html        # Customer-facing templates
│   ├── media/            # Uploaded media files
│   │   ├── products/     # Product images
│   │   └── admins/       # Admin profile images
│   ├── website/
│   │   ├── settings.py   # Django settings
│   │   └── urls.py       # Main URL configuration
│   └── db.sqlite3        # SQLite database
├── venv/                 # Virtual environment
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🎯 Key Models

- **Customer**: User profile with address and join date
- **Admin**: Admin user profile with image and contact
- **Category**: Product categories
- **Product**: Product details with pricing and images
- **Cart**: Shopping cart for customers
- **CartProduct**: Individual items in cart
- **Order**: Order details with status tracking

## 🔐 User Roles

### Customer
- Register and login
- Browse and search products
- Add products to cart
- Place orders
- View order history
- Update profile

### Admin
- Login to admin panel
- Manage products (CRUD operations)
- View and manage orders
- Update order status
- View system statistics

## 📱 Usage

### For Customers

1. **Browse Products**: Visit the home page to see featured products
2. **Search**: Use the search bar to find specific products
3. **View Details**: Click on any product to see detailed information
4. **Add to Cart**: Click "Add to Cart" to add products
5. **Manage Cart**: Visit "My Cart" to update quantities or remove items
6. **Checkout**: Proceed to checkout and place your order
7. **Track Orders**: View order status in your profile

### For Admins

1. **Login**: Access admin panel at `/admin-login/`
2. **Dashboard**: View pending orders and statistics
3. **Manage Products**: Add, edit, or delete products
4. **Manage Orders**: Update order status and view order details

## 🔒 Security Features

- CSRF protection enabled
- Password hashing
- User authentication and authorization
- Session-based cart management
- Secure payment processing

## 🌐 API Endpoints

### Customer Endpoints
- `/` - Home page
- `/all-products/` - All products listing
- `/product/<slug>/` - Product detail page
- `/add-to-cart-<id>/` - Add product to cart
- `/my-cart/` - View cart
- `/checkout/` - Checkout page
- `/register/` - Customer registration
- `/login/` - Customer login
- `/profile/` - Customer profile
- `/search/` - Product search

### Admin Endpoints
- `/admin-login/` - Admin login
- `/admin-home/` - Admin dashboard
- `/admin-product/list/` - Product list
- `/admin-product/add/` - Add product
- `/admin-product/update/<id>/` - Update product
- `/admin-product/delete/<id>/` - Delete product
- `/admin-all-orders/` - Order list
- `/admin-order/<id>/` - Order detail

