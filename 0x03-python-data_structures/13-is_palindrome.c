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
int ispali(listint_t *h, listint_t **ptr, int ln, int c){
	int tmp = 1;

	if (c < ln)
	{
		tmp = ispali(h->next, ptr, ln, c+1) && ((*ptr)->n == h->n);
		(*ptr) = (*ptr) -> next;
		return (tmp);
	}
	else if (c == ln)
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
	int ln = 1;
	listint_t **ptr = malloc(sizeof(*ptr));
	*ptr = *head;

	if (!*head)
		return (1);
	while(tail->next)
	{
		tail = tail->next;
		ln++;
	}
	return (ispali(*head, ptr, ln, 1));
}
