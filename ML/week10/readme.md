Instructions Lab 11

The task for today’s lab is to the effect of different kernel functions in soft margin SVM. In order to
visualize the effects of the kernel function, you will work in 2D space. Actually, you will start with a
feature space that has a dimensionality greater than 2 and then you will apply PCA to reduce the
dimensionality to 2. 
Start by downloading the water potability dataset from:
https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability

The last column gives the class label and the other columns represent the features of the samples.
Reduce the dimensionality of the feature space to 2 using PCA.
Perform a train-test split.
Apply linear SVM with hard margin and note the accuracy.
Now apply linear soft margin SVM with penalty = {0.01, 0.1, 1, 10, 100, 1000, 10000}. Note the accuracy
in each case.

Now apply polynomial soft margin SVM. Use the best penalty value as determined in the earlier step.
Use polynomials of order 2, 3 and 4. Note the accuracy in each case.

Now apply RBF soft margin SVM. Use the best penalty value as determined in the earlier step. Change
the value of sigma as {0.1, 1, 10}. Note the accuracy in each case.

For all the above cases show the decision boundary in a 2D plot. 
Samples belonging to the two classes
should be in two distinct colors. The decision boundary obtained using different values of the
hyperparameter should be plotted as a curve in the same plot.

In case you find the SVC function a little slow then do try the NuSVC function.

Show your work, even if it is partial, during the lab hours. What you show during the lab will
contribute toward your final grade.