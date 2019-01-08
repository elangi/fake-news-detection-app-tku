# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:07:10 2018

@author: sone_e
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.externals import joblib
from sklearn.calibration import CalibratedClassifierCV

# Multinomial Naives Bayes(MNB)


def multinomialNB(X_train, X_test, y_train, y_test):
    mnb = MultinomialNB()
    mnb.fit(X_train, y_train)  # train training set
    # test model with X_test, store the result in y_pred
    y_pred = mnb.predict(X_test)

    print("The accuracy of Multinomial Naives Bayes classifier is: ",
          mnb.score(X_test, y_test))
    print(classification_report(y_test, y_pred))
    '''
    cm = metrics.confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])
    plot.plot_confusion_matrix(cm, classes=['FAKE', 'REAL'])
    '''
    save_model(mnb)

# Decision Tree


def decisionTree(X_train, X_test, y_train, y_test):
    tree = DecisionTreeClassifier(criterion='entropy')
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)

    print("The accuracy of Decision Tree classifier is: ",
          tree.score(X_test, y_test))
    print(classification_report(y_test, y_pred))

    save_model(tree)

# Linear support vector classifier


def svc(X_train, X_test, y_train, y_test):
    svc = LinearSVC()
    #svc.fit(X_train, y_train)
    clf = CalibratedClassifierCV(svc, cv=5)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("The accuracy of SVC classifier is: ", clf.score(X_test, y_test))
    print(classification_report(y_test, y_pred))

    save_model(clf)

# random forests


def randomForest(X_train, X_test, y_train, y_test):
    forest = RandomForestClassifier()
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)

    print("The accuracy of Random Forest classifier is: ",
          forest.score(X_test, y_test))
    print(classification_report(y_test, y_pred))

    save_model(forest)

# logistic regression


def logisticReg(X_train, X_test, y_train, y_test):
    lr = LogisticRegression()

    lr.fit(X_train, y_train)  # train model with fit
    lr_y_predict = lr.predict(X_test)  # use trained lr model to test X_test

    print("The accuracy of LR classifier is: ", lr.score(X_test, y_test))
    print(classification_report(y_test, lr_y_predict))

    save_model(lr)

#SGDClassifer


def sgdClassifier(X_train, X_test, y_train, y_test):
    sgdc = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5)
    sgdc.fit(X_train, y_train)
    sgdc_y_predict = sgdc.predict(X_test)

    print("The accuracy of SGD classifier is: ", sgdc.score(X_test, y_test))
    print(classification_report(y_test, sgdc_y_predict))

    save_model(sgdc)

# Gradient Tree Boosting


def gradientBoost(X_train, X_test, y_train, y_test):
    gbc = GradientBoostingClassifier()
    gbc.fit(X_train, y_train)
    y_pred = gbc.predict(X_test)

    print("The accuracy of Gradient Tree Boosting classifier is: ",
          gbc.score(X_test, y_test))
    print(classification_report(y_test, y_pred))

    save_model(gbc)


def save_model(classifier):
    joblib.dump(classifier, 'classifier.pkl')
