#pragma once

class LinkedList
{
public:
    LinkedList();
    ~LinkedList() = default;
    int first();
    int last();
    void add(int p, int n);
    void add_first(int n);
    void add_last(int n);
    int retrieve(int p);
    int pop_first();
    int pop_last();
    int remove(int p);
    int search(int n);
    void print_list();
private:
    int size;
    struct Node {
        int value;
        Node* node;
    };
    Node* head;
    Node* tail;
};
