# NLP_summarization
### Description :
- In this project, we will compare 5 different state-of-the-art models to summarize articles from BBC news dataset.
- Given an article each model predicts the summary for the article.
- Then we compare summaries predicted by the models.

### Dataset:
- The data is taken from [hugging face dataset](https://huggingface.co/datasets/gopalkalpande/bbc-news-summary)
- The dataset contains summaries for about 2300 BBC-news articles of five different domains i.e;
  1) Entertainment
  2) politics
  3) Tech
  4) sport
  5) business

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
| GPT-2 | 99.77 | 99.77 |
| pegasus | 44.37 | 30.62 |

Note : Here rouge scores are multiplied by 100

### GPT-2
- As we can see GPT-2 outperforms all the other models by a big margin.
- GPT-2 was trained as a language model so it could do many NLP tasks.
- For summarization it was pretrained by adding " TL;DR " (too long didn't read) between the input and the label
- So while training we did the same

### BART
- This model is by Facebook AI research that combines Google's BERT as encoder and OpenAI's GPT as decoder .  It is bidirectional like BERT and is auto-regressive like GPT.
- it also does a nice job

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




