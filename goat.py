# -*- coding: utf-8 -*-
"""GOAT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1949iZ8EFk-nWW3fjR0PfzR9gAEutetf4
"""

#!pip install -q sklearn

import tensorflow as tf
import pandas as pd
import random

column=['name','author']
genre=['fiction','non-fiction','sci-fi','humour','mystery','thriller','horror']

train=pd.read_excel('https://drive.google.com/uc?id=13nsAHr6bZMNKMR_KHHJ6jxcaeAXQ_STe&export=download')
train.head()

l_train=train.pop('genre')
l_train.head()

def input_fn(feature,labels,training=True,batch_=32):
  dt=tf.data.Dataset.from_tensor_slices((dict(feature),labels))

  if training:
    dt=dt.shuffle(600).repeat()
  return dt.batch(batch_)

indicator_column_name=['name','author']
feature=[]
for col_name in indicator_column_name:
  categorical_column=tf.feature_column.categorical_column_with_vocabulary_list(
      col_name, train[col_name].unique())
  indicator_column=tf.feature_column.indicator_column(categorical_column)
  feature.append(indicator_column)

print(feature)

mod=tf.estimator.DNNClassifier(
    feature_columns=feature,
    hidden_units=[14,8],
    n_classes=7
)

mod.train(
    input_fn=lambda: input_fn(train,l_train,training=True),
    steps=2000
)

def pre_fn(features,batch_size=32):
   return tf.data.Dataset.from_tensor_slices(dict(features)).batch(batch_size)

features=['name','author'] 
predict={}

print("please type in the name of last book you read: ")

for feature in features:
  valid=True
  while valid:
    val=input(feature+": ")
    res= isinstance(val,str)
    if not str(res)==False:
      valid=False
 
  predict[feature]=[str(val)]
prediction=mod.predict(input_fn=lambda: pre_fn(predict))
for pred in prediction :
  class_id=pred['class_ids'][0]
  prediction=genre [class_id]
result=class_id
print(result)

fiction=['The Great Gatsby, by F. Scott Fitzgerald',"F*ck! I'm in My Twenties by Emma Koenig",'The Fault in Our Star by John Green','A Man in Full by Tom Wolfe'
             'Timeline by Michael Crichton','The Thief by Megan Whalen','The Plot Against America by Philip Roth', 'There There by Tommy Orange','Angels and Demons by Dan Brown'
              ,'11/22/63 by Stephen King']


non-fiction= ['Common Ground by J. Anthony Lukas','Hackers: Heroes of the Computer Revolution by Steven Levy','The Soul of a New Machine by Tracy Kidder'
             ,' Gifts of Deceit by Robert B. Boettcher','Untamed by Glennon Doyle','Breath: The New Science of a Lost Art by James Nestor',' Too Much and Never Enough by Mary L. Trump',
             'Life by James Fox','The Emperor of All Maladies by Siddhartha Mukherjee','Parting the Waters by Taylor Branch' ]


sci-fi=[" Ender's Game by Orson Scott Card","'Consider Phlebas by Iain Banks'","'Blood Music by Greg Bear'","'Footfall by Jerry Pournelle'","' Agency by William Gibson'","'Contact by Carl Sagan'"
           ,"'The Fifth Season by N. K. Jemisin'","'Red Rising by Pierce Brown'","'Six Wakes by Mur Lafferty","The Wise Mans Fear by Patrick Rothfuss"]





humour=['Deep Thoughts by Jack Handey','Big Trouble by Dave Barry','Election by Tom Perrotta',' About a Boy by Nick Hornby','Trainspotting by Irvine Welsh','Wishful Drinking by Joshua Ravetch'
              'I Am America by Stephen Colbert','Into Hot Air by Chris Elliott','Less by Andrew Sean Greer','Trust No Aunty by Maria Qamar']




mystery=['THE MISTLETOE MURDER by P.D JAMES','GONE GIRL by GILLIAN FLYNN','ANATOMY OF A MURDER by ROBERT TRAVER','THE DAUGHTER OF TIME by JOSEPHINE TEY'
              ,'THE HOUND OF THE BASKERVILLES by SIR ARTHUR CONAN DOYLE','CASE HISTORIES by KATE ATKINSON','SHUTTER ISLAND by DENNIS LEHANE'
        	,'THE FIRM by JOHN GRISHAM','OUT by NATSUO KIRINO','THE GOLDEN SCALES	by PARKER BILAL']


thriller=[ 'BIG LITTLE LIES by LIANE MORIARTY','THE DINNER by HERMAN KOCH','THE GIRL ON THE TRAIN by PAULA HAWKINS','LONG MAN by AMY GREENE','THE SILENCE OF LAMBS by THOMAS HARRIS'
           ,'TELL NO ONE by HARLAN COBEN','WOLF IN WHITE VAN by JOHN DARNIELLE','A TIME TO KILL by JOHN GRISHAM',' JAWS by PETER BENCHLEY','DARK MATTER by BLAKE CROUCH']




horror=['Children of the Night by Dan Simmons','The Cipher by Kathe Koja','No Blood Spilled by Les Daniels','Superstitious by R. L. Stine','The Fisherman by Zoe L. Albright	'
            ,'My Best Friends Exorcism by Grady Hendrix','Horns by Joe Hill','Rot & Ruin by Jonathan Maberry','Home Before Dark by Riley Sager','Malorie by Josh Malerman'		]

a=random.randint(0,10)
print(a)

if result==0:
  print(fiction[a])

  elif result==1:
    print(non-fiction[a])

  elif result==2:
     print(sci-fi[a])

  elif result==3:
     print(humour[a])

   elif result==4:
     print(mystery[a])

   elif result==5:
    print(thriller[a])

   elif result==6:
    print(horror[a])