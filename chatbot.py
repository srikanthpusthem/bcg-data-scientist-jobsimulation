from flask import Flask, request, jsonify

# Sample financial data from Task 1
financial_data = {
    "total_revenue": "The total revenue for the last fiscal year is $211 billion for Microsoft, $81.5 billion for Tesla, and $394.3 billion for Apple.",
    "net_income_change": "Microsoft's net income decreased by $15.3 billion last year, Tesla's remained stable, and Apple's showed no change.",
    "assets_liabilities": "On average, Microsoft has $380 billion in assets and $191 billion in liabilities. Tesla has $83 billion in assets and $37 billion in liabilities. Apple has $353 billion in assets and $283 billion in liabilities.",
    "cash_flow": "The cash flow from operating activities is $95 billion for Microsoft, $15 billion for Tesla, and $122 billion for Apple.",
    "performance_summary": "Apple is the most stable performer, Microsoft is facing revenue declines, and Tesla is in a growth phase with revenue volatility."
}

# Initialize Flask app
app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def simple_chatbot():
    user_query = request.json.get('query', '').lower()

    # Match user queries to predefined responses
    if "total revenue" in user_query:
        return jsonify({"response": financial_data["total_revenue"]})
    elif "net income" in user_query:
        return jsonify({"response": financial_data["net_income_change"]})
    elif "assets and liabilities" in user_query:
        return jsonify({"response": financial_data["assets_liabilities"]})
    elif "cash flow" in user_query:
        return jsonify({"response": financial_data["cash_flow"]})
    elif "financial performance" in user_query:
        return jsonify({"response": financial_data["performance_summary"]})
    else:
        return jsonify({"response": "Sorry, I can only provide information on predefined queries."})

if __name__ == '__main__':
    app.run(debug=True)
