#include "lists.h"
/**
 * check_cycle - hi
 * @list: hi
 * Return: int
 */
int check_cycle(listint_t *list){
	listint_t *ptr, *slowptr;

	if (!list || !list->next)
		return (0);
	slowptr = list, ptr = list->next;
	while (slowptr != ptr)
	{
		if (!ptr->next || !ptr->next->next)
			return (0);
		slowptr = slowptr->next;
		ptr = ptr->next->next;
	}
	return (1);
}
