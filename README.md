# WeatherChatbot

The `WeatherChatbot` is a simple chatbot to get weather report.

## What’s inside this example?

This example contains some training data and the main files needed to build an
assistant on your local machine. The `WeatherChatbot` consists of the following files:

- **data/nlu.md** contains training examples for the NLU model  
- **data/stories.md** contains training stories for the Core model  
- **config.yml** contains the model configuration
- **domain.yml** contains the domain of the assistant  
- **credentials.yml** contains credentials for the different channels

## How to use ?

Using this example you can build an actual assistant and chat with it on
different channels. To do so execute the following steps:

1. Train a Rasa model containing the Rasa NLU and Rasa Core models by running:
    ```
    rasa train
    ```
    The model will be stored in the `/models` directory as a zipped file.
2. For Custom Action Server runn the following command in a new terminal:
   ```
   rasa run actions
   ```
3. To run the chatbot in command line, enter the following command:
    ```
    rasa shell

4. To run the chatbot in interactive mode, enter the following command:
    ```
    rasa interactive --models models/path_to_model_(latest_one).zip
    ```
5. To run the chatbot in browser, enter the following command:
    ```
    rasa x
    ```
This ChatBot was created by #Aman Pasi
