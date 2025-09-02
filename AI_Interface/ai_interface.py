from llama_cpp.llama import Llama
from openai import OpenAI
import globals


API_KEY = ""
def load_local_model():
    modelInput = "Tell me a story about a goat."
    
    #Load the model
    globals.LOCAL_LLM = Llama(model_path="./Model/llama-2-7b.Q8_0.gguf",
                n_gpu_layers=-1,
                main_gpu=1)

    modelInput = "Hello"

    # output = LOCAL_LLM(
    #     modelInput,
    #     max_tokens=0,
    #     echo=False,
    #     model="QWQ",
    #     stream=True,
    # )
    
    #print(output['choices'])

    #Open the file with the append suffix, so all new data that is added is appended
    # reportFile = open("complete.txt", "a")
    
    # writeToFile = False
    # streamToConsole = True
    
    # print("==============================")
    #for line in output:
    #     if streamToConsole:
    #    print(line['choices'][0]['text'], end="")
    #         #print(line)
    #         #print(line, end="")
    #     if writeToFile:
    #         reportFile.write(line['choices'][0]['text'])
    #         #reportFile.write(output)
    #     #print(line)
    # print("\n==============================")

def query_local_model(model_query : str):
    
    print("querying model")

    output = globals.LOCAL_LLM(
        model_query,
        max_tokens=0,
        echo=False,
        model="llama2",
        stream=True,
    )

    return_string = ""

    for line in output:
        return_string += line['choices'][0]['text']
    
    return return_string


def load_chatGPT():

    client = OpenAI(api_key=API_KEY)

    response = client.responses.create(
        model="gpt-4o",
        input="Write a one-sentence bedtime story about a unicorn."
    )

    print(response.output_text)