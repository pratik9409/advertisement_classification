# Advertisement Classification

![advert](https://user-images.githubusercontent.com/67755812/204614265-deda81a7-137b-479b-9be5-705b06197fb0.gif)


In this project we will be working on text dataset which holds transcriptions for video of different ads. We preprocess the data into a more usable format and train our Deep Learning LSTM model. This model is based on Neural Net-Architecture and provides very high performance on sequence based datsets as it has a feedback structure helping the model remembe sequence of data input and the changes that are happening. Then we create a django-project which becomes our base website that will be hosted on google cloud.

LSTM networks were designed specifically to overcome the long-term dependency problem faced by recurrent neural networks RNNs (due to the vanishing gradient problem). LSTMs have feedback connections which make them different to more traditional feedforward neural networks. This property enables LSTMs to process entire sequences of data (e.g time series) without treating each point in the sequence independently, but rather,retaining useful information about previous data in the sequence to help with the processing of new data points.

The dataset contains 4 columns (Video id, Title, Description and Category) and 10333 rows.
In the Description columns we have some null values that we will be dropping it. Because its a categorical values and we can't just predict the Description of video based on Title. Also checked for the duplicate rows with same Title, that may contain Description but there were no values for the same Title. So decided to drop the rows with NaN values.

Then we will use the stopwords and set the words to English. Then I have created a list which I thought might be useful because the stop words do not provide much information, so I added some more stop words in the list.
Now we will preprocess, as the text data is unstructured and at most part it is inconsistent too. So we need a function to clean the data before moving with feature engineering or any other things. The pre-process function takes the text that is just a sentence, then will lower casing each and every word in the sentence. After that, we remove different kind of tags, special character. Then we will split our text data into words using list.And will remove the stopwords. We will check the stopwords from the list that is been splited and will remove the stopwords. After this we will remove the word that has letters less than 3. Then lastly I am lemmatizing my words. As we have splitted our sentence to words for cleaning now again we join the words to form a sentence.

We create a new dataframe docs and will save some random 5000 rows in it.
Afterwards we will use LabelEncoder to encode the Category columns values to numerical values.

Now we will be vectorizing text features using TF-IDF (Term Frequency - Inverse Document Frequency). So now, we will take our clean data and create features using the clean data. Term Frequency of word in a document  is a real count of instances . Inverse Document Frequency of the word is actually calculated across a set of documents. So I have created a object for title and description differently; setting the normalization to l2 and n_gram to (1,2) (n_gram is actually set of words). Then we fit and transform the title and description.

So now we will be using LSTM model to train the data. Firstly, I have specified maximum nuber of words as 10000, sequence length as 50 and embedding dimensions as 100. Now will be combining title and description into a single sentence then with the help of tokenizer function from keras (spedcifically made for text data handling) then we fit_on_texts our data and we word_index as well. Now we will convert the text data to numerical data (padded sequences) so that we can input into the model. After this we encode our category data using one hot encoding.
Now we train test split the data to X_train, X_test, y_train, y_test.
After splitting we finally define the LSTM model. LSTM model takes the input with max numbers of words, embedding dimension and input length. Then we will take 100 neurons for LSTM model and dropout and recurrent_dropout is 0.2, then setting the Dense activation function as "softmax". Then we will compile the model. We can see the information with the help of model.summary function. 
Now we will train the model with epochs as 25 amd batch size as 128 and fit the model. So we plot a graph to understand how the model working. So in the graph we can see that the train or loss function is constant till 23 and aferwards it increases a little. So from here, I can understand that maybe in my model I should stop at 23 epoch because I'm getting the lowest loss here. 

![loss_plot](https://user-images.githubusercontent.com/67755812/203398662-ae8ec687-a6d9-478f-aa71-cf847475ae6a.png)


Then in test data we can see that it is varying and at 23 it increases a lot. We can see the accuracy plot for train it is 0.99 and for test it is 0.95 or 0.96. 

![accuracy_plot](https://user-images.githubusercontent.com/67755812/203398687-1b7be4be-8d80-4923-bc81-f06bc71b825c.png)
