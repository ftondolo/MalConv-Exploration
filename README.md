# MalConv-Exploration
A Study on Computational Performance of Malware Detection Using Convolutional Neural Networks
Final Project for COMSE 6998 - Hiph Performance machine Learning | Spring Semester 2023
Federico Tondolo - Pedro Leandro La Rotta

## Description
### What We Set Out To Do:
As Malware identifiaction is an ever growing problem in today's vastly digitally interconnected landscape we set out to explore the field of malware recognition and detection from the side of machine learning networks. Networks such as the convolutional model explord herein have the potential to provide a flexible and bleeding edge solution to teh task of malware identification and we sought to not only better understand the current ML efforts towards this task but attempt to improve performance, from both a temporal and quantitive standpoint, through the implementation of knowledge learned throughout the course of the semester in this course.

### What's Here?
Here we Have a jupyter notebook containing many of the models we tested including graohs of the data and print outs of the training for each. Moreover we have atached our dataset (a small sample of 40 execs, 20 malware and 20 freeware, if you would like the whole thing contact us!) alongside the categorization CSV (containing labels for each executable) the scripts wee used to scrape and label this data (in the scripts directory), saved models from our various experiments (in the checkpoints directory), and an example cofiguration file for an experimental run. We also have the code we used to run inference analysis on our model and a writeup of our findings.

### How do I run all of this?
To Execute our code there is not much you need to know thanks to the use of our Jupyter notebooks! Ensure your paths are updated to point to the correct directories but other than that it should be a simple matter of running the cells in sequence for the project to execute as intended!

## Results and Observations
While a more comprehensive view of our results is available in the writeup, here is a brief overview of how to interpret our data:

<img width="586" alt="image" src="https://github.com/ftondolo/MalConv-Exploration/assets/20714356/ec6c4b5d-5b91-4e15-b1da-af8d687eb0e4">

Distribution of inference times for samples run against the three versions of the MalConv model. There is a marginal improvement in mean inference time with weight quantization.

For Training, we kept track of three metrics with varying levels of granularity: loss, accurcy (cumulative, averaged out over an epoch as batchs are fed into the model), and loss (batch by batch). We used these with the intent of training two models, the first, highly accurate, which while slow from a computational standpoint (both with regards to inference and training) which would allow for better malware recognition albeit run and trained on a sporadic basis (as a normal anti-virus software might scan a drive at EOD for any malicious packages installed during the day; the other, far faster, less accurate and prone to false positives but able to be quickly trained and run to provide a seamless 24/7 protection which could seamlessly integrate new viral samples in its dataset while running its program with little computational overhead.
We can see what our metrics looked like for a particular model below (though again, more detail can be found in our writeup):
Loss over Training:

<img width="586" alt="Screenshot 2023-05-11 at 22 39 56" src="https://github.com/ftondolo/MalConv-Exploration/assets/51007153/1dbe7e66-cd28-49d7-a1fd-5aae18c48d69">

Training and Validation Times with regards in Proportion Dataloader Enumeration Time:

<img width="586" alt="Screenshot 2023-05-11 at 22 39 27" src="https://github.com/ftondolo/MalConv-Exploration/assets/51007153/a6958cc3-4927-4bba-8b2d-ed0894eccbce">

And Finally, Accuracy, in this instance not cumulative but on a by-batch basis:

<img width="586" alt="Screenshot 2023-05-11 at 22 39 47" src="https://github.com/ftondolo/MalConv-Exploration/assets/51007153/e0a2baba-4d90-4273-82c3-dc122d6c3efa">
