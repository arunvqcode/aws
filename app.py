from flask import Flask, render_template, request, Response
import openai
import json

app = Flask(__name__)

openai.api_key = "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"

def generate_chunks(prompt):
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "user",
                "content": f"""if you got any question you have to answer from the below text.
                text: 1. Introduction
                Zatara is a platform designed to connect businesses with potential customers via an
                interactive mobile app. The apps motto is Eat, Drink & Save Money. It aims to benefi businesses by promoting their offers and rewards customers based on their spending habits within the app. 2. User Types & Functionalities
                2.2. Business
                1. Sign-up/Login
                • Register using official email address.
                • Verification process for authenticity.
                2. Admin Dashboard
                • Manage offers: Add, edit, set timings, and control visibility.
                • Monitor redemption statistics.
                • View customer reviews and ratings.
                • Boost offers to target premium customers.
                3. AI Zatara Butler Interaction
                • Post-login, the AI Zatara Butler greets businesses.
                • The butler provides a tutorial on how to use the backend portal and manage offers.
                • Businesses can interact with the AI Zatara Butler for FAQs or guidance on using the portal at
                any time.
                4. Offer Management
                • Set start and end dates for offers.
                • Specify offer timings.
                • Label offers as "hot" for promotional purposes
                .
                5. Google Place Integration - when you add a new business, we want the ability to pull in data
                from google places such as name, any
                6. Payment method is for businesses. They have to pay £20/month to be listed or 1 year upfront
                for 10% discount of £220/year and 1 month free if paid 1 year.
                7. Hot Offers - Inside the business app the business can select hot offer on/off which will display
                to premium customers that have paid and customers that are top spenders in the app at the top
                of the banners.
                Business App FAQs:
                1. How can my business join Zatara?
                - Register using your official business email address. After registration, there's a verification
                process to ensure authenticity.
                2. How do I manage offers for my business?
                - Use the Admin Dashboard to add, edit, set timings, and control the visibility of your offers.
                3. What is the AI Zatara Butler for businesses?
                - Post-login, the AI Zatara Butler greets businesses and provides a tutorial on using the backend
                portal. You can also interact with the Butler for guidance at any time.
                4. How do I set up "hot" offers?
                - While managing your offers, you can label specific offers as "hot" for promotional purposes.
                These will be displayed prominently to premium customers.5. What are the payment options for businesses?
                - Businesses can opt for a monthly subscription at £20/month or pay upfront for a year at £220,
                which includes a 10% discount and an additional free month.
                6. How does Google Place Integration work?
                - When adding a new business, the system can pull data from Google Places, such as the name
                and other relevant details.
                
                you can also send this URL along with the response to the user. This link is about zatara app. URL = https://youtu.be/DPFsjv2dFRQ . If you get stuck you can either email mailto:zatara@zatara.uk or ask more questions here
                                
                question : {prompt}"""
            }
        ],
        stream=True
    )

    for chunk in result:
        response = chunk.choices[0].delta.get("content", "")
        words = response.split()
        for word in words:
            yield word
            
def generate_chunkss(prompt):
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "user",
                "content": f"""if you got any question you have to answer from the below text.
                text: 1. Introduction
                Zatara is a platform designed to connect businesses with potential customers via an
                interactive mobile app. The apps motto is Eat, Drink & Save Money. It aims to benefi businesses by promoting their offers and rewards customers based on their spending habits within the app. 2. User Types & Functionalities
                2.1. Customer
                1. Sign-up/Login
                • Upon first download, users must either log in or sign up to access the app.
                • Register using email, phone number, or social media accounts.
                • Password recovery feature.
                • Verification via email or phone number.
                2. Video introduction
                • Here the video shows the customer the benefits of the app
                • A short 1-2 min animation video how to use the app demo
                3. Location-Based Services
                • As Zatara is in its initial phase, it will operate within limited areas in London.
                • Users must select their location from a dropdown list of areas where Zatara operates.
                • Once Zatara expands its coverage, automatic GPS detection will be enabled to detect user
                location.
                • Display available offers based on the selected location.
                4. Offer Redemption & Tracking
                • View and redeem offers from selected businesses.
                • Unique animation displayed upon redemption to ensure authenticity and prevent misuse.
                • The app tracks the users spending after redeeming an offer (e.g., a free coffee).
                • A counter keeps track of the users spend. Once they reach a certain amount (e.g., £25
                spend for the same business within a 30 day period), they are granted the same free item to
                use within 30 days expiry.
                • Premium customers, those who track their spend and spend more with Zatara, get access
                to hot offers from businesses.
                • View offers history redeemed
                5. Reviews and Ratings
                • Rate and review businesses after redeeming offers.
                • View personal review history.
                3. AI Zatara Butler Assistant Interaction
                • Users can interact with the AI Zatara Butler for FAQs or guidance on using the app at any
                time
                .
                7. Premium upgrade
                • Customer will see hot offers in the main page
                • When they click on the hot offer, it will popup to say upgrade your package to premium for£3.50 for 12 months agreement
                • Benefits are that these offers will be only from top 3* and above places
                1. How do I sign up for Zatara?
                - You can sign up using your email, phone number, or social media accounts. After
                registration, youll need to verify via email or phone number.
                2. What areas does Zatara cover?
                - Currently, Zatara operates within specific areas in London. You can select your location
                from a dropdown list in the app.
                3. How do I redeem offers?
                - Browse through available offers based on your location, select the one you like, and follow
                the in-app instructions to redeem.
                4. What is the Zatara Butler?
                - The Zatara Butler is an AI assistant that can guide you on using the app and answer any
                questions you might have.
                5. How do I upgrade to Premium?
                - Click on a hot offer, and youll be prompted to upgrade your package to premium for a
                12-month agreement at £3.50.
                
                you can also send this URL along with the response to the user. This link is about zatara app. URL = https://youtu.be/rlEaT_dJJrE .If you get stuck you can either email mailto:zatara@zatara.uk or ask more questions here
                                
                question : {prompt}"""
            }
        ],
        stream=True
    )

    for chunk in result:
        response = chunk.choices[0].delta.get("content", "")
        words = response.split()
        for word in words:
            yield word

@app.route('/business')
def business():
    return render_template('index.html')

@app.route('/ask_business')
def business_response():
    prompt = request.args.get('prompt', '')

    def stream_response():
        chunks_generator = generate_chunks(prompt)
        for word in chunks_generator:
            yield 'data: ' + json.dumps(word) + '\n\n'

    return Response(stream_response(), mimetype='text/event-stream')


@app.route('/customer')
def index():
    return render_template('base.html')

@app.route('/ask_customer')
def get_response():
    prompt = request.args.get('prompt', '')

    def stream_response():
        chunks_generator = generate_chunkss(prompt)
        for word in chunks_generator:
            yield 'data: ' + json.dumps(word) + '\n\n'

    return Response(stream_response(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
  