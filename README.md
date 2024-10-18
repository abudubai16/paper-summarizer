# Research Paper Downloader & Chatbot System Using RAG and Llama-Index

This project is designed to create a chatbot capable of discussing the content of specific research papers using a Retrieval-Augmented Generation (RAG) system and Llama-Index. The system downloads a research paper based on its DOI using Selenium, ingests it into a document retrieval system (via Llama-Index), and uses ChatGPT as the LLM backend to provide detailed and accurate responses about the paper. Future plans include downloading and analyzing papers from the bibliography of the primary research paper, ensuring more comprehensive answers and reducing hallucinations.

## Features

- **DOI-based Paper Downloading**: Automatically downloads research papers using Selenium by providing a DOI.
- **RAG with Llama-Index**: Uses Llama-Index to ingest and retrieve relevant sections of the paper when interacting with the chatbot.
- **Chatbot Integration with ChatGPT**: A user-friendly chatbot that provides information based on the content of the downloaded research papers.
- **Future Plans**:
  - Automatically download and include referenced papers in the primary research paper’s bibliography.
  - Enhance chatbot accuracy by providing broader topic coverage and minimizing hallucinations.

## Project Overview

### How It Works

1. **Research Paper Downloading**:

   - Using Selenium, the system downloads research papers based on a provided DOI and stores them locally.

2. **Ingestion via Llama-Index**:

   - The downloaded paper is processed by Llama-Index, which creates a document index for fast retrieval of relevant sections during the chatbot interaction.

3. **Chatbot Powered by ChatGPT**:

   - The chatbot interacts with users and provides answers based on the content of the downloaded and indexed research papers.

4. **Future Enhancements**:
   - The system will evolve to download referenced papers from the bibliography of the original research paper to ensure a deeper understanding and response accuracy. This will be vital in avoiding hallucinations and improving the chatbot's coverage of the topic.

## Architecture

- **Selenium Web Scraper**: Downloads research papers using the provided DOI.
- **Llama-Index**: Used to ingest and retrieve information from the downloaded research papers.
- **ChatGPT Integration**: Provides responses based on the research paper’s content using ChatGPT, ensuring user-friendly interactions.

  **Flow Diagram**:

  ```
  +------------------+       +-------------------------+        +-----------------------+
  | DOI Input        | ----> | Selenium (Web Scraping)  | -----> | Downloaded Paper      |
  +------------------+       +-------------------------+        +-----------------------+
                                                                    |
                                                                    v
                                                          +-----------------------+
                                                          | Llama-Index (RAG)     |
                                                          +-----------------------+
                                                                    |
                                                                    v
                                                          +-----------------------+
                                                          | Chatbot (ChatGPT API) |
                                                          +-----------------------+
  ```

## Future Work

1. **Bibliography Paper Downloading**:

   - Automatically identify and download papers referenced in the primary research paper.
   - Integrate these papers into the Llama-Index to improve the chatbot’s comprehension of the topic.

2. **Hallucination Prevention**:

   - Expand the training and retrieval system to minimize hallucinations and provide more factually grounded responses.

3. **User Interface**:

   - Develop a user-friendly interface to easily interact with the application and access the chatbot's functionality.

4. **Local LLM Support**:

   - Provide the option to run certain large language models locally on hardware capable of handling such models, for those who wish to avoid relying on external APIs.

5. **Performance Optimizations**:
   - Streamline paper processing and response generation for faster chatbot responses.

## Conclusion

This project aims to provide users with a highly accurate and responsive chatbot system tailored to the content of specific research papers. By incorporating additional resources such as referenced papers, developing a proper user interface, and allowing local LLM support, the chatbot's capacity to discuss and analyze research topics will greatly improve, ensuring comprehensive and reliable interactions.
