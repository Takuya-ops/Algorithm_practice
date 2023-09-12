class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    first_num = getNumber(linkedListOne)
    second_num = getNumber(linkedListTwo)
    sum_result = first_num + second_num

    return makeList(sum_result)


def getNumber(lista):
    digit_position = 1
    number = 0
    while lista:
        number += lista.value * digit_position
        digit_position *= 10
        lista = lista.next
    return number


def makeList(num):
    digit = num % 10
    head = LinkedList(digit)
    node = head
    num = num // 10
    while num > 0:
        digit = num % 10
        node.next = LinkedList(digit)
        num = num // 10
        node = node.next
    return head
