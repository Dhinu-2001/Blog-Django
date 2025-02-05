# 📝 DailyBlog - A Simple Django Blog Application

A lightweight blog application built with **Django**, featuring user authentication, blog post creation, editing, and deletion.

---

## 🚀 Features
- User authentication (register, login, logout)
- Create, update, and delete blog posts
- Display a list of posts with pagination
- Secure access control for authenticated users
- Bootstrap-styled UI for a clean design

---

## 🛠️ Setup and Installation

### **1️⃣ Clone the Repository**
First, download the project to your local machine:
```bash
git clone https://github.com/Dhinu-2001/Blog-Django.git
cd Blog-Django

### **2️⃣ Create a Virtual Environment**
Second, to isolate dependencies, create a virtual environment:
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

### **3️⃣ Install Dependencies**
Third, install the required packages using:
cd DailyBlog
pip install -r requirements.txt

### **4️⃣ Apply Database Migrations**
Run the following to set up the database:
Configure your postgres db in .env in main app, then enter below commands:
python manage.py makemigrations
python manage.py migrate

### **5️⃣ Run the Development Server**
Start the Django development server:
python manage.py runserver

Now, open http://127.0.0.1:8000/ in your browser.
