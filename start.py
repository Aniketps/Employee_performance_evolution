import os
import pickle
import random
import numpy as np
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
model = pickle.load(open('LogisticRegression_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('start.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values() if x not in ['name', 'location', 'city']]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output == 1:
        return render_template('start.html', prediction_text='Congratulations! You have good chances to get promoted.')    
    else:
        return render_template('start.html', prediction_text='Sorry, we cannot promote you at this time. Thank you for your time.')


@app.route('/bot', methods=['POST'])
def chat():
    user_input = request.form['message']
    if user_input.lower() in ["bye", "thank you", "see you", "good bye", "thanks for help", "understood"]:
        bot_reply = farewell()
    elif user_input.lower() in ["what is age", "age", "what age is", "age is what", "about age"]:
        bot_reply = "Enter the number of years you have spend in the world since born"
    elif user_input.lower() in ["what is number of trainings you have done", "number of trainings you have done",
                                "what number of trainings you have done is", "number of trainings you have done is what",
                                "about number of trainings you have done"]:
        bot_reply = "Enter the number of training you have completed in last few years all must be certified"
    
    elif user_input.lower() in ["what is previous year rating", "previous year rating", 
                                "what previous year rating is",
                                "previous year rating is what",
                                "about previous year rating"]:
        bot_reply = "Enter the rating between 0 to 5 you have got in last year from higher offiser in in company or team"
    
    elif user_input.lower() in ["what is length of service", "length of service",
                                "what length of service is", "length of service is what",
                                "about length of service"]:
        bot_reply = "Enter the number of services you have provided to comstumers in work time"
    
    elif user_input.lower() in ["what is awards won", "awards won", "what awards won is",
                                "awards won is what", "about awards won"]:
        bot_reply = "Enter the count of Awards you won in the current profession"
    
    elif user_input.lower() in ["what is average training score", "average training score",
                                "what average training score is",
                                "average training score is what", "about average training score"]:
        bot_reply = "Enter the Avg score you have got in your training(score must be between 0 to 100)"
    
    else:
        bot_reply = respond(user_input)
    return render_template('start.html', bot_reply=bot_reply)

def greeting():
    responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Bye for now!", "Farewell!"]
    return random.choice(responses)

def respond(message):
    if "hello" in message.lower() or "hi" in message.lower() or "hey" in message.lower():
        return greeting()
    elif "bye" in message.lower() or "goodbye" in message.lower():
        return farewell()
    else:
        return "I'm sorry, I didn't understand that."


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
