#include "linked_list.hpp"
#include <iostream>

LinkedList::LinkedList()
{
    head = new Node();
    head->node = nullptr;
    tail = new Node();
    tail->node = nullptr;
    size = 0;
}

/**
 * @brief Retrieves the first element in the list
 * 
 * @return int First element in list
 */
int LinkedList::first()
{
    return head->node->value;
}

/**
 * @brief Retrieves the last element in the list
 * 
 * @return int Last element in list
 */
int LinkedList::last()
{
    return tail->node->value;
}

/**
 * @brief Adds element n at position p
 * 
 * @param p Position in list
 * @param n Element to add to list
 */
void LinkedList::add(int p, int n)
{
    if (p == 0)
        add_first(n);
    else if (p == size)
        add_last(n);
    else
    {
        Node *node = new Node();
        node->value = n;
        node->node = nullptr;
        Node *traverser = head;
        for (int i = 0; i < p; i++)
            traverser = traverser->node;
        node->node = traverser->node;
        traverser->node = node;
        size++;
    }
}

/**
 * @brief Add an element to the beginning of the list
 * 
 * @param n Number to add
 */
void LinkedList::add_first(int n)
{
    Node *old_first = head->node;
    Node *new_first = new Node();
    new_first->value = n;
    new_first->node = old_first;
    head->node = new_first;
    size++;
    if (tail->node == nullptr)
        tail->node = new_first;
}

/**
 * @brief Add an element to the end of the list
 * 
 * @param n Number to add
 */
void LinkedList::add_last(int n)
{
    Node *new_last = new Node();
    new_last->value = n;
    new_last->node = nullptr;
    if (tail->node == nullptr) tail->node = new_last;
    else
    {
        tail->node->node = new_last;
        tail->node = tail->node->node;
    }
    size++;
    if (head->node == nullptr)
        head->node = new_last;
}

/**
 * @brief Retrieve a number from a certain point in the list
 * 
 * @param p Location where to retrieve int
 * @return int Int at position p
 */
int LinkedList::retrieve(int p)
{
    Node *traverser = head;
    for (int i = 0; i < p; i++)
    {
        traverser = traverser->node;
    }
    return traverser->node->value;
}

/**
 * @brief Pops the first element from the list
 * 
 * @return int Int popped from list
 */
int LinkedList::pop_first()
{
    Node *old_head = head->node;
    head->node = head->node->node;
    int first = old_head->value;
    size--;
    delete old_head;
    return first;
}

/**
 * @brief Pops the last element from the list
 * 
 * @return int Int popped from the list
 */
int LinkedList::pop_last()
{
    Node *old_tail = tail->node;
    Node *traverser = head;
    for (int i = 0; i < size - 1; i++)
        traverser = traverser->node;
    tail->node = traverser;
    tail->node->node = nullptr;
    int last = old_tail->value;
    size--;
    delete old_tail;
    return last;
}

/**
 * @brief Removes an element from a specified position in the list
 * 
 * @param p Position to remove element from
 * @return int Element removed at position
 */
int LinkedList::remove(int p)
{
    if (p == 0)
        return pop_first();
    else if (p == size - 1)
        return pop_last();
    else
    {
        Node *traverser = head;
        for (int i = 0; i < p; i++)
            traverser = traverser->node;
        Node *removal_node = traverser->node;
        traverser->node = traverser->node->node;
        int value = removal_node->value;
        size--;
        delete removal_node;
        return value;
    }
}

/**
 * @brief Searches for an element in the list. If it exists, return the 
 * index it is located at. If it does not exist, return -1
 * 
 * @param n Int to search for
 * @return int Position index or -1 if not found
 */
int LinkedList::search(int n)
{
    Node *traverser = head;
    int index = 0;
    while (traverser->node != nullptr)
    {
        traverser = traverser->node;
        if (traverser->value == n)
        {
            return index;
        }
        index++;
    }
    return -1;
}

/**
 * @brief Prints the contents of the list
 * 
 */
void LinkedList::print_list()
{
    Node *traverser = head;
    while (traverser->node != nullptr)
    {
        traverser = traverser->node;
        std::cout << traverser->value;
        if (traverser->node != nullptr)
            std::cout << ", ";
    }
    std::cout << std::endl;
}
