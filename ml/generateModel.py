import tensorflow as tf
import matplotlib.pyplot as plt
import emnist


def generate_model():
    model = tf.keras.Sequential()

    train_images, train_labels = emnist.extract_training_samples('letters')
    test_images, test_labels = emnist.extract_test_samples('letters')
    print(train_labels.shape)

    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(train_labels[i])
    plt.show()

    train_images = train_images / 255.0

    test_images = test_images / 255.0

    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
    model.add(tf.keras.layers.Dense(256, activation="relu"))
    model.add(tf.keras.layers.Dense(128, activation="relu"))
    model.add(tf.keras.layers.Dense(64, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.04))
    model.add(tf.keras.layers.Dense(27))

    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=35)
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    model.save('model.myLetters')

    print('\nTest accuracy:', test_acc)
