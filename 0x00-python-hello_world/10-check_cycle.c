#include "lists.h"
/**
*check_cycle - a program to check if a linked list has a cycle in it or not
*@list: the linked list We will be given
*Return: 0 if there is no loop, 1 if there is a loop.
*/
int check_cycle(listint_t *list)
{
	listint_t *first;
	listint_t *third;
	int cont;

	first = list;
	third = first->next;

	if (list == NULL)
	{
		return (0);
	}

	for (cont = 0; first && third; cont++)
	{
		first = first->next;
		third = third->next;
		if (first == third)
		{
			return (1);
		}
	}
	return (0);
}
