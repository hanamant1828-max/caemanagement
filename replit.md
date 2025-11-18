# Friendscars Auto Marketplace

## Overview
A comprehensive Flask-based auto marketplace web application for managing and browsing vehicle inventory. The platform features separate interfaces for administrators (vehicle management) and customers (vehicle browsing by category).

## Project Status
Successfully migrated from Replit Agent to Replit environment on November 18, 2025.

## Key Features

### Customer Features
- **Category-Based Browsing**: Customers can browse vehicles by category (Cars, Trucks, Commercial Vehicles)
- **Vehicle Listings**: View detailed vehicle information with up to 6 images per vehicle
- **Search Functionality**: Search across vehicle make, model, and title
- **Detailed Vehicle Pages**: Comprehensive vehicle details including engine specs, ownership history, insurance info

### Admin Features
- **Admin Authentication**: Secure login system for administrators
- **Vehicle Management**: Add, edit, and delete vehicle listings
- **Image Upload**: Support for up to 6 images per vehicle
- **Comprehensive Vehicle Data**: Manage extensive vehicle details including:
  - Basic info (make, model, year, price, mileage)
  - Engine & Performance (fuel type, transmission, horsepower)
  - Ownership History (number of owners, service records, accident history)
  - Insurance & Documentation (policy numbers, VIN, registration)
  - Additional Features (exterior/interior color, condition rating, warranty)

## Technology Stack
- **Backend**: Flask 3.1.2
- **Database**: SQLite (default) or PostgreSQL (via DATABASE_URL environment variable)
- **ORM**: SQLAlchemy 2.0.44 with Flask-SQLAlchemy 3.1.1
- **Forms**: Flask-WTF 1.2.2 with WTForms 3.2.1
- **Server**: Gunicorn 23.0.0 (production-ready WSGI server)
- **Frontend**: Bootstrap (via CDN), Font Awesome icons
- **File Uploads**: Werkzeug secure file handling

## Project Structure
```
.
├── app.py                 # Flask application setup and configuration
├── main.py               # Application entry point
├── models.py             # Database models (Vehicle, AdminUser)
├── routes.py             # Route handlers and business logic
├── forms.py              # WTForms form definitions
├── templates/            # Jinja2 HTML templates
│   ├── base.html
│   ├── category_selection.html
│   ├── browse_vehicles.html
│   ├── vehicle_detail.html
│   ├── admin_login.html
│   ├── admin.html
│   └── ...
├── static/               # Static assets
│   ├── css/
│   │   └── custom.css
│   ├── js/
│   │   ├── main.js
│   │   └── enhanced-forms.js
│   └── uploads/          # Vehicle images storage
└── instance/
    └── automarket.db     # SQLite database
```

## Configuration

### Environment Variables
- `SESSION_SECRET`: Flask session secret key (defaults to "replit-automarket-secret-key-2025")
- `DATABASE_URL`: PostgreSQL connection string (optional, defaults to SQLite)

### Database
- **Default**: SQLite (`instance/automarket.db`)
- **Production**: PostgreSQL (set `DATABASE_URL` environment variable)
- Auto-creates tables on startup via `db.create_all()`

### Upload Settings
- Max file size: 16MB
- Supported formats: PNG, JPG, JPEG, GIF
- Storage location: `static/uploads/`
- Max images per vehicle: 6

## Running the Application

### Development
The application runs on Gunicorn with auto-reload enabled:
```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

### Access Points
- Root (`/`): Redirects to marketplace
- `/marketplace`: Customer category selection page
- `/browse?category=<category>`: Browse vehicles by category
- `/vehicle/<id>`: View individual vehicle details
- Admin interface available (login required)

## Database Models

### Vehicle Model
Comprehensive vehicle data model with 40+ fields including:
- Basic information (title, category, make, model, year, price, mileage)
- Engine & performance specs
- Ownership and service history
- Insurance and registration details
- Features and condition ratings
- Image gallery (JSON-stored filenames)
- Status tracking (available/sold)

### AdminUser Model
- Username and hashed password authentication
- Created timestamp tracking

## Security Features
- Password hashing with Werkzeug security
- Secure filename handling for uploads
- ProxyFix middleware for reverse proxy compatibility
- CSRF protection available (currently disabled, can be enabled)

## Migration Notes
- All Python dependencies successfully installed via packager
- Gunicorn configured for Replit environment
- Application runs on port 5000
- Database auto-initializes on startup
- Sample data initialization available via `initialize_sample_data()`

## Recent Changes
- **2025-11-18**: Migrated from Replit Agent to Replit environment
  - Installed all required Python packages
  - Configured Gunicorn WSGI server
  - Verified application functionality
  - Database and file uploads working correctly
