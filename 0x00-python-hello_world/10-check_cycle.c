#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to list
 * Return: 0 if cycle does not exist, 1 if it does
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *tmp = list;

	if (list == NULL || list->next == NULL)
		return (0);

	current = current->next;
	while (current != NULL)
	{
		if (current == tmp)
			return (1);
		current = current->next;

		if (current == NULL)
			return (0);
		current = current->next;
		tmp = tmp->next;
	}
	return (0);
}
