# Deploying to Render.com

This guide will help you deploy your Flask Auto Market application to Render.com.

## Prerequisites

- A GitHub account
- A Render.com account (free tier available)
- Your project pushed to a GitHub repository

## Step 1: Push to GitHub

1. Initialize a git repository (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Flask Auto Market app"
   ```

2. Create a new repository on GitHub and push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Create a Web Service on Render

1. Log in to [Render.com](https://render.com)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: Choose a name for your app (e.g., `auto-market`)
   - **Region**: Select the closest region to your users
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (unless your app is in a subdirectory)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (this is already in your Procfile)

## Step 3: Set Environment Variables

In the Render dashboard for your web service, go to the "Environment" tab and add these variables:

### Required Variables:
- **SECRET_KEY**: A secure random string for Flask sessions
  ```
  Example: your-very-secret-random-key-here-change-this
  ```
  Generate a secure key with Python:
  ```python
  import secrets
  print(secrets.token_hex(32))
  ```

### Optional Variables:
- **SQLITE_PATH**: Path for SQLite database (default: `instance/app.db`)
  ```
  Example: instance/app.db
  Note: Use relative paths only. Absolute paths may cause permission errors.
  ```

- **PORT**: The port your app will run on (Render sets this automatically, usually 10000)
  ```
  Note: Render automatically sets this, you don't need to add it
  ```

## Step 4: Deploy

1. Click "Create Web Service"
2. Render will automatically:
   - Install Python 3.11.9 (from `runtime.txt`)
   - Install dependencies from `requirements.txt`
   - Run your app with `gunicorn app:app`
3. Wait for the deployment to complete (usually 2-5 minutes)
4. Your app will be live at: `https://YOUR_APP_NAME.onrender.com`

## Step 5: Verify Deployment

1. Visit your app URL
2. Test the marketplace browsing functionality
3. Test the admin login at: `https://YOUR_APP_NAME.onrender.com/secret-admin-access-2025`
   - Username: `abc`
   - Password: `123`

## Important Notes

### Database Persistence
- **SQLite on Render Free Tier**: The free tier uses ephemeral storage, meaning your database will reset when the service restarts or redeploys
- **For Production**: Consider upgrading to a paid plan with persistent disk, or use PostgreSQL:
  1. Create a PostgreSQL database on Render
  2. Set the `DATABASE_URL` environment variable to your PostgreSQL connection string
  3. The app will automatically use PostgreSQL instead of SQLite

### File Uploads
- Uploaded vehicle images are stored in `static/uploads/`
- On the free tier, these will also be ephemeral
- For production, consider using a service like Cloudinary or AWS S3 for image storage

### Admin Credentials
- **Change the default admin credentials** in production!
- Edit `models.py` to use secure credentials or implement a proper authentication system

### Static Files
- Flask will serve static files automatically
- All CSS, JS, and images in `static/` folder will be accessible

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Verify `requirements.txt` has all dependencies
- Ensure `runtime.txt` specifies a valid Python version

### App Crashes on Startup
- Check the logs in Render dashboard
- Verify environment variables are set correctly
- Make sure the database directory can be created

### Database Not Persisting
- Free tier has ephemeral storage
- Upgrade to a paid plan or use PostgreSQL

## Testing Locally

Before deploying, test locally with gunicorn:

```bash
# Set environment variables (optional)
export SECRET_KEY="your-test-secret-key"
export SQLITE_PATH="data/app.db"
export PORT=8000

# Run with gunicorn
gunicorn app:app --bind 0.0.0.0:8000

# Or run with the exact Render configuration
gunicorn app:app
```

Visit `http://localhost:8000` to test.

## Next Steps

1. Set up a custom domain (available on paid plans)
2. Configure automatic deployments from GitHub
3. Set up environment-specific configurations
4. Consider migrating to PostgreSQL for data persistence
5. Implement proper authentication and authorization
6. Add monitoring and logging

## Support

- Render Documentation: https://render.com/docs
- Flask Documentation: https://flask.palletsprojects.com/
- Gunicorn Documentation: https://docs.gunicorn.org/
