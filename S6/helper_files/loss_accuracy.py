# -*- coding: utf-8 -*-
"""loss_accuracy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U6q01bRAMfhg9x5itLWAKnVxK9d8_hpU
"""

import matplotlib.pyplot as plt

def visualize_graph(filepath, regularizers, train_loss, test_loss, train_accuracy, test_accuracy):
  '''
  Function to visualize the training and test loss and accuracy graphs.

  :param train_loss: (dict), dictionary of mappings between each regularization option and it's list of losses during training
  :param test_loss: (dict), dictionary of mappings between each regularization option and it's list of losses during testing
  :param train_accuracy: (dict), dictionary of mappings between each regularization option and it's list of accuracies during training
  :param test_accuracy: (dict), dictionary of mappings between each regularization option and it's list of accuracies during testing
  '''
  fig, axs = plt.subplots(2, 2, figsize = (12, 8))
  for reg_type in regularizers:
      # Plot training loss
      axs[0, 0].plot(train_loss[reg_type])
      axs[0, 0].set_title('Training Loss Curve')
      axs[0, 0].set_xlabel('Epochs')
      axs[0, 0].set_ylabel('Training Loss')
      axs[0, 0].legend(regularizers)
      # Plot training accuracy
      axs[0, 1].plot(train_accuracy[reg_type])
      axs[0, 1].set_title('Training Accuracy Curve')
      axs[0, 1].set_xlabel('Epochs')
      axs[0, 1].set_ylabel('Training Accuracy')
      axs[0, 1].legend(regularizers)
      # Plot test loss
      axs[1, 0].plot(test_loss[reg_type])
      axs[1, 0].set_title('Test Loss Curve')
      axs[1, 0].set_xlabel('Epochs')
      axs[1, 0].set_ylabel('Test Loss')
      axs[1, 0].legend(regularizers)
      # Plot test accuracy
      axs[1, 1].plot(test_accuracy[reg_type])
      axs[1, 1].set_title('Test Accuracy Curve')
      axs[1, 1].set_xlabel('Epochs')
      axs[1, 1].set_ylabel('Test Accuracy')
      axs[1, 1].legend(regularizers)
  fig.tight_layout()
  fig.savefig(filepath + '/EVA_figures/train_test_loss_accuracy.png');