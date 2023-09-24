import streamlit as st
import openai
import json

# Set your OpenAI API key here
api_key = st.secrets["openai"]

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to simulate the conversation
def simulate_customer_interaction():
    st.sidebar.markdown("### Customer Persona")
    customer_persona = st.sidebar.text_area("Enter the customer persona:")

    try:
        customer_persona_dict = json.loads(customer_persona)
    except ValueError as e:
        st.error("Error: Invalid JSON format for customer persona. Please enter it in valid JSON format.")
        return

    st.write(type(customer_persona_dict))
    
    initial_message = st.text_input("You:", "Hello, I have some questions about your product")

    conversation = [customer_persona_dict, initial_message]

    if st.button("Send"):
        user_input = st.text_input("You:")
        conversation.append(f"You: {user_input}")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
        )

        bot_reply = response['choices'][0]['message']['content']
        st.text("Chatbot:")
        st.success(bot_reply)
        conversation.append(f"Chatbot: {bot_reply}")

def main():
    st.title("Customer Support Chatbot")
    st.sidebar.title("Settings")
    st.sidebar.info("This app simulates a customer interacting with a customer support chatbot.")

    simulate_customer_interaction()

if __name__ == "__main__":
    main()
