import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64
matplotlib.use('Agg')

def plot(X_train, y_train, X_test, y_test, predictions):

    plots = []
    for i in range(X_test.shape[1]):

        # Visualising the Training set results
        plt.scatter(X_train[:, i], y_train, color='red')
        plt.plot(X_train[:, i], predictions, color='blue')
        plt.title('Training set')
        plt.xlabel('Dependent')
        plt.ylabel('Independent')
        figfile = BytesIO()
        plt.savefig(figfile, format='png')
        figfile.seek(0)  # rewind to beginning of file
        plots.append(base64.b64encode(figfile.getvalue()).decode('utf-8'))
        plt.show()
        plt.close()

        # Visualising the Test set results
        plt.scatter(X_test[:, i], y_test, color = 'red')
        plt.plot(X_train[:, i], predictions, color = 'blue')
        plt.title('Test set')
        plt.xlabel('Dependent')
        plt.ylabel('Independent')
        figfile2 = BytesIO()
        plt.savefig(figfile2, format='png')
        figfile2.seek(0)  # rewind to beginning of file
        plots.append(base64.b64encode(figfile2.getvalue()).decode('utf-8'))
        plt.show()
        plt.close()

    return plots
