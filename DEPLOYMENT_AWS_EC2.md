
# AWS EC2 Deployment Guide

## 1. Launch an EC2 Instance
- Recommended AMI: Ubuntu Server 22.04 LTS  
- Instance type: t2.micro (for testing) or higher  
- Network configurations (Security Group):  
  - Open port 22 (SSH)  
  - Open port 80 (HTTP)  
  - Open port 443 (HTTPS)  
  - Open port 8080 (optional for development or direct API exposure)

## 2. Access via SSH
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```
We can also use the AWS terminal to access to the instance.

## 3. Install Dependencies on EC2
```bash
sudo apt update && sudo apt install -y docker.io docker-compose nginx git ufw
sudo systemctl enable docker
```

## 4. Clone Your Project
```bash
git clone https://github.com/youruser/book-app-api.git
cd book-app-api
```

## 5. Docker Build and Deployment
```bash
docker-compose build --no-cache
docker-compose up
```
If it fails (e.g., because the database wasn’t ready):
```bash
docker-compose down
docker-compose up -d
```

## 6. Configure NGINX as a Proxy
Create the NGINX config file:
```bash
sudo nano /etc/nginx/sites-available/book-app
```
Add the following content:
```nginx
server {
    listen 80;
    server_name my-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
Enable the site and reload NGINX:
```bash
sudo ln -s /etc/nginx/sites-available/book-app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## 7. Configure DNS
At your domain provider (GoDaddy, Cloudflare, etc.), create an A record pointing:
```
my-domain.com -> [Your EC2 Public IP]
```

## 8. Access the Application
Open your browser and go to:
http://localhost:8080 or http://my-domain.com

#### 📚 Available Routes

| Path             | Description                |
|------------------|----------------------------|
| `/admin/`        | Django Admin               |
| `/api/v1/`       | API endpoints              |
| `/schema/`       | OpenAPI schema     |
| `/docs/swagger/` | Swagger UI documentation   |
| `/docs/redoc/`   | ReDoc UI documentation     |

## Optional: Configure HTTPS with Certbot
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d my-domain.com
```
Then open your browser and go to:
https://my-domain.com