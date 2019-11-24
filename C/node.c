/*
	node.c - basic implementation of a node tree.

	Libraries used:
	         stddef - used for NULL
				stdlib - used for malloc
				stdio  - used for input / output

	Input  - None
	Output - None
*/


#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

#define DEBUG

/*
	Defines a node with two node children.
*/
typedef struct node
{
	int data;
	struct node * left;
	struct node * right;
} node;


int preorder(node * n, int * pre, int index)
{
	if (n == NULL)
	{
		return index;
	}
#ifdef DEBUG
	printf("Setting index %d to %d\n", index, n->data);
#endif
	pre[index] = n->data;
	index++;
	if (n->left != NULL)
	{
		index = preorder(n->left, pre, index);
	}
	if (n->right != NULL)
	{
		index = preorder(n->right, pre, index);
	}
	return index;
}

int populated_nodes(node * n)
{
	if (n == NULL)
	{
		return 0;
	}
	return populated_nodes(n->left) + 1 + populated_nodes(n->right);
}

int main()
{
	node * head = NULL;
	head = malloc(sizeof(node));
	head->data = 1;
	head->left = malloc(sizeof(node));
	node * left_node = head->left;
	left_node->data = 2;
	head->right = malloc(sizeof(node));
	node * right_node = head->right;
	right_node->data = 3;
	int p = populated_nodes(head);
	printf("%d\n", left_node->data);
	printf("Populated nodes: %d\n", p);

	int size = populated_nodes(head);
	int pre[size];
	preorder(head, pre, 0);
	int *a;
	for (a = pre; a < pre+size; a++)
	{
		printf("%d\n", *a);
	}


	free(head);
}
