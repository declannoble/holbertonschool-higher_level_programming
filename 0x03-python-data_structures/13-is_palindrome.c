#include "lists.h"
/**
 * is_palindrome- checks if a linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if not, and 1 if so.
 */

int is_palindrome(listint_t **head);
{
	if (*head == NULL || *head->next == NULL)
		return (1);

}
