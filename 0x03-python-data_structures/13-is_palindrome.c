#include "lists.h"
#include <stdlib.h>
/**
 * ispali - hi
 * @h: hi
 * @ptr: hi
 * @ln: hi
 * @c: hi
 * Return: hi
 */
int ispali(listint_t *h, listint_t **ptr){
	int tmp = 1;

	if (h->next)
	{
		tmp = ispali(h->next, ptr) && ((*ptr)->n == h->n);
		(*ptr) = (*ptr) -> next;
		return (tmp);
	}
	else
	{
		tmp = (h->n == (*ptr)->n);
		(*ptr) = (*ptr)->next;
		return (tmp);
	}
	return (tmp);
}
/**
 * is_palindrome - hi
 *
 * @head: hi
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *tail = *head;
	int ln = 1, x;
	listint_t **ptr = malloc(sizeof(*ptr));
	*ptr = *head;

	if (!*head)
	{
		free(ptr);
		return (1);
	}
	while(tail->next)
	{
		tail = tail->next;
		ln++;
	}
	x = ispali(*head, ptr);
	free(ptr);
	return (x);
}
