#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a ne number to a sorted linked list
 * @head: points to elements of list
 * @number: number to add to list
 * Return: address of the ne_node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *ne_node;
	if (tmp == NULL)
	{
		return (NULL);
	}
	ne_node = (listint_t *)malloc(sizeof(listint_t));
	if (!ne_node)
	{
		return (NULL);
	}
	ne_node->n = number;
	ne_node->next = *head;
	*head = ne_node;
	return (*head);
}
