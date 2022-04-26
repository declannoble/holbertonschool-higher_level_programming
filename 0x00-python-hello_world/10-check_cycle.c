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

  while (current->next != NULL)
    {
      if (current == tmp)
	return (1);

      if (current->next == NULL)
	return (0);

    }
  return (0);
}
      
      

  
