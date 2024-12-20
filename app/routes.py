from flask import Blueprint, render_template, request ,session
from app.model import RecommendationModel
import matplotlib.pyplot as plt
import os
import matplotlib
import matplotlib.pyplot as plt


# تعريف Blueprint
app_routes = Blueprint('app_routes', __name__)

# تحميل نموذج توصيات
model = RecommendationModel(data_path="data/fashion.csv")
model.build_recommendations()
matplotlib.use('Agg')

# الصفحة الرئيسية
@app_routes.route("/")
def home():
    # Pagination setup
    page = int(request.args.get("page", 1))
    items_per_page = 10

    start = (page - 1) * items_per_page
    end = start + items_per_page

    total_items = len(model.products)
    products = model.products.iloc[start:end].to_dict(orient='records')

    has_next = end < total_items
    has_previous = start > 0

    # Get top-selling products
    top_selling = model.products.sort_values("sales", ascending=False).head(5).to_dict(orient='records')

    return render_template(
        "home.html",
        products=products,
        top_selling=top_selling,
        page=page,
        has_next=has_next,
        has_previous=has_previous
    )

# حفظ المنتجات التي تم تصفحها في الجلسة
@app_routes.route("/product/<int:product_id>")
def product_details(product_id):
    # جلب تفاصيل المنتج
    product = model.products.loc[model.products["product_id"] == product_id].to_dict(orient="records")
    if not product:
        return redirect("/")  # إذا لم يتم العثور على المنتج، إعادة التوجيه للصفحة الرئيسية
    product = product[0]

    # جلب التوصيات للمنتج
    recommendations = model.recommend(product_id)

    # Track user behavior in the session
    if "viewed_products" not in session:
        session["viewed_products"] = []
    if product_id not in session["viewed_products"]:
        session["viewed_products"].append(product_id)

    return render_template(
        "product_details.html",
        product=product,
        recommendations=recommendations
    )




@app_routes.route("/model_behavior")
def model_behavior():
    # Calculate general statistics
    total_products = len(model.products)
    sample_product_id = model.products["product_id"].iloc[0]
    recommendations = model.recommend(sample_product_id)
    
    # Analyze user behavior
    viewed_products = session.get("viewed_products", [])
    viewed_product_details = model.products[model.products["product_id"].isin(viewed_products)]
    
    # Most viewed categories
    category_distribution = viewed_product_details["category"].value_counts().to_dict()

    return render_template(
        "model_behavior.html",
        total_products=total_products,
        sample_product_id=sample_product_id,
        recommendations=recommendations,
        category_distribution=category_distribution,
        viewed_products=viewed_product_details.to_dict(orient="records")
    )



@app_routes.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    results = model.products[model.products["product_name"].str.contains(query, case=False, na=False)]
    return render_template("search_results.html", query=query, results=results.to_dict(orient="records"))


@app_routes.route("/recommendations")
def personalized_recommendations():
    viewed_products = session.get("viewed_products", [])
    recommendations = []
    for product_id in viewed_products:
        recommendations.extend(model.recommend(product_id))
    unique_recommendations = {rec["product_id"]: rec for rec in recommendations}.values()
    return render_template("recommendations.html", recommendations=unique_recommendations)


@app_routes.route("/dashboard")
def dashboard():
    # Mock user data for evaluation (ground truth)
    ground_truth = {
        1: [2, 3, 4],  # User viewed products 2, 3, 4 after viewing product 1
        5: [6, 7],     # User viewed products 6, 7 after viewing product 5
    }

    # Evaluate model performance
    precision_list = []
    recall_list = []

    for product_id, relevant_items in ground_truth.items():
        # Model recommendations for this product
        recommendations = [rec["product_id"] for rec in model.recommend(product_id)]

        # Calculate Precision and Recall
        relevant_recommended = set(recommendations) & set(relevant_items)
        precision = len(relevant_recommended) / len(recommendations) if recommendations else 0
        recall = len(relevant_recommended) / len(relevant_items) if relevant_items else 0

        precision_list.append(precision)
        recall_list.append(recall)

    # Average Precision and Recall
    avg_precision = sum(precision_list) / len(precision_list) if precision_list else 0
    avg_recall = sum(recall_list) / len(recall_list) if recall_list else 0

    # F1 Score
    f1_score = (
        2 * avg_precision * avg_recall / (avg_precision + avg_recall)
        if avg_precision + avg_recall > 0
        else 0
    )

    # Total products and recommendations
    total_products = len(model.products)
    total_recommendations = len(ground_truth)

    # Category distribution
    category_distribution = model.products["category"].value_counts().to_dict()

    return render_template(
        "model_dashboard.html",
        total_products=total_products,
        total_recommendations=total_recommendations,
        avg_precision=avg_precision,
        avg_recall=avg_recall,
        f1_score=f1_score,
        category_distribution=category_distribution
    )
