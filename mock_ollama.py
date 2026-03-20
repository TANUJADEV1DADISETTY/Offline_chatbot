import http.server
import socketserver
import json
import time

PORT = 11434

class MockOllamaHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Ollama is running")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        try:
            req_json = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_error(400, "Bad Request")
            return

        model = req_json.get("model", "unknown")
        prompt = req_json.get("prompt", "")
        
        # Simple simulated responses based on the prompt
        response_text = "I'm sorry, I cannot fulfill this request at this time."
        
        if "discount code" in prompt.lower():
            if "EXAMPLE START" in prompt: # One-shot
                response_text = "I'm sorry your code isn't working! Please check if the items in your cart are eligible, or try applying it again. If it still doesn't work, I can issue you a new code."
            else: # Zero-shot
                response_text = "Discount codes can sometimes be tricky. Make sure you entered it correctly without spaces. Also check its expiration date."
        elif "shipping status" in prompt.lower():
            if "EXAMPLE START" in prompt:
                response_text = "You can track your order by clicking the track link in your confirmation email, or by logging into your account and viewing the order details."
            else:
                response_text = "Tracking is available on the order history page of your account."
        elif "return policy" in prompt.lower():
            response_text = "We have a 30-day return policy for unused items in original packaging."
        elif "paypal" in prompt.lower():
            response_text = "Yes, we proudly accept PayPal as a payment option."
        elif "password" in prompt.lower():
            response_text = "You can reset your password by clicking 'Forgot Password' on the login screen."
        elif "customer support" in prompt.lower():
            response_text = "You can call us directly at 1-800-CHIC-BOU during normal business hours."
        elif "international" in prompt.lower():
            response_text = "Yes, we offer shipping to over 50 countries worldwide. Shipping rates apply at checkout."
        else:
            response_text = "Thank you for contacting Chic Boutique! We will help you with your query as soon as possible."

        time.sleep(0.5) # Simulate inference delay
        
        resp_json = {
            "model": model,
            "created_at": "2023-11-20T10:00:00Z",
            "response": response_text,
            "done": True
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(resp_json).encode('utf-8'))

with socketserver.TCPServer(("", PORT), MockOllamaHandler) as httpd:
    print(f"Serving mock Ollama on port {PORT}")
    httpd.serve_forever()
