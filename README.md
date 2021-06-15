# MTGPredictByImage

## Team Members
David Kim, Ericka Koyama, James DeSelms

## Introduction
Our project, <b>MTGPredictByImage</b>, was undertaken to see if it would be possible to predict the type of a card based on the cover art image with an accuracy rate higher than random chance, 20%. During the creation of the project, our team would discover the steps needed to convert our image data into something a computer can comprehend and use to train a model. In addition, our team would find what is involved in tuning our training model to more accurately predict the right card. Last, we use various other predictors to see if other training models offered a better accuracy result.

## Selection of Data
The source of our dataset was from the <b>Scyfall API</b><sup>2</sup>. The Scryfall API has a wide variety of data available for the cards in the Magic: The Gathering universe. This universe encompasses a wide variety of decks and sets.

Within these sets of cards, the Scryfall API provides information like the title of the card, mana cost, type of creature, card description, cover art, and much more.<sup>2</sup>

![Magic Card Types(Enchantment, Land, Instant or Sorcery, Artifact, and Creature)](/images/cardTypes.png?raw=true)

For our data, we selected five types of cards to examine: <b>Enchantment, Land, Instant or Sorcery, Artifact, and Creature</b>. Enchantments apply an effect to the playing field or game.<sup>1</sup> Land can be used as a resource.<sup>1</sup> Instant or Sorcery types apply a spell during your turn or a reaction to the opponents move.<sup>1</sup> Artifact cards have a wide range of uses.<sup>1</sup> Last, the creature types are your units.<sup>1</sup> We selected a total of one-hundred twenty-five cards split evenly among the five types.

![Python Code with out data munging and engineering](/images/dataEngineering.png?raw=true)

For our data input, there was a lot of munging required to remove unneeded data. To start off, our team removed sixty-one unneeded features. For the feature our team was examining, type_line, we modified the string to remove any miscellaneous data that did not specify the type of the card. The other features that remained in the dataset included the image, name of the card, colors, color identity and several other features.

## Methods
<b>Scyfall API</b> - The Scryfall API was used as the source of our data.<sup>2</sup>

<b>Scrython</b> - The Scrython python library was utilized to access the Scryfall API, previously mentioned in the data section, using native Python methods and commands.<sup>3</sup>

<b>SVM/SVC from SKLearn</b> - For our predictor engine, we utilized the SVM/SVC library from SKLearn.<sup>4</sup> 

<b>Official and Community Magic: The Gathering Websites</b> - Our team researched Magic: The Gathering through various official and community driven websites to gather more information about the various data points that could be used within a playing card.<sup>5</sup> 

## Results

![Correlation heat map](/images/heatmap.png?raw=true)

Before creating our training model, our team looked at the features that we gathered from the cards. The heat map revealed that a lot of the features did not correlate strongly. The only features that had a strong correlation was the name of the card and oracle text. The oracle text refers to the official function description of a card by the publisher.<sup>6</sup>

![Artist by type](/images/artistByType.png?raw=true)

In addition, our team plotted which type of card a particular artist created. Our plot shows the top ten highest ranking values. The cards were created from a wide range of artists.

![Artist by color](/images/artistByColor.png?raw=true)

Last, our team plotted the color type of a card by a particular artist. Again our plot shows the top ten highest ranking values. Similar to the previous plot, there were a wide range of artists that were associated with the various color types.

![training mode and accuracy](/images/model.png?raw=true)

For our training model, we create an 75/25 split between our training and test data, respectively. Our preferred predictor engine was the SVC library. We tried other predictor engines, such as SGDClassifier, but those predictor engines, with additional parameter tuning, resulted in lower accuracy scores. We were able to get the optimal results using the following parameters with the SVC library: kernel=’linear’ and C=1E10. In addition, we found that the random state affected our accuracy results. Our team found the optimal value to be 7. This tuning resulted in an <b>accuracy of forty-four percent.</b>

Out of all the card types, the creature cards were miscategorized heavily. The land and instant or sorcery type cards were generaly categorized correctly. Below is a screenshot of the confusion matrix.

![training mode and accuracy](/images/confusionMatrix.png?raw=true)

## Discussion
This result shows that building an accurate prediction model may require either a lot more data or tuning. Our training models used a small sample size due to the size of the images. If we were to use a larger dataset, our accuracy with our training model could have performed better. In addition, our results could improve with additional tuning of our training model. To our training model, the image of a creature versus another type of card may look similar in shape. You can see this occur with the following two cards below.

![training mode and accuracy](/images/exampleCards.png?raw=true)

If we were able to implement a solution for our training model to recognize facial or architectural features, this additional knowledge by our training model would likely result in much higher accuracy.

## Summary
Our team sought out to find a prediction engine that could predict the type of a Magic: The Gathering card just by the cover art, but the training model yielded substandard results using the SVM/SVC libraries from SKLearn. We found that additional data and tuning would be required to improve the accuracy of our training model if we were to use cover art with our prediction engine.

## Bibliography
###### 1 - https://primagames.com/tips/magic-gathering-card-type-guide
###### 2 - https://scryfall.com/docs/api/cards
###### 3 - https://github.com/NandaScott/Scrython
###### 4 - https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html?highlight=svc#sklearn.svm.SVC
###### 5 - https://mtgjson.com/, https://primagames.com/tips/magic-gathering-card-type-guide 
###### 6 - https://mtg-archive.fandom.com/wiki/Oracle_text 
