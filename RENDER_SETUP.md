# Deploy AutoMarket to Render

## Quick Setup Steps

### 1. Prerequisites
- GitHub account with your code pushed to a repository
- Render account (sign up at https://render.com)

### 2. Create PostgreSQL Database on Render

1. Go to your Render Dashboard
2. Click **New +** → **PostgreSQL**
3. Configure:
   - **Name**: `automarket-db`
   - **Database**: `automarket`
   - **User**: `automarket`
   - **Region**: Choose closest to your users
   - **Plan**: Free (or paid for production)
4. Click **Create Database**
5. Copy the **Internal Database URL** (starts with `postgres://`)

### 3. Deploy Web Service

1. Click **New +** → **Web Service**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `automarket` (or your preferred name)
   - **Region**: Same as database
   - **Branch**: `main` (or your default branch)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT main:app`

### 4. Environment Variables

Add these environment variables in the Render dashboard:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SESSION_SECRET` | (Generate a random string) |
| `DATABASE_URL` | (Paste the Internal Database URL from step 2) |

To generate a secure SESSION_SECRET, use:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Deploy

1. Click **Create Web Service**
2. Render will automatically build and deploy your app
3. Your app will be live at: `https://your-app-name.onrender.com`

## Using render.yaml (Alternative Method)

If you prefer Infrastructure as Code:

1. The `render.yaml` file is already configured in your project
2. Go to Render Dashboard → **New +** → **Blueprint**
3. Connect your repository
4. Render will automatically detect `render.yaml` and set everything up

## Important Notes

### Database Migration
Your app automatically creates tables on first run (`db.create_all()` in app.py)

### File Uploads
Render's free tier has ephemeral storage. For production:
- Use cloud storage (AWS S3, Cloudinary, etc.) for vehicle images
- Or upgrade to a paid Render plan with persistent disk

### Free Tier Limitations
- App sleeps after 15 minutes of inactivity
- First request after sleep takes ~30 seconds to wake up
- 750 hours/month free (sufficient for one app)

## Troubleshooting

### Build Fails
- Check `requirements.txt` has all dependencies
- Verify Python version compatibility

### App Crashes on Start
- Check environment variables are set correctly
- Verify DATABASE_URL format
- Check logs in Render dashboard

### Database Connection Issues
- Ensure DATABASE_URL uses the Internal Database URL
- Check database and web service are in same region
- Verify database is running

## Post-Deployment

1. Visit your app URL
2. Create admin account if needed
3. Test vehicle upload functionality
4. Monitor logs in Render dashboard

## Need Help?
- Render Docs: https://render.com/docs
- Check deployment logs in Render dashboard
- Verify all environment variables are set
