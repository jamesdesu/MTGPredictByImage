# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Reset the kernel between runs, an IncompleteRead error is raised otherwise.

#Import numpy.
import numpy as np
#Import pandas.
import pandas as pd
#Import scrython. Be sure to install it with pip or what have you.
import scrython
#Import seaborn.
import seaborn as sns
#Import nest_asyncio.
import nest_asyncio
#Import train_test_split from model sklearn.
from sklearn.model_selection import train_test_split
#Import io from skimage.
from skimage import io
#Import GaussianNB from sklearn.
from sklearn.naive_bayes import GaussianNB
#Import Isomap from sklearn.
from sklearn.manifold import Isomap
#Import accuracy score from sklearn.
from sklearn.metrics import accuracy_score

#The number of cards per type to use.
no_cards_per_type = 20;
#The number of card types.
no_types = 5;

#Apply nest_asyncio.
nest_asyncio.apply()

#Query for some cards.
cards = scrython.cards.Search(q='((set:kld and -set:aer) or (-set:kld and set:aer)) and ((-type:"artifact creature" -type:"legendary" -type:vehicle -type:basic) or (!Plains or !Island or !Swamp or !Mountain or !Forest)) set:kld unique:prints')
#Query for some more cards. We perform a second query in order to reduce confusion.
more_cards = scrython.cards.Search(q='(-set:kld and set:aer) -type:"artifact creature" -type:legendary -type:vehicle')
#Load both of those cards into a dataframe.
df = pd.DataFrame(cards.data()).append(more_cards.data())
#Split the image_uris into three columns.
df = pd.concat([df.drop(['image_uris'], axis=1), df['image_uris'].apply(pd.Series)], axis=1)
#Drop uneeded columns.
df = df.drop(['id', 'oracle_id', 'multiverse_ids', 'mtgo_id', 'mtgo_foil_id', 'tcgplayer_id', 'cardmarket_id', 'lang', 
    'released_at', 'uri', 'scryfall_uri', 'layout', 'highres_image', 'image_status', 'keywords', 'legalities', 'games',
    'reserved', 'foil', 'nonfoil', 'oversized', 'promo', 'reprint', 'variation', 'set_type', 'set_uri', 'set_search_uri',
    'scryfall_set_uri', 'rulings_uri', 'prints_search_uri', 'collector_number', 'digital', 'rarity', 'flavor_text', 'set',
    'card_back_id', 'artist_ids', 'illustration_id', 'border_color', 'frame', 'full_art', 'textless', 'booster', 'set_name',
    'story_spotlight', 'edhrec_rank', 'prices', 'related_uris', 'purchase_uris', 'power', 'toughness', 'border_crop',
    'produced_mana', 'all_parts', 'watermark', 'promo_types', 'small', 'normal', 'large', 'png'], axis=1).groupby('type_line').head(no_cards_per_type)
#Use regex to manipulate typlines so they contain no subtypes or supertypes.
df = df.replace(regex=r'^Creature(.*)', value='Creature')
df = df.replace(regex=r'^Artifact(.*)', value='Artifact')
df = df.replace(regex=r'^Enchantment(.*)', value='Enchantment')
#Combine instant and sorcery into one type.
df = df.replace(regex=r'^Sorcery(.*)', value='Instant or Sorcery')
df = df.replace(regex=r'^Instant(.*)', value='Instant or Sorcery')
#Change all Basic Lands into just Land.
df = df.replace(regex=r'^Basic(.*)', value='Land')
#Turn colors into a concetenated string (e.g., WUBRG) instead of a list (e.g., [W,U,B,R,G]).
df['colors'] = df['colors'].apply(lambda x: 'C' if not x else ''.join(x))

#Take the image urls.
image_urls = df['art_crop'].values.tolist()
#Take the raw image data.
images = np.array([io.imread(url) for url in image_urls])
#Get the dimensions for reshaping.
nsamples, nx, ny, nz = images.data.shape
#Set X to the reshaped images.
X = images.reshape((nsamples,nx*ny*nz))
#Isomap.
iso = Isomap(n_components=4)
#Fit X.
iso.fit(X)
#Transform X.
data_projected = iso.transform(X)
#Set y to the type lines.
y = df['type_line']
#Set Xtrain, Xtest, ytrain, and ytest to randomly distributed cards.
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=30, train_size=70)

#Create a Gaussian NB model.
model = GaussianNB()
#Fit this model.
model.fit(Xtrain, ytrain)
#Test model performance.
y_model = model.predict(Xtest)
#Print the accuracy.
print(accuracy_score(ytest, y_model))

#Plot some interesting data...
#Which type lines are the most common?
df['type_line'].value_counts().plot.bar()
#Which artists?
df['artist'].value_counts()[:10].plot.bar()
#Which colors?
df['colors'].value_counts().plot.bar()
#Plot out a heatmap of a few columns. I don't know if this actually means anything.
sns.heatmap(df.drop(['object', 'color_identity', 'art_crop'], axis=1).apply(lambda x: x.factorize()[0]).corr())
#What are the most common type line artist combinations?
df.groupby('artist')['type_line'].value_counts().sort_values(ascending=False)[:10].plot.bar()
#What are the most common artist color combinations?
df.groupby('artist')['colors'].value_counts().sort_values(ascending=False)[:10].plot.bar()
#What are the most common color type line combinations?
df.groupby('colors')['type_line'].value_counts().sort_values(ascending=False)[:10].plot.bar()