from dataStructures import *
from random import randrange, seed


def solution(llist1, llist2):
    # TODO write your answer here
    l1 = llist1.getLinkedlist()
    l2 = llist2.getLinkedlist()
    mergedlsit = llist1.getLinkedlist() + llist2.getLinkedlist()
    l3 = LinkedList()
    for i in mergedlsit:
        l3.addwithsort(i)
    return l3


    """
    merge the 2 sorted linked lists into a single output list
    :param llist1: the first sorted linked list
    :param llist2: the second sorted linked list
    :return: output sorted linkedlist

    Sample input
    2 16 19 24 25 26 30 31 32 48
    6 8 8 13 18 22 32 37 39 48

    Expected output
    out list: 2 6 8 8 13 16 18 19 22 24 25 26 30 31 32 32 37 39 48 48
    """
    return out


def checker(n=10):
    """
    Don't touch this code
    This will print the input and the output for you
    """
    seed(0)
    llist1 = LinkedList()
    llist2 = LinkedList()
    a = sorted([randrange(50) for i in range(n)])[::-1]
    b = sorted([randrange(50) for i in range(n)])[::-1]

    for i in a:
        llist1.add(i)
    for i in b:
        llist2.add(i)

    llist1.printList()
    llist2.printList()
    o = solution(llist1, llist2)

    try:
        print("out list:", end=" ")
        o.printList()
    except:
        pass


def main():
    checker(10)


if __name__ == "__main__":
    main()
