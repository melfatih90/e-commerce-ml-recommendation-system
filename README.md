
# **E-Commerce Recommendation System**

This project is an **E-commerce Recommendation System** built with **Python**, **Flask**, and **Machine Learning** to suggest products based on user preferences and behaviors. It features a dynamic dashboard to evaluate model performance and provides a user-friendly interface for browsing and personalized recommendations.

---

## **Features**

### **1. Recommendation System**
- Suggests similar products based on user interactions.
- Uses **Cosine Similarity** on product metadata to generate recommendations.

### **2. User Interaction Tracking**
- Tracks user behavior, including viewed products.
- Provides recommendations tailored to user preferences.

### **3. Model Performance Dashboard**
- Interactive dashboard to evaluate the model using metrics:
  - **Precision**
  - **Recall**
  - **F1 Score**
- Visual insights:
  - Category distribution (Pie Chart).
  - User behavior trends (Bar Chart).

### **4. Responsive Web Interface**
- Built with **Bootstrap 5** for a modern and mobile-friendly design.
- Clean and consistent layout for home, product details, and dashboard pages.

---

## **Tech Stack**

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap 5, Chart.js
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Database:** CSV file (can be extended to SQL/NoSQL)
- **Visualization:** Chart.js for interactive charts

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Add the Dataset**
- Place your `fashion.csv` dataset in the `data/` directory.
- Ensure the dataset contains the following columns:
  - `ProductId`, `ProductTitle`, `Category`, `SubCategory`, `ProductType`, `Colour`, `Usage`, `ImageURL`

### **5. Run the Application**
```bash
flask run
```

### **6. Open the Application**
Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## **Folder Structure**

```
ecommerce-recommendation-system/
│
├── app/
│   ├── __init__.py         # Flask app initialization
│   ├── routes.py           # Application routes
│   ├── model.py            # Recommendation model logic
│   └── templates/          # HTML templates
│
├── static/
│   ├── styles.css          # Custom CSS
│   └── images/             # Static images
│
├── data/
│   └── fashion.csv         # Dataset for recommendations
│
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── run.py                  # Main application entry point
```

---

## **Key Components**

### **Model**
- The recommendation system leverages **CountVectorizer** and **Cosine Similarity** to analyze product metadata and generate recommendations.

### **Routes**
- **Home Page** (`/`): Displays top-selling and all products.
- **Product Details** (`/product/<product_id>`): Shows product details and recommendations.
- **Dashboard** (`/dashboard`): Displays model performance metrics and insights.

### **Dashboard Insights**
- **Metrics:** 
  - Precision: Measures the proportion of recommended products that are relevant.
  - Recall: Measures the proportion of relevant products that are recommended.
  - F1 Score: Combines Precision and Recall for a balanced evaluation.
- **Charts:**
  - Category Distribution: Shows the product category breakdown.
  - User Behavior Trends: Tracks user interactions (views and clicks).

---

## **Future Improvements**

- **Enhance Model:**
  - Use **TF-IDF** for better text-based recommendations.
  - Incorporate collaborative filtering or deep learning techniques.
- **Real Database:**
  - Integrate with **PostgreSQL** or **MongoDB** for scalable data management.
- **Advanced Personalization:**
  - Use **user purchase history** and **clickstream data** for real-time recommendations.
- **Better Metrics:**
  - Include metrics like **Coverage**, **Diversity**, and **NDCG** for deeper evaluation.

---

## **Contributing**

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**

- Dataset source: [Kaggle Fashion Dataset](https://www.kaggle.com/datasets)
- Libraries: Flask, Pandas, Scikit-learn, Chart.js

---
