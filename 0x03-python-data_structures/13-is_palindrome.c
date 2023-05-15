#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - hi
 *
 * @head: hi
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *tail = *head;
	int ln = 1, i = 0;
	listint_t **arr, *ptr = *head;

	if (!*head)
		return (1);
	while(tail->next)
	{
		tail = tail->next;
		ln++;
	}
	arr = malloc(ln * sizeof(*arr));
	for (i = 0; i < ln; i++)
	{
		arr[i] = ptr;
		ptr = ptr->next;
	}
	for (i = 0; i < ln / 2; i++)
	{
		if (arr[i]->n != arr[ln - i - 1]->n)
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
