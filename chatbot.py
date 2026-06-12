import google.generativeai as genai

# Paste your Gemini API Key here
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def chatbot():

    print("=" * 50)
    print(" Smart University Academic Assistant ")
    print(" Type 'exit' to quit")
    print("=" * 50)

    while True:

        query = input("\nStudent: ")

        if query.lower() == "exit":
            print("\nBot: Thank you. Have a great day!")
            break

        prompt = f"""
You are a Smart University Academic Assistant.

Answer student questions related to:
- Admissions
- Attendance
- Examinations
- Fee Payments
- Internships
- Placements
- Faculty Information

Student Question:
{query}
"""

        try:
            response = model.generate_content(prompt)
            print("\nBot:", response.text)

        except Exception as e:
            print("\nError:", e)

chatbot()