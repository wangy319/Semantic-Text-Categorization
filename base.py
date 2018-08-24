import os
import string
import json

def main():
    #f = ReadAndSave()
    #fp = open("C:\\Users\\HN65058\\Desktop\\data.txt", 'w')
    #fp.writelines(["%s\n" % item for item in f])
    #fp.close()
    #print(len(f))

    sentences = ReadAndSave("C:\\Users\\HN65058\\Desktop\\WinError.h")
    fp = open("C:\\Users\\HN65058\\Desktop\\unfiltered.txt", 'w')
    fp.writelines(["%s\n" % item for item in sentences])
    fp.close()


    keywords = FilterOut(sentences)
    fp = open("C:\\Users\\HN65058\\Desktop\\filtered2.txt", 'w')
    fp.writelines(["%s\n" % item for item in keywords])
    fp.close()


def ReadAndSave(file_path):
    f = open(file_path, 'r')
    read_data = f.readlines()
    f.close()
    list = []
    for i in range(0, len(read_data)):
        if "MessageId" in read_data[i]:
            if "MessageText" in read_data[i+2]:
                value = read_data[i+4].split("// ")[1].strip()
                sublist = value.split(" ")
                list.append(sublist)
    return list


def FilterOut(collection):

    filter_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    for i in range (0, len(collection)):
        collection[i] = list(filter(lambda word: word.lower() not in filter_list, collection[i]))

    return collection


if __name__ == "__main__":
    main()





