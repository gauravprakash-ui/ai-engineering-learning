# AI Engineering Learning Demo
# Author: Gaurav
# Purpose: Testing Gemini Enterprise GitHub Integration

# ---- 1. Basic Greeting Function ----
def greet(name):
    """Returns a greeting message for the given name"""
    return f"Hello, {name}! Welcome to AI Engineering."

# ---- 2. Math Operations ----
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    return a + b

def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result"""
    return a * b

# ---- 3. List Operations ----
def get_ai_topics():
    """Returns a list of AI learning topics"""
    topics = [
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing",
        "Computer Vision",
        "Generative AI",
        "Prompt Engineering"
    ]
    return topics

# ---- 4. Simple AI Model Simulator ----
def predict_sentiment(text):
    """
    A simple rule-based sentiment predictor.
    Returns: 'positive', 'negative', or 'neutral'
    """
    positive_words = ["good", "great", "excellent", "amazing", "love"]
    negative_words = ["bad", "terrible", "awful", "hate", "poor"]
    
    text_lower = text.lower()
    
    if any(word in text_lower for word in positive_words):
        return "positive"
    elif any(word in text_lower for word in negative_words):
        return "negative"
    else:
        return "neutral"

# ---- Main Execution ----
if __name__ == "__main__":
    # Test greet
    print(greet("Gaurav"))
    
    # Test math
    print(f"10 + 20 = {add_numbers(10, 20)}")
    print(f"5 x 6 = {multiply_numbers(5, 6)}")
    
    # Test topics
    print("\nAI Topics to Learn:")
    for topic in get_ai_topics():
        print(f"  - {topic}")
    
    # Test sentiment
    print("\nSentiment Analysis:")
    print(predict_sentiment("This is a great course!"))
    print(predict_sentiment("This is a terrible experience"))
    print(predict_sentiment("This is a course"))
