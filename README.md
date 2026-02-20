# TripMe ✈️

TripMe is a comprehensive travel management web application built with Django. It provides a platform to browse destinations, manage customer travel profiles, and search for available trips. This project demonstrates proficiency in Python, Django, PostgreSQL, relational database design, and frontend integration using Bootstrap.

> **Note:** This project was coded entirely by hand without the use of AI assistance, demonstrating my solid fundamental knowledge of backend web development, MVC architecture, and Python.

## 🚀 Features
- **Destination Management**: Create and manage travel destinations with associated costs, days, and categories.
- **Customer Profiles**: Store user data, including personal information and many-to-many relationships with their booked destinations.
- **Trip Calculation**: Automatically calculates return dates based on departure dates and trip length using Python's `datetime` module.
- **Employee Search**: Search functionality to find employees within the company directory via a custom search view.
- **Responsive UI**: Integrated with Bootstrap and custom CSS for a mobile-friendly user experience.

## 🛠️ Technologies Used
- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 4, FontAwesome
- **Architecture:** MVT (Model-View-Template)

## 💻 Technical Highlights
- **Relational Database Modeling**: Designed complex relationships including `OneToOneField` and `ManyToManyField`.
- **Custom Model Properties**: Implemented dynamic `@property` decorators to calculate logical fields like full names and return dates seamlessly.
- **Overridden Save Methods**: Centralized data formatting by overriding the Django Model `save()` method (e.g., auto-capitalizing specific user inputs).
- **Dynamic Routing**: Configured views and URLs to handle complex route parameters and query strings efficiently.

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/TripMe.git
   cd TripMe
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install django psycopg2
   ```

4. **Database Setup**
   Create a PostgreSQL database named `travel`.
   Update `tripme/settings.py` with your database credentials (or set up environment variables). Then run:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/` in your browser.
