from flask import Flask, render_template, request, session
import pandas as pd


# RecommendationModel Class
class RecommendationModel:
    def __init__(self, data_path):
        # Load product data
        self.data = pd.read_csv(data_path)

        # Extract necessary columns
        self.products = self.data[[
            "ProductId", "ProductTitle", "Category", "SubCategory", 
            "ProductType", "Colour", "Usage", "ImageURL"
        ]].drop_duplicates()

        # Rename columns for consistency
        self.products.rename(columns={
            "ProductId": "product_id",
            "ProductTitle": "product_name",
            "Category": "category",
            "SubCategory": "subcategory",
            "ProductType": "product_type",
            "Colour": "colour",
            "Usage": "usage",
            "ImageURL": "image_url"
        }, inplace=True)

        # Add a sales column for demonstration purposes
        self.products["sales"] = pd.Series([50, 100, 150, 200, 300] * (len(self.products) // 5 + 1))[:len(self.products)]
        
        self.product_recommendations = None

    def build_recommendations(self):
        # Prepare data for recommendations
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        # Convert product titles to numerical matrix
        vectorizer = CountVectorizer()
        product_matrix = vectorizer.fit_transform(self.products["product_name"])

        # Calculate similarity matrix
        similarity_matrix = cosine_similarity(product_matrix)

        # Store recommendations as a DataFrame
        recommendations = pd.DataFrame(
            similarity_matrix, 
            index=self.products["product_id"], 
            columns=self.products["product_id"]
        )
        self.product_recommendations = recommendations

    def recommend(self, product_id, num_recommendations=3):
        if product_id not in self.products["product_id"].values:
            raise ValueError(f"Product ID {product_id} is invalid. Please choose a valid product ID.")

        if product_id not in self.product_recommendations.index:
            print(f"Product ID {product_id} not found. Returning fallback recommendations.")
            return self.products.sample(n=num_recommendations).to_dict(orient='records')

        # Continue with recommendations
        similar_products = self.product_recommendations[product_id].sort_values(ascending=False)[1:num_recommendations + 1]
        recommended_products = self.products[self.products["product_id"].isin(similar_products.index)]
        return recommended_products.to_dict(orient='records')




# Load data and initialize recommendation model

