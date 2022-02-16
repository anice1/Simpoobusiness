import matplotlib.pyplot as plt


def plot_lr(history, experiment_name:str, lr=3e-1):
    """plots the learning rate curve of our model

    Args:
        history ([type]): [description]
        lr (learning_rate, optional): The set learning rate of your model, if not set, defaults to Adam optimizer's learning rate 3e-1.
    """

    loss = history.history["loss"]
    learning_rate = lr * 10 ** (np.arange(len(loss))/20)
    plt.plot(lr, loss)
    plt.xlabel('Learning Rate')
    plt.ylabel('Loss')
    plt.title(experiment_name)
