#include "array_based_queue.hpp"

/**
 * @brief Construct a new Array Based Queue:: Array Based Queue object
 * This implementation mainly proves to show why an array-based queue is 
 * a bad idea. In a stack, using an array makes sense because items being 
 * removed from the stack are getting popped at the end of the list. When 
 * a resize occurs, there's no inefficiencies in the space being used in 
 * the original array
 * 
 * In a queue, items are dequeued from the front of the array. If nothing 
 * is done to reuse this space, as is done in this implementation, the 
 * amount of unused space will approach infinity. There are techniques to 
 * avoid this, such as reusing the space at the beginning of the array 
 * once items are dequeued. However, this requires either the array to 
 * be restructured at some point, or to add additional tracking indicies 
 * to ensure the right items are dequeued at the right time. 
 * 
 */
ArrayBasedQueue::ArrayBasedQueue() : DynamicSet()
{
    add_index = 0;
}

/**
 * @brief Add to the queue
 * 
 * @param n Item to add
 */
void ArrayBasedQueue::add(int n)
{
    if (add_index == size) resize();
    if (index == -1) index = 0;
    data[add_index] = n;
    add_index++;
}

/**
 * @brief Pop an item from the queue
 * 
 * @return int Item dequeued
 */
int ArrayBasedQueue::pop()
{
    index++;
    return data[index - 1];
}
