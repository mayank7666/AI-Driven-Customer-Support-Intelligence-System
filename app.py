from classify import classify_query

def auto_reply(category):
    responses = {
        "Order Tracking": "You can track your order here: https://track.beastlife.com",
        "Delivery Delay": "We apologize for the delay. Your order will arrive soon.",
        "Refund Request": "Your refund request has been initiated.",
        "Product Issue": "Please share product images for assistance.",
        "Payment Failure": "Please retry payment or use another method.",
        "Subscription Issue": "Manage your subscription from account settings.",
        "General Query": "Our team will assist you shortly."
    }
    return responses.get(category, "We will get back to you soon.")

print("🤖 AI Support System Started\n")

while True:
    query = input("Customer: ")
    
    if query.lower() == "exit":
        break
    
    category = classify_query(query)
    reply = auto_reply(category)
    
    print("Category:", category)
    print("Reply:", reply)
    print("-" * 40)