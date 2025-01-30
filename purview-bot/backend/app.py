from flask import Flask, jsonify, request
from utils.purview_api import fetch_alerts  # Import Purview API utility
from utils.llama_api import classify_query  # Import Llama-based utility
from flask_cors import CORS  # Import CORS
 
app = Flask(__name__)
CORS(app) 
 
# MS Purview and Llama configuration
PURVIEW_BASE_URL = "https://.purview.azure.com"
PURVIEW_API_KEY = "<your-api-key>"
 
@app.route("/api/alerts", methods=["POST"])
def fetch_alerts_endpoint():
    """
    Fetch alerts from MS Purview based on severity and top_k.
    """
    data = request.json
    severity_factor = data.get("severity", "high")
    top_k = data.get("top_k", 5)
 
    alerts_response = fetch_alerts(PURVIEW_BASE_URL, PURVIEW_API_KEY, severity_factor)  # Use utility function
    if "error" in alerts_response:
        return jsonify({"error": alerts_response}), 500
 
    # Sort and return top_k alerts
    sorted_alerts = sorted(alerts_response["value"], key=lambda x: x["severity"], reverse=True)[:top_k]
    return jsonify(sorted_alerts), 200
 
@app.route("/api/chat", methods=["POST"])
def chatbot():
    """
    Chatbot endpoint to handle user queries.
    """
    # user_query = request.json.get("query", "")
 
    # # Use the new Llama-based classify_query function
    # query_response = classify_query(None, user_query)  # API key not required for Llama
 
    # if "alert" in query_response.lower():
    #     # Handle alert-specific logic
    #     severity_factor = "high"
    #     if "medium" in query_response.lower():
    #         severity_factor = "medium"
    #     elif "low" in query_response.lower():
    #         severity_factor = "low"
 
    #     # Fetch alerts
    #     alerts_response = fetch_alerts(PURVIEW_BASE_URL, PURVIEW_API_KEY, severity_factor)
    #     if "error" in alerts_response:
    #         return jsonify({"response": alerts_response["error"]})
 
    #     # Format alert response
    #     response_text = "Here are the top alerts based on your query:\n"
    #     for idx, alert in enumerate(alerts_response["value"], 1):
    #         response_text += f"{idx}. Alert: {alert['name']} | Severity: {alert['severity']} | Description: {alert['description']}\n"
    #     return jsonify({"response": response_text})
 
    # # General response
    # return jsonify({"response": query_response})

    # ----------------------------- new code
    user_query = request.json.get("query", "")
    if not user_query:
        return jsonify({"response": "Error: No query provided."}), 400

    print(f"Received query: {user_query}")  # Debugging line
    llama_response = classify_query(None, user_query)
    print(f"Llama Response: {llama_response}")  # Debugging line

    return jsonify({"response": llama_response})
if __name__ == "__main__":
    app.run(debug=True)