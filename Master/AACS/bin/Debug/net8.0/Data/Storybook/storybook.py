from twilio.rest import Client
from random import choice

account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

def generate_story_variation(story_path):
  with open(story_path, "r") as f:
    story_text = f.read()
  
  # Placeholder for AI-generated variations
  # Replace with your AI integration
  variations = [
    {"choice": "A", "text": "The hero bravely faced the dragon."},
    {"choice": "B", "text": "The hero wisely sought help from a wise old wizard."}
  ]
  
  return story_text

def send_story_via_twilio(to_number, story_text):
  message = client.messages.create(
      to=to_number,
      from_="your_twilio_number",
      body=story_text
  )
  print(message.sid)

# Example usage
user_input = input("Enter your choice (A or B): ")
story_path = "story.txt"
story_text = generate_story_variation(story_path)
send_story_via_twilio("+1234567890", story_text)


"workout_app.py"