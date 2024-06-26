# NLP_summarization

<img src="https://github.com/piyushjain4/NLP_summarization/blob/main/summarizer.png?raw=true" alt="RLE" width="400" />

### Description :
- In this project, we will compare 5 different state-of-the-art models to summarize articles from BBC news dataset.
- Given an article each model predicts the summary for the article.
- Then we compare summaries predicted by the models.

### Link to project :
[Live Summarization Demo!](https://colab.research.google.com/drive/1HLG7Touc97xg1noJvg6u6hdwyPsEf4AR#scrollTo=zr8qrzvhBP_C)
  
### Screenshots from the project :
<img src="https://github.com/piyushjain4/NLP_summarization/blob/main/Screenshot 2024-06-01 074835.png?raw=true" alt="RLE" width="400" />
<img src="https://github.com/piyushjain4/NLP_summarization/blob/main/Screenshot 2024-06-01 075300.png?raw=true" alt="RLE" width="400" />

### Dataset:
- The data is taken from [hugging face dataset](https://huggingface.co/datasets/gopalkalpande/bbc-news-summary)
- The dataset contains summaries for about 2300 BBC-news articles of five different domains i.e;
  1) Entertainment
  2) politics
  3) Tech
  4) sport
  5) business

### visualizing data:
<img src="https://github.com/piyushjain4/NLP_summarization/blob/main/Screenshot%202023-08-10%20221710.png?raw=true" alt="RLE" width="400" />

### Contents
- Training_notebooks:  Contains the notebooks used for training. Contains training notebook for each of the 5 models
- Inference_notebook:  Contains the notebooks used for Inference

### Training
- Finetuned 5 different SOTA models from pretrained models from hugging face transformer library.
- Trained models include
   1) Google's T5
   2) Facebook's BART
   3) AllenAI's Longformer
   4) OpenAI's GPT-2
   5) Google' pegasus
- Transfer-learning was used by taking these pretrained models and finetuning them on BBC-news data
### Transfer-learning
- Transfer learning (TL) is a technique in machine learning (ML) in which knowledge learned from a task is re-used in order to boost performance on a related task

### Inference-time
- All the models are compared according to their summary generated using rogue score

### Rouge_score
- Recall-Oriented Understudy for Gisting Evaluation (ROUGE) scoring algorithm calculates the similarity between a candidate document and a collection of reference documents
- It is a widely used metric for summarization evaluation
- But this metric tries matching exact words between predicted summary and label
- As summaries can be written in different ways so human evaluation is also needed

### Comparing models on the basis of rogue score

| Model | rouge1 | rougeL|
|-------|------------------|-----------------|        
| T5 | 35.93 | 27.79 |
| Bart | 54.12 | 54.12 |
| Longformer | 45.31 | 27.19 |
| GPT-2 | 32.16 | 16.22 |
| pegasus | 44.37 | 30.62 |

Note : Here rouge scores are multiplied by 100

### GPT-2
- GPT performed the worst, likely because it is an autoregressive model rather than an encoder-decoder architecture.
-  While GPT generates text by predicting the next token in a sequence, encoder-decoder models can utilize the entire input context, leading to better performance in tasks requiring full context understanding.
- GPT-2 was trained as a language model so it could do many NLP tasks.
- For summarization it was pretrained by adding " TL;DR " (too long didn't read) between the input and the label

- For all other models we used a prefix " Summarize: " before input text
### BART
- This model is by Facebook AI research that combines Google's BERT as encoder and OpenAI's GPT as decoder .  It is bidirectional like BERT and is auto-regressive like GPT.
- it does a commendable job at providing extractive summaries from the text.

### Longformer
- Transformer-based models are unable to process long sequences due to their self-attention operation, which scales quadratically with the sequence length
- so we use Longformer with an attention mechanism that scales linearly with sequence length, making it easy to process documents of thousands of tokens or longer
- Here longformer has a good rouge score but sentences get repeated in its output which shows that rouge score is not the best metric for evaluation

### T5
- T5, or Text-to-Text Transfer Transformer, is a Transformer based architecture that uses a text-to-text approach
- It does not perform well in our dataset as it had grammatical and context errors

### pegasus
- It uses pretraining objectives based on abstractive summarization
- It performed quite well for our dataset and produced good abstractive summaries i,e; output contains new text and summaries not present in input

### Follow up Work
- We could add an extra feature that provides a summary from any website given its URL. This enhancement would enable users to quickly understand the content of a webpage without needing to read the entire text.




