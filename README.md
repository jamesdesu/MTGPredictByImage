# MTGPredictByImage

## Team Members
David Kim, Ericka Koyama, James DeSelms, Jess Sparrow

## Introduction
Our project, MTG Predictor, was undertaken to see if it would be possible to predict the type of a card based on the cover art image with an error rate lower than random chance, 20%. During the creation of the project, our team would discover the steps needed to convert our image data into something a computer can comprehend and use to train a model. In addition, our team would find what is involved in tuning our training model to more accurately predict the right card. Last, we use various other predictors to see if other training models offered a better accuracy result.

## Selection of Data

The source of our dataset was from the Scyfall API<sup>2</sup>. The Scryfall API has a wide variety of data available for the cards in the Magic: The Gathering universe. This universe encompasses a wide variety of decks and sets of cards.

Within these sets of cards, the Scryfall API provides information like the title of the card, mana cost, type of creature, card description, cover art, and much more.<sup>2</sup>

![Magic Card Types(Enchantment, Land, Instant or Sorcery, Artifact, and Creature)](/images/cardTypes.png?raw=true)

For our data, we selected five types of cards to examine: Enchantment, Land, Instant or Sorcery, Artifact, and Creature. Enchantments apply an effect to the playing field or game.<sup>1</sup> Land can be used as a resource.<sup>1</sup> Instant or Sorcery types apply a spell during your turn or a reaction to the opponents move.<sup>1</sup> Last, the creature types are your units.<sup>1</sup> We selected a total of one-hundred twenty-five cards split evenly among the five types.

![Python Code with out data munging and engineering](/images/dataEngineering.png?raw=true)

For our data input, there was a lot of munging required to remove data that was unneeded for our research. To start off, our team removed sixty-one unneeded features. For the feature our team was examining, type_line, we modified the string to remove any miscellaneous data that did not help in specifying the type of card. The other features that remained in the dataset included the image, name of the card, colors, color identity and several other features.

## Methods
*pic of the scrython github page*

Scrython - The Scrython python library was utilized to access the Scryfall API, previously mentioned in the data section, using native Python methods and commands.<sup>3</sup>

*pic of the SVC Documentation page*

SVM/SVC from SKLearn - For our predictor engine, we utilized the SVM/SVC library from SKLearn.<sup>4</sup> 

*variety of Magic the Gathering websites*

Official and Community Magic: The Gathering Websites - In preparation for this project, we researched on the topic through various official and community driven Magic: The Gathering websites to figure out more about the game and the cards that are involved.<sup>5</sup> 

## Results
*show correlation map*

Before creating our training model, our team looked at the features that we gathered from the cards. The heat map revealed that a lot of the features did not correlate strongly. The only features that had a strong correlation was the name of the card and oracle text. The oracle text refers to the official function description of a card by the publisher.<sup>6</sup>

*show artist by card type plot*

In addition, our team plotted which type of card a particular artist created. Our plot shows the top ten highest ranking values. The cards were created from a wide range of artists.

“Show artist by color type plot*

Last, our team plotted the color type of a card by a particular artist. Again our plot shows the top ten highest ranking values. Similar to the previous plot, there were a wide range of artists that were associated with the various color types.

*show our model, training, and accuracy code*

For our training model, we create an 80/20 split between our training and test data, respectively. 
After some parameter tuning, we were able to get the optimal results using the SVC model with the following parameters: kernel=’linear’ and C=1E10. This resulted in an accuracy of fifty percent. 


## Discussion
This result shows that building an accurate prediction model may require either a lot more data or tuning. Our training models used a small sample size due to the size of the images. If we were to use a larger dataset, our accuracy with our training model could have performed better. In addition, our results could improve with additional tuning of our training model. To our training model, the image of a creature versus a building may look similar in shape resulting in a lower accuracy than expected. If we were able to implement a solution for our training model to recognize facial or architectural features, this additional knowledge by our training model would likely result in much higher accuracy.

Two cards as an example.
Acrobatic maneuver
Aetherflux reservoir

Random state affects results. This may possibly show that the order of training may affect the accuracy.

Creatures are typically miscategorized; random state 3.


## Summary
Our team sought out to find a prediction engine that could predict the type of a Magic: The Gathering card just by the cover art, but the training model yielded substandard results using the SVM/SVC libraries from SKLearn. We found that additional data and tuning would be required to improve the accuracy of our training model if we were to use cover art with our prediction engine.

## Bibliography
###### 1 - https://primagames.com/tips/magic-gathering-card-type-guide
###### 2 - https://scryfall.com/docs/api/cards
###### 3 - https://github.com/NandaScott/Scrython
###### 4 - https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html?highlight=svc#sklearn.svm.SVC
###### 5 - https://mtgjson.com/, https://primagames.com/tips/magic-gathering-card-type-guide 
###### 6 - https://mtg-archive.fandom.com/wiki/Oracle_text 
###### 7- https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#sphx-glr-auto-examples-decomposition-plot-faces-decomposition-py
