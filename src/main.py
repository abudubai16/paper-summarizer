from llama_index.llms.ollama import Ollama

def main():
    print('Loading Model: ')

    llm = Ollama(model="llama3", request_timeout=120.0)
    print('Model Loaded: ')
    print('Generating response: ')

    resp = llm.complete('What')
    print(resp)
    


if __name__ == '__main__':
    main()    
    pass
