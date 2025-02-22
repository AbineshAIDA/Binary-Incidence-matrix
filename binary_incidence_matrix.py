# -*- coding: utf-8 -*-
"""Binary_incidence_matrix.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OLjF2RbF1-Miz37PIKL4kHHPSnY1OapW
"""

def create_binary_incidence_vectors(documents, dictionary):

    sorted_dictionary = sorted(dictionary)


    binary_incidence_vectors = []


    for document in documents:

        binary_vector = []


        for word in sorted_dictionary:

            if word in document:

                binary_vector.append(1)
            else:

                binary_vector.append(0)


        binary_incidence_vectors.append(binary_vector)

    return binary_incidence_vectors


documents = ["This is document 1.", "Another document here.", "Document three."]
dictionary = ["Another", "Document", "This", "is", "document", "here", "three"]
binary_vectors = create_binary_incidence_vectors(documents, dictionary)
print(binary_vectors)