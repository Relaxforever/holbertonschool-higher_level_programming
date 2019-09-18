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
	unsigned int cont;

	tmp = *head;
	ptr = NULL;
	prev = NULL;
	for (cont = 0; ptr != NULL; cont++)
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
	unsigned int cont;

	first = *head;
	second = *head;
	for (cont = 0; first != NULL && first->next != NULL; cont++)
	{
		first = first->next->next;
		second = second->next;
	}
	medio = second;
	reversing_list(&medio);
	tmp = *head;
	for (cont = 0; medio != NULL; cont++)
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
