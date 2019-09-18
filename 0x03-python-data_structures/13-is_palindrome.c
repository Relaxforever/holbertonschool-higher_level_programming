#include "lists.h"
/**
*reversing_list - reverses the list
*@head: the head of the node
*/
void reversing_list(listint_t **head)
{
	listint_t *tmp;
	listint_t *ptr;
	listint_t *prev;

	tmp = *head;
	ptr = NULL;
	prev = NULL;
	while (ptr != NULL)
	{
		ptr = tmp->next;
		tmp->next = prev;
		prev = tmp;
		tmp = ptr;
	}
	*head = prev;
}
/**
* is_palindrome - checks is a linked list is palindrome
*@head: the beginning of the list
*Return: 1 if it's palindrome, 0 if it's not
*/
int is_palindrome(listint_t **head)
{
	listint_t *first;
	listint_t *second;
	listint_t *medio;
	listint_t *tmp;

	if (*head == NULL)
	{
		return (1);
	}
	first = *head;
	second = *head;
	if (*head == NULL)
	{
		return (1);
	}
	while (first != NULL && first->next != NULL)
	{
		first = first->next->next;
		second = second->next;
	}
	medio = second;
	reversing_list(&medio);
	tmp = *head;
	while (medio != NULL)
	{
		if (medio->n != tmp->n)
		{
			return (0);
		}
		medio = medio->next;
		tmp = tmp->next;
	}
	return (1);
}
