#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - hi
 * @head: hi
 * @number: hi
 * Return: hi
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *newnode;

	if (!*head)
	{
		*head = malloc(sizeof(listint_t));
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	newnode = malloc(sizeof(listint_t));
	newnode->n = number;
	if (number < ptr->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (*head);
	}
	while (ptr->next && ptr->next->n < number)
	{
		ptr = ptr->next;
	}
	newnode->next = ptr->next;
	ptr->next = newnode;
	return (newnode);
}
