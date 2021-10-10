#include "queue.hpp"

#include "linked_list.hpp"

/**
 * @brief Construct a new Queue:: Queue object
 * Relies mainly on the linked list implementation 
 * for functionality.
 * 
 */
Queue::Queue()
{
    queue = LinkedList();
}

/**
 * @brief Add to the queue
 * 
 * @param n Element to ad
 */
void Queue::add(int n)
{
    queue.add_last(n);
}

/**
 * @brief Dequeue
 * 
 * @return int Element dequeued
 */
int Queue::pop()
{
    return queue.pop_first();
}
