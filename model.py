import joblib
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as txt
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
df = pd.read_csv("new.csv")
x=df.loc[:,'Sentence']
y=df.loc[:,'Label']
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.90)
bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/1")
bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/3")
def get_sentence_embedding(sentences):
    preprocessed_text=bert_preprocess(sentences)
    return bert_encoder(preprocessed_text)['pooled_output']
#bert layers
text_input=tf.keras.layers.Input(shape=(),dtype=tf.string,name='text')
preprocessed_text=bert_preprocess(text_input)
outputs=bert_encoder(preprocessed_text)
#nueral network layers
l=tf.keras.layers.Dropout(0.1,name='dropout')(outputs['pooled_output'])
l=tf.keras.layers.Dense(1,activation='sigmoid',name='output')(l)
#model
model=tf.keras.Model(inputs=[text_input],outputs=[l])
METRICS = [
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall')
]
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=METRICS)
model.fit(x_train, y_train, epochs=10)
model.evaluate(x_test,y_test)
y_predicted = model.predict(x_test)
y_predicted = y_predicted.flatten()
y_predicted = np.where(y_predicted > 0.5, 1, 0)
cm = confusion_matrix(y_test, y_predicted)
print(sn.heatmap(cm, annot=True, fmt='d'))
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
print(classification_report(y_test, y_predicted))
model.save("bert_model.h5")
x=model.predict(["SELECT * FROM login WHERE admin='alan' AND passw='or 1=1'","SELECT * FROM login WHERE admin='alan' AND passw='arjun@1"])
print(x)